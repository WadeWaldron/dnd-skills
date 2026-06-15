---
name: roll-dice
description: A skill for rolling dice using standard notation (e.g., 1d20+5, 2d6, 1d8+1d4). This ensured fair and accurate results by using a Python script instead of LLM-generated numbers.
---

# Roll Dice

This skill allows you to roll dice using standard notation like `5d6+10` or `d20-2`. It uses a Python script to ensure that the results are truly random.

When the skill is executed, it will ask the user for the dice notation if it hasn't been provided.

## Step 1: Get Dice Notation

**If the dice notation is not provided:**
1. Ask the user: "What dice would you like to roll? (e.g., 1d20+5, 2d6)"
2. Wait for the user's response and store it as `dice_notation`.

**If the dice notation is provided:**
1. Store the provided dice notation as `dice_notation`.

## Step 2: Roll the Dice

Use the `roll_dice.py` Python script to perform the roll.

1. Ensure that the `roll_dice.py` script is in the same directory as this skill.
2. Execute:
```
python3 roll_dice.py "{dice_notation}"
```
3. Capture the output from the script, which will be the total result of the roll.
4. Tell the user the result of the roll.
