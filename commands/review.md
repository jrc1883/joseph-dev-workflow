---
name: pop:review
description: Code review with confidence-based filtering - only reports high-confidence issues (80+ threshold)
---

# /review - Code Review

Review code changes with confidence-based issue filtering.

## Usage

```
/review                        # Review uncommitted changes
/review --staged               # Review staged changes only
/review --branch feature/auth  # Review branch vs main
/review --pr 67                # Review PR changes
/review --file src/auth.ts     # Review specific file
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
/review --focus simplicity     # Focus on DRY/elegance
/review --focus correctness    # Focus on bugs
/review --focus conventions    # Focus on patterns
/review --threshold 70         # Lower confidence threshold
/review --verbose              # Include lower-confidence issues
```

## Integration

Part of development workflow:
- After each task in subagent-driven development
- Before creating PRs
- On request during implementation
