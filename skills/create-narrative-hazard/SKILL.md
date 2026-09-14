---
name: create-narrative-hazard
description: Creates a high-tension, non-combat D&D encounter run with Progress and Danger clocks, Position, Edges, and Complications. Use when the user wants a narrative hazard, a skill challenge, a chase, an escape, or a "fiction-first" sequence such as fleeing a burning building or crossing a collapsing bridge.
license: CC0-1.0
compatibility: Requires Python 3
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
---

# Create Narrative Hazard

A narrative hazard is a non-combat encounter modeled after *Blades in the Dark* and adapted to D&D. Players describe what their characters do, and the fiction decides which skill or ability they roll. The consequences are mechanical: clocks, position, damage, conditions, and resources. Every roll moves the scene forward, and the party always reaches the goal. The Danger Clock decides what it costs them.

## Workflow

1. **Gather the inputs.**
   - Party level.
   - The goal (what the party is trying to reach or do) and the threat (what is working against them).
   - Where the hazard goes: a new document, or a heading inside an existing one (a dungeon room, a location, a session plan).
   - Read related campaign files (Locations, NPCs, Encounters) for names, tone, and details.
2. **Copy [assets/hazard-template.md](assets/hazard-template.md)** into the target document.
   - The hazard heading can sit at any level. Keep every subheading one level below it, and the two Ending subheadings one level below Ending.
3. **Fill in every placeholder.** Placeholders are the text in square brackets. Follow the rules below.
4. **Validate.** Run:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_hazard.py "{{document_path}}" --section "{{hazard_name}}"`
   Fix every problem it lists and run it again. Repeat until it prints `PASS`.
5. **Report** the hazard's location and give a one-line summary to the user.

## Limits

- Copy all fixed text from the template word for word: the Position DCs, the Outcomes table, every Edge and Complication effect, and the Ending opening line.
- Use only the Edges and Complications in the template, in the template's order. Do not add, remove, rename, or reword them.
- Only the *In this hazard*, Opportunity, and Ending entries are written fresh. They describe how a fixed mechanic shows up in this scene. They never add a new mechanical effect.
- Do not add sections, tables, or rules that are not in the template.

## Rules

### Clocks

- **Progress Clock:** the party's goal.
- **Danger Clock:** the threat.
- Each clock has 4 segments (quick), 6 segments (standard), or 8 segments (long). The two clocks can differ in size.
- A normal action ticks exactly one clock. A targeted action ticks the Danger Clock on a failure and no clock on a success.
- The hazard ends as soon as either clock fills.

### Position

Position applies to the whole party. It sets the DC and the Damage dice. Only the Position Improves and Position Degrades results change it.

DCs are 13 (Controlled), 15 (Risky), and 17 (Desperate) at every level. Damage is sized so the hazard costs resources without killing a healthy character:

- **Risky:** 1d6 per 3 party levels, rounded up.
- **Desperate:** double the Risky dice.
- **Controlled:** half the Risky dice, rounded up (1d4 at levels 1-3).

| Party Level | Controlled | Risky | Desperate |
| ----------- | ---------- | ----- | --------- |
| 1-3         | 1d4        | 1d6   | 2d6       |
| 4-6         | 1d6        | 2d6   | 4d6       |
| 7-9         | 2d6        | 3d6   | 6d6       |
| 10-12       | 2d6        | 4d6   | 8d6       |
| 13-15       | 3d6        | 5d6   | 10d6      |
| 16-18       | 3d6        | 6d6   | 12d6      |
| 19-20       | 4d6        | 7d6   | 14d6      |

Temporary Respite always uses the Controlled dice.

### Taking Turns

- Every character gets a turn before anyone takes a second one. The order within a round is flexible, and the DM can make exceptions when the fiction calls for it.
- On their turn, a player describes an action. The DM picks the ability or skill that fits, and the player rolls against the current position's DC.
- **Help:** A character can use their turn to help another. The helped roll has advantage.
- **Spells and features:** A spell or feature that clearly accomplishes the action counts as a success on the Outcomes table without a roll.

### Outcomes

The Outcomes table in the template is the rule for each roll.

- **Result steps:** From lowest to highest, results are Fail by 5+, Fail by 1-4, Succeed by 0-4, and Succeed by 5+. Clear Path moves a result one step up and Cascading Failure moves it one step down. A result can't move past either end.
- **Targeted action:** A player can aim an action at one Edge instead of the goal (for example, stabilizing a platform to improve position). It is either a success or a failure, with no partial result. A success gains that Edge and ticks no clock. A failure ticks the Danger Clock and gives no Edge or Complication.

### Edges and Complications

The template's effect text is the rule for each Edge and Complication. For each one, the *In this hazard* line describes what it looks like in this scene.

- **Damage** names a damage type that fits the scene.
- **Condition** names which of the listed conditions fits the scene.

### Opportunities

Opportunities are optional prizes the party can go after instead of pushing toward the goal.

- Write at least two for each hazard.
- The Opportunity Edge reveals one. Claiming it takes a successful targeted action.
- Each Opportunity is one of these:
  - **Treasure:** a reward that lasts beyond the hazard, such as loot, a magic item, a clue, or a grateful NPC. The effect says exactly what the party gains.
  - **Aid:** something that helps within the hazard. The effect names one Edge (not Opportunity). Any character can spend an Aid at any time to gain that Edge. An unspent Aid is gone when the hazard ends.

### Ending

The party always reaches the goal.

- **Progress Clock fills:** The party reaches the goal cleanly. Describe how, and where they end up.
- **Danger Clock fills:** The party still reaches the goal, but pays for it:
  - **Mechanical:** Choose the one that fits the threat. Either every character takes the Desperate damage dice for the party level with a fitting damage type, or every character gains 1 level of exhaustion. There is no saving throw.
  - **Narrative:** A lasting setback, such as an alerted enemy, a damaged environment, or a harder next scene.
