#!/usr/bin/env python3
"""
Validate a puzzle against assets/puzzle-template.md.

The puzzle can be a whole document or one section inside a larger document.
"""

import argparse
import re
import sys
from pathlib import Path

SUBSECTIONS = ["Description", "Approaches", "Magic", "Practical Solution", "Success"]
ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
SKILLS = [
    "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History",
    "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception",
    "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival",
]
TIERS = {"Easy": 10, "Moderate": 15, "Hard": 20}
COSTS = ["Damage", "Exhaustion", "Resource Loss", "Alert", "Tactical Disadvantage", "High Cost Path"]
DAMAGE_TYPES = [
    "acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
    "piercing", "poison", "psychic", "radiant", "slashing", "thunder",
]

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
FAILURE = re.compile(r"^\s+- \*On a failure:\*\s*(.*)$")
CHECK = re.compile(rf"^DC (\d+) ({'|'.join(ABILITIES)}) \((.+?)\), (Easy|Moderate|Hard)$")
MAGIC = re.compile(r"^- \*([^*]+)\*:\s*\S")
DAMAGE_COST = re.compile(rf"^(\d+d\d+) ({'|'.join(DAMAGE_TYPES)}) damage \((Nuisance|Deadly)\)")


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
        return [(n, t) for n, t in self.body() if t.strip() and not t.lstrip().startswith("- ")]

    def fields(self):
        return [(n, m.group(1).strip(), m.group(2).strip())
                for n, t in self.body() if (m := FIELD.match(t.rstrip()))]


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


def checks_with_failures(section):
    """Parse '- **DC ...:** action' entries and their '*On a failure:*' sub-bullets."""
    entries = []
    for number, text in section.body():
        field = FIELD.match(text.rstrip())
        failure = FAILURE.match(text.rstrip())
        if field:
            entries.append({"line": number, "check": field.group(1).strip(),
                            "action": field.group(2).strip(), "failure": None})
        elif failure and entries:
            entries[-1]["failure"] = (number, failure.group(1).strip())
    return entries


def damage_options(level, severity):
    for levels, options in DAMAGE_DICE:
        if level in levels:
            return options[severity]
    return []


def validate(section):
    errors = []

    def error(line, message):
        errors.append((line, message))

    def check_entry(entry, is_tool):
        match = CHECK.match(entry["check"])
        if not match:
            example = "DC 15 Intelligence (Carpenter's Tools), Moderate" if is_tool \
                else "DC 15 Strength (Athletics), Moderate"
            error(entry["line"], f"Check must look like '{example}:'")
        else:
            dc, _, name, tier = match.groups()
            if int(dc) != TIERS[tier]:
                error(entry["line"], f"{tier} checks are DC {TIERS[tier]}; found DC {dc}")
            if is_tool and name in SKILLS:
                error(entry["line"], f"Practical Solution uses a tool, not the {name} skill")
            if not is_tool and name not in SKILLS:
                error(entry["line"], f"'{name}' is not a skill")
        if not entry["action"]:
            error(entry["line"], "Check is missing what the character does")
        if entry["failure"] is None:
            error(entry["line"], "Check is missing '*On a failure:*'")
            return
        number, value = entry["failure"]
        kind, _, detail = value.partition(":")
        kind, detail = kind.strip(), detail.strip()
        if kind not in COSTS:
            error(number, f"Failure cost must start with one of {COSTS} and a colon")
        elif not detail:
            error(number, f"{kind} cost is missing its mechanics")
        elif kind == "Damage":
            damage = DAMAGE_COST.match(detail)
            if not damage:
                error(number, "Damage cost must start like '2d10 fire damage (Nuisance)'")
            elif level:
                options = damage_options(level, damage.group(3))
                if damage.group(1) not in options:
                    error(number, f"{damage.group(3)} damage at level {level} must be one of {options}")
        elif kind == "Exhaustion" and not re.search(r"\d+ levels? of exhaustion", detail):
            error(number, "Exhaustion cost must say how many levels of exhaustion")
        elif kind == "Alert" and "surprised" not in detail.lower() and "+2 AC" not in detail:
            error(number, "Alert cost must say the party is surprised or the enemies gain +2 AC in the next encounter")
        elif kind == "High Cost Path" and not re.search(r"\b(Low|Moderate)\b", detail):
            error(number, "High Cost Path must name a Low or Moderate encounter")

    for number, text in section.lines:
        for placeholder in PLACEHOLDER.findall(text):
            error(number, f"Unfilled placeholder {placeholder}")

    if not section.prose():
        error(None, "Missing the overview sentence under the puzzle heading")

    header = {label: (number, value) for number, label, value in section.fields()}
    level = None
    for key in ["Party Level", "Original Purpose", "Current State"]:
        if not header.get(key, (None, ""))[1]:
            error(None, f"Missing '- **{key}:**' under the puzzle heading")
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

    for title in ["Description", "Success"]:
        if title in by_title and not by_title[title].prose():
            error(None, f"{title} is empty")

    if "Approaches" in by_title:
        entries = checks_with_failures(by_title["Approaches"])
        if not 2 <= len(entries) <= 3:
            error(None, f"Approaches must have 2 or 3 skill checks; found {len(entries)}")
        skills = [m.group(3) for e in entries if (m := CHECK.match(e["check"]))]
        if len(skills) != len(set(skills)):
            error(None, "Each approach must use a different skill")
        for entry in entries:
            check_entry(entry, is_tool=False)

    if "Magic" in by_title:
        spells = [(n, t) for n, t in by_title["Magic"].body() if t.startswith("- ")]
        if not 1 <= len(spells) <= 2:
            error(None, f"Magic must list 1 or 2 spells; found {len(spells)}")
        for number, text in spells:
            if not MAGIC.match(text):
                error(number, "Magic entries must look like '- *Spell Name*: how it solves the obstacle'")

    if "Practical Solution" in by_title:
        entries = checks_with_failures(by_title["Practical Solution"])
        if len(entries) != 1:
            error(None, f"Practical Solution must have exactly 1 tool check; found {len(entries)}")
        for entry in entries:
            check_entry(entry, is_tool=True)

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Markdown file containing the puzzle")
    parser.add_argument("--section", required=True, help="The puzzle's heading text")
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
        print(f"PASS: '{args.section}' matches the puzzle template.")
        return 0
    print(f"FAIL: {len(errors)} problem(s) in '{args.section}':")
    for line, message in errors:
        print((f"  line {line}: " if line else "  ") + message)
    return 1


if __name__ == "__main__":
    sys.exit(main())
