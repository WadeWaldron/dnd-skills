#!/usr/bin/env python3
"""
Validate a trap against assets/trap-template.md.

The trap can be a whole document or one section inside a larger document.
"""

import argparse
import re
import sys
from pathlib import Path

SUBSECTIONS = ["Telegraph", "Trigger", "Detection", "Effect", "Countermeasures"]
PURPOSES = ["Intentional Security", "Environmental Hazard", "Execution", "Alarm", "Deterrent"]
CONSEQUENCES = ["Condition", "Environmental Complication", "Resource Attrition", "Alarm"]
ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
DAMAGE_TYPES = [
    "acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
    "piercing", "poison", "psychic", "radiant", "slashing", "thunder",
]

DC_RANGE = {"Nuisance": (10, 15), "Deadly": (15, 20)}
ATTACK_RANGE = {"Nuisance": (3, 5), "Deadly": (6, 9)}

# Damage Severity by Level (2024 Dungeon Master's Guide; see the damage-severity skill)
DAMAGE_DICE = [
    (range(1, 5), {"Nuisance": ["1d10", "2d4", "1d8"], "Deadly": ["2d10", "3d6", "4d4"]}),
    (range(5, 11), {"Nuisance": ["2d10", "3d6", "4d4"], "Deadly": ["4d10", "6d6", "5d8"]}),
    (range(11, 17), {"Nuisance": ["4d10", "6d6", "5d8"], "Deadly": ["10d10", "15d6", "8d12"]}),
    (range(17, 21), {"Nuisance": ["10d10", "15d6", "8d12"], "Deadly": ["18d10", "28d6", "15d12"]}),
]

HEADING = re.compile(r"^(#+)\s+(.*?)\s*#*\s*$")
PLACEHOLDER = re.compile(r"\[[^\]]*\](?!\()")
FIELD = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")
DC_CHECK = re.compile(rf"^DC (\d+) ({'|'.join(ABILITIES)}) \((.+?)\)$")
SAVE = re.compile(rf"^DC (\d+) ({'|'.join(ABILITIES)}) saving throw$")
ATTACK = re.compile(r"^\+(\d+) to hit$")
DAMAGE = re.compile(rf"^(\d+d\d+) ({'|'.join(DAMAGE_TYPES)}) damage(, half on a successful save)?$")
MAGIC = re.compile(r"^\*([^*]+)\*:\s*\S")


class Section:
    def __init__(self, title, level, lines):
        self.title = title
        self.level = level
        self.lines = lines  # list of (line_number, text)

    def body(self):
        result = []
        for number, text in self.lines:
            if HEADING.match(text):
                break
            result.append((number, text))
        return result

    def children(self):
        found = []
        current = None
        for number, text in self.lines:
            match = HEADING.match(text)
            if match and len(match.group(1)) == self.level + 1:
                current = Section(match.group(2).strip(), self.level + 1, [])
                found.append(current)
            elif current is not None:
                current.lines.append((number, text))
        return found

    def prose(self):
        return [(n, t) for n, t in self.body() if t.strip() and not t.startswith("- ")]

    def fields(self):
        """Return (line, label, value) for each '- **Label:** value' line."""
        result = []
        for number, text in self.body():
            match = FIELD.match(text.rstrip())
            if match:
                result.append((number, match.group(1).strip(), match.group(2).strip()))
        return result


def find_section(lines, title):
    numbered = list(enumerate(lines, start=1))
    for index, (_, text) in enumerate(numbered):
        match = HEADING.match(text)
        if match and match.group(2).strip().lower() == title.strip().lower():
            level = len(match.group(1))
            body = []
            for number, later in numbered[index + 1:]:
                heading = HEADING.match(later)
                if heading and len(heading.group(1)) <= level:
                    break
                body.append((number, later))
            return Section(match.group(2).strip(), level, body)
    return None


def damage_options(level, severity):
    for levels, options in DAMAGE_DICE:
        if level in levels:
            return options[severity]
    return []


def validate(section):
    errors = []

    def error(line, message):
        errors.append((line, message))

    def check_dc(line, dc, label):
        if severity in DC_RANGE:
            low, high = DC_RANGE[severity]
            if not low <= dc <= high:
                error(line, f"{label} DC {dc} is outside the {severity} range of {low}-{high}")

    for number, text in section.lines:
        for placeholder in PLACEHOLDER.findall(text):
            error(number, f"Unfilled placeholder {placeholder}")

    if not section.prose():
        error(None, "Missing the overview sentence under the trap heading")

    header = {label: (number, value) for number, label, value in section.fields()}
    severity = level = None
    for key in ["Purpose", "Severity", "Party Level"]:
        if key not in header:
            error(None, f"Missing '- **{key}:**' under the trap heading")
    if "Purpose" in header and header["Purpose"][1] not in PURPOSES:
        error(header["Purpose"][0], f"Purpose must be one of {PURPOSES}")
    if "Severity" in header:
        if header["Severity"][1] in DC_RANGE:
            severity = header["Severity"][1]
        else:
            error(header["Severity"][0], "Severity must be Nuisance or Deadly")
    if "Party Level" in header:
        value = header["Party Level"][1]
        if value.isdigit() and 1 <= int(value) <= 20:
            level = int(value)
        else:
            error(header["Party Level"][0], "Party Level must be a number from 1 to 20")

    children = section.children()
    titles = [c.title for c in children]
    if titles != SUBSECTIONS:
        error(None, f"Subsections must be exactly {SUBSECTIONS} at heading level "
                    f"{section.level + 1}; found {titles}")
    by_title = {c.title: c for c in children}

    for title in ["Telegraph", "Trigger"]:
        if title in by_title and not by_title[title].prose():
            error(None, f"{title} is empty")

    if "Detection" in by_title:
        checks = by_title["Detection"].fields()
        if not 1 <= len(checks) <= 2:
            error(None, f"Detection must have 1 or 2 checks; found {len(checks)}")
        for number, label, value in checks:
            match = DC_CHECK.match(label)
            if not match or match.group(3) not in ("Perception", "Investigation"):
                error(number, "Detection checks must look like 'DC 15 Wisdom (Perception):' "
                              "or 'DC 15 Intelligence (Investigation):'")
            else:
                check_dc(number, int(match.group(1)), "Detection")
            if not value:
                error(number, "Detection check is missing what it reveals")

    if "Effect" in by_title:
        effect = by_title["Effect"]
        if not effect.prose():
            error(None, "Effect is missing its description")
        fields = {label: (number, value) for number, label, value in effect.fields()}
        has_save = "Save" in fields
        if has_save == ("Attack" in fields):
            error(None, "Effect must have exactly one of '- **Save:**' or '- **Attack:**'")
        if has_save:
            number, value = fields["Save"]
            match = SAVE.match(value)
            if not match:
                error(number, "Save must look like 'DC 15 Dexterity saving throw'")
            else:
                check_dc(number, int(match.group(1)), "Save")
        if "Attack" in fields:
            number, value = fields["Attack"]
            match = ATTACK.match(value)
            if not match:
                error(number, "Attack must look like '+5 to hit'")
            elif severity:
                low, high = ATTACK_RANGE[severity]
                if not low <= int(match.group(1)) <= high:
                    error(number, f"Attack bonus is outside the {severity} range of +{low} to +{high}")
        if "Damage" not in fields:
            error(None, "Effect is missing '- **Damage:**' (use 'None' for no damage)")
        else:
            number, value = fields["Damage"]
            if value != "None":
                match = DAMAGE.match(value)
                if not match:
                    error(number, "Damage must look like '2d10 fire damage' "
                                  "(add ', half on a successful save' if it applies) or 'None'")
                else:
                    if match.group(3) and not has_save:
                        error(number, "'half on a successful save' needs a Save")
                    if level and severity:
                        options = damage_options(level, severity)
                        if match.group(1) not in options:
                            error(number, f"{severity} damage at level {level} must be one of {options}")
        if "Consequence" not in fields:
            if fields.get("Damage", (None, "None"))[1] == "None":
                error(None, "A trap with no damage needs a '- **Consequence:**'")
        else:
            number, value = fields["Consequence"]
            kind, _, detail = value.partition(":")
            if kind.strip() not in CONSEQUENCES:
                error(number, f"Consequence must start with one of {CONSEQUENCES} and a colon")
            elif not detail.strip():
                error(number, "Consequence is missing its mechanical detail")
        unknown = [label for label in fields if label not in ("Save", "Attack", "Damage", "Consequence")]
        if unknown:
            error(None, f"Unexpected Effect fields {unknown}")

    if "Countermeasures" in by_title:
        fields = by_title["Countermeasures"].fields()
        disables = [f for f in fields if f[1] == "Disable"]
        magic = [f for f in fields if f[1] == "Magic"]
        if len(disables) != 1:
            error(None, f"Countermeasures must have exactly 1 Disable; found {len(disables)}")
        for number, _, value in disables:
            check, _, detail = value.partition(":")
            match = DC_CHECK.match(check.strip())
            if not match:
                error(number, "Disable must look like 'DC 15 Dexterity (Thieves' Tools): how'")
            else:
                check_dc(number, int(match.group(1)), "Disable")
            if not detail.strip():
                error(number, "Disable is missing what disabling looks like")
        if not 1 <= len(magic) <= 2:
            error(None, f"Countermeasures must have 1 or 2 Magic entries; found {len(magic)}")
        for number, _, value in magic:
            if not MAGIC.match(value):
                error(number, "Magic must look like '*Spell Name*: how it helps'")
        unknown = [f[1] for f in fields if f[1] not in ("Disable", "Magic")]
        if unknown:
            error(None, f"Unexpected Countermeasures fields {unknown}")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Markdown file containing the trap")
    parser.add_argument("--section", required=True, help="The trap's heading text")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}")
        return 2
    section = find_section(path.read_text(encoding="utf-8").splitlines(), args.section)
    if section is None:
        print(f"No heading named '{args.section}' in {path}")
        return 2

    errors = validate(section)
    if not errors:
        print(f"PASS: '{args.section}' matches the trap template.")
        return 0
    print(f"FAIL: {len(errors)} problem(s) in '{args.section}':")
    for line, message in errors:
        print((f"  line {line}: " if line else "  ") + message)
    return 1


if __name__ == "__main__":
    sys.exit(main())
