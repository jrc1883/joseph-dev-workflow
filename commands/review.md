---
description: Code review with confidence-based filtering - only reports high-confidence issues (80+ threshold)
---

# /popkit:review - Code Review

Review code changes with confidence-based issue filtering.

## Usage

```
/popkit:review                        # Review uncommitted changes
/popkit:review --staged               # Review staged changes only
/popkit:review --branch feature/auth  # Review branch vs main
/popkit:review --pr 67                # Review PR changes
/popkit:review --file src/auth.ts     # Review specific file
```

## Process

Invokes the **code-review** skill:

### Step 1: Gather Changes

```bash
git diff HEAD~1...HEAD         # For branch review
git diff --cached              # For staged
git diff                       # For uncommitted
```

### Step 2: Analyze Categories

- **Simplicity/DRY/Elegance** - Duplication, complexity, abstractions
- **Bugs/Correctness** - Logic errors, edge cases, type safety
- **Conventions** - Project patterns, naming, organization

### Step 3: Score and Filter

Each issue gets confidence score (0-100):
- 0-49: Ignored (likely false positive)
- 50-79: Noted but not reported
- 80-89: Important (should fix)
- 90-100: Critical (must fix)

**Threshold: 80+** only reported.

### Step 4: Report

```markdown
## Code Review: Feature Auth

### Summary
Clean implementation with good test coverage. Two issues found.

### Critical Issues (Must Fix)

#### Issue 1: Missing null check
- **File**: `src/auth.ts:45`
- **Confidence**: 95/100
- **Category**: Bug/Correctness
- **Description**: `user.email` accessed without null check
- **Fix**: Add optional chaining or null check

### Important Issues (Should Fix)

#### Issue 2: Duplicate validation logic
- **File**: `src/auth.ts:60-75`
- **Confidence**: 82/100
- **Category**: Simplicity/DRY
- **Description**: Email validation duplicated from utils
- **Fix**: Import and use existing validateEmail()

### Assessment

**Ready to merge?** With fixes

**Reasoning**: Critical null check issue must be resolved.
Minor DRY improvement recommended.

### Quality Score: 7/10
```

## Options

```
/popkit:review --focus simplicity     # Focus on DRY/elegance
/popkit:review --focus correctness    # Focus on bugs
/popkit:review --focus conventions    # Focus on patterns
/popkit:review --threshold 70         # Lower confidence threshold
/popkit:review --verbose              # Include lower-confidence issues
```

## Integration

Part of development workflow:
- After each task in subagent-driven development
- Before creating PRs
- On request during implementation
