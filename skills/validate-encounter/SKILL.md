---
name: validate-encounter
description: This skill validates a proposed encounter's difficulty based on the party's XP thresholds and the selected monsters. It calculates the adjusted XP to determine the final difficulty.
---

# Validate Encounter

This skill is the "enforcer" for encounter balance. Once you have selected a group of monsters for an encounter, use this skill to verify that the final difficulty matches your target.

When executed, it expects:
1. The XP thresholds for the party (Easy, Medium, Hard, and Deadly). These should be obtained from the **calculate-xp-threshold** skill.
2. The target difficulty for the encounter (Easy, Medium, Hard, or Deadly).
3. A list of monsters including their names, XP values, and how many of each are present.

It will then:
1. Apply the encounter multiplier based on the total number of monsters.
2. Compare the resulting **Adjusted XP** against the provided thresholds.
3. Check the resulting difficulty against your **Target**.
4. Report a **STATUS (SUCCESS/FAIL)** and provide **ADVICE** if the encounter needs adjustment.

## Step 1: Provide Parameters

You must provide:
- `easy`: Easy XP threshold
- `medium`: Medium XP threshold
- `hard`: Hard XP threshold
- `deadly`: Deadly XP threshold
- `target`: The target difficulty level (easy, medium, hard, deadly)
- `monsters`: A JSON-formatted list of monsters. Example: `[{"name": "Goblin", "xp": 50, "count": 4}, {"name": "Bugbear", "xp": 200, "count": 1}]`

## Step 2: Execute Validation

Run the `validate_encounter.py` script:

`python3 validate_encounter.py --easy {{easy}} --medium {{medium}} --hard {{hard}} --deadly {{deadly}} --target {{target}} --monsters '{{monsters_json}}'`

## Example Usage

**Input:**
- Thresholds: Easy: 300, Medium: 600, Hard: 900, Deadly: 1200
- Target: medium
- Monsters: `[{"name": "Orc", "xp": 100, "count": 3}]`

**Output:**
```
Monsters: 3 total
Raw XP: 300
Adjusted XP: 600 (2.0x multiplier)
Resulting Difficulty: MEDIUM
STATUS: SUCCESS (Matches target difficulty MEDIUM)
--- Thresholds ---
Easy:   300
Medium: 600
Hard:   900
Deadly: 1200
```

## Guidance for the Assistant
- If the status is **FAIL**, follow the **ADVICE** provided by the script (e.g., removing or adding monster XP).
- Always present the validation results and the final status to the user.
