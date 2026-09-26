#!/usr/bin/env python3
"""
Roll NPC prompts from references/npc-tables.md.

Each table in the reference file is a '## Heading' followed by a markdown
table whose first column is the die result. Rolls one prompt per table.
"""

import argparse
import random
import re
import sys
from pathlib import Path

TABLES_PATH = Path(__file__).parent.parent / "references" / "npc-tables.md"
HEADING = re.compile(r"^##\s+(.+?)\s*$")
ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*$")


def load_tables():
    tables = {}
    current = None
    for line in TABLES_PATH.read_text(encoding="utf-8").splitlines():
        heading = HEADING.match(line)
        row = ROW.match(line)
        if heading:
            current = heading.group(1)
            tables[current] = []
        elif row and current:
            tables[current].append(row.group(2))
    return {name: rows for name, rows in tables.items() if rows}


def main():
    tables = load_tables()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tables", type=str,
                        help=f"Comma-separated tables to roll on (default: all). Available: {', '.join(tables)}")
    args = parser.parse_args()

    names = list(tables)
    if args.tables:
        requested = [n.strip() for n in args.tables.split(",") if n.strip()]
        lookup = {n.lower(): n for n in tables}
        unknown = [n for n in requested if n.lower() not in lookup]
        if unknown:
            print(f"Unknown table(s): {', '.join(unknown)}. Available: {', '.join(tables)}")
            return 2
        names = [lookup[n.lower()] for n in requested]

    for name in names:
        rows = tables[name]
        roll = random.randint(1, len(rows))
        print(f"{name} (d{len(rows)}: {roll}): {rows[roll - 1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
