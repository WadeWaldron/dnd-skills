---
name: update-skills
description: Updates the local .agents folder by downloading the latest version from the official GitHub repository.
---

# Update Skills

This skill allows you to keep your D&D Agent Skills up to date. It downloads the latest `.agents` folder from the official repository and replaces the local version with the newest files.

## Usage

To update your skills, simply use the command:
```
update-skills
```

## How It Works

1. The skill identifies the workspace root and the local `.agents` folder.
2. It downloads a snapshot of the `WadeWaldron/dnd-skills` repository.
3. It extracts the `.agents` folder from the download.
4. It replaces the local skill files with the downloaded versions while preserving the execution environment.

## Execution

The skill uses a Python helper script to perform the update:

1. Locate the `update_skills.py` script in the `.agents/skills/update-skills/` directory.
2. Execute the script:
```bash
python3 .agents/skills/update-skills/update_skills.py
```
3. After the script completes, the local skills will be updated to the latest version.
