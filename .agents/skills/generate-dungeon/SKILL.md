---
name: generate-dungeon
description: This skill will generate a dungeon by selecting and customizing a variety of room types to create a structured and engaging adventure.
---

# Generate Dungeon

This skill will generate a dungeon by drawing from a catalog of specific room types to create a balanced and thematic experience.

When the skill is executed, it will:
1. Ask the user for the theme or setting of the dungeon (e.g., "Sunken Temple of the Kraken").
2. Ask for the desired number of rooms (defaulting to 5 or more).
3. Generate details for each room by selecting from the files in `room-types/`:
    - [The Combat](room-types/01-combat.md)
    - [The Cache](room-types/02-cache.md)
    - [The Sidekick](room-types/03-sidekick.md)
    - [The Offshoot](room-types/04-offshoot.md)
    - [The Foreshadowing](room-types/05-foreshadowing.md)
    - [The History](room-types/06-history.md)
    - [The Oddity](room-types/07-oddity.md)
    - [The Forge](room-types/08-forge.md)
    - [The Factions](room-types/09-factions.md)
    - [The Map](room-types/10-map.md)
4. Present the full dungeon layout, including descriptions and encounter details for each room, ensuring they are tied together by the chosen theme.

## Step 1: Get Dungeon Theme

**If the theme is not provided:**
1. Ask the user: "What is the theme or setting of the dungeon? (e.g., 'A clockwork laboratory gone rogue')"
2. Wait for the user's response and store it as `dungeon_theme`.

**If the theme is provided:**
1. Store the provided theme as `dungeon_theme`.

## Step 2: Get Number of Rooms

**If the number of rooms is not provided:**
1. Ask the user: "How many rooms should this dungeon have? (Typically 3-7 works well for a single session)"
2. Wait for the user's response and store it as `room_count`.

## Step 3: Generate Rooms

1. Randomly select or intentionally choose `room_count` types from the `room-types/` directory.
2. For each selected room, use the corresponding file as a guide to generate content that fits the `dungeon_theme`.
3. Ensure at least one **Combat** room is included if the `room_count` is 3 or more.
4. Integrate the rooms into a cohesive narrative or layout.
