---
name: calculate-xp-threshold
description: A skill that calculates the experience points (XP) threshold for an encounter based on the party's level and the desired difficulty of the encounter.
---

# Calculate XP Threshold

This skill calculates the experience points (XP) requirements for an encounter based on the party's level, size, and the desired difficulty of the encounter.

When the skill is executed, it will ask the user for the party's level, size, and the desired difficulty of the encounter (easy, medium, hard, or deadly). It will then:
1. Randomly generate a monster count (favoring smaller encounters)
2. Calculate the encounter XP threshold (the target difficulty)
3. Calculate the required monster XP (what monsters should total)
4. Determine the encounter multiplier (based on monster count)

This follows D&D 5e rules where: **Monster XP × Encounter Multiplier = Encounter XP**

## Step 1: Get Party Level

**If the party level is not provided:**
1. Ask the user: "What is the party's level?"
2. Wait for the user's response and store it as `party_level`.

**If the party level is provided:**
1. Store the provided party level as `party_level`.

## Step 2: Get Party Size

**If the party size is not provided:**
1. Ask the user: "What is the party's size (number of characters)?"
2. Wait for the user's response and store it as `party_size`.

**If the party size is provided:**
1. Store the provided party size as `party_size`.

## Step 3: Get Desired Difficulty

**If the desired difficulty is not provided:**
1. Ask the user: "What is the desired difficulty of the encounter? (easy, medium, hard, or deadly)"
2. Wait for the user's response and store it as `desired_difficulty`.

**If the desired difficulty is provided:**
1. Store the provided desired difficulty as `desired_difficulty`.

## Step 4: Calculate XP Threshold

Use the `calculate_xp.py` Python script to perform the calculation.

1. Ensure that the `calculate_xp.py` script is in the same directory as this skill.
2. Execute:
```
python3 calculate_xp.py --party-level {party_level} --party-size {party_size} --difficulty {desired_difficulty}
```
3. Capture the output from the script, which will include:
   - **Encounter XP**: The party's difficulty threshold (constant)
   - **Monster XP**: The total XP that monsters should have (varies by random monster count)
   - **Average XP per Monster**: The average XP value per individual monster
   - **Monster Count**: A randomly generated number of creatures (favors smaller encounters)
   - **Encounter Multiplier**: The scaling factor based on monster count
4. Present the results to the user, highlighting these key values and explaining what they mean for building the encounter.

## Example Output

```
Party Level: 10
Party Size: 3
Difficulty: Hard
XP per Character: 1900
Monster Count: 4
Monster Difficulty Modifier: 2.0
Total Monster XP: 2850.0
Average XP per Monster: 712.5
Total Encounter XP: 5700

For a hard encounter with a level 10 party of 3 characters:
- Encounter XP (target): 5,700 XP
- Monster Count (random): 4 creatures
- Encounter Multiplier: 2.0x
- Required Monster XP: 2,850 XP total
- Average XP per Monster: 712.5 XP

This means you should select 4 monsters that total approximately 2,850 XP (average 712.5 XP each).
When the 2.0x multiplier is applied, it will result in a hard encounter worth 5,700 XP.
```

## Next Steps

Once you have the required monster XP, use the **lookup-creatures** skill to find specific creatures that match your XP targets!