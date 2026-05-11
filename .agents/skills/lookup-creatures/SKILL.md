---
name: lookup-creatures
description: A skill that looks up creatures from D&D 5e based on XP values. Useful for finding appropriate monsters to build encounters with specific XP budgets.
---

# Lookup Creatures

This skill allows you to find appropriate creatures in D&D 5e based on their XP values. It's designed to work in conjunction with the **calculate-xp-threshold** skill.

## Step 1: Get Target XP Value

**If the target XP value is not provided:**
1. Ask the user: "What is the target XP value for the creature(s) you're looking for?"
2. Wait for the user's response and store it as `target_xp`.

**If the target XP value is provided:**
1. Store the provided target XP value as `target_xp`.

## Step 2: Get Tolerance (Optional)

**If the tolerance is not provided:**
1. Ask the user: "What tolerance percentage would you like? (default: 20%) This determines how close creatures must be to your target XP."
2. Wait for the user's response and store it as `tolerance_percent`. If the user doesn't provide a value, use 20.

**If the tolerance is provided:**
1. Store the provided tolerance as `tolerance_percent`.

## Step 3: Get Maximum Results (Optional)

**If the maximum results is not provided:**
1. Ask the user: "How many creature suggestions would you like? (default: 5)"
2. Wait for the user's response and store it as `max_results`. If the user doesn't provide a value, use 5.

**If the maximum results is provided:**
1. Store the provided maximum results as `max_results`.

## Step 4: Get Additional Filters (Optional)

You can optionally filter results by the following criteria. Ask only if relevant. You can specify multiple filters of the same type to broaden results (OR logic within filter types):

**Size Filter:**
- Ask: "Would you like to filter by size? (e.g., Small, Medium, Large, Huge). You can specify multiple sizes separated by commas."
- Store as `sizes`. Leave blank if no preference.

**Type Filter:**
- Ask: "Would you like to filter by creature type? (e.g., Dragon, Humanoid, Undead, Beast, Monstrosity). You can specify multiple types separated by commas."
- Store as `creature_types`. Leave blank if no preference.

**Subtype Filter:**
- Ask: "Would you like to filter by subtype? You can specify multiple subtypes separated by commas."
- Store as `subtypes`. Leave blank if no preference.

**Group Filter:**
- Ask: "Would you like to filter by creature group? (e.g., Silver Dragon, Demon, Vampire). You can specify multiple groups separated by commas."
- Store as `groups`. Leave blank if no preference.

**Environment Filter:**
- Ask: "Would you like to filter by environment? (e.g., Mountains, Urban, Underdark, Forest, Ocean). You can specify multiple environments separated by commas."
- Store as `environments`. Leave blank if no preference.

## Step 5: Execute Lookup

Use the `lookup_creatures.py` Python script to search for creatures.

1. Ensure that the `lookup_creatures.py` script is in the same directory as this skill.
2. Execute (including optional filters if provided):
```
python3 lookup_creatures.py --xp-target {target_xp} --tolerance {tolerance_percent} --count {max_results} [--size {size}]... [--type {creature_type}]... [--subtype {subtype}]... [--group {group}]... [--environment {environment}]...
```

**Note:** Filters can be specified multiple times. For example:
- `--environment Ocean --environment Coastal` - searches for creatures in Ocean OR Coastal environments
- `--type Dragon --type Humanoid` - searches for Dragon OR Humanoid creatures
- `--size Large --size Huge` - searches for Large OR Huge creatures

3. Capture the complete markdown statblock output from the script.
4. Return the markdown output directly to the user as-is, without reformatting.

## Example Output

```
Found 1 creature(s) matching 18000.0 XP (±20%):

# Adult Red Dragon

*Huge Dragon, Chaotic Evil*

**Armor Class** 19

**Hit Points** 256

**Speed** 40 ft., climb 40 ft., fly 80 ft.

| STR | DEX | CON | INT | WIS | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 27 | 10 | 25 | 16 | 13 | 21 |

**Saving Throws** DEX +6, CON +13, WIS +7, CHA +11

**Skills** Perception +13, Stealth +6

***Eldest of red dragons, a tyrant of flame and devastation. Legendary in scale and power.***

**Challenge** 17 (18000 XP)
```