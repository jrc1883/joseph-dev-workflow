---
description: Morning health check via MCP (Ready to Code score 0-100)
---

# /popkit:morning - Morning Health Check

Start your day with a comprehensive project health assessment.

## Usage

```
/popkit:morning           # Full morning report
/popkit:morning quick     # Compact summary only
```

## Output Style

Uses `output-styles/morning-report.md` for formatting.

## Process

### Step 1: Git Status

```bash
git status --porcelain
git log --oneline -3
git rev-parse --abbrev-ref HEAD
git remote show origin 2>/dev/null | grep -E "(behind|ahead)" || echo "up to date"
```

Checks:
- Current branch
- Uncommitted changes (staged/unstaged)
- Last 3 commits
- Remote sync status

### Step 2: Code Quality (if configured)

Detect and run quality tools if present:

**TypeScript** (if tsconfig.json exists):
```bash
npx tsc --noEmit 2>&1 | head -20
```

**ESLint** (if .eslintrc* or eslint.config.* exists):
```bash
npx eslint . --max-warnings 10 2>&1 | tail -5
```

**Tests** (if package.json has test script):
```bash
npm test 2>&1 | tail -10
```

Note: Skip checks for tools not configured in the project.

### Step 3: Calculate Ready to Code Score

| Check | Points | Criteria |
|-------|--------|----------|
| Clean working directory | 25 | No uncommitted changes |
| Up to date with remote | 15 | Not behind origin |
| TypeScript clean | 20 | No type errors (or no tsconfig) |
| Lint clean | 15 | No lint errors (or no eslint) |
| Tests passing | 25 | All tests pass (or no tests) |

**Total: 100 points**

Projects without certain tools get full points for those checks (don't penalize simpler projects).

### Step 4: Generate Recommendations

Based on issues found:
- "Pull latest changes" if behind remote
- "Commit or stash changes" if dirty working tree
- "Fix type errors" if TypeScript fails
- "Fix lint issues" if ESLint fails
- "Fix failing tests" if tests fail

### Step 5: Output Report

Use the morning-report output style:

```
┌─────────────────────────────────────────────────────────────┐
│ 🌅 Morning Report - [Project Name]                          │
│ [Date] [Time]                                               │
├─────────────────────────────────────────────────────────────┤
│ Ready to Code Score: [XX/100] 🟢/🟡/🟠/🔴                   │
├─────────────────────────────────────────────────────────────┤
│ Git Status                                                   │
│ Branch: main                                                 │
│ Last commit: abc123 - feat: add feature (2 hours ago)       │
│ Working tree: clean                                         │
│ Remote sync: up to date                                     │
├─────────────────────────────────────────────────────────────┤
│ Code Quality                                                 │
│ TypeScript: ✓ No errors                                     │
│ Lint: ✓ Clean                                               │
│ Tests: ✓ All passing                                        │
├─────────────────────────────────────────────────────────────┤
│ Recommendations                                              │
│ None - you're ready to code!                                │
└─────────────────────────────────────────────────────────────┘
```

## Quick Mode

For quick status (with `quick` argument):

```
Morning Report: 85/100 🟢
✓ Git (clean) | ⚠ Lint (2 warnings) | ✓ Tests (passing)
Branch: main | Last: feat: add feature (2h ago)
```

## Project-Specific Extension

For project-specific health checks (database, services, etc.), use `/popkit:generate-morning` to create a customized version that includes:
- Service health checks (Redis, database, etc.)
- Framework-specific checks (Next.js, Express, etc.)
- Domain-specific validations (API keys, etc.)

## Examples

**Full report:**
```
/popkit:morning

🌅 Morning Report - my-project
2025-01-15 09:00

Ready to Code Score: 75/100 🟡

Git Status:
  Branch: feature/auth
  Last commit: abc123 - feat: add login
  Uncommitted: 3 files modified
  Remote: up to date

Code Quality:
  TypeScript: 2 errors
  Lint: clean
  Tests: 45/45 passing

Recommendations:
1. Fix 2 TypeScript errors before committing
2. Commit or stash your current changes
```

**Quick mode:**
```
/popkit:morning quick

Morning: 75/100 🟡 | ⚠ TS (2 errors) | ✓ Lint | ✓ Tests
Branch: feature/auth | 3 uncommitted files
```
