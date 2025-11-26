---
name: project-init
description: Initialize new project with .claude/ directory structure including agents, skills, commands, hooks, and project documentation templates
---

# Project Initialization

## Overview

Scaffold a new project with complete Claude Code configuration including agents, skills, commands, and documentation.

**Core principle:** Every project gets a consistent, well-organized .claude/ structure.

**Trigger:** `/init-project` command or when starting work on a new project

## Directory Structure Created

```
.claude/
├── agents/                    # Project-specific agents
│   └── README.md
├── commands/                  # Slash commands
│   └── README.md
├── hooks/                     # Hook scripts (pre-tool-use, etc.)
│   └── README.md
├── skills/                    # Project-specific skills
│   └── README.md
├── scripts/                   # Utility scripts
│   ├── session-start.ps1     # Session startup script
│   └── session-end.ps1       # Session cleanup script
├── logs/                      # Log files
│   └── .gitkeep
├── plans/                     # Implementation plans
│   └── .gitkeep
├── STATUS.json               # Session continuity state
└── settings.json             # Claude Code settings
CLAUDE.md                     # Project instructions
```

## Initialization Process

### Step 1: Detect Project Type

```bash
# Detect project type from files
if [ -f "package.json" ]; then
  type="node"
elif [ -f "Cargo.toml" ]; then
  type="rust"
elif [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
  type="python"
elif [ -f "go.mod" ]; then
  type="go"
else
  type="generic"
fi
```

### Step 2: Create Directory Structure

```bash
mkdir -p .claude/{agents,commands,hooks,skills,scripts,logs,plans}
touch .claude/logs/.gitkeep
touch .claude/plans/.gitkeep
```

### Step 3: Create CLAUDE.md

Generate project instructions template:

```markdown
# [Project Name] - Claude Instructions

## Project Identity
- **Name**: [Project Name]
- **Type**: [Detected type]
- **Stack**: [Detected tech stack]

## Quick Start
\`\`\`bash
# Development
[Project-specific dev commands]
\`\`\`

## Key Files
- [Main entry point]
- [Configuration files]
- [Test directories]

## Current Focus
[Area currently being worked on]

## Important Notes
- [Project-specific rules]
- [Things to avoid]
```

### Step 4: Create STATUS.json

Initialize empty status:

```json
{
  "lastUpdate": "[ISO timestamp]",
  "project": "[project-name]",
  "sessionType": "Fresh",
  "git": {
    "branch": "main",
    "lastCommit": "",
    "uncommittedFiles": 0
  },
  "tasks": {
    "inProgress": [],
    "completed": []
  },
  "services": {},
  "context": {
    "focusArea": "",
    "nextAction": ""
  }
}
```

### Step 5: Create settings.json

```json
{
  "model": "claude-sonnet-4-20250514",
  "maxTokens": 8192,
  "permissions": {
    "allowBash": true,
    "allowFileOperations": true,
    "allowGit": true
  }
}
```

### Step 6: Update .gitignore

Add to .gitignore:

```
# Claude Code
.claude/logs/
.claude/STATUS.json
.worktrees/
```

### Step 7: Create README Files

Create README.md in each subdirectory explaining purpose and how to add items.

## Project-Type Specific Setup

### Node.js Projects

- Add npm/yarn run commands to CLAUDE.md
- Detect test framework (jest, mocha, vitest)
- Note port from package.json scripts

### Python Projects

- Add pip/poetry commands
- Detect test framework (pytest, unittest)
- Note virtual environment

### Rust Projects

- Add cargo commands
- Note workspace structure

### Go Projects

- Add go commands
- Note module structure

## Post-Init Recommendations

After initialization:

```
Project initialized at .claude/

Recommended next steps:
1. Review and customize CLAUDE.md
2. Run /analyze-project for codebase analysis
3. Run /setup-precommit for quality gates
4. Run /generate-mcp for project-specific MCP server

Would you like me to run any of these?
```

## Integration

**Triggers:**
- `/init-project` command
- Manual skill invocation

**Followed by:**
- **/analyze-project** - Deep codebase analysis
- **/generate-mcp** - Project-specific MCP server
- **/setup-precommit** - Pre-commit hooks
