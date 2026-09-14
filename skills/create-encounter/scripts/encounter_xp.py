#!/usr/bin/env python3
"""
Calculate XP budgets and check encounter difficulty using the 2024 D&D rules.

The party's budget for each difficulty is the sum of every character's budget
for their level. An encounter's difficulty is the lowest budget its total
monster XP fits within. There is no monster-count multiplier.

Without --monsters, prints the party's budgets. With --monsters, also prints
the encounter's difficulty and an Encounter Balance block for the write-up.
"""

import argparse
import json
import sys

DIFFICULTIES = ["low", "moderate", "high"]

# XP budget per character by level (2024 Dungeon Master's Guide)
XP_BUDGET_PER_CHARACTER = {
    1: (50, 75, 100),
    2: (100, 150, 200),
    3: (150, 225, 400),
    4: (250, 375, 500),
    5: (500, 750, 1100),
    6: (600, 1000, 1400),
    7: (750, 1300, 1700),
    8: (1000, 1700, 2100),
    9: (1300, 2000, 2600),
    10: (1600, 2300, 3100),
    11: (1900, 2900, 4100),
    12: (2200, 3700, 4700),
    13: (2600, 4200, 5400),
    14: (2900, 4900, 6200),
    15: (3300, 5400, 7800),
    16: (3800, 6100, 9800),
    17: (4500, 7200, 11700),
    18: (5000, 8700, 14200),
    19: (5500, 10700, 17200),
    20: (6400, 13200, 22000),
}


def party_budgets(levels):
    totals = [0, 0, 0]
    for level in levels:
        for index, amount in enumerate(XP_BUDGET_PER_CHARACTER[level]):
            totals[index] += amount
    return dict(zip(DIFFICULTIES, totals))


def difficulty_for(total_xp, budgets):
    for difficulty in DIFFICULTIES:
        if total_xp <= budgets[difficulty]:
            return difficulty
    return "beyond high"


def describe_party(levels):
    if len(set(levels)) == 1:
        return f"{len(levels)} characters, level {levels[0]}"
    return f"{len(levels)} characters, levels {', '.join(str(l) for l in levels)}"


def parse_monsters(text):
    monsters = json.loads(text)
    if not isinstance(monsters, list) or not monsters:
        raise ValueError("--monsters must be a non-empty JSON list")
    for monster in monsters:
        for key in ("name", "cr", "xp", "count"):
            if key not in monster:
                raise ValueError(f"Each monster needs name, cr, xp, and count; missing '{key}' in {monster}")
        if not isinstance(monster["xp"], int) or not isinstance(monster["count"], int) or monster["count"] < 1:
            raise ValueError(f"xp and count must be whole numbers, count at least 1, in {monster}")
    return monsters


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    party = parser.add_mutually_exclusive_group(required=True)
    party.add_argument("--party-level", type=int, help="Level of every character (use with --party-size)")
    party.add_argument("--levels", type=str, help='Comma-separated level of each character, e.g. "5,5,6,4"')
    parser.add_argument("--party-size", type=int, help="Number of characters (use with --party-level)")
    parser.add_argument("--monsters", type=str,
                        help='JSON list: [{"name": "Orc", "cr": "1/2", "xp": 100, "count": 3}]')
    parser.add_argument("--target", choices=DIFFICULTIES, help="Target difficulty (requires --monsters)")
    args = parser.parse_args()

    if args.party_level is not None:
        if args.party_size is None or args.party_size < 1:
            parser.error("--party-level requires --party-size of at least 1")
        levels = [args.party_level] * args.party_size
    else:
        if args.party_size is not None:
            parser.error("--party-size is only used with --party-level")
        try:
            levels = [int(l) for l in args.levels.split(",")]
        except ValueError:
            parser.error("--levels must be comma-separated whole numbers")
    if any(level not in XP_BUDGET_PER_CHARACTER for level in levels):
        parser.error("Character levels must be from 1 to 20")
    if args.target and not args.monsters:
        parser.error("--target requires --monsters")

    budgets = party_budgets(levels)
    print(f"Party: {describe_party(levels)}")
    print("--- XP Budgets ---")
    for difficulty in DIFFICULTIES:
        print(f"{difficulty.capitalize():<9} {budgets[difficulty]}")

    if not args.monsters:
        return 0

    try:
        monsters = parse_monsters(args.monsters)
    except ValueError as error:
        print(f"Error: {error}")
        return 2

    total = sum(m["xp"] * m["count"] for m in monsters)
    difficulty = difficulty_for(total, budgets)
    print(f"Total XP: {total}")
    print(f"Difficulty: {difficulty.upper()}")

    status = 0
    if args.target:
        target_index = DIFFICULTIES.index(args.target)
        floor = budgets[DIFFICULTIES[target_index - 1]] if target_index > 0 else 0
        ceiling = budgets[args.target]
        if difficulty == args.target:
            print(f"STATUS: SUCCESS (Matches target {args.target.upper()})")
        else:
            status = 1
            print(f"STATUS: FAIL (Target {args.target.upper()}, encounter is {difficulty.upper()})")
            if total > ceiling:
                print(f"ADVICE: Remove at least {total - ceiling} XP of monsters.")
            else:
                print(f"ADVICE: Add more than {floor - total} XP of monsters, up to {ceiling - total} XP.")

    print()
    print("--- Encounter Balance (copy into the write-up) ---")
    for m in monsters:
        print(f"- {m['count']} × {m['name']} (CR {m['cr']}, {m['xp']} XP each) = {m['xp'] * m['count']} XP")
    print(f"- Party budgets ({describe_party(levels)}): "
          f"Low {budgets['low']}, Moderate {budgets['moderate']}, High {budgets['high']}")
    label = "Beyond High" if difficulty == "beyond high" else difficulty.capitalize()
    print(f"- **Total: {total} XP ({label} difficulty)**")
    return status


if __name__ == "__main__":
    sys.exit(main())
