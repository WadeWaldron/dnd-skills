#!/usr/bin/env python3
"""
Initialize a D&D campaign folder.

Creates the canonical campaign folders and the instruction files agents read:
AGENTS.md holds the instructions, and CLAUDE.md imports it for Claude Code.
Existing content is never moved, deleted, or overwritten.
"""

import argparse
import os
import re
from pathlib import Path

FOLDERS = [
    "NPCs",
    "Players",
    "Monsters",
    "Magic-Items",
    "Encounters",
    "Campaign",
    "Rules",
    "History",
    "Religion",
    "Locations",
    "Organizations",
    "Lore",
    "Sessions",
]

# Checked in order; the first that exists is used.
AGENTS_CANDIDATES = ["AGENTS.md", ".agents/AGENTS.md"]
CLAUDE_CANDIDATES = ["CLAUDE.md", ".claude/CLAUDE.md"]

ASSETS = Path(__file__).parent / "assets"
AGENTS_IMPORT = re.compile(r"^@(\S*AGENTS\.md)\s*$")


def find_existing(root, candidates):
    for candidate in candidates:
        path = root / candidate
        if path.is_file():
            return path
    return None


def create_folders(root):
    created, present = [], []
    for name in FOLDERS:
        path = root / name
        if path.is_dir():
            present.append(name)
        else:
            path.mkdir()
            created.append(name)
    others = sorted(
        p.name for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(".")
        and p.name.lower() not in {f.lower() for f in FOLDERS}
    )
    return created, present, others


def ensure_agents(root):
    existing = find_existing(root, AGENTS_CANDIDATES)
    if existing:
        return existing, f"Already present: {existing.relative_to(root)} (left unchanged)"
    path = root / "AGENTS.md"
    path.write_text((ASSETS / "AGENTS.md").read_text())
    return path, "Created: AGENTS.md"


def ensure_claude(root, agents_path):
    claude_path = find_existing(root, CLAUDE_CANDIDATES) or root / "CLAUDE.md"
    rel = Path(os.path.relpath(agents_path, claude_path.parent)).as_posix()
    import_line = f"@{rel}"
    name = claude_path.relative_to(root)

    if not claude_path.exists():
        claude_path.write_text(import_line + "\n")
        return f"Created: {name} with {import_line}"

    lines = claude_path.read_text().splitlines()
    kept, removed = [], []
    for line in lines:
        match = AGENTS_IMPORT.match(line.strip())
        if match and match.group(1) != rel:
            if (claude_path.parent / match.group(1)).is_file():
                kept.append(line)
            else:
                removed.append(line.strip())
            continue
        kept.append(line)

    if import_line in (l.strip() for l in kept):
        if not removed:
            return f"Already present: {name} imports {import_line} (left unchanged)"
        claude_path.write_text("\n".join(kept) + "\n")
    else:
        claude_path.write_text("\n".join([import_line] + kept) + "\n")

    result = f"Updated: {name} now imports {import_line}"
    if removed:
        result += f" (removed broken import: {', '.join(removed)})"
    return result


def main():
    parser = argparse.ArgumentParser(description="Initialize a D&D campaign folder.")
    parser.add_argument("campaign", nargs="?", default=".",
                        help="Campaign root folder (default: current directory)")
    args = parser.parse_args()

    root = Path(args.campaign).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    created, present, others = create_folders(root)
    agents_path, agents_result = ensure_agents(root)
    claude_result = ensure_claude(root, agents_path)

    print(f"Campaign: {root}\n")
    print("Created folders:", ", ".join(created) or "none")
    print("Already present:", ", ".join(present) or "none")
    print("Other folders:", ", ".join(others) or "none")
    print()
    print("AGENTS.md ->", agents_result)
    print("CLAUDE.md ->", claude_result)


if __name__ == "__main__":
    main()
