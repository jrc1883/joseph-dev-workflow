# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**joseph-dev-workflow** is a Claude Code plugin providing AI-powered development workflows through skills, agents, commands, and hooks. It implements a two-tier architecture:

- **Tier 1 (this repo)**: Universal, project-agnostic tools that work anywhere
- **Tier 2 (generated)**: Project-specific MCP servers, skills, and agents created via `/generate-mcp` and `/generate-skills`

## Repository Structure

```
.claude-plugin/          Plugin manifest (plugin.json, marketplace.json)
agents/                  29 agent definitions with tiered activation
  config.json            Agent routing, workflows, confidence thresholds
  tier-1-always-active/  11 core agents (code-reviewer, bug-whisperer, etc.)
  tier-2-on-demand/      15 specialized agents
  feature-workflow/      3 agents for 7-phase feature development
skills/                  21 reusable skill definitions (.md with YAML frontmatter)
commands/                17 slash commands for workflows
hooks/                   10 Python hooks for safety and orchestration
output-styles/           8 output format templates
templates/mcp-server/    Template for generating project-specific MCP servers
```

## Development Notes

This is a **configuration-only plugin** - no build, test, or lint commands exist. All content is:
- Markdown files with YAML frontmatter (skills, commands, agents)
- JSON configuration (plugin.json, config.json)
- Python scripts (hooks)
- TypeScript templates (mcp-server)

## Key Architectural Patterns

### Agent Routing (agents/config.json)

Agents are routed via three mechanisms:
1. **Keywords**: "bug" → bug-whisperer, "security" → security-auditor
2. **File patterns**: `*.test.ts` → test-writer-fixer, `*.sql` → query-optimizer
3. **Error patterns**: TypeError → bug-whisperer, SecurityError → security-auditor

### Confidence-Based Filtering

Code review uses 80+ confidence threshold to filter issues:
- 0-25: Likely false positive, skip
- 50-75: Worth mentioning
- 80-100: Must address

### 7-Phase Feature Development

The `/feature-dev` command and feature-workflow agents follow: Discovery → Exploration (code-explorer) → Questions → Architecture (code-architect) → Implementation → Review (code-reviewer) → Summary

### Session Continuity

Three skills manage state between sessions:
- `session-capture`: Saves state to STATUS.json
- `session-resume`: Restores context on startup
- `context-restore`: Loads previous session

## The Chicken-and-Egg Problem

When developing this plugin:
1. The skills/agents you're editing are the same ones you're using to edit
2. Changes to hooks affect the current session behavior
3. Use `/worktree create` to test changes in isolation before merging

## Testing Changes

Since there's no test suite, verify changes by:
1. Creating a test worktree: `/worktree create test-feature`
2. Installing the plugin from the worktree path
3. Running the modified command/skill/agent
4. Comparing output to expected behavior

## MCP Server Template

Located in `templates/mcp-server/`, this TypeScript template generates project-specific MCP servers with:
- Health checks (dev server, database)
- Git tools (status, diff, recent commits)
- Quality tools (typecheck, lint, tests)
- Semantic tool discovery via embeddings

To build the template locally:
```bash
cd templates/mcp-server
npm install
npm run build
```

## Key Files for Plugin Behavior

| File | Purpose |
|------|---------|
| `.claude-plugin/plugin.json` | Plugin manifest and activation triggers |
| `agents/config.json` | All routing rules, workflows, confidence levels |
| `hooks/pre-tool-use.py` | Safety checks before tool execution |
| `hooks/post-tool-use.py` | Cleanup and validation after tools |
| `hooks/agent-orchestrator.py` | Agent sequencing and routing logic |

## Conventions

- All commits use conventional commit format with Claude attribution
- Output styles define templates for PRs, issues, releases, reviews
- Skills can invoke other skills; commands can invoke skills
- Python hooks use `#!/usr/bin/env python3` and are chmod +x
