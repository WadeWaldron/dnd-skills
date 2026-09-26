# Changelog

All notable changes to the `dnd-skills` plugin. Versions follow [Semantic Versioning](https://semver.org).

## [1.0.0] - 2026-09-26

### Added
- `create-npc` skill: builds NPCs with appearance, voice, goals, secrets, connections, social check DCs set by attitude, and what they can offer the party. Includes random prompt tables and a validator.

### Changed
- The plugin now follows full semantic versioning: major for breaking changes, minor for new features, patch for fixes.

## [0.4.0] - 2026-09-13

### Removed
- `calculate-xp-threshold` and `validate-encounter` skills. Their math is now part of `create-encounter`.

### Changed
- `create-encounter` uses the 2024 Dungeon Master's Guide XP budgets. Difficulties are now Low, Moderate, and High, with no monster-count multiplier. Mixed-level parties are supported.
- `create-trap` and `create-puzzle` follow fill-in templates with fixed rules for DCs, damage, and consequences.
- Scripts run without an approval prompt in Claude Code while their skill is active.
- Every skill description says when to use the skill.

### Added
- `create-encounter` can check the difficulty of an existing encounter.
- Validation scripts for encounters, traps, and puzzles. Each checks a finished document, including one placed inside a larger file.

## [0.3.0] - 2026-09-13

### Changed
- `create-narrative-hazard` rebuilt around a fixed template with clear rules for clocks, position, edges, complications, and endings. Damage scales with party level and is sized to drain resources rather than kill.

### Added
- Opportunities in narrative hazards: optional prizes the party can go after instead of the goal.
- Validation script for narrative hazards.

## [0.2.1] - 2026-09-13

### Changed
- `lookup-creatures` installs about 13 MB smaller.
- New campaigns get updated Dungeon Master instructions from `initialize-campaign`.

## [0.2.0] - 2026-09-13

### Added
- `create-character-sheet` skill: a printable character sheet and spell cards built from one data file.

### Changed
- `initialize-campaign` creates folders and instruction files with a script.

## [0.1.0] - 2026-09-13

### Added
- First release as a Claude Code plugin and marketplace.
