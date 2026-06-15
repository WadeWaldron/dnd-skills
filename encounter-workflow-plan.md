# Encounter Creation Workflow Update

This plan outlines the transition from a "Pre-calculated Logic" model to a "Selection -> Validation" model for better thematic encounter generation.

- [ ] **Task 1: Update `calculate-xp-threshold` to provide target ranges**
  - Modify `calculate_xp.py` to remove the random monster count logic.
  - Return the XP thresholds for all difficulty levels (Easy, Medium, Hard, Deadly).
  - Update `SKILL.md` to reflect that it now provides a full budget overview.

- [ ] **Task 2: Create `validate-encounter` skill for XP verification**
  - Create a new skill directory and `SKILL.md`.
  - Create a Python script that takes a list of monsters and party stats.
  - Calculate the final difficulty based on the 2024 D&D rules (Adjusted XP).
  - Provide clear feedback on whether the encounter meets the target difficulty.

- [ ] **Task 3: Update `lookup-creatures` to support broader thematic searches**
  - Adjust `SKILL.md` to encourage using the tool for thematic discovery rather than just exact XP matching.
  - Ensure the script supports filtering by environment, type, and size effectively.

- [ ] **Task 4: Revise `create-encounter` workflow**
  - Update `SKILL.md` to establish the new order of operations:
    1. Calculate thresholds for context.
    2. Search for monsters based on theme/environment.
    3. Verify the final selection against the thresholds.
    4. Adjust as needed if the validation fails.
