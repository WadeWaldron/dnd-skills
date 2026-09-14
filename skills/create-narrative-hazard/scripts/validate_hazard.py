#!/usr/bin/env python3
"""
Validate a narrative hazard against assets/hazard-template.md.

The hazard can be a whole document or one section inside a larger document.
Fixed rules text is read from the template, so the template is the single
source for Outcomes, Edges, Complications, and the Ending rule.
"""

import argparse
import re
import sys
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "assets" / "hazard-template.md"

SUBSECTIONS = [
    "Narrative Context",
    "Setup",
    "Position",
    "Outcomes",
    "Edges",
    "Complications",
    "Opportunities",
    "Ending",
]
ENDING_SUBSECTIONS = ["Progress Clock Fills", "Danger Clock Fills"]

POSITIONS = [("Controlled", "13"), ("Risky", "15"), ("Desperate", "17")]

DAMAGE_TYPES = [
    "acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
    "piercing", "poison", "psychic", "radiant", "slashing", "thunder",
]
CONDITIONS = ["blinded", "deafened", "frightened", "poisoned", "prone", "restrained"]

HEADING = re.compile(r"^(#+)\s+(.*?)\s*#*\s*$")
PLACEHOLDER = re.compile(r"\[[^\]]*\](?!\()")
TOP_BULLET = re.compile(r"^- \*\*(.+?)\*\*\s*(.*)$")
SUB_BULLET = re.compile(r"^\s+- \*(.+?):\*\s*(.*)$")
SETUP_ITEM = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")
CLOCK = re.compile(r"^(.+?)\s*\((\d+) segments\)$")


def norm(text):
    text = text.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text).strip()


def dice_for_level(level):
    """Controlled, Risky, and Desperate damage dice for a party level."""
    risky = -(-level // 3)
    controlled = "1d4" if risky == 1 else f"{-(-risky // 2)}d6"
    return (controlled, f"{risky}d6", f"{risky * 2}d6")


class Section:
    """A heading and the numbered lines under it, split into child sections."""

    def __init__(self, title, level, lines):
        self.title = title
        self.level = level
        self.lines = lines  # list of (line_number, text)

    def body(self):
        """Lines before the first child heading."""
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
                current = Section(match.group(2), self.level + 1, [])
                found.append(current)
            elif current is not None:
                current.lines.append((number, text))
        return found

    def text_lines(self):
        return [(n, t) for n, t in self.body() if t.strip()]


def find_section(lines, title):
    numbered = list(enumerate(lines, start=1))
    for index, (number, text) in enumerate(numbered):
        match = HEADING.match(text)
        if match and norm(match.group(2)).lower() == norm(title).lower():
            level = len(match.group(1))
            body = []
            for later_number, later_text in numbered[index + 1:]:
                later = HEADING.match(later_text)
                if later and len(later.group(1)) <= level:
                    break
                body.append((later_number, later_text))
            return Section(match.group(2), level, body)
    return None


def table_rows(section):
    rows = []
    for number, text in section.body():
        stripped = text.strip()
        if not stripped.startswith("|"):
            continue
        cells = [norm(c) for c in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append((number, cells))
    return rows[1:]  # drop the header row


def rules_list(section):
    """Parse '- **Name:** effect' bullets with '*In this hazard:*' sub-bullets."""
    entries = []
    for number, text in section.body():
        top = TOP_BULLET.match(text)
        sub = SUB_BULLET.match(text)
        if top:
            name = norm(top.group(1)).rstrip(":")
            entries.append({"line": number, "name": name, "rest": norm(top.group(2)), "subs": {}})
        elif sub and entries:
            entries[-1]["subs"][norm(sub.group(1)).lower()] = norm(sub.group(2))
    return entries


def load_template():
    lines = TEMPLATE_PATH.read_text(encoding="utf-8").splitlines()
    top = next(
        (HEADING.match(t) for t in lines if HEADING.match(t)), None
    )
    section = find_section(lines, top.group(2))
    children = {c.title: c for c in section.children()}
    ending_text = [norm(t) for _, t in children["Ending"].text_lines()]
    return {
        "outcomes": [cells for _, cells in table_rows(children["Outcomes"])],
        "edges": [(e["name"], e["rest"]) for e in rules_list(children["Edges"])],
        "complications": [(e["name"], e["rest"]) for e in rules_list(children["Complications"])],
        "ending_intro": ending_text,
    }


def validate(section, template):
    errors = []

    def error(line, message):
        errors.append((line, message))

    for number, text in section.lines:
        for placeholder in PLACEHOLDER.findall(text):
            error(number, f"Unfilled placeholder {placeholder}")

    if not section.text_lines():
        error(None, "Missing the overview sentence under the hazard heading")

    children = section.children()
    titles = [norm(c.title) for c in children]
    if titles != SUBSECTIONS:
        error(None, f"Subsections must be exactly {SUBSECTIONS} at heading level "
                    f"{section.level + 1}; found {titles}")
    by_title = {norm(c.title): c for c in children}

    if "Narrative Context" in by_title and not by_title["Narrative Context"].text_lines():
        error(None, "Narrative Context is empty")

    level = None
    if "Setup" in by_title:
        setup = {}
        for number, text in by_title["Setup"].body():
            match = SETUP_ITEM.match(text)
            if match:
                setup[norm(match.group(1))] = (number, norm(match.group(2)))
        for key in ["Party Level", "Progress Clock", "Danger Clock", "Starting Position"]:
            if key not in setup:
                error(None, f"Setup is missing '- **{key}:**'")
        if "Party Level" in setup:
            number, value = setup["Party Level"]
            if value.isdigit() and 1 <= int(value) <= 20:
                level = int(value)
            else:
                error(number, f"Party Level must be a number from 1 to 20; found '{value}'")
        for key in ["Progress Clock", "Danger Clock"]:
            if key in setup:
                number, value = setup[key]
                match = CLOCK.match(value)
                if not match:
                    error(number, f"{key} must look like 'Name (6 segments)'; found '{value}'")
                elif match.group(2) not in ("4", "6", "8"):
                    error(number, f"{key} must have 4, 6, or 8 segments; found {match.group(2)}")
        if "Starting Position" in setup:
            number, value = setup["Starting Position"]
            if value not in [p for p, _ in POSITIONS]:
                error(number, f"Starting Position must be Controlled, Risky, or Desperate; found '{value}'")

    if "Position" in by_title:
        rows = table_rows(by_title["Position"])
        dice = dice_for_level(level) if level else None
        if len(rows) != len(POSITIONS):
            error(None, f"Position table must have {len(POSITIONS)} rows; found {len(rows)}")
        for index, (number, cells) in enumerate(rows[:len(POSITIONS)]):
            name, dc = POSITIONS[index]
            expected = [name, dc, dice[index]] if dice else [name, dc] + cells[2:3]
            if cells != expected:
                error(number, f"Position row must be {' | '.join(expected)}; found {' | '.join(cells)}")

    if "Outcomes" in by_title:
        rows = table_rows(by_title["Outcomes"])
        found = [cells for _, cells in rows]
        if found != template["outcomes"]:
            error(rows[0][0] if rows else None,
                  "Outcomes table must match the template exactly")

    for title, key in [("Edges", "edges"), ("Complications", "complications")]:
        if title not in by_title:
            continue
        entries = rules_list(by_title[title])
        names = [e["name"] for e in entries]
        expected_names = [n for n, _ in template[key]]
        if names != expected_names:
            error(None, f"{title} must list exactly {expected_names} in order; found {names}")
        effects = dict(template[key])
        for entry in entries:
            name = entry["name"]
            if name not in effects:
                continue
            effect = effects[name]
            if entry["rest"] != effect:
                error(entry["line"], f"{name} effect must match the template: '{effect}'")
            fiction = entry["subs"].get("in this hazard", "")
            if not fiction:
                error(entry["line"], f"{name} is missing '*In this hazard:*'")
            elif name == "Damage" and not any(t in fiction.lower() for t in DAMAGE_TYPES):
                error(entry["line"], "Damage must name a damage type in 'In this hazard'")
            elif name == "Condition" and not any(c in fiction.lower() for c in CONDITIONS):
                error(entry["line"], f"Condition must name one of {CONDITIONS} in 'In this hazard'")

    if "Opportunities" in by_title:
        entries = rules_list(by_title["Opportunities"])
        if len(entries) < 2:
            error(None, f"Opportunities must have at least 2 entries; found {len(entries)}")
        aid_edges = [n for n, _ in template["edges"] if n != "Opportunity"]
        for entry in entries:
            match = re.fullmatch(r"\((Treasure|Aid)\)", entry["rest"])
            if not match:
                error(entry["line"], f"{entry['name']} must be followed by (Treasure) or (Aid)")
            for sub in ["in this hazard", "effect"]:
                if not entry["subs"].get(sub):
                    error(entry["line"], f"{entry['name']} is missing '*{sub.capitalize()}:*'")
            effect = entry["subs"].get("effect", "")
            if match and match.group(1) == "Aid" and not any(e in effect for e in aid_edges):
                error(entry["line"], f"{entry['name']} is an Aid, so its Effect must name one of {aid_edges}")

    if "Ending" in by_title:
        ending = by_title["Ending"]
        intro = [norm(t) for _, t in ending.text_lines()]
        if intro != template["ending_intro"]:
            error(None, f"Ending must open with: {' '.join(template['ending_intro'])}")
        ending_children = {norm(c.title): c for c in ending.children()}
        if list(ending_children) != ENDING_SUBSECTIONS:
            error(None, f"Ending subsections must be exactly {ENDING_SUBSECTIONS} at heading "
                        f"level {ending.level + 1}; found {list(ending_children)}")
        progress = ending_children.get("Progress Clock Fills")
        if progress and not progress.text_lines():
            error(None, "Progress Clock Fills is empty")
        danger = ending_children.get("Danger Clock Fills")
        if danger:
            items = {}
            for number, text in danger.body():
                match = SETUP_ITEM.match(text)
                if match:
                    items[norm(match.group(1))] = (number, norm(match.group(2)))
            if "Narrative" not in items or not items["Narrative"][1]:
                error(None, "Danger Clock Fills is missing '- **Narrative:**'")
            if "Mechanical" not in items:
                error(None, "Danger Clock Fills is missing '- **Mechanical:**'")
            else:
                number, value = items["Mechanical"]
                desperate = dice_for_level(level)[2] if level else r"\d+d\d+"
                damage = re.fullmatch(
                    rf"Every character takes {desperate} ({'|'.join(DAMAGE_TYPES)}) damage\.", value
                )
                exhaustion = value == "Every character gains 1 level of exhaustion."
                if not (damage or exhaustion):
                    dice_text = desperate if level else "[Desperate dice]"
                    error(number, "Mechanical must be exactly 'Every character takes "
                                  f"{dice_text} [type] damage.' or "
                                  "'Every character gains 1 level of exhaustion.'")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Markdown file containing the hazard")
    parser.add_argument("--section", required=True, help="The hazard's heading text")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}")
        return 2
    section = find_section(path.read_text(encoding="utf-8").splitlines(), args.section)
    if section is None:
        print(f"No heading named '{args.section}' in {path}")
        return 2

    errors = validate(section, load_template())
    if not errors:
        print(f"PASS: '{args.section}' matches the narrative hazard template.")
        return 0
    print(f"FAIL: {len(errors)} problem(s) in '{args.section}':")
    for line, message in errors:
        prefix = f"  line {line}: " if line else "  "
        print(prefix + message)
    return 1


if __name__ == "__main__":
    sys.exit(main())
