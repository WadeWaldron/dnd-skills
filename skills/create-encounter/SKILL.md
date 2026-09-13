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

### 7. The Tension Die (Optional: High-Tension Variation)
To inject uncertainty and urgency, you may include a **Visible Tension Die** mechanic. This die serves as a countdown to a significant shift in the encounter.

- **When to use:** Use this selectively. It is perfect for Boss Fights, Climaxes, or even regular mob encounters where reinforcements or environmental instability add to the drama. Do **not** use this for every encounter; some battles should serve as "tension relief" where the party can simply enjoy their power.
- **The Mechanic:** A d6 starts at a target value (usually **4** for high-impact or **6** for slow-burn encounters) and **decreases** by 1 at the end of each round.
- **The Trigger:** The foreshadowed event triggers when the die reaches **1**.
- **The Constraints:** 
    - **Visible Doom:** The die must be visible to the players so they can see the "doom" approaching. 
    - **Narrative Logic:** The event *must* be foreshadowed in the initial description (e.g., "The ceiling is cracked," "A horn sounds in the distance," "The ritual circle begins to glow").
    - **No Deus Ex Machina:** Events must have a logical reason within the world (e.g., reinforcements were heard earlier, or the structural damage was visible).
    - **Ambiguity:** While the timing is visible, the exact nature of the outcome (Positive, Negative, or Mixed) can remain a mystery until it triggers.
    - **Stability:** To preserve balance, prioritize **Environmental Changes** or **Tactical Shifts** over raw power increases.
- **Examples:** 
    - *The Ceiling Collapses:* (Foreshadowed: "Dust falls from the cracked beams"). A section of the map becomes Difficult Terrain or creates a new barrier.
    - *The Floodgates Shift:* (Foreshadowed: "The sound of rushing water grows louder"). A new path opens or a current pushes combatants towards a specific zone.
    - *Neutral Reinforcements:* (Foreshadowed: "A group of scavengers waits nearby"). They arrive and may scavenge from both sides or offer a social escape.

## Guidelines for the Assistant
- **No Manual Math:** Do not try to calculate Adjusted XP or multipliers yourself. Trust the **validate-encounter** tool.
- **Thematic Integrity:** Use your internal knowledge to pick candidates that make sense together (e.g., don't mix desert and arctic creatures unless there's a story reason).
- **Iterate:** If the first draft fails validation, don't guess—use the `ADVICE` provided by the validation tool to fix it.
