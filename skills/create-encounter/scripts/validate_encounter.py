#!/usr/bin/env python3
"""
Validate an encounter write-up against assets/encounter-template.md.

The encounter can be a whole document or one section inside a larger document.
The Encounter Balance math is recalculated with encounter_xp.py.
"""

import argparse
import re
import sys
from fractions import Fraction
from pathlib import Path

from encounter_xp import XP_BUDGET_PER_CHARACTER, difficulty_for, party_budgets

REQUIRED = ["The Enemy", "Encounter Balance", "Statistics", "Tactics", "Scaling", "Aftermath"]
ORDER = ["The Enemy", "Encounter Balance", "Statistics", "Tactics", "The Objective",
         "Complications", "Scaling", "Aftermath"]
TEMPLATE_NOTES = ["(omit if the objective is to defeat the enemy)", "(optional)",
                  "Repeat as needed for each distinct creature", "only if applicable"]
STAT_FIELDS = ["Armor Class", "Hit Points", "Speed"]

HEADING = re.compile(r"^(#+)\s+(.*?)\s*#*\s*$")
PLACEHOLDER = re.compile(r"\[[^\]]*\](?!\()")
ENEMY = re.compile(r"^- \*\*(\d+) × (.+?)\*\*\s+[—-]\s+\S")
BALANCE_MONSTER = re.compile(r"^- (\d+) × (.+?) \(CR ([\d/.]+), (\d+) XP each\) = (\d+) XP$")
BALANCE_PARTY = re.compile(
    r"^- Party budgets \((\d+) characters, levels? ([\d, ]+)\): Low (\d+), Moderate (\d+), High (\d+)$"
)
BALANCE_TOTAL = re.compile(r"^- \*\*Total: (\d+) XP \((Low|Moderate|High|Beyond High) difficulty\)\*\*$")
CHALLENGE = re.compile(r"\*\*Challenge\*\*\s+([\d/.]+)\s+\((\d[\d,]*) XP\)")


def cr_value(text):
    return Fraction(text)


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

    def has_text(self, whole=False):
        lines = self.lines if whole else self.body()
        return any(t.strip() and not HEADING.match(t) for _, t in lines)


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

    for number, text in section.lines:
        for placeholder in PLACEHOLDER.findall(text):
            error(number, f"Unfilled placeholder {placeholder}")
        for note in TEMPLATE_NOTES:
            if note in text:
                error(number, f"Template note left in: '{note}'")

    if not section.has_text():
        error(None, "Missing the read-aloud description under the encounter heading")

    children = section.children()
    titles = [c.title for c in children]
    by_title = {c.title: c for c in children}
    for title in REQUIRED:
        if title not in by_title:
            error(None, f"Missing subsection '{title}' at heading level {section.level + 1}")
    unknown = [t for t in titles if t not in ORDER]
    if unknown:
        error(None, f"Unexpected subsections {unknown}; allowed: {ORDER}")
    known = [t for t in titles if t in ORDER]
    if known != sorted(known, key=ORDER.index):
        error(None, f"Subsections must be in the order {ORDER}; found {known}")
    for title in ["The Enemy", "Tactics", "Aftermath", "The Objective", "Complications"]:
        if title in by_title and not by_title[title].has_text():
            error(None, f"'{title}' is empty")

    enemies = {}
    if "The Enemy" in by_title:
        for number, text in by_title["The Enemy"].body():
            if text.startswith("- "):
                match = ENEMY.match(text)
                if match:
                    enemies[match.group(2)] = int(match.group(1))
                else:
                    error(number, "Enemy entries must look like '- **3 × Name** — who they are'")

    balance = {}
    if "Encounter Balance" in by_title:
        party_levels = None
        party_line = total_line = None
        for number, text in by_title["Encounter Balance"].body():
            text = text.rstrip()
            if not text.startswith("- "):
                continue
            monster = BALANCE_MONSTER.match(text)
            party = BALANCE_PARTY.match(text)
            total = BALANCE_TOTAL.match(text)
            if monster:
                count, name, cr, xp, subtotal = monster.groups()
                balance[name] = (number, int(count), cr, int(xp))
                if int(count) * int(xp) != int(subtotal):
                    error(number, f"{name} subtotal should be {int(count) * int(xp)} XP")
            elif party:
                party_line = (number, party.groups())
            elif total:
                total_line = (number, total.groups())
            else:
                error(number, "Unrecognized Encounter Balance line; copy the block from encounter_xp.py")
        if not balance:
            error(None, "Encounter Balance lists no monsters")
        if party_line is None:
            error(None, "Encounter Balance is missing the 'Party budgets' line")
        else:
            number, (size, levels_text, low, moderate, high) = party_line
            levels = [int(l) for l in re.split(r"[,\s]+", levels_text.strip()) if l]
            if len(levels) == 1:
                levels = levels * int(size)
            if len(levels) != int(size) or any(l not in XP_BUDGET_PER_CHARACTER for l in levels):
                error(number, "Party budgets line has an invalid party size or levels")
            else:
                party_levels = levels
                budgets = party_budgets(levels)
                found = {"low": int(low), "moderate": int(moderate), "high": int(high)}
                if found != budgets:
                    error(number, f"Party budgets should be Low {budgets['low']}, "
                                  f"Moderate {budgets['moderate']}, High {budgets['high']}")
        if total_line is None:
            error(None, "Encounter Balance is missing the '**Total:**' line")
        elif balance:
            number, (total_xp, label) = total_line
            expected_total = sum(count * xp for _, count, _, xp in balance.values())
            if int(total_xp) != expected_total:
                error(number, f"Total should be {expected_total} XP")
            if party_levels:
                expected = difficulty_for(expected_total, party_budgets(party_levels)).title()
                if label != expected:
                    error(number, f"Difficulty should be {expected}")

    if enemies and balance:
        for name in sorted(set(enemies) | set(balance)):
            if name not in balance:
                error(None, f"'{name}' is in The Enemy but not in Encounter Balance")
            elif name not in enemies:
                error(None, f"'{name}' is in Encounter Balance but not in The Enemy")
            elif enemies[name] != balance[name][1]:
                error(None, f"'{name}' count differs between The Enemy and Encounter Balance")

    if "Statistics" in by_title:
        blocks = {c.title: c for c in by_title["Statistics"].children()}
        for name in balance:
            if name not in blocks:
                error(None, f"Statistics has no stat block heading for '{name}'")
        for name, block in blocks.items():
            if balance and name not in balance:
                error(None, f"Stat block '{name}' is not in Encounter Balance")
            text = "\n".join(t for _, t in block.lines)
            for field in STAT_FIELDS:
                if f"**{field}**" not in text:
                    error(None, f"Stat block '{name}' is missing **{field}**")
            if not re.search(r"\|\s*STR\s*\|\s*DEX\s*\|\s*CON\s*\|\s*INT\s*\|\s*WIS\s*\|\s*CHA\s*\|", text):
                error(None, f"Stat block '{name}' is missing the ability score table")
            challenge = CHALLENGE.search(text)
            if not challenge:
                error(None, f"Stat block '{name}' is missing '**Challenge** CR (XP XP)'")
            elif name in balance:
                cr, xp = challenge.group(1), int(challenge.group(2).replace(",", ""))
                if (cr_value(cr), xp) != (cr_value(balance[name][2]), balance[name][3]):
                    error(None, f"Stat block '{name}' Challenge {cr} ({xp} XP) does not match "
                                f"Encounter Balance CR {balance[name][2]} ({balance[name][3]} XP)")

    if "Scaling" in by_title:
        scaling = {c.title: c for c in by_title["Scaling"].children()}
        for title in ["Easier", "Harder"]:
            if title not in scaling or not scaling[title].has_text():
                error(None, f"Scaling needs a non-empty '{title}' subsection")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Markdown file containing the encounter")
    parser.add_argument("--section", required=True, help="The encounter's heading text")
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
        print(f"PASS: '{args.section}' matches the encounter template.")
        return 0
    print(f"FAIL: {len(errors)} problem(s) in '{args.section}':")
    for line, message in errors:
        print((f"  line {line}: " if line else "  ") + message)
    return 1


if __name__ == "__main__":
    sys.exit(main())
