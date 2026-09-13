# D&D Skills

This repository contains a collection of [Agent Skills](https://agentskills.io) for Dungeons & Dragons (5e). These skills combine Python-based mathematical rigor with LLM creativity to help Dungeon Masters generate balanced and thematic encounters, dungeons, and more.

## Current Skills

The repository features a comprehensive suite of tools for campaign management and adventure design:

### Campaign & Project Setup
- **[initialize-campaign](skills/initialize-campaign/SKILL.md)**: Automates the creation of a standard D&D campaign folder structure.

### Adventure Design
- **[create-dungeon](skills/create-dungeon/SKILL.md)**: Generates structured dungeon layouts with variety and purpose.
- **[create-encounter](skills/create-encounter/SKILL.md)**: An orchestrator skill that coordinates balancing and creature selection into a thematic workflow.
- **[create-narrative-hazard](skills/create-narrative-hazard/SKILL.md)**: Generates high-tension, "fiction-first" encounters using Clocks and Position/Effect logic.
- **[create-puzzle](skills/create-puzzle/SKILL.md)**: Creates thematic, in-world environmental challenges with meaningful consequences.
- **[create-shop](skills/create-shop/SKILL.md)**: Generates a thematic shop with inventory based on settlement size and item scarcity.
- **[create-trap](skills/create-trap/SKILL.md)**: Designs logical, thematic traps with defined triggers, effects, and sensory telegraphs.
- **[create-treasure](skills/create-treasure/SKILL.md)**: Generates balanced, theme-appropriate loot and magic items.

### Mechanics & Balancing
- **[calculate-xp-threshold](skills/calculate-xp-threshold/SKILL.md)**: Calculates XP budgets for a party based on level and size.
- **[lookup-creatures](skills/lookup-creatures/SKILL.md)**: Searches monster databases for creatures by environment, type, and XP.
- **[validate-encounter](skills/validate-encounter/SKILL.md)**: Mathematically validates encounter balance using DMG multipliers.
- **[customize-creature](skills/customize-creature/SKILL.md)**: Adapts standard monster templates to new themes without changing their mechanical bones.

### Core Utilities
- **[roll-dice](skills/roll-dice/SKILL.md)**: A utility for fair and accurate dice rolling using Python.
- **[difficulty-class](skills/difficulty-class/SKILL.md)**: Guidance for setting appropriate DCs for various tasks.
- **[damage-severity](skills/damage-severity/SKILL.md)**: Reference for environmental damage and trap severity.

## Installation

### Claude Code

This repository is a Claude Code plugin and its own marketplace. Install it once and the skills are available in every campaign, with no files copied into your campaign folders:

```bash
claude plugin marketplace add WadeWaldron/dnd-skills
claude plugin install dnd-skills@dnd-skills
```

Update later with `claude plugin update dnd-skills`.

Skills installed this way are namespaced, so `create-encounter` is invoked as `/dnd-skills:create-encounter`. Claude still selects them automatically based on what you ask for.

### GitHub Copilot and other agents

Copilot reads skills from `~/.agents/skills` (all projects) or `.agents/skills` (one repository). Clone this repository and link the `skills` directory:

```bash
git clone https://github.com/WadeWaldron/dnd-skills.git
ln -s "$PWD/dnd-skills/skills" ~/.agents/skills
```

Any agent that supports the Agent Skills standard can read `skills/` directly — each subdirectory is a self-contained skill.

## Setting up a campaign

Run the `initialize-campaign` skill in an empty campaign folder. It creates the standard folder structure and writes an `AGENTS.md` holding the Dungeon Master persona, plus a `CLAUDE.md` that imports it. Claude Code reads `CLAUDE.md`; other agents read `AGENTS.md`; both get the same instructions.

## How it works

Each skill directory contains a `SKILL.md` file that provides specific instructions for the AI agent. When you ask for a task (e.g., "Create a level 5 encounter in a swamp"), the agent will:
1. Identify the relevant skill.
2. Execute any necessary scripts (like Python for math).
3. Generate thematic content based on the skill's logic.

## Repository layout

```
.claude-plugin/    Plugin and marketplace manifests
skills/            The skills themselves, one directory each
.agents/skills     Symlink to skills/, so Copilot finds them in this repo
AGENTS.md          Instructions for agents working in this repository
CLAUDE.md          Imports AGENTS.md for Claude Code
```
