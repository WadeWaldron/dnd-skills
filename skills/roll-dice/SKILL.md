---
name: roll-dice
description: Rolls dice in standard notation (such as 1d20+5, 2d6, or 1d8+1d4) with a Python script for fair, random results. Use whenever a roll is needed, such as attacks, damage, checks, or random tables, or when the user asks to roll.
license: CC0-1.0
compatibility: Requires Python 3
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
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

Use the `scripts/roll_dice.py` Python script to perform the roll.

1. Run:
```
python3 ${CLAUDE_SKILL_DIR}/scripts/roll_dice.py "{dice_notation}"
```
3. Capture the output from the script, which will be the total result of the roll.
4. Tell the user the result of the roll.
