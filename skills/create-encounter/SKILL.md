---
name: create-encounter
description: Creates balanced D&D 5e combat encounters using the 2024 XP budget rules, or checks the difficulty of an existing encounter. Use when the user wants a combat encounter, a fight, a battle, or asks for an XP budget or whether an encounter is too easy or too hard.
license: CC0-1.0
compatibility: Requires Python 3
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
---

# Create Encounter

Builds a combat encounter from a Low, Moderate, or High XP budget (2024 Dungeon Master's Guide), picks thematic monsters, and writes it up with full stat blocks. It can also check the difficulty of an encounter that already exists.

All XP math comes from `scripts/encounter_xp.py`. Never calculate budgets, totals, or difficulty by hand.

## Party Input

Every run of `scripts/encounter_xp.py` describes the party in one of two ways:

- Same level: `--party-level 5 --party-size 4`
- Mixed levels: `--levels "5,5,6,4"`

## Creating an Encounter

### 1. Gather Requirements

1. **Party:** size and level of each character.
2. **Target Difficulty:** Low, Moderate, or High.
3. **Theme/Environment:** for example, "Underdark" or "Forest with Undead."

Ask for anything missing before continuing.

### 2. Get the XP Budget

Run:

`python3 ${CLAUDE_SKILL_DIR}/scripts/encounter_xp.py --party-level {{party_level}} --party-size {{party_size}}`

The budget for the target difficulty is the most monster XP the encounter can hold.

### 3. Find Creatures

Use the **lookup-creatures** skill (Discovery) to find 10-15 candidates that fit the theme.

- Search for a leader (higher XP) and minions (lower XP) separately for a more interesting fight.

### 4. Select Creatures

Draft specific monsters and quantities that fit the theme and budget (for example, "1 Wight and 4 Skeletons"). Do not fetch full stat blocks yet.

### 5. Check the Draft

Run:

`python3 ${CLAUDE_SKILL_DIR}/scripts/encounter_xp.py --party-level {{party_level}} --party-size {{party_size}} --target {{target}} --monsters '{{monsters_json}}'`

- `monsters_json` is a list like `[{"name": "Wight", "cr": "3", "xp": 700, "count": 1}, {"name": "Skeleton", "cr": "1/4", "xp": 50, "count": 4}]`, using the CR and XP from **lookup-creatures**.
- If the status is `FAIL`, adjust the monsters using the `ADVICE` line and run it again. Repeat until the status is `SUCCESS`.

### 6. Customize Creatures (Optional)

If the theme calls for creatures that aren't in the monster list (for example, pirates), use the **customize-creature** skill to reskin the checked monsters. Their CR, XP, and stats stay exactly the same.

### 7. Get Stat Blocks

Use **lookup-creatures** (Detail) with the exact `--names` and `--full` to get full stat blocks. Apply any reskinning from step 6.

### 8. Add a Tension Die (Optional)

A Visible Tension Die is a countdown to a big change in the fight. Use it for boss fights, climaxes, or fights with reinforcements or an unstable environment. Most encounters don't need one.

- **The Mechanic:** A d6 starts at 4 (high impact) or 6 (slow burn) and drops by 1 at the end of each round.
- **The Trigger:** The event happens when the die reaches 1.
- **Constraints:**
  - **Visible Doom:** The players can see the die.
  - **Foreshadowed:** The opening description hints at the event (for example, "The ceiling is cracked" or "A horn sounds in the distance").
  - **Grounded:** The event has a logical cause in the world, such as reinforcements heard earlier or visible structural damage.
  - **Ambiguous:** The timing is visible, but whether the event helps, hurts, or both can stay hidden until it happens.
  - **Stable:** Prefer environmental changes or tactical shifts over making monsters stronger.
- **Examples:**
  - *The Ceiling Collapses* (foreshadowed by dust falling from cracked beams): part of the map becomes difficult terrain or a new barrier.
  - *The Floodgates Shift* (foreshadowed by the growing sound of rushing water): a new path opens, or a current pushes combatants toward one area.
  - *Neutral Reinforcements* (foreshadowed by scavengers waiting nearby): they arrive and may loot from both sides or offer a way out through talking.

If used, describe the Tension Die under **Complications** in the write-up.

### 9. Write It Up

Fill in the [Encounter Template](assets/encounter-template.md).

- The encounter heading can sit at any level inside a larger document. Keep every subheading one level below it, and each stat block and the Easier and Harder headings one level below their section.
- Copy the **Encounter Balance** block exactly as `scripts/encounter_xp.py` printed it in the final successful run of step 5.
- Use the same creature names in The Enemy, Encounter Balance, and the stat block headings.
- Leave out The Objective when the goal is to defeat the enemy, and Complications when there are none. Remove the template's italic notes.

### 10. Validate

Run:

`python3 ${CLAUDE_SKILL_DIR}/scripts/validate_encounter.py "{{document_path}}" --section "{{encounter_name}}"`

Fix every problem it lists and run it again. Repeat until it prints `PASS`.

## Checking an Existing Encounter

Use this when the user asks how hard an encounter is, or wants an existing encounter checked.

1. Get the party's size and levels.
2. List every monster and its count. Get each monster's CR and XP from **lookup-creatures** (`--names`). For a reskinned monster, use its base creature.
3. Run `scripts/encounter_xp.py` with `--monsters`, plus `--target` if the user named a difficulty.
4. Report the difficulty and the party's budgets. If a target was given and the status is `FAIL`, pass along the `ADVICE`.
5. If the encounter document has an **Encounter Balance** block, replace it with the new block, after confirming with the user. Then run `scripts/validate_encounter.py` on it and report any problems.

## Guidelines

- **No manual math:** XP totals, budgets, and difficulty come only from `scripts/encounter_xp.py`.
- **Thematic integrity:** Pick monsters that make sense together. Don't mix desert and arctic creatures without a story reason.
- **Iterate with the script:** When a draft fails, use the `ADVICE` line instead of guessing.
