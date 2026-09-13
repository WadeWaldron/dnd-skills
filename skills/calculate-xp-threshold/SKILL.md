---
name: calculate-xp-threshold
description: A skill that calculates the experience points (XP) threshold for an encounter based on the party's level and the desired difficulty of the encounter.
---

# Calculate XP Threshold

This skill calculates the experience points (XP) requirements for an encounter based on the party's level and size. It provides the thresholds for all difficulty levels (Easy, Medium, Hard, and Deadly).

When the skill is executed, it will ask the user for the party's level and size. It will then:
1. Calculate the XP thresholds for each difficulty level.
2. Present these thresholds to you so you can decide which budget to aim for.

## Step 1: Get Party Level

**If the party level is not provided:**
1. Ask the user: "What is the party's level?"
2. Wait for the user's response and store it as party_level.

**If the party level is provided:**
1. Store the provided party level as party_level.

## Step 2: Get Party Size

**If the party size is not provided:**
1. Ask the user: "What is the party's size (number of characters)?"
2. Wait for the user's response and store it as party_size.

**If the party size is provided:**
1. Store the provided party size as party_size.

## Step 3: Calculate XP Thresholds

Use the calculate_xp.py Python script to perform the calculation.

1. Ensure that the calculate_xp.py script is in the same directory as this skill.
2. Execute:
   python3 calculate_xp.py --party-level {{party_level}} --party-size {{party_size}}
3. Present the results to the user.

## Example Output

```
Party Level: 10
Party Size: 3
--- XP Thresholds ---
Easy:   1800
Medium: 3600
Hard:   5700
Deadly: 8400
```