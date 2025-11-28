---
name: popkit:code-review
description: "Use when completing tasks, implementing major features, or before merging to verify work meets requirements - reviews implementation against plan or requirements with confidence-based issue filtering (80+ threshold)"
---

# Code Review with Confidence Filtering

## Overview

Review code for bugs, quality issues, and project conventions with confidence-based filtering. Only reports HIGH confidence issues to reduce noise.

**Core principle:** Review early, review often. Filter out false positives.

## When to Request Review

**Mandatory:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## Confidence Scoring

Each identified issue receives a confidence score (0-100):

| Score | Meaning | Action |
|-------|---------|--------|
| 0 | Not a real problem | Ignore |
| 25 | Possibly valid | Ignore |
| 50 | Moderately confident | Note for reference |
| 75 | Highly confident | Report |
| 100 | Absolutely certain | Report as critical |

**Threshold: 80+** - Only issues scoring 80 or higher are reported.

## Filter Out

- Pre-existing problems (not introduced in this change)
- Linter-catchable issues (let the linter handle it)
- Pedantic nitpicks (style preferences without substance)
- Hypothetical edge cases (unlikely to occur in practice)

## Review Categories

### 1. Simplicity/DRY/Elegance
- Code duplication
- Unnecessary complexity
- Missed abstractions
- Overly clever code

### 2. Bugs/Correctness
- Logic errors
- Edge case handling
- Type safety issues
- Error handling gaps

### 3. Conventions/Abstractions
- Project pattern compliance
- Naming conventions
- File organization
- Import patterns

## Output Format

```markdown
## Code Review: [Feature/PR Name]

### Summary
[1-2 sentences on overall quality]

### Critical Issues (Must Fix)
_Issues with confidence 90+_

#### Issue 1: [Title]
- **File**: `path/to/file.ts:line`
- **Confidence**: 95/100
- **Category**: Bug/Correctness
- **Description**: What's wrong
- **Fix**: How to fix it

### Important Issues (Should Fix)
_Issues with confidence 80-89_

#### Issue 2: [Title]
- **File**: `path/to/file.ts:line`
- **Confidence**: 82/100
- **Category**: Conventions
- **Description**: What's wrong
- **Fix**: How to fix it

### Assessment

**Ready to merge?** Yes / No / With fixes

**Reasoning**: [1-2 sentences explaining the assessment]

### Quality Score: [X/10]
```

## How to Request Review

**1. Get git SHAs:**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatch code-reviewer subagent:**
- What was implemented
- Plan or requirements reference
- Base and head commits
- Brief description

**3. Act on feedback:**
- Fix Critical issues immediately
- Fix Important issues before proceeding
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Parallel Review

Launch 3 code-reviewer agents in parallel with different focuses:
1. **Simplicity Focus**: DRY, elegance, unnecessary complexity
2. **Correctness Focus**: Bugs, edge cases, error handling
3. **Conventions Focus**: Project patterns, naming, organization

Consolidate findings and filter by confidence threshold.

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore Critical issues
- Proceed with unfixed Important issues
- Argue with valid technical feedback

**If reviewer wrong:**
- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification

## Key Principle

"Ask what you want to do" - After presenting issues, ask the user how to proceed rather than making assumptions.
