---
name: pop:finish-branch
description: Complete development work with 4-option flow - merge, PR, keep, or discard
---

# /finish-branch - Complete Development

Guide completion of development work with structured options.

## Usage

```
/finish-branch                 # Finish current branch
/finish-branch feature/auth    # Finish specific branch
```

## Process

Invokes the **finishing-a-development-branch** skill:

### Step 1: Verify Tests

```bash
npm test
```

```
Running tests...
✓ 47 tests passing

Tests verified. Proceeding to options.
```

If tests fail:
```
✗ 2 tests failing

Cannot proceed until tests pass.
[Show failing tests]
```

### Step 2: Present Options

```
Implementation complete. What would you like to do?

1. Merge back to main locally
2. Push and create a Pull Request
3. Keep the branch as-is (handle later)
4. Discard this work

Which option? [1-4]
```

### Option 1: Merge Locally

```bash
git checkout main
git pull
git merge feature/auth
npm test  # Verify merged result
git branch -d feature/auth
```

```
Merged feature/auth into main.
Branch deleted.
Worktree cleaned up.
```

### Option 2: Create PR

```bash
git push -u origin feature/auth
gh pr create --title "..." --body "..."
```

```
PR created: https://github.com/owner/repo/pull/68

Branch pushed and PR ready for review.
Worktree preserved for potential updates.
```

### Option 3: Keep As-Is

```
Keeping branch feature/auth.
Worktree preserved at .worktrees/feature-auth

You can return to this work anytime.
```

### Option 4: Discard

```
⚠️ This will permanently delete:
- Branch: feature/auth
- Commits: abc123, def456, ghi789
- Worktree: .worktrees/feature-auth

Type 'discard' to confirm:
```

If confirmed:
```bash
git checkout main
git branch -D feature/auth
git worktree remove .worktrees/feature-auth
```

## Safety

- Always verifies tests first
- Never force-pushes without confirmation
- Requires typed confirmation for discard
- Preserves worktree for PR option
