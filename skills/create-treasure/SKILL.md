---
name: create-treasure
description: Generates thematic and balanced loot for D&D encounters, ensuring rewards fit the dungeon context and party level.
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
Refer to standard D&D 5e treasure tables or use the following guidelines:
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

## Appendix: Reference Treasure Tables (5e)

### Individual Treasure: Challenge 0–4

| Result (d100)  | CP               | SP               | GP               | PP               |
| :------------- | :--------------- | :--------------- | :--------------- | :--------------- |
| **01–30**      | 5d6 (17)         | —                | —                | —                |
| **31–60**      | —                | 4d6 (14)         | —                | —                |
| **61–70**      | —                | 3d6 (10)         | 2d6 (7)          | —                |
| **71–95**      | —                | —                | 3d6 (10)         | —                |
| **96–00**      | —                | —                | —                | 1d6 (3)          |

### Individual Treasure: Challenge 5–10

| Result (d100)  | CP                 | SP               | EP                 | GP               | PP               |
| :------------- | :----------------- | :--------------- | :----------------- | :--------------- | :--------------- |
| **01–30**      | 4d6 × 100 (1,400)  | —                | 1d6 × 10 (35)      | —                | —                |
| **31–60**      | —                  | 6d6 × 10 (210)   | —                  | 2d6 × 10 (70)    | —                |
| **61–70**      | —                  | —                | 3d6 × 10 (105)     | 2d6 × 10 (70)    | —                |
| **71–95**      | —                  | —                | —                  | 4d6 × 10 (140)   | —                |
| **96–00**      | —                  | —                | —                  | 2d6 × 10 (70)    | 3d6 (10)         |

### Individual Treasure: Challenge 11–16

| Result (d100)  | SP                 | EP                 | GP                 | PP               |
| :------------- | :----------------- | :----------------- | :----------------- | :--------------- |
| **01–20**      | 4d6 × 100 (1,400)  | —                  | 1d6 × 100 (350)    | —                |
| **21–35**      | —                  | 1d6 × 100 (350)    | 1d6 × 100 (350)    | —                |
| **36–75**      | —                  | —                  | 2d6 × 100 (700)    | 1d6 × 10 (35)    |
| **76–00**      | —                  | —                  | 2d6 × 100 (700)    | 2d6 × 10 (70)    |

### Individual Treasure: Challenge 17+

| Result (d100)  | GP                   | PP                    |
| :------------- | :------------------- | :-------------------- |
| **01–15**      | 2d6 × 1,000 (7,000)  | 8d6 × 100 (2,800)     |
| **16–55**      | 1d6 × 1,000 (3,500)  | 1d6 × 1,000 (3,500)   |
| **56–00**      | 1d6 × 1,000 (3,500)  | 2d6 × 1,000 (7,000)   |

### Treasure Hoard: Challenge 0–4

*Base Coins: 6d6 × 100 cp (2,100), 3d6 × 100 sp (1,050), 2d6 × 10 gp (70)*

| Result (d100)  | Gems/Art                    | Magic Items      |
| :------------- | :-------------------------- | :--------------- |
| **01–06**      | —                           | —                |
| **07–16**      | 2d6 (7) × 10 gp gems        | —                |
| **17–26**      | 2d4 (5) × 25 gp art objects | —                |
| **27–36**      | 2d6 (7) × 50 gp gems        | —                |
| **37–44**      | 2d6 (7) × 10 gp gems        | 1d6 Roll Table A |
| **45–52**      | 2d4 (5) × 25 gp art objects | 1d6 Roll Table A |
| **53–60**      | 2d6 (7) × 50 gp gems        | 1d6 Roll Table A |
| **61–75**      | 2d4 (5) × 25 gp art objects | 1d4 Roll Table B |
| **76–85**      | 2d6 (7) × 50 gp gems        | 1d4 Roll Table B |
| **86–92**      | 2d4 (5) × 25 gp art objects | 1d4 Roll Table C |
| **93–97**      | 2d6 (7) × 50 gp gems        | 1d4 Roll Table C |
| **98–00**      | 2d6 (7) × 50 gp gems        | 1 roll Table F   |

### Treasure Hoard: Challenge 5–10

*Base Coins: 2d6 × 100 cp (700), 2d6 × 1,000 sp (7,000), 6d6 × 100 gp (2,100), 3d6 × 10 pp (105)*

| Result (d100)  | Gems / Art Objects              | Magic Items                  |
| :------------- | :------------------------------ | :--------------------------- |
| **01–04**      | —                               | —                            |
| **05–10**      | 2d4 (5) × 25 gp art objects     | —                            |
| **11–16**      | 3d6 (10) × 50 gp gems           | —                            |
| **17–22**      | 3d6 (10) × 100 gp gems          | —                            |
| **23–28**      | 2d4 (5) × 250 gp art objects    | —                            |
| **29–32**      | 2d4 (5) × 25 gp art objects     | 1d6 Roll Table A             |
| **33–36**      | 3d6 (10) × 50 gp gems           | 1d6 Roll Table A             |
| **37–40**      | 3d6 (10) × 100 gp gems          | 1d6 Roll Table A             |
| **41–44**      | 2d4 (5) × 250 gp art objects    | 1d6 Roll Table A             |
| **45–49**      | 2d4 (5) × 25 gp art objects     | 1d4 Roll Table B             |
| **50–54**      | 3d6 (10) × 50 gp gems           | 1d4 Roll Table B             |
| **55–59**      | 3d6 (10) × 100 gp gems          | 1d4 Roll Table B             |
| **60–63**      | 2d4 (5) × 250 gp art objects    | 1d4 Roll Table B             |
| **64–66**      | 2d4 (5) × 25 gp art objects     | 1d4 Roll Table C             |
| **67–69**      | 3d6 (10) × 50 gp gems           | 1d4 Roll Table C             |
| **70–72**      | 3d6 (10) × 100 gp gems          | 1d4 Roll Table C             |
| **73–74**      | 2d4 (5) × 250 gp art objects    | 1d4 Roll Table C             |
| **75–76**      | 2d4 (5) × 25 gp art objects     | 1d4 Roll Table D             |
| **77–78**      | 3d6 (10) × 50 gp gems           | 1d4 Roll Table D             |
| **79–80**      | 3d6 (10) × 100 gp gems          | 1d4 Roll Table D             |
| **81–84**      | 2d4 (5) × 250 gp art objects    | 1d4 Roll Table E             |
| **85–88**      | 3d6 (10) × 100 gp gems          | 1d4 Roll Table F             |
| **89–91**      | 2d4 (5) × 250 gp art objects    | 1d4 Roll Table F             |
| **92–94**      | 3d6 (10) × 100 gp gems          | 1d4 Roll Table G             |
| **95–96**      | 2d4 (5) × 250 gp art objects    | 1d4 Roll Table G             |
| **97–98**      | 3d6 (10) × 100 gp gems          | 1 Roll Table H               |
| **99–00**      | 2d4 (5) × 250 gp art objects    | 1 Roll Table H               |

### High-Tier Hoards (CR 11+)
For Hoards of **Challenge 11–16** and **Challenge 17+**, rewards consist of thousands of gold/platinum pieces, dozens of high-value gems (500–5,000 gp), and multiple Major Magic Items (Tables G, H, I). Refer to the DMG Chapter 7 for the specific probability spreads.

*Note: For full tables and magic item definitions, refer to the Dungeon Master's Guide (DMG) Chapter 7.*
