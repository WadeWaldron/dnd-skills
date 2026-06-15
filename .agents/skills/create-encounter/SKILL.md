---
name: create-encounter
description: Orchestrates the creation of balanced D&D encounters using a modular budget-search-validate workflow.
---

# Create Encounter

This skill orchestrates the creation of a balanced D&D encounter by coordinating three specialized sub-skills. It moves away from arbitrary LLM-math to a rigorous **Selection -> Validation** workflow.

## Step 0: Gather Requirements

Before starting the workflow, ensure you have the following information:
1. **Party Level:** (e.g., Level 5)
2. **Party Size:** (number of characters)
3. **Target Difficulty:** (Easy, Medium, Hard, or Deadly)
4. **Theme/Environment:** (e.g., "Underdark", "Forest with Undead")

If any of these are missing from the user's request, ask clarifying questions before proceeding.

## Strategy: The Modular Workflow

You must follow these steps in order to ensure mathematical accuracy and thematic flavor:

### 1. XP Threshold
Call the **calculate-xp-threshold** skill with the party's level and size. 
- **Goal:** Obtain the XP values for Easy, Medium, Hard, and Deadly difficulties. 
- *Never skip this step.* This establishes the "budget" you must work within for the specific party.

### 2. Creature Lookup
Identify the desired theme (environment, creature types, etc.). Use the **lookup-creatures** skill (Phase 1) to find candidates.
- **Goal:** Get a summary table of 10-15 potential monsters.
- **Tip:** Search for "Leaders" (high XP percentage) and "Minions" (low XP percentage) separately if you want a complex encounter.

### 3. Creature Selection
Pick specific monsters and quantities from the summary table that conceptually fit the user's requested difficulty.
- **Note:** Do not show full statblocks yet. Just draft the list (e.g., "1 Wight and 4 Skeletons").

### 4. Encounter Validation
Call the **validate-encounter** skill with the thresholds from Step 1 and your draft list from Step 3.
- **Goal:** Get a `STATUS: SUCCESS`. 
- **Action:** If the status is `FAIL`, follow the script's `ADVICE` (add/remove monsters) and re-validate until it passes.

### 5. Creature Customization (Optional)
If the user requested a specific theme (e.g., "Pirates") that isn't perfectly represented by standard monster names, apply the **customize-creature** skill.
- **Goal:** Re-skin the validated monsters into thematic versions (e.g., Veteran -> Pirate Captain).
- **Constraint:** Maintain the exact math and balance confirmed in Step 4.

### 6. Final Lookup & Presentation
Call **lookup-creatures** (Phase 2) using exact `--names` and the `--full` flag to retrieve the rich statblocks. 
- If you performed Step 5, apply the descriptive changes to the statblocks before presenting.
- **Goal:** Present the final encounter with full mechanics, thematic descriptions, and the confirmed difficulty status.

## Guidelines for the Assistant
- **No Manual Math:** Do not try to calculate Adjusted XP or multipliers yourself. Trust the **validate-encounter** tool.
- **Thematic Integrity:** Use your internal knowledge to pick candidates that make sense together (e.g., don't mix desert and arctic creatures unless there's a story reason).
- **Iterate:** If the first draft fails validation, don't guess—use the `ADVICE` provided by the validation tool to fix it.
