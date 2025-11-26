---
name: init-project
description: Initialize new project with .claude/ directory structure
---

# /init-project - Project Initialization

Scaffold a new project with complete Claude Code configuration.

## Usage

```
/init-project                  # Initialize current directory
/init-project my-app           # Initialize named project
```

## Process

Invokes the **project-init** skill:

1. Detect project type (Node.js, Python, Rust, Go)
2. Create `.claude/` directory structure
3. Generate CLAUDE.md with project instructions
4. Initialize STATUS.json for session continuity
5. Update .gitignore
6. Report and offer next steps

## What Gets Created

```
.claude/
├── agents/           # Project-specific agents
├── commands/         # Custom slash commands
├── hooks/            # Hook scripts
├── skills/           # Project-specific skills
├── scripts/          # Utility scripts
├── logs/             # Log files
├── plans/            # Implementation plans
├── STATUS.json       # Session state
└── settings.json     # Claude settings

CLAUDE.md             # Project instructions
```

## Example

```
/init-project

Detecting project type...
✓ Node.js (Next.js 14) detected

Creating .claude/ structure...
✓ Directories created
✓ CLAUDE.md generated
✓ STATUS.json initialized
✓ .gitignore updated

Project initialized!

Recommended next steps:
1. Review and customize CLAUDE.md
2. Run /analyze-project for codebase analysis
3. Run /setup-precommit for quality gates
4. Run /generate-mcp for project-specific tools

Would you like me to run any of these?
```
