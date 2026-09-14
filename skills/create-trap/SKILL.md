---
name: create-trap
description: Creates thematic D&D 5e traps with a telegraph, trigger, detection and disable DCs, a mechanical effect, and magical countermeasures, all scaled to party level. Use when the user wants a trap, a security measure, or a dangerous mechanism for a dungeon, vault, or building.
license: CC0-1.0
compatibility: Requires Python 3
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
---

# Create Trap

Traps are functional security measures, workplace hazards, or decaying structures that fit the place they are in. Every trap warns the party, can be found and disabled, and changes the party's situation when it goes off.

## Workflow

1. **Gather the inputs.**
   - Party level.
   - Where the trap is and who built it, or what caused it.
   - Severity: Nuisance or Deadly.
   - Where the trap goes: a new document, or a heading inside an existing one (a dungeon room, a location).
   - Read related campaign files (Locations, Organizations, History) for details that shape the trap.
2. **Copy [assets/trap-template.md](assets/trap-template.md)** into the target document.
   - The trap heading can sit at any level. Keep every subheading one level below it.
3. **Fill in every placeholder** using the rules below. Where the template offers a choice with OR, keep one option.
4. **Validate.** Run:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_trap.py "{{document_path}}" --section "{{trap_name}}"`
   Fix every problem it lists and run it again. Repeat until it prints `PASS`.
5. **Report** the trap's location and give a one-line summary to the user.

## Rules

### Purpose

Every trap has one purpose:

- **Intentional Security:** keeps intruders out (a vault lock, a poisoned needle in a jewelry box).
- **Environmental Hazard:** a natural or workplace danger (a rotting mine floor, a leaking steam pipe).
- **Execution:** built to kill or maim (a spiked pit, a falling blade).
- **Alarm:** alerts the inhabitants (a bell, a thunder glyph).
- **Deterrent:** slows, weakens, or isolates intruders (a glue trap, a slowing gas).

### Workplace Logic

The trap makes sense for the people who built it or for the state the place is in now. A library might protect its vault from teleporting thieves. A forge might pour molten lead. A room the inhabitants walk through every day has no blade trap unless there is a clear bypass.

### Telegraph

Every trap has a sensory clue the party notices before it triggers, such as shifting stone, faint clicking, scuff marks, dried blood on a latch, a draft, or the smell of oil. The clue prompts players to look closer. It is never hidden behind a check.

### Severity and Numbers

| Severity | DCs (Detection, Save, Disable) | Attack Bonus |
| -------- | ------------------------------ | ------------ |
| Nuisance | 10-15                          | +3 to +5     |
| Deadly   | 15-20                          | +6 to +9     |

Damage comes from the **damage-severity** skill's table for the party level and severity. Use one of the dice options it lists.

### Detection

One or two checks, using Wisdom (Perception) or Intelligence (Investigation). Each says what a success reveals.

### Effect

- Exactly one of a saving throw or an attack roll.
- **Damage** is dice and a damage type, or None.
- **Consequence** changes the party's situation beyond hit points. A trap with no damage must have one. Every consequence is one of these, with exact mechanics and a duration:
  - **Condition:** a condition, who it affects, and how it ends.
  - **Environmental Complication:** a lasting change to the area, such as difficult terrain, heavy obscurement, or a sealed exit.
  - **Resource Attrition:** a specific loss, such as a destroyed shield, 1d4 ruined rations, or an expended spell slot.
  - **Alarm:** who is alerted and what they do, such as the next encounter starting with the party surprised.

### Countermeasures

- **Disable:** one ability check with a DC, usually Dexterity (Thieves' Tools) or Strength (Athletics), and what disabling looks like.
- **Magic:** one or two spells that bypass or stop the trap, and how.

## Limits

- Do not add sections or fields that are not in the template.
- Every DC, attack bonus, and damage roll follows the Severity and Numbers rules.
