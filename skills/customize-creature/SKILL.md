---
name: customize-creature
description: A skill for customizing a creature's stats, abilities, and traits based on a base creature template. This allows for quick creation of unique monsters or NPCs by modifying existing stat blocks.
---

# Customize Creature

This skill is for "re-skinning" or "re-flavoring" monsters. It preserves the exact mathematical balance (CR/XP/Stats) of a base creature while changing its name, description, and thematic flavor to fit a specific encounter.

## The Workflow

### 1. Select a Base Template
Use the **lookup-creatures** skill to find a monster that provides the correct mathematical "bones" for your need.
*Example: Use a "Veteran" for a "Pirate Captain" or a "Guard" for a "Palace Sentry".*

### 2. Define the "Skin"
Identify the thematic changes needed:
- **Name:** New title for the creature.
- **Flavor Text:** A new summary describing its appearance and role.
- **Terminology Swaps:** Rename weapons or abilities (e.g., "Mace" becomes "Heavy Plank", "Longsword" becomes "Cutlass").
- **Damage Types:** Change damage types if appropriate (e.g., Slashing -> Necrotic for a ghost version).

### 3. Apply Re-flavoring
Rewrite the statblock with the new flavor while strictly adhering to the "No Math Changes" rule.

## Guidelines for the Assistant

1.  **The Math is Sacred:** NEVER change AC, HP, Ability Scores, CR, XP, Attack Bonuses, or Damage Dice. These are the fixed mechanical "bones" of the creature.
2.  **Strict Descriptive Swaps:** 
    - Rename weapons and abilities to match the theme.
    - Update all descriptions to refer to the new name and equipment.
3.  **Thematic Senses/Languages:** You may add or change languages and senses (like Darkvision) if it fits the new theme and doesn't significantly impact CR.
4.  **No New Mechanics:** Do NOT add new traits or actions that have mathematical weight (like "Pack Tactics" or "Multiattack" if the base didn't have them). If you add a purely flavor trait, ensure it has no mechanical benefit.

## Example Transformation

**Base:** Veteran (CR 3)
**New Flavor:** Pirate Captain
- **Weapon rename:** Longsword -> Heavy Cutlass.
- **Weapon rename:** Shortsword -> Boarding Dagger.
- **Math:** Kept exactly at +5 to hit and 1d8+3 damage.
- **Description:** Updated to describe the captain's salted beard and scarred face.


