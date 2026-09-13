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

## Workflow

All folder and file changes are made by the script. Do not create folders, write `AGENTS.md`, or edit `CLAUDE.md` by hand.

1. Run the script from this skill's directory, passing the campaign root:
   `python3 init_campaign.py "{{campaign_root}}"`
2. Relay the script's output to the user.
3. Review **Other folders** for campaign-specific names that overlap a canonical folder, such as `Items/` beside `Magic-Items/`. Name each pair so the user can move the content or delete the empty folder. Do not attempt either on your own.

## Folders created

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

Creating folders is additive. Existing folders are left exactly as they are.

Folder matching follows the filesystem. On macOS and Windows an existing `campaign/` already satisfies `Campaign`; on Linux the two are separate folders. Mention this when a campaign under version control uses lowercase folder names.

## Instruction files

- `AGENTS.md` holds the Dungeon Master persona and folder conventions, copied from [assets/AGENTS.md](assets/AGENTS.md). An existing `AGENTS.md` at the root or in `.agents/` is used as is.
- `CLAUDE.md` imports `AGENTS.md`, because Claude Code reads `CLAUDE.md` rather than `AGENTS.md`. The import path points at wherever `AGENTS.md` actually lives. An existing `CLAUDE.md` (at the root or in `.claude/`) keeps its content, gains the import as its first line, and loses any `@AGENTS.md` import that points at a missing file.

Campaign-specific rules can be added to `AGENTS.md`, or below the import in `CLAUDE.md` when they should apply to Claude only.
