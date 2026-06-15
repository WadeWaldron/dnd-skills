# D&D Skills

This repository contains a collection of Agent Skills for Dungeons & Dragons (5e). These skills combine Python-based mathematical rigor with LLM creativity to help Dungeon Masters generate balanced and thematic encounters, dungeons, and more.

## Current Skills

The repository currently features a modular workflow for encounter and dungeon building:

- **[calculate-xp-threshold](.agents/skills/calculate-xp-threshold/SKILL.md)**: Calculates XP budgets for a party based on level and size (Easy to Deadly).
- **[lookup-creatures](.agents/skills/lookup-creatures/SKILL.md)**: Searches a dedicated `monsters.json` database for creatures by environment, type, and XP.
- **[validate-encounter](.agents/skills/validate-encounter/SKILL.md)**: Mathematically validates encounter balance using DMG multipliers.
- **[customize-creature](.agents/skills/customize-creature/SKILL.md)**: A "re-skinning" skill that adapts standard monster templates to new themes without changing their mechanical "bones".
- **[create-encounter](.agents/skills/create-encounter/SKILL.md)**: An orchestrator skill that coordinates the above tools into a complete, balanced, and thematic workflow.
- **[generate-dungeon](.agents/skills/generate-dungeon/SKILL.md)**: A skill for generating structured dungeon layouts with variety and purpose.
- **[roll-dice](.agents/skills/roll-dice/SKILL.md)**: A utility for fair and accurate dice rolling using Python.
- **[difficulty-class](.agents/skills/difficulty-class/SKILL.md)**: Guidance for setting appropriate DCs for various tasks.
- **[damage-severity](.agents/skills/damage-severity/SKILL.md)**: Reference for environmental damage and trap severity.

## Usage

These skills are intended for use with AI coding agents (like GitHub Copilot, Claude Code, or Cursor). Each skill directory contains a `SKILL.md` file that provides instructions for the agent on how to use the specific tool or script.
