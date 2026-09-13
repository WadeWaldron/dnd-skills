---
name: create-puzzle
description: This skill generates thematic, in-world puzzles and hazards for D&D encounters, moving away from abstract or "gamified" logic.
---

# Create Puzzle

This skill creates non-combat obstacles that feel like a natural part of the dungeon's environment and history. These are often better understood as "Environmental Skill Challenges" rather than abstract puzzles.

## Step 1: Define the Room's Context
Before designing the challenge, establish:
1.  **Original Functional Purpose:** What was this room built for? (e.g., A library, a kitchen, a forge, a barracks).
2.  **Current State:** Why is it a challenge now? (e.g., Abandoned, decaying, occupied, malfunctioning magic, or literal geography like a swamp).

## Step 2: Mandatory Design Rules
Every challenge must strictly adhere to the following three rules. If a design violates any of these, it must be discarded.

### Rule 1: The "Workplace Logic" Test
The obstacle must be a natural, functional consequence of the room's original purpose or the environment's geography.
- **The Test:** Ask "Would this hazard exist if there were no adventurers here?" (e.g., A kitchen fire exists because of cooking; a door locked by 'golden spoons' only exists for players).
- **Forbidden:** Abstract riddles, "collect-the-item" gates, or arbitrary mini-games (e.g., chess tiles, glowing motes, numerical levers).

### Rule 2: Mechanical Weight
Environmental effects must have explicit mechanical consequences.
- *Dense Fog* isn't just flavor; it creates Heavily Obscured areas that affect combat and navigation.
- *Deep Mud* isn't just flavor; it requires Acrobatics or special gear to avoid becoming *Restrained*.

### Rule 3: Fail Forward (Consequences)
Failure on a check must never result in a complete dead-end. Instead, players "succeed at a cost." Choose a cost that is detectable and manageable within the dungeon's structure:
- **Immediate Damage:** Physical harm or environmental injury. Use the `damage-severity` skill.
- **Attrition (Levels of Exhaustion):** Physical or mental strain that lingers (e.g., navigating a frozen pass or toxic swamp).
- **Asset/Resource Loss:** Explicit loss of gear (broken shield, snapped rope) or depletion of consumables (ruined rations, lost ammunition).
- **Dungeon Alert State:** Failure creates noise or visible signs of passage. *Effect:* The next encounter in the dungeon starts with the party **Surprised** or the enemies in a **Defensive Position** (+2 AC for the first round).
- **Tactical Disadvantage:** Players arrive at the far side of the hazard in a compromised state (e.g., split party, Prone, or with one character isolated).
- **The "High Cost" Path:** Players eventually succeed, but only by taking a longer, more dangerous route that triggers an extra **Nuisance** or **Moderate** encounter. (Requires the `create-encounter` skill).

### Rule 4: Explicit Difficulty
Every skill check or saving throw must include a specific **Difficulty Class (DC)**.
- **The Process:** Use the **difficulty-class** skill to determine the appropriate DC based on the intended difficulty (e.g., Moderate = DC 15).
- **Presentation:** Always present the DC alongside the skill name (e.g., "DC 14 Athletics").

## Step 3: Architecture of the Challenge
Every challenge must support multiple solutions.

1.  **Skills:** Allow 2-3 different skill checks (e.g., Survival to find a path, Athletics to row, Investigation to spot a flaw).
2.  **Magic:** Identify 1-2 types of spells that would bypass or mitigate the hazard (e.g., *Levitate* for mud, *Control Flames* for fire).
3.  **Practical Solutions:** Reward the use of Tools or creative mundane solutions (e.g., crafting "swamp shoes" with leatherworker tools, using a rope to tie characters together).

## Examples for Inspiration

### The Kitchen
- **GOOD:** A grease fire has attracted **Smoke Mephits**. Players must extinguish the fire or use *Control Flames* to safely reach the pantry.
- **BAD:** A magical door that won't open unless the players find 3 "golden spoons" hidden in the cupboards.

### The Forge
- **GOOD:** The furnace is overheating, creating extreme heat damage. Players must repair a ruptured cooling pipe or manually vent the steam to pass.
- **BAD:** A series of numerical levers (1-4-2-3) that must be pulled in order to unlock a weapon rack.

### The Barracks
- **GOOD:** The floor has partially collapsed. Players must navigate narrow support beams or use magic to reach the far side.
- **BAD:** A chessboard-patterned floor where players can only move in "L-shapes" like knights to avoid pressure plates.

### The Swamp (Environment)
- **GOOD:** An "impassable" stretch of deep, sucking mud. Players can use magic (*Levitate*), Survival/Investigation checks to find a firm path, or a Tool Check (Carpenter/Leatherworker) to craft "swamp shoes." The challenge is an inherent property of the geography.
- **BAD:** A series of giant stone frogs that must be fed specific "swamp berries" in a certain order to make a bridge appear.

### The Razor Straits (Navigation)
- **GOOD:** Navigating a small boat through razor-sharp rocks in high surf. Success requires a sequence of Skill Checks (Athletics to row, Perception to spot rocks, Water Vehicles tool check). Failure causes boat damage or forced setbacks.
- **BAD:** A magical barrier that asks a riddle about "what has teeth but cannot bite" before the rocks disappear.

## Step 4: Scale the Threat
Use the **damage-severity** skill to ensure hazards present a legitimate threat (Nuisance vs. Deadly) based on the party's level.
