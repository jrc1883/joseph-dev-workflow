---
name: worktree
description: Manage git worktrees for parallel development - create, list, analyze, remove
---

# /worktree - Git Worktree Management

Create and manage isolated workspaces for parallel development.

## Usage

```
/worktree <subcommand> [options]
```

## Subcommands

### create

Create new worktree with branch:

```
/worktree create <name>
/worktree create feature/auth
/worktree create fix-123 --from main
```

Process:
1. Check worktree directory exists
2. Verify .gitignore includes worktrees
3. Create worktree: `git worktree add .worktrees/<name> -b <name>`
4. Run project setup (npm install, etc.)
5. Verify tests pass
6. Report location

### list

List all worktrees:

```
/worktree list
```

Output:
```
Worktrees:
- main (default): /path/to/project
- feature/auth: /path/to/project/.worktrees/feature-auth
- fix/login: /path/to/project/.worktrees/fix-login
```

### analyze

Find opportunities for worktrees:

```
/worktree analyze
```

Checks for:
- Multiple in-progress branches
- Stale branches with uncommitted work
- Complex merge situations

### remove

Remove worktree and optionally branch:

```
/worktree remove <name>
/worktree remove feature/auth --keep-branch
```

Process:
1. Confirm worktree exists
2. Check for uncommitted changes
3. Warn if uncommitted: "Worktree has uncommitted changes. Delete anyway?"
4. Remove: `git worktree remove .worktrees/<name>`
5. Optionally delete branch

### prune

Clean up stale worktrees:

```
/worktree prune
```

Removes worktrees with deleted directories.

## Integration

Uses **using-git-worktrees** skill for:
- Directory selection logic
- .gitignore verification
- Project setup detection
- Test verification

## Examples

```
# Start new feature
/worktree create feature/user-profiles

# See all workspaces
/worktree list

# Clean up after merge
/worktree remove feature/user-profiles

# Find parallel work opportunities
/worktree analyze
```
