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
- The frontmatter also has `license: CC0-1.0`. Skills with scripts add `compatibility: Requires Python 3`, and skills with other environment needs describe them in `compatibility`.
- Skills with scripts add `allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)`, so Claude Code runs the skill's own scripts without asking for approval. The rule only matches commands written with `${CLAUDE_SKILL_DIR}`.
- The `description` is what an agent uses to decide whether to load the skill. Say what the skill does and when to use it, including phrases a user is likely to type.
- Keep `SKILL.md` focused on the workflow. Move long reference material, templates, and data into separate files and link to them with relative paths.
- Anything that needs exact math or real randomness (XP budgets, dice rolls, data lookups, file creation) goes in a Python script, not in LLM reasoning. `SKILL.md` gives the exact command as `python3 ${CLAUDE_SKILL_DIR}/scripts/<name>.py`.
- Skills that produce a document follow a fill-in template and include a validation script that checks the finished document. The validator finds the document by heading, so it works when the content sits inside a larger file.
- Scripts use only the Python 3 standard library.
- Skills can call on other skills by name (for example, `create-encounter` uses `lookup-creatures` and `customize-creature`). Keep each skill usable on its own.
- Skills can read campaign folders for context (NPCs, Locations, Monsters, and so on). The folder names are defined by `initialize-campaign`.

### Skill Folders

Files other than `SKILL.md` go in these subfolders, following the [Agent Skills](https://agentskills.io) standard. Create only the folders a skill needs.

- `scripts/` - Code the agent runs, such as calculators, generators, and validators. Scripts find other skill files relative to their own location (`Path(__file__).parent.parent`), never the working directory.
- `assets/` - Files used in the skill's output or read by its scripts: fill-in templates, files copied into a campaign unchanged (such as the character sheet's `sheet.html` and `cards.html`), and data files (such as `monsters.json`).
- `references/` - Documentation the agent reads only when a step calls for it, such as the dungeon room types.

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
