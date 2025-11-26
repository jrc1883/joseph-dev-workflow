# joseph-dev-workflow

Universal development workflow plugin for Claude Code with AI-powered skills, agents, and automation.

## Features

- **26 Specialized Agents** - Tier-1 always-active + Tier-2 on-demand agents
- **23+ Skills** - From brainstorming to code review to git worktrees
- **50+ Commands** - Full GitHub lifecycle, git operations, and more
- **10+ Hooks** - Safety checks, agent orchestration, session management
- **Output Styles** - Consistent templates for commits, PRs, reviews
- **Project Generators** - MCP server and skill generators for project-specific tooling

## Installation

```bash
claude plugins add joseph-dev-workflow
```

Or install from GitHub:

```bash
claude plugins add https://github.com/joseph-cannon/joseph-dev-workflow
```

## Quick Start

### New Project Setup

```bash
/init-project           # Create .claude/ structure
/prd                    # Create requirements document
/analyze-project        # Discover patterns and opportunities
/setup-precommit        # Configure quality gates
/generate-mcp           # Create project-specific MCP server
```

### Feature Development

```bash
/brainstorm             # Refine idea with Socratic questioning
/worktree create feat-x # Create isolated workspace
/write-plan             # Generate implementation plan
/execute-plan           # Build with TDD
/review                 # Code review with confidence filtering
/finish-branch          # Merge, PR, keep, or discard
```

### Issue-Driven Development

```bash
/issue create           # Create AI-executable GitHub issue
/worktree create fix-123
/debug                  # Systematic debugging
/pr create              # Submit fix with template
/issue close            # Mark complete
```

## Commands Reference

### Core Workflow
| Command | Description |
|---------|-------------|
| `/brainstorm` | Interactive design refinement using Socratic method |
| `/write-plan` | Create detailed implementation plan |
| `/execute-plan` | Execute plan in batches with review checkpoints |
| `/debug` | Systematic debugging with root cause analysis |
| `/review` | Code review with confidence-based filtering |
| `/feature-dev` | 7-phase feature development workflow |

### Git Operations
| Command | Description |
|---------|-------------|
| `/commit` | Auto-generate commit message matching repo style |
| `/commit-push-pr` | Full workflow: branch -> commit -> push -> PR |
| `/clean-gone` | Remove stale branches after PR merges |
| `/worktree create <name>` | Create isolated workspace with branch |
| `/worktree analyze` | Identify worktree opportunities |
| `/finish-branch` | Complete work with 4-option flow |

### GitHub Lifecycle
| Command | Description |
|---------|-------------|
| `/issue create` | Create AI-executable GitHub issue |
| `/issue list/view/close` | Issue management |
| `/pr create` | Create PR with template |
| `/pr list/view/merge` | PR management |
| `/run list/view/rerun` | GitHub Actions management |
| `/release create` | Create GitHub release |

### Project Setup
| Command | Description |
|---------|-------------|
| `/init-project` | Initialize new project with .claude/ structure |
| `/prd` | Create Product Requirements Document |
| `/generate-mcp` | Generate project-specific MCP server |
| `/generate-skills` | Generate project-specific skills |
| `/analyze-project` | Full codebase analysis |
| `/setup-precommit` | Configure pre-commit hooks |

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
- `brainstorming` - Design refinement through Socratic questioning
- `systematic-debugging` - 4-phase debugging framework
- `writing-plans` - Detailed implementation planning
- `executing-plans` - Plan execution with review checkpoints
- `tdd` - Test-driven development workflow
- `verification` - Pre-completion verification
- `root-cause-tracing` - Bug backward tracing
- `code-review` - Quality review with confidence scoring
- `simplification-cascades` - Complexity reduction

### Session Management
- `session-capture` - Save session state to STATUS.json
- `session-resume` - Restore context on startup
- `context-restore` - Load previous session context

### Generators
- `project-init` - Scaffold new projects
- `prd-creator` - Create PRDs from brainstorming
- `mcp-generator` - Generate project-specific MCP servers
- `skill-generator` - Generate project-specific skills

### Analysis
- `analyze-project` - Full codebase analysis
- `setup-precommit` - Configure pre-commit hooks

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
/generate-mcp       # Creates .claude/mcp-servers/[project]-dev/
/generate-skills    # Creates .claude/skills/[project]-*
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
