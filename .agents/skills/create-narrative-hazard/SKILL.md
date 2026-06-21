---
name: create-narrative-hazard
description: Generates high-tension, non-combat encounters using Clocks and Position/Effect logic to create a frantic, "fiction-first" pace.
---

# Create Narrative Hazard

This skill replaces traditional D&D turn-based mechanics with a "fiction-first" flow modeled after *Blades in the Dark*. Actions always move the narrative forward, even on a failure.

## Step 1: The Clocks
Use clocks to track progress or encroaching danger.
- **Progress Clock (Success):** Tracks the player's goal (e.g., "Escape the Sinking Ship").
- **Danger Clock (Threat):** Tracks the environment's threat (e.g., "The Deck Submerges").

**Standard Sizes:** 4 segments (Quick/High Risk), 6 segments (Standard), 8 segments (Complex).

## Step 2: The Outcome Ladder
Instead of binary pass/fail, use the relative difference between the roll and the **DC** to determine the narrative result.

- **Succeed by 5+ (Yes, and...):** You achieve your goal. The **Progress Clock ticks twice**. The DM also chooses an edge:
    - **Insight**: Gain information or a clue.
    - **Setup**: Grant Advantage to a teammate's next roll.
    - **Observation**: See a hidden item or alternate path.
    - **Momentum**: Position improves (Desperate -> Risky -> Controlled).
- **Succeed by 0–4 (Yes, but...):** You achieve your goal. The **Progress Clock ticks once**. The DM also chooses a complication:
    - **Strain**: Take damage based on position.
    - **Condition**: Gain a condition (blinded, poisoned, etc.).
    - **Harassed**: Grant Disadvantage to a teammate's next roll.
- **Fail by 1–4 (No, but...):** Fail your goal (0 Progress segments). The **Danger Clock ticks once**. The DM also chooses an edge:
    - **Insight**: Gain information or a clue.
    - **Setup**: Grant Advantage to a teammate's next roll.
    - **Observation**: See a hidden item or alternate path.
- **Fail by 5+ (No, and...):** Fail your goal (0 Progress segments). The **Danger Clock ticks twice**. The DM also chooses a complication:
    - **Strain**: Take damage based on position.
    - **Condition**: Gain a condition (blinded, poisoned, etc.).
    - **Harassed**: Grant Disadvantage to a teammate's next roll.
    - **Slip**: Position degrades (Controlled -> Risky -> Desperate).

## Step 3: Position (The Stakes)
Before the roll, the DM establishes the **Position** to set the narrative and mechanical context for complications and edges.

- **Controlled (Respite):** You have the upper hand or a moment of safety.
    - **Damage**: **Minor** (1d4 or 1d6) or none. The threat is environmental inconvenience, not injury.
    - **Complications**: Focus on narrative setbacks. **Harassed** might mean losing your next move or dropping a non-essential item rather than mechanical Disadvantage.
    - **Edges**: Highly impactful. **Insight** and **Observation** provide deep knowledge. **Setup** is powerful—granting Advantage to *multiple* teammates or an Advantage that doesn't expire until used.
- **Risky (Standard):** The classic, unstable adventuring environment where things can go either way.
    - **Damage**: **Nuisance** (from `damage-severity`). The environment is dangerous but usually won't drop a healthy character.
    - **Complications**: Uses standard results. **Harassed** grants Disadvantage to the next teammate's roll.
    - **Edges**: Uses standard results. **Setup** grants Advantage to the next teammate's roll.
- **Desperate (Crisis):** Everything is going wrong, and you are fighting for your life.
    - **Damage**: **2x Nuisance** (from `damage-severity`). Every hit matters and can put a character near death.
    - **Complications**: Catastrophic. In addition to standard choices, the DM can choose **Loss** (permanent loss of an NPC, asset, or gear). **Harassed** is severe—granting Disadvantage to *multiple* teammates as your failure cascades.
    - **Edges**: An edge here is a narrow escape. **Setup** is powerful—granting Advantage to *every* teammate as you clear a path or draw all the heat.

## Step 4: Logic & Difficulty
- **Clock Driven:** Successes always move the Progress Clock; failures (especially "No, but" and "No, and") always move the Danger Clock.
- **Fiction First:** Players describe their action; the DM assigns the DC.
- **Difficulty:** Use the `difficulty-class` skill (Typical DC 15).
- **Damage:** Use the `damage-severity` skill for consequences based on party level.
- **Fail Forward:** A failure must always change the situation. Either the danger increases, the position worsens, or a dark truth is revealed.

