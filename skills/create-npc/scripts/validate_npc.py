#!/usr/bin/env python3
"""
Validate an NPC against assets/npc-template.md.

The NPC can be a whole document or one section inside a larger document.
"""

import argparse
import re
import sys
from pathlib import Path

SUBSECTIONS = ["Appearance", "Voice and Manner", "Wants", "Connections", "Social Play"]
HEADER_FIELDS = ["Role", "Species", "Pronouns", "Location", "Attitude", "Stat Block"]
BASE_DC = {"Friendly": 10, "Indifferent": 15, "Hostile": 20}
APPROACHES = ["Persuasion", "Deception", "Intimidation"]

HEADING = re.compile(r"^(#+)\s+(.*?)\s*#*\s*$")
PLACEHOLDER = re.compile(r"\[[^\]]*\](?!\()")
FIELD = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")


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
        return [(n, t) for n, t in self.body()
                if t.strip() and not t.startswith(("- ", "|"))]

    def fields(self):
        return [(n, m.group(1).strip(), m.group(2).strip())
                for n, t in self.body() if (m := FIELD.match(t.rstrip()))]

    def table_rows(self):
        rows = []
        for number, text in self.body():
            stripped = text.strip()
            if not stripped.startswith("|"):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            rows.append((number, cells))
        return rows[1:]  # drop the header row


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


def validate(section):
    errors = []

    def error(line, message):
        errors.append((line, message))

    def require_fields(sub, names):
        found = {label: (number, value) for number, label, value in sub.fields()}
        for name in names:
            if not found.get(name, (None, ""))[1]:
                error(None, f"{sub.title} is missing '- **{name}:**'")
        return found

    for number, text in section.lines:
        for placeholder in PLACEHOLDER.findall(text):
            error(number, f"Unfilled placeholder {placeholder}")

    if not section.prose():
        error(None, "Missing the overview sentence under the NPC heading")

    header = {label: (number, value) for number, label, value in section.fields()}
    for name in HEADER_FIELDS:
        if not header.get(name, (None, ""))[1]:
            error(None, f"Missing '- **{name}:**' under the NPC heading")
    attitude = None
    if "Attitude" in header:
        number, value = header["Attitude"]
        if value in BASE_DC:
            attitude = value
        else:
            error(number, "Attitude must be Hostile, Indifferent, or Friendly")

    children = section.children()
    titles = [c.title for c in children]
    if titles != SUBSECTIONS:
        error(None, f"Subsections must be exactly {SUBSECTIONS} at heading level "
                    f"{section.level + 1}; found {titles}")
    by_title = {c.title: c for c in children}

    if "Appearance" in by_title and not by_title["Appearance"].prose():
        error(None, "Appearance is empty")
    if "Voice and Manner" in by_title:
        require_fields(by_title["Voice and Manner"], ["Voice", "Manner"])
    if "Wants" in by_title:
        require_fields(by_title["Wants"], ["Goal", "Fear", "Secret"])

    if "Connections" in by_title:
        connections = [f for f in by_title["Connections"].fields() if f[2]]
        if not 1 <= len(connections) <= 3:
            error(None, f"Connections must list 1 to 3 entries; found {len(connections)}")

    if "Social Play" in by_title:
        social = by_title["Social Play"]
        rows = social.table_rows()
        names = [cells[0] for _, cells in rows]
        if names != APPROACHES:
            error(None, f"Social Play table must have rows {APPROACHES} in order; found {names}")
        for number, cells in rows:
            if len(cells) != 3:
                error(number, "Social Play rows need Approach, DC, and Notes columns")
                continue
            approach, dc, notes = cells
            if not dc.isdigit():
                error(number, f"{approach} DC must be a number")
            elif attitude:
                base = BASE_DC[attitude]
                allowed = [base - 5, base, base + 5]
                if int(dc) not in allowed:
                    error(number, f"{attitude} NPCs have DCs of {allowed[0]}, {allowed[1]}, or "
                                  f"{allowed[2]}; {approach} is DC {dc}")
            if not notes:
                error(number, f"{approach} is missing its notes")
        require_fields(social, ["Leverage", "Won't Budge", "Offers"])

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Markdown file containing the NPC")
    parser.add_argument("--section", required=True, help="The NPC's heading text")
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
        print(f"PASS: '{args.section}' matches the NPC template.")
        return 0
    print(f"FAIL: {len(errors)} problem(s) in '{args.section}':")
    for line, message in errors:
        print((f"  line {line}: " if line else "  ") + message)
    return 1


if __name__ == "__main__":
    sys.exit(main())
