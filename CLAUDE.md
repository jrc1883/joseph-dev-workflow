# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**popkit** is a Claude Code plugin providing AI-powered development workflows through skills, agents, commands, and hooks. All commands use the `popkit:` prefix (e.g., `/popkit:commit`, `/popkit:review`). It implements a two-tier architecture:

- **Tier 1 (this repo)**: Universal, project-agnostic tools that work anywhere
- **Tier 2 (generated)**: Project-specific MCP servers, skills, and agents created via `/generate-mcp` and `/generate-skills`

## Repository Structure

```
.claude-plugin/          Plugin manifest (plugin.json, marketplace.json)
.mcp.json                MCP server configuration
agents/                  29 agent definitions with tiered activation
  config.json            Agent routing, workflows, confidence thresholds
  tier-1-always-active/  11 core agents (code-reviewer, bug-whisperer, etc.)
  tier-2-on-demand/      16 specialized agents (including rapid-prototyper)
  feature-workflow/      2 agents for 7-phase feature development
skills/                  24 reusable skills (SKILL.md format in subdirectories)
commands/                20 slash commands for workflows
hooks/                   10 Python hooks (JSON stdin/stdout protocol)
  hooks.json             Hook configuration and event mapping
output-styles/           8 output format templates
templates/mcp-server/    Template for generating project-specific MCP servers
tests/                   Plugin self-test definitions
  hooks/                 Hook input/output tests
  routing/               Agent routing tests
  structure/             File structure validation tests
```

## Development Notes

This is a **configuration-only plugin** - no build or lint commands exist. All content is:
- Markdown files with YAML frontmatter (skills, commands, agents)
- JSON configuration (plugin.json, config.json, hooks.json, .mcp.json)
- Python scripts (hooks with JSON stdin/stdout protocol)
- TypeScript templates (mcp-server)
- JSON test definitions (tests/)

**Self-testing available:** Run `/popkit:plugin-test` to validate plugin integrity.

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

The `/popkit:feature-dev` command and feature-workflow agents follow: Discovery → Exploration (code-explorer) → Questions → Architecture (code-architect) → Implementation → Review (code-reviewer) → Summary

### Session Continuity

Three skills manage state between sessions:
- `popkit:session-capture`: Saves state to STATUS.json
- `popkit:session-resume`: Restores context on startup
- `popkit:context-restore`: Loads previous session

## Installing popkit for Development

To use popkit while developing popkit (chicken-and-egg), install it from GitHub:

```
/plugin marketplace add jrc1883/popkit
/plugin install popkit@popkit-marketplace
```

Then **restart Claude Code** to load the plugin. After restart, `/popkit:` commands will be available.

## The Chicken-and-Egg Problem

When developing this plugin:
1. The skills/agents you're editing are the same ones you're using to edit
2. Changes to hooks affect the current session behavior
3. Use `/popkit:worktree create` to test changes in isolation before merging

## Testing Changes

Verify changes using the built-in test framework:
1. Run `/popkit:plugin-test` to validate all components
2. Run `/popkit:plugin-test hooks` to test hook JSON protocol
3. Run `/popkit:plugin-test routing` to verify agent selection
4. For isolation: Create a worktree with `/popkit:worktree create test-feature`

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
| `.mcp.json` | MCP server and tool configuration |
| `agents/config.json` | All routing rules, workflows, confidence levels |
| `hooks/hooks.json` | Hook event configuration |
| `hooks/pre-tool-use.py` | Safety checks before tool execution |
| `hooks/post-tool-use.py` | Cleanup and validation after tools |
| `hooks/agent-orchestrator.py` | Agent sequencing and routing logic |

## New Features (v1.1.0)

- **Auto-Documentation** (`/popkit:auto-docs`): Generate and sync documentation
- **Plugin Self-Testing** (`/popkit:plugin-test`): Validate all plugin components
- **Routing Debugger** (`/popkit:routing-debug`): Debug agent selection logic
- **SKILL.md Format**: Skills now use directory structure (`skills/name/SKILL.md`)
- **JSON Hook Protocol**: All hooks use stdin/stdout JSON instead of argv
- **MCP Configuration**: `.mcp.json` for Model Context Protocol integration

## Conventions

- All commits use conventional commit format with Claude attribution
- Output styles define templates for PRs, issues, releases, reviews
- Skills can invoke other skills; commands can invoke skills
- Python hooks use `#!/usr/bin/env python3` and are chmod +x
