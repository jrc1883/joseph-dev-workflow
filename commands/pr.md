---
description: GitHub pull request management - create, list, view, merge, review with templates
---

# /popkit:pr - Pull Request Management

Manage GitHub pull requests with structured templates.

## Usage

```
/popkit:pr <subcommand> [options]
```

## Subcommands

### create

Create new pull request:

```
/popkit:pr create                     # Interactive
/popkit:pr create --title "Add auth"  # With title
/popkit:pr create --draft             # As draft
/popkit:pr create --base develop      # Target branch
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
/popkit:pr list                       # Open PRs
/popkit:pr list --state all           # All PRs
/popkit:pr list --author @me          # My PRs
/popkit:pr list --review-requested    # Needs my review
/popkit:pr list --draft               # Draft PRs only
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
/popkit:pr view 67
/popkit:pr view 67 --comments
/popkit:pr view 67 --files
/popkit:pr view 67 --checks
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
/popkit:pr merge 67                   # Default merge
/popkit:pr merge 67 --squash          # Squash and merge
/popkit:pr merge 67 --rebase          # Rebase and merge
/popkit:pr merge 67 --delete-branch   # Delete branch after
```

**Pre-merge checks:**
1. All required reviews approved
2. All status checks passing
3. No merge conflicts
4. Branch is up to date

### review

Add PR review:

```
/popkit:pr review 67 --approve
/popkit:pr review 67 --request-changes --comment "Please fix X"
/popkit:pr review 67 --comment "Looks good with minor suggestions"
```

### checkout

Check out PR locally:

```
/popkit:pr checkout 67
```

### diff

View PR diff:

```
/popkit:pr diff 67
/popkit:pr diff 67 --file src/auth.ts
```

### ready

Mark PR as ready for review (from draft):

```
/popkit:pr ready 67
```

### update

Update PR branch with base:

```
/popkit:pr update 67
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
/popkit:pr create --title "Add user authentication" --body "..."

# Check PR status
/popkit:pr view 67 --checks

# Squash merge with branch cleanup
/popkit:pr merge 67 --squash --delete-branch

# Review and approve
/popkit:pr review 67 --approve --comment "LGTM!"
```
