---
name: calculate-xp-threshold
description: A skill that calculates the experience points (XP) threshold for an encounter based on the party's level and the desired difficulty of the encounter.
---

# Calculate XP Threshold

This skill calculates the experience points (XP) threshold for an encounter based on the party's level, size, and the desired difficulty of the encounter.

When the skill is executed, it will ask the user for the party's level, size, and the desired difficulty of the encounter (easy, medium, hard, or deadly). It will then calculate and return the XP threshold for that encounter.

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
python calculate_xp.py --party-level {party_level} --party-size {party_size} --difficulty {desired_difficulty}
```
3. Capture the output from the script, which will include the calculated XP threshold.
4. Return the calculated XP threshold to the user in the following format:
```
The XP threshold for a {desired_difficulty} encounter for a party of level {party_level} and size {party_size} is: {xp_threshold} XP.
```