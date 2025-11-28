# popkit

Pop Toolkit - AI-powered development workflows for Claude Code with skills, agents, and automation. All commands use the `pop:` prefix (e.g., `/pop:commit`, `/pop:review`).

## Features

- **29 Specialized Agents** - 11 Tier-1 always-active + 15 Tier-2 on-demand + 3 feature-workflow
- **21 Skills** - From brainstorming to code review to git worktrees
- **17 Commands** - Full GitHub lifecycle, git operations, and more
- **10 Hooks** - Safety checks, agent orchestration, session management
- **8 Output Styles** - Consistent templates for commits, PRs, reviews
- **MCP Server Template** - Generate project-specific dev servers with semantic search

## Installation

```bash
claude plugins add popkit
```

Or install from GitHub:

```bash
claude plugins add https://github.com/jrc1883/popkit
```

## Quick Start

### New Project Setup

```bash
/pop:init-project           # Create .claude/ structure
/pop:prd                    # Create requirements document
/pop:analyze-project        # Discover patterns and opportunities
/pop:setup-precommit        # Configure quality gates
/pop:generate-mcp           # Create project-specific MCP server
```

### Feature Development

```bash
/pop:brainstorm             # Refine idea with Socratic questioning
/pop:worktree create feat-x # Create isolated workspace
/pop:write-plan             # Generate implementation plan
/pop:execute-plan           # Build with TDD
/pop:review                 # Code review with confidence filtering
/pop:finish-branch          # Merge, PR, keep, or discard
```

### Issue-Driven Development

```bash
/pop:issue create           # Create AI-executable GitHub issue
/pop:worktree create fix-123
/pop:debug                  # Systematic debugging
/pop:pr create              # Submit fix with template
/pop:issue close            # Mark complete
```

## Commands Reference

### Core Workflow
| Command | Description |
|---------|-------------|
| `/pop:brainstorm` | Interactive design refinement using Socratic method |
| `/pop:write-plan` | Create detailed implementation plan |
| `/pop:execute-plan` | Execute plan in batches with review checkpoints |
| `/pop:debug` | Systematic debugging with root cause analysis |
| `/pop:review` | Code review with confidence-based filtering |
| `/pop:feature-dev` | 7-phase feature development workflow |

### Git Operations
| Command | Description |
|---------|-------------|
| `/pop:commit` | Auto-generate commit message matching repo style |
| `/pop:commit-push-pr` | Full workflow: branch -> commit -> push -> PR |
| `/pop:clean-gone` | Remove stale branches after PR merges |
| `/pop:worktree create <name>` | Create isolated workspace with branch |
| `/pop:worktree analyze` | Identify worktree opportunities |
| `/pop:finish-branch` | Complete work with 4-option flow |

### GitHub Lifecycle
| Command | Description |
|---------|-------------|
| `/pop:issue create` | Create AI-executable GitHub issue |
| `/pop:issue list/view/close` | Issue management |
| `/pop:pr create` | Create PR with template |
| `/pop:pr list/view/merge` | PR management |
| `/pop:run list/view/rerun` | GitHub Actions management |
| `/pop:release create` | Create GitHub release |

### Project Setup
| Command | Description |
|---------|-------------|
| `/pop:init-project` | Initialize new project with .claude/ structure |
| `/pop:prd` | Create Product Requirements Document |
| `/pop:generate-mcp` | Generate project-specific MCP server |
| `/pop:generate-skills` | Generate project-specific skills |
| `/pop:analyze-project` | Full codebase analysis |
| `/pop:setup-precommit` | Configure pre-commit hooks |

## Agents

### Tier-1 (Always Active)
- `code-reviewer` - Code quality and best practices
- `bug-whisperer` - Complex debugging specialist
- `security-auditor` - Vulnerability assessment
- `test-writer-fixer` - Test implementation and fixes
- `api-designer` - API design patterns
- `performance-optimizer` - Performance analysis
- `refactoring-expert` - Code restructuring
- `documentation-maintainer` - Doc synchronization
- `query-optimizer` - Database query optimization
- `migration-specialist` - System migrations
- `accessibility-guardian` - A11y compliance

### Tier-2 (On-Demand)
- `ai-engineer` - ML/AI integration
- `deployment-validator` - Deployment verification
- `feature-prioritizer` - Backlog management
- `rapid-prototyper` - Quick MVP creation
- `backup-coordinator` - Backup strategies
- `meta-agent` - Agent configuration
- `researcher-agent` - Codebase research
- `user-story-writer` - Requirements documentation
- `devops-automator` - CI/CD automation
- `bundle-analyzer` - Bundle optimization
- `log-analyzer` - Log analysis
- And more...

### Feature Workflow (from Anthropic)
- `code-explorer` - Trace execution paths and data flow
- `code-architect` - Design blueprints and implementation maps
- `code-reviewer` - Confidence-based issue filtering (80+ threshold)

## Skills

### Core Development
- `pop:brainstorming` - Design refinement through Socratic questioning
- `pop:systematic-debugging` - 4-phase debugging framework
- `pop:writing-plans` - Detailed implementation planning
- `pop:executing-plans` - Plan execution with review checkpoints
- `pop:test-driven-development` - Test-driven development workflow
- `pop:verification-before-completion` - Pre-completion verification
- `pop:root-cause-tracing` - Bug backward tracing
- `pop:code-review` - Quality review with confidence scoring
- `pop:simplification-cascades` - Complexity reduction

### Session Management
- `pop:session-capture` - Save session state to STATUS.json
- `pop:session-resume` - Restore context on startup
- `pop:context-restore` - Load previous session context

### Generators
- `pop:project-init` - Scaffold new projects
- `pop:mcp-generator` - Generate project-specific MCP servers
- `pop:skill-generator` - Generate project-specific skills

### Analysis
- `pop:analyze-project` - Full codebase analysis
- `pop:setup-precommit` - Configure pre-commit hooks

### Design & Quality
- `frontend-design` - UI/UX with bold typography, color, motion
- `hookify` - Pattern-based hook creation
- `confidence-filtering` - Code review scoring (80+ threshold)

## Output Styles

Templates for consistent formatting:

### Git/GitHub
- `commit-message` - Conventional commits with attribution
- `pull-request` - PR template with summary, changes, test plan
- `github-issue` - AI-executable issue format
- `release-notes` - Changelog with highlights and breaking changes

### Development
- `code-review` - Structured review with confidence levels
- `implementation-plan` - Task-based planning format
- `design-document` - Architecture documentation
- `changelog` - Version history format

### Session
- `morning-report` - Daily status summary
- `nightly-summary` - End-of-day review
- `handoff-notes` - Context transfer format

## Architecture

This plugin implements a **two-tier architecture**:

### Tier 1: Universal Plugin (this repo)
- General-purpose skills, agents, hooks
- Works on ANY project
- Publishable to GitHub + Claude Marketplace

### Tier 2: Project-Specific (generated)
- Custom MCP server with semantic search
- Project-specific skills based on codebase
- Custom agents with auto-trigger rules

Generate Tier 2 tooling with:
```bash
/pop:generate-mcp       # Creates .claude/mcp-servers/[project]-dev/
/pop:generate-skills    # Creates .claude/skills/[project]-*
```

## Alignment with Anthropic Best Practices

| Best Practice | Implementation |
|--------------|----------------|
| Tool Search Tool | MCP template with semantic embeddings |
| defer_loading | Non-critical tools marked for deferred load |
| Progress Documentation | STATUS.json pattern |
| Feature Tracking | TodoWrite integration |
| Session Startup Protocol | session-resume skill |

## License

MIT

## Author

Joseph Cannon (joseph.cannon@outlook.com)
