---
name: initialize-campaign
description: Creates a folder structure for a new D&D campaign. Use this when the user types "initialize-campaign" or "create campaign folders".
---

# Initialize Campaign Skill

This skill sets up a complete folder structure for organizing a D&D campaign, along with the instruction files that tell agents how to work within it.

## Quick start

To use this skill, ask Claude to initialize a campaign with the command:
```
initialize-campaign
```

## Folders created

The skill creates the following folders at the root project level:

**Core Campaign:**
- NPCs - Non-player characters
- Players - Player character information
- Monsters - Monster stat blocks and encounters
- Magic-Items - Magic items and treasure
- Encounters - Combat and roleplay encounters
- Campaign - Campaign overview and notes
- Rules - House rules and rule variations
- History - Campaign timeline and history
- Religion - Pantheon and religious information
- Locations - Towns, dungeons, and significant places
- Organizations - Factions, guilds, and groups
- Lore - World-building and background information
- Sessions - Individual session notes and logs

## Running on an existing campaign

Creating folders is additive. Nothing is moved, renamed, or deleted, and a folder that already exists is left exactly as it is.

Always report the outcome in two lists:

- **Created** — folders that did not exist before
- **Already present** — folders that were left untouched

Both lists matter. A campaign that uses its own folder names will keep them and gain the canonical ones alongside, so `Items/` and a new empty `Magic-Items/` can end up side by side. Say so plainly when it happens, and name the pairs, so the user can move the content or delete the empty folder. Do not attempt either on your own.

Folder matching follows the filesystem. On macOS and Windows an existing `campaign/` already satisfies `Campaign`, so nothing is created; on Linux the two are separate folders. Mention this when a campaign under version control uses lowercase folder names, since the difference only appears once someone clones it on another platform.

## Instruction files created

Two files are written at the campaign root:

- `AGENTS.md` — copied from [assets/AGENTS.md](assets/AGENTS.md). Holds the Dungeon Master persona and the folder conventions above. Read by agents that follow the AGENTS.md convention.
- `CLAUDE.md` — copied from [assets/CLAUDE.md](assets/CLAUDE.md). A single `@AGENTS.md` import line, because Claude Code reads `CLAUDE.md` rather than `AGENTS.md`.

Keeping the content in `AGENTS.md` and importing it means both tools read the same instructions without a second copy to keep in sync. Campaign-specific rules can be added to `AGENTS.md`, or below the import in `CLAUDE.md` when they should apply to Claude only.

**If these files already exist:**

- `AGENTS.md` — leave it as is. It holds the campaign's own instructions; say so rather than overwriting it.
- `CLAUDE.md` — insert `@AGENTS.md` as the first line, keeping the existing content below it. Skip this if the import is already there.

## What this skill does

Creates a well-organized directory structure that covers all aspects of campaign management from character tracking to world-building, and seeds the instruction files an agent needs to use it.
