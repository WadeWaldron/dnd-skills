# D&D Skills

This repository contains a collection of Agent Skills for Dungeons & Dragons (5e). These skills combine Python-based mathematical rigor with LLM creativity to help Dungeon Masters generate balanced and thematic encounters, dungeons, and more.

## Current Skills

The repository features a comprehensive suite of tools for campaign management and adventure design:

### Campaign & Project Setup
- **[initialize-campaign](.agents/skills/initialize-campaign/SKILL.md)**: Automates the creation of a standard D&D campaign folder structure.
- **[update-skills](.agents/skills/update-skills/SKILL.md)**: Updates the local Agent Skills by downloading the latest version from GitHub.

### Adventure Design
- **[create-dungeon](.agents/skills/create-dungeon/SKILL.md)**: Generates structured dungeon layouts with variety and purpose.
- **[create-encounter](.agents/skills/create-encounter/SKILL.md)**: An orchestrator skill that coordinates balancing and creature selection into a thematic workflow.
- **[create-narrative-hazard](.agents/skills/create-narrative-hazard/SKILL.md)**: Generates high-tension, "fiction-first" encounters using Clocks and Position/Effect logic.
- **[create-puzzle](.agents/skills/create-puzzle/SKILL.md)**: Creates thematic, in-world environmental challenges with meaningful consequences.
- **[create-trap](.agents/skills/create-trap/SKILL.md)**: Designs logical, thematic traps with defined triggers, effects, and sensory telegraphs.
- **[create-treasure](.agents/skills/create-treasure/SKILL.md)**: Generates balanced, theme-appropriate loot and magic items.

### Mechanics & Balancing
- **[calculate-xp-threshold](.agents/skills/calculate-xp-threshold/SKILL.md)**: Calculates XP budgets for a party based on level and size.
- **[lookup-creatures](.agents/skills/lookup-creatures/SKILL.md)**: Searches monster databases for creatures by environment, type, and XP.
- **[validate-encounter](.agents/skills/validate-encounter/SKILL.md)**: Mathematically validates encounter balance using DMG multipliers.
- **[customize-creature](.agents/skills/customize-creature/SKILL.md)**: Adapts standard monster templates to new themes without changing their mechanical bones.

### Core Utilities
- **[roll-dice](.agents/skills/roll-dice/SKILL.md)**: A utility for fair and accurate dice rolling using Python.
- **[difficulty-class](.agents/skills/difficulty-class/SKILL.md)**: Guidance for setting appropriate DCs for various tasks.
- **[damage-severity](.agents/skills/damage-severity/SKILL.md)**: Reference for environmental damage and trap severity.

## Usage

These skills are designed for use with AI coding agents like **GitHub Copilot**. 

### Setup
1. Copy the `.agents` folder into your D&D campaign repository.
2. Ensure you have the [copilot-instructions.md](.github/copilot-instructions.md) file in your `.github/` folder (or reference it in your agent settings).

### How it Works
Each skill directory contains a `SKILL.md` file that provides specific instructions for the AI agent. When you ask for a task (e.g., "Create a level 5 encounter in a swamp"), the agent will:
1. Identify the relevant skill.
2. Execute any necessary scripts (like Python for math).
3. Generate thematic content based on the skill's logic.
