---
name: lookup-creatures
description: A skill that looks up creatures from D&D 5e based on criteria. Useful for finding appropriate monsters to build encounters.
---

# Lookup Creatures

This skill is used for finding thematic and level-appropriate monsters. It supports a two-phase workflow: **Discovery** (finding candidates) and **Detail** (retrieving full statblocks).

## Phase 1: Discovery (Thematic Search)

Use this to find a "menu" of potential monsters based on theme, environment, and XP budget. By default, it returns a compact summary table.

### Filter Parameters:
- `--target-xp`: Optional. Find creatures near this XP value.
- `--types`: Comma-separated list (e.g., "Undead, Monstrosity")
- `--environments`: Comma-separated list (e.g., "Forest, Swamp")
- `--sizes`: Comma-separated (e.g., "Medium, Large")
- `--max-results`: Default 10.

### Example:
`python3 lookup_creatures.py --environments "Forest" --types "Beast" --target-xp 450`

## Phase 2: Detail (Get Statblocks)

Once you have selected the specific creatures for your encounter, use this to retrieve their full statblocks.

### Specific Parameters:
- `--names`: Comma-separated list of exact creature names.
- `--full`: Force output of full Markdown statblocks.

### Example:
`python3 lookup_creatures.py --names "Dire Wolf, Wolf" --full`

## Guidelines for the Assistant
1. **Curate the Menu:** When searching for candidates, present the summary table to the user and explain *why* these monsters fit the requested theme.
2. **Mix Roles:** For complex encounters, search for a "Leader" (high XP target) and "Minions" (low XP target) separately to build a dynamic fight.
3. **Wait for Selection:** Do not fetch full statblocks until the encounter composition is finalized and validated.
