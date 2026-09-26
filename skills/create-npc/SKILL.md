---
name: create-npc
description: Creates a D&D 5e non-player character with appearance, voice, goals, secrets, connections, social check DCs, and what they can offer the party, plus an optional stat block. Use when the user wants an NPC, a shopkeeper, a villain, a quest giver, a random townsperson, or any named character the party will meet.
license: CC0-1.0
compatibility: Requires Python 3
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
---

# Create NPC

NPCs are people the DM can run at the table without improvising: how they look and sound, what they want, what they hide, who they are tied to, and what it takes to get something from them.

## Workflow

1. **Gather the inputs.**
   - The NPC's role, and where the party meets them.
   - Any details the user already has in mind, such as a name, species, attitude, or secret.
   - Whether the NPC might fight.
   - Where the NPC goes: by default, a new file in the campaign's `NPCs/` folder named after them (for example, `NPCs/Marda Voss.md`). When the user asks, a heading inside an existing document instead (a location, a shop).
   - Read related campaign files (NPCs, Locations, Organizations) for names, factions, and relationships. Check `NPCs/` for an existing NPC with the same name or role.
2. **Copy [assets/npc-template.md](assets/npc-template.md)** into the target document.
   - In its own file, the NPC's name is the top heading. Inside another document, the NPC heading can sit at any level. Keep every subheading one level below it.
   - Add a second or third connection by repeating the entry.
3. **Fill in every placeholder** using the rules below.
4. **Validate.** Run:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_npc.py "{{document_path}}" --section "{{npc_name}}"`
   Fix every problem it lists and run it again. Repeat until it prints `PASS`.
5. **Report** the NPC's location and give a one-line summary to the user.

## Rules

### Random Prompts

When the user asks for a random NPC, or leaves details open, run:

`python3 ${CLAUDE_SKILL_DIR}/scripts/roll_npc.py`

Add `--tables "Voice,Secret"` to roll on only some tables. Each result is a prompt, not a finished detail. Fill it in to fit the NPC, their role, and the setting. The tables are in [references/npc-tables.md](references/npc-tables.md).

### Attitude and DCs

Attitude sets the DC for every social check, matching the **difficulty-class** skill:

| Attitude    | Base DC |
| ----------- | ------- |
| Friendly    | 10      |
| Indifferent | 15      |
| Hostile     | 20      |

Each approach in the Social Play table uses the base DC, or 5 higher or lower when something about the NPC makes that approach easier or harder. The Notes column says what works and why.

### Social Play

- **Leverage:** something the party can find or do that gives advantage on the NPC's social checks, such as a debt, a secret, or a favor to someone they care about.
- **Won't Budge:** what the NPC refuses no matter the roll, in one clear line.
- **Offers:** exactly what the party can get: a specific piece of information, access to a place or person, goods at a named price, or help with a named task.

### Wants

- **Goal** says what they are doing about it right now, so the NPC has something going on when the party arrives.
- **Secret** says what changes if the party learns it: who reacts, and how.

### Connections

One to three entries. Each names a person, faction, or place, and says what the relationship means for the party. Link to the matching campaign file when one exists.

### Stat Block

When the NPC might fight, use the **lookup-creatures** skill to find a creature that fits (such as Commoner, Guard, Noble, or Mage), or the **customize-creature** skill to reskin one. Put its name in **Stat Block**. Otherwise, write None.

## Limits

- Do not add sections or fields that are not in the template.
- Every social DC follows the Attitude and DCs rule.
