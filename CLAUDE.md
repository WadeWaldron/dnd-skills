# Claude

Load and execute all instructions in the `.agents/AGENTS.md` file.

Once you have finished executing the instructions in `.agents/AGENTS.md` respond with `Instructions executed.`

## Installing Skills

This project stores skills in the `.agents/skills/` directory. To make Claude Code discover these skills, create a symlink from the default skills directory:

```bash
mkdir -p .claude
ln -s ../.agents/skills .claude/skills
```

This command:
1. Creates the `.claude` directory if it doesn't exist
2. Creates a symlink from `.claude/skills` to `.agents/skills`

After creating the symlink, restart Claude Code or run `/hooks` to reload the configuration. The skills will then be automatically available in Claude Code.

