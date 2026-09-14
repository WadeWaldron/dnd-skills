---
name: create-puzzle
description: Creates in-world D&D 5e environmental obstacles with several skill approaches, magic and tool solutions, and a mechanical fail-forward cost for each failure. Use when the user wants a puzzle, an obstacle, an environmental challenge, or a non-combat room that isn't a riddle or mini-game.
license: CC0-1.0
compatibility: Requires Python 3
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
---

# Create Puzzle

Puzzles here are environmental obstacles, not riddles. Each one is a natural part of the place: a collapsed floor, a grease fire, deep mud, a flooded passage. The party gets past by choosing an approach. A failure still gets them through, but it costs them something.

## Workflow

1. **Gather the inputs.**
   - Party level.
   - The place: what it was built for, and why it is an obstacle now (abandoned, decaying, occupied, malfunctioning, or natural geography).
   - Where the puzzle goes: a new document, or a heading inside an existing one (a dungeon room, a location).
   - Read related campaign files (Locations, History) for details that shape the obstacle.
2. **Copy [assets/puzzle-template.md](assets/puzzle-template.md)** into the target document.
   - The puzzle heading can sit at any level. Keep every subheading one level below it.
   - Add a third approach or a second spell by repeating the entry.
3. **Fill in every placeholder** using the rules below.
4. **Validate.** Run:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_puzzle.py "{{document_path}}" --section "{{puzzle_name}}"`
   Fix every problem it lists and run it again. Repeat until it prints `PASS`.
5. **Report** the puzzle's location and give a one-line summary to the user.

## Rules

### Workplace Logic

The obstacle exists because of what the place is or was, not because adventurers showed up. Ask: "Would this be here if nobody came?" A kitchen fire exists because of cooking. A door that needs three golden spoons only exists for players.

No abstract riddles, collect-the-item gates, or mini-games such as chess tiles, glowing orbs, or numbered levers.

### Resolving the Puzzle

A character picks one solution:

- **Approaches:** 2 or 3 skill checks, each using a different skill. One check decides the outcome. On a success the party gets through. On a failure the party still gets through and pays that approach's cost.
- **Magic:** 1 or 2 spells that solve the obstacle with no check. The spell slot is the cost.
- **Practical Solution:** 1 tool check that works like an approach, with its own DC and cost.

### DCs

Each check is labeled Easy (DC 10), Moderate (DC 15), or Hard (DC 20), matching the **difficulty-class** skill. An easier approach can carry a harsher cost.

### Fail-Forward Costs

Every approach and the practical solution have one cost, which starts with its type. Each cost has exact mechanics:

- **Damage:** dice, a damage type, and severity, such as `2d10 fire damage (Nuisance)`. Use the dice from the **damage-severity** skill's table for the party level and severity. Say who takes it.
- **Exhaustion:** how many levels of exhaustion, and who gains them.
- **Resource Loss:** exactly what is lost, such as a broken shield, 1d4 ruined rations, or 50 feet of rope.
- **Alert:** the next encounter starts with the party surprised or the enemies gaining +2 AC for the first round.
- **Tactical Disadvantage:** the exact situation the party arrives in, such as split up, prone, or one character isolated on the far side.
- **High Cost Path:** the party takes a longer route that adds a Low or Moderate encounter, built with the **create-encounter** skill.

## Examples

### The Kitchen
- **Good:** A grease fire has drawn smoke mephits. The party must put out the fire, or use *Control Flames*, to reach the pantry.
- **Bad:** A magic door that won't open until the party finds three golden spoons hidden in the cupboards.

### The Forge
- **Good:** The furnace is overheating and the heat is dangerous. The party must repair a cooling pipe or vent the steam to get through.
- **Bad:** Numbered levers (1-4-2-3) that must be pulled in order to unlock a weapon rack.

### The Barracks
- **Good:** The floor has partly collapsed. The party must cross narrow support beams or use magic to reach the far side.
- **Bad:** A chessboard floor where characters can only move like knights to avoid pressure plates.

### The Swamp
- **Good:** A stretch of deep, sucking mud. The party can use *Levitate*, Survival or Investigation to find firm ground, or leatherworker's tools to make swamp shoes.
- **Bad:** Giant stone frogs that must be fed swamp berries in a certain order to raise a bridge.

## Limits

- Do not add sections or fields that are not in the template.
- Every check has a DC that matches its label, and every failure has a cost from the list above.
