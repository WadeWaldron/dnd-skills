---
name: create-dungeon
description: This skill will generate a dungeon by selecting and customizing a variety of room types to create a structured and engaging adventure.
---

# Generate Dungeon

This skill generates a dungeon by applying the "5-Room Dungeon" philosophy to any scale. It maps the user's requested room count to the 5 mandatory narrative beats: **The Guardian, The Puzzle, The Setback, The Climax, and The Revelation.**

## Step 1: Gather Requirements
1.  **Theme/Setting:** (e.g., "Ancient Dwarven Library")
2.  **Room Count:** (How many physical rooms are needed?)
3. **Player Level and Party Size:** (e.g., Level 5, 4 players)

## Step 2: The Structural Strategy
Choose the architecture based on the room count:

| Room Count | Architecture | Description |
| :--- | :--- | :--- |
| **3-7 Rooms** | **Classic** | 1:1 mapping of rooms to narrative beats. |
| **8-15 Rooms** | **Phased** | Each "beat" is a cluster of 2-3 rooms. Use **Creative Grouping** (see below). |
| **16+ Rooms** | **Nested** | Each "beat" is its own specialized wing or level of the dungeon. |

### Creative Grouping (for Phased/Nested)
When a narrative beat spans multiple rooms, do not simply repeat the same room type. Mix types to create a cohesive sequence.
- **Non-Linear Navigation:** Design the dungeon with branching paths, loops, or multiple entrances. Ensure items needed for progression are placed in side-branches or early rooms that don't depend on the progress they unlock.
- **The Linked Challenge:** A combat room containing a key (Combat) followed by a locked library (History/Puzzle).
- **The Social Ecosystem:** Two rooms occupied by rival factions (Factions x2) that must be navigated.
- **The Multi-Part Obstacle:** A foreshadowing room (Foreshadowing) that hints at the mechanics of a complex trap (e.g., how to bypass a forge's heat) in the next room (History/Puzzle).
- **The Guarded Secret:** A guardian (Combat) defending a hidden mechanism (Oddity) that reveals a shortcut.
- **Dependency Map:** When designing connections, explicitly state the dependency (e.g., "[Room 3] contains the key for [Room 4]"). Verify [Room 3] is accessible before [Room 4].

## Step 3: Mapping the Beats
For every dungeon, ensure these 5 beats are present, regardless of scale:

1.  **The Guardian (Entrance):** A challenge (combat or social) that bars entry.
2.  **The Puzzle/Roleplay (Engagement):** A non-combat obstacle that reveals lore or requires interaction.
3.  **The Trick/Setback (The Twist):** A room that seems one way but is another, or forces a change in tactics.
4.  **The Climax (Big Battle):** The primary confrontation or challenge of the dungeon.
5.  **The Revelation (Reward/Lore):** The final room containing the treasure, the secret, or the bridge to the next adventure. Use the **create-treasure** skill for the final reward.

## Step 4: Component Selection
Generate details for each room by selecting appropriate categories from `room-types/`. For larger dungeons, group multiple types under a single beat.

- [The Combat](room-types/01-combat.md) (Best for Guardians and Climaxes)
- [The Cache](room-types/02-cache.md) (Best for Revelations)
- [The Sidekick](room-types/03-sidekick.md) (Good for Roleplay)
- [The Offshoot](room-types/04-offshoot.md) (Exploration/Flavor)
- [The Foreshadowing](room-types/05-foreshadowing.md) (Atmosphere/Setup)
- [The History](room-types/06-history.md) (Lore/Puzzles)
- [The Oddity](room-types/07-oddity.md) (Memorable moments/Tricks)
- [The Forge](room-types/08-forge.md) (Crafting/Upgrade opportunities)
- [The Factions](room-types/09-factions.md) (Social dynamics/Setbacks)
- [The Map](room-types/10-map.md) (Navigation/Discovery)

## Step 5: Puzzle and Encounter Generation
For each room in the dungeon, generate the necessary challenges:

1.  **Combat Encounters:** For any room that requires combat (typically **The Guardian** and **The Climax**, plus some **Phases** or **Wings**):
    *   Use the **create-encounter** skill to generate a balanced combat encounter.
    *   Ensure the encounter difficulty aligns with the dungeon's overall challenge level.
2.  **Non-Combat Puzzles/Hazards:** For rooms requiring exploration, engagement, or setbacks:
    *   Use the **create-puzzle** skill to generate thematic, in-world challenges.
    *   Ensure the puzzle's complexity and danger align with the room's narrative purpose.
3.  **Traps:** For rooms requiring hazards or security:
    *   Use the **create-trap** skill to design functional and logical traps.
    *   Ensure the trap's trigger and effect align with the room's original purpose.
4.  **Loot & Rewards:** For rooms containing significant treasures or the final revelation:
    *   Use the **create-treasure** skill to generate context-appropriate loot.
    *   Ensure rewards are balanced for the party's current tier and level.

## Step 6: Visual Representation & Validation
Include an ASCII map at the end of the dungeon generation to visualize the layout and verify the logical path.

### Map Generation Rules:
1.  **Symbols:** Use consistent symbols (e.g., `[#]` for rooms, `|` or `-` for corridors, `?` for hidden doors, `<` or `>` for stairs).
2.  **Labeling:** Number the rooms in the map to correspond with the room descriptions (e.g., `[1]`, `[2]`).
3.  **Non-Linearity:** Prioritize non-linear layouts. Use branching paths, loops, and shortcuts. A single room should often connect to more than one other room where possible.
4.  **Logical Verification (CRITICAL):** Before finalizing the map, trace the "Critical Path." Ensure any room that requires a specific item (key, password, amulet, etc.) has at least one path to it that first passes through a room containing that item.
5.  **Verticality:** For multi-level dungeons (like towers), use separate ASCII blocks for each floor or clearly indicate stairs/lifts.

**Example ASCII Map (Non-Linear):**
```text
       [3] (Offshoot - Has Key)
        |
[1] -- [2] -- [4] (Locked Door - Needs Key from [3])
        |      |
       [5] ----/
```

## Guidelines for the Assistant
1.  **Narrative Flow & Purpose:** Every room must have a clear reason for existing within the theme. Ask: "Why was this room built by the original inhabitants?" (e.g., A wizard's tower needs a Scrying Room or a Component Pantry, not just a "Puzzle Room"). 
2.  **Room Connectivity & Dependency:** Use the rules in **Step 6** to ensure the path is logically sound. Never create logical deadlocks.
3.  **Delegate Complexity:** 
    *   Use **create-encounter** for all combat math and statblocks.
    *   Use **create-puzzle** for all non-combat hazards and structural obstacles.
4.  **Scale Appropriately:** If the user asks for 10 rooms, group them by narrative beat (e.g., 2 rooms for The Guardian, 2 for The Puzzle, etc.). The layout should prioritize non-linearity and verticality.
5.  **The Twist:** Always include a "Setback" that feels significant—a physical collapse, a betrayal, or a tactical change that forces the players to rethink their approach.


