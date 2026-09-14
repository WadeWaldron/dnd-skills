---
name: create-treasure
description: Creates thematic, level-appropriate D&D 5e loot, from pocket change on a single creature to a full treasure hoard. Use when the user wants treasure, loot, a reward, or to know what the party finds on a defeated enemy or in a vault.
license: CC0-1.0
---

# Create Treasure

This skill generates loot that feels like a natural part of the environment while maintaining balance for the player characters.

## Step 1: Establish Context
Treasure should never feel "randomly" placed. Answer these questions first:
1.  **Who Owned This?** (e.g., A wizard, a bandit king, a forgotten temple, a natural predator).
2.  **Where Is It?** (e.g., A locked chest, a hidden alcove, scattered on a floor, inside a creature's stomach).

## Step 2: Design Rules

### Rule 1: Thematic Integrity
Loot must match the room's purpose and the owner's nature.
- **Example:** A pirate's stash contains stamped coins, exotic spices, and maps; a necromancer's cache contains onyx gems, preserved organs, and scrolls of *Ray of Sickness*.
- **Forbidden:** Finding a pristine *Holy Avenger* in a simple goblin cave without significant story justification.

### Rule 3: Tiered Rewards
Categorize treasure into three types:
- **Liquid Assets:** Coinage (CP, SP, GP, PP) and trade bars.
- **Valuables:** Gems, art objects, jewelry, and rare materials (silks, spices).
- **Utility & Power:** Potions, scrolls, ammunition, and permanent magic items.

### Rule 4: Balanced Distribution
Use the party's level to determine the "Weight" of the treasure.
- **Minor Cache:** Consumables (1-2) + Small amount of coin.
- **Major Hoard:** Permanent magic item (1) + Consumables (2-4) + Significant valuables.

## Step 3: Architecture of Discovery
Treasure shouldn't always be "free."
1.  **The Barrier:** Is it locked (DC 15 Thieves' Tools), trapped (DC 15 investigation/perception), or hidden (DC 15 Investigation)?
2.  **The Identity:** Use the `identify` spell or a relevant skill check (Arcana for magic, History for art, Nature for poisons/herbs) to understand unusual items.

## Step 4: Scale the Reward
Use the [treasure tables](references/treasure-tables.md) or the following guidelines:
- **Levels 1-4:** 1st-level scrolls/potions, gems (10-50 gp).
- **Levels 5-10:** 2nd/3rd-level scrolls, +1 weapons/armor, gems (100-500 gp).
- **Levels 11+:** Rare+ items, major art objects (1,000+ gp).

## Terminology

### Challenge (CR)
"Challenge" refers to the **Challenge Rating (CR)** of the creature(s) defeated. Higher CR monsters guard more wealth and more powerful magic.

### Individual Treasure
- **What it is:** Personal pocket change and trinkets found on a single creature.
- **When to use:** Use when looting basic enemies after a minor skirmish (e.g., a single bandit or a lone beast).
- **Contents:** Primarily currency (CP, SP, GP, PP). Rarely contains magic items.

### Treasure Hoard
- **What it is:** A significant collection of relative wealth stored in a chest, vault, or lair.
- **When to use:** Use for major milestones, bosses, or at the end of a dungeon.
- **Contents:** Significant currency, gems/art objects, and magic items.

## Treasure Tables

Individual treasure and treasure hoard tables by Challenge are in [references/treasure-tables.md](references/treasure-tables.md).
