---
name: pop:pr
description: GitHub pull request management - create, list, view, merge, review with templates
---

# /pr - Pull Request Management

Manage GitHub pull requests with structured templates.

## Usage

```
/pr <subcommand> [options]
```

## Subcommands

### create

Create new pull request:

```
/pr create                     # Interactive
/pr create --title "Add auth"  # With title
/pr create --draft             # As draft
/pr create --base develop      # Target branch
```

**PR Template:**
```markdown
## Summary
<2-3 bullet points describing changes>

## Changes
- `file.ts`: <what changed>
- `other.ts`: <what changed>

## Test Plan
- [ ] Unit tests pass
- [ ] Manual testing completed
- [ ] <specific verification>

## Screenshots
<if UI changes>

## Related Issues
Closes #<issue-number>

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### list

List pull requests:

```
/pr list                       # Open PRs
/pr list --state all           # All PRs
/pr list --author @me          # My PRs
/pr list --review-requested    # Needs my review
/pr list --draft               # Draft PRs only
```

Output:
```
Open PRs (5):
#67 [ready] Add authentication - @user - 2 reviews
#66 [draft] Refactor API - @user - 0 reviews
#65 [changes] Fix login bug - @user - 1 review
...
```

### view

View PR details:

```
/pr view 67
/pr view 67 --comments
/pr view 67 --files
/pr view 67 --checks
```

Output:
```
#67: Add authentication
State: open (ready for review)
Author: @username
Base: main <- feature/auth
Created: 2 days ago

Checks:
✓ CI / build
✓ CI / test
✓ CI / lint

Reviews:
✓ @reviewer1: approved
⏳ @reviewer2: pending

Files changed (5):
+120 -45 src/auth/login.ts
...
```

### merge

Merge pull request:

```
/pr merge 67                   # Default merge
/pr merge 67 --squash          # Squash and merge
/pr merge 67 --rebase          # Rebase and merge
/pr merge 67 --delete-branch   # Delete branch after
```

**Pre-merge checks:**
1. All required reviews approved
2. All status checks passing
3. No merge conflicts
4. Branch is up to date

### review

Add PR review:

```
/pr review 67 --approve
/pr review 67 --request-changes --comment "Please fix X"
/pr review 67 --comment "Looks good with minor suggestions"
```

### checkout

Check out PR locally:

```
/pr checkout 67
```

### diff

View PR diff:

```
/pr diff 67
/pr diff 67 --file src/auth.ts
```

### ready

Mark PR as ready for review (from draft):

```
/pr ready 67
```

### update

Update PR branch with base:

```
/pr update 67
```

## GitHub CLI Integration

All commands use `gh` CLI:
```bash
gh pr create --title "..." --body "..."
gh pr list --state open
gh pr view 67
gh pr merge 67 --squash
gh pr review 67 --approve
gh pr checkout 67
```

## Examples

```
# Create PR from current branch
/pr create --title "Add user authentication" --body "..."

# Check PR status
/pr view 67 --checks

# Squash merge with branch cleanup
/pr merge 67 --squash --delete-branch

# Review and approve
/pr review 67 --approve --comment "LGTM!"
```
