# Agents

This repository is `dnd-skills`, a collection of [Agent Skills](https://agentskills.io) for Dungeons & Dragons 5th Edition, packaged as a Claude Code plugin. Work here means building and maintaining the skills themselves, not running a campaign.

Use detailed knowledge of the D&D 5e rules, including the 2024 rules, when writing or reviewing skill content.

## Repository Layout

- `skills/` - One directory per skill. Each directory is self-contained.
- `.claude-plugin/` - `plugin.json` (plugin manifest and version) and `marketplace.json` (the repo as its own marketplace).
- `hooks/` - Plugin hooks. `table_format.py` aligns markdown tables after every write or edit.
- `skills/initialize-campaign/assets/AGENTS.md` - The Dungeon Master instructions copied into each new campaign. Changes to how agents behave inside a campaign go there, not in this file.

## Writing Skills

- Each skill lives in `skills/<skill-name>/` with a `SKILL.md` at its root.
- `SKILL.md` starts with frontmatter holding `name` and `description`. `name` matches the directory name, in kebab-case.
- The `description` is what an agent uses to decide whether to load the skill. Say what the skill does and when to use it, including phrases a user is likely to type.
- Keep `SKILL.md` focused on the workflow. Move long reference material, templates, and data into separate files in the skill directory and link to them with relative paths.
- Anything that needs exact math or real randomness (XP budgets, dice rolls, data lookups, file creation) goes in a Python script, not in LLM reasoning. `SKILL.md` gives the exact `python3` command to run from the skill's directory.
- Scripts use only the Python 3 standard library.
- Skills can call on other skills by name (for example, `create-encounter` uses `calculate-xp-threshold`, `lookup-creatures`, and `validate-encounter`). Keep each skill usable on its own.
- Skills can read campaign folders for context (NPCs, Locations, Monsters, and so on). The folder names are defined by `initialize-campaign`.

## Adding or Changing a Skill

- Add new skills to the **Current Skills** list in `README.md`, under the matching category.
- Bump the version as described in **Versioning**.

## Versioning

The plugin version lives in `version` in `.claude-plugin/plugin.json` and follows [Semantic Versioning](https://semver.org) (`MAJOR.MINOR.PATCH`). Installed plugins only update when this number changes.

- **Major** - A change that breaks something users already rely on:
  - Removing or renaming a skill (its invocation name changes).
  - Changing the campaign folder structure in a way existing campaigns no longer match.
  - Changing a data file format so existing files stop working (for example, the `create-character-sheet` data file).
  - Removing or renaming a script argument that users or other skills call.
- **Minor** - New functionality that works with everything that exists:
  - Adding a skill or a hook.
  - Adding options, room types, tables, or other content to an existing skill.
  - Adding new optional script arguments or data file fields.
- **Patch** - Fixes and polish with no new functionality:
  - Correcting rules, math, stat blocks, or monster data.
  - Fixing script bugs.
  - Rewording `SKILL.md` instructions or descriptions without changing what the skill does.

While the version is `0.x`, breaking changes bump the minor version and everything else bumps the patch version.

Bump the version once per pull request, using the largest change it contains. Changes that don't reach users (`README.md`, this file, repository tooling) don't need a bump.

## Document Content: State, Not History

Skill files, templates, and generated campaign documents record the current state of the world, story, or mechanic — never the history of how that state was reached.

- Do not narrate the process: no "originally we had X, but changed it to Y," no recounting of earlier drafts, rejected ideas, or corrections that happened along the way.
- Do not justify decisions or explain why something was chosen over an alternative unless that reasoning is itself part of the fiction (e.g. a character's in-world motivation). Record the outcome and move on.
- Do not reference a connection, mechanic, or detail that used to exist, even to say it no longer applies or "isn't needed." If it isn't true now, it isn't mentioned at all.
- Treat every document as if it were being written fresh, knowing only the final answer — not as a log of the conversation that produced it.
