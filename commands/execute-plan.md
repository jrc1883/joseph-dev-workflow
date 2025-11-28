---
name: pop:execute-plan
description: Execute implementation plan in batches with review checkpoints
---

# /execute-plan - Plan Execution

Execute implementation plans in controlled batches with review checkpoints.

## Usage

```
/execute-plan [plan-file]
/execute-plan                              # Select from recent plans
/execute-plan docs/plans/2025-01-15-auth.md
```

## Process

Invokes the **executing-plans** skill:

### Step 1: Load and Review

```
Loading plan: docs/plans/2025-01-15-auth.md

Plan Summary:
- Goal: Add user authentication
- Tasks: 8
- Estimated: 2-3 hours

Review Questions:
- [Any concerns about the plan]

Proceed with execution? [y/N]
```

### Step 2: Execute Batch

Default: 3 tasks per batch

```
Executing Batch 1 (Tasks 1-3):

Task 1: Create auth context [in_progress]
- Writing test...
- Test fails as expected
- Implementing...
- Test passes
- Committed: abc123

Task 1: Complete ✓

Task 2: Add login form [in_progress]
...
```

### Step 3: Report and Review

```
Batch 1 Complete:
✓ Task 1: Create auth context
✓ Task 2: Add login form
✓ Task 3: Add validation

Commits: 3
Tests: 12 passing

Ready for feedback.
```

User provides feedback → apply changes → continue.

### Step 4: Repeat

Continue with next batch until all tasks complete.

### Step 5: Finish

After all tasks:
- Run final verification
- Present completion options (merge, PR, keep, discard)

## Options

```
/execute-plan --batch-size 5     # Larger batches
/execute-plan --start-at 4       # Resume from task 4
/execute-plan --dry-run          # Preview without executing
```

## Handling Blockers

If blocked mid-batch:
1. Stop immediately
2. Report the blocker
3. Ask for clarification
4. Don't guess or work around

## Integration

Uses skills:
- **test-driven-development** - For each task
- **verification-before-completion** - After each batch
- **finishing-a-development-branch** - At completion
