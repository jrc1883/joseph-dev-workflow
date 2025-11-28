---
name: pop:commit-push-pr
description: Full workflow - stage, commit, push to branch, and create pull request
---

# /pop:commit-push-pr - Full PR Workflow

One command to go from changes to pull request.

## Usage

```
/pop:commit-push-pr [branch-name]
```

## Process

### Step 1: Verify Clean State

```bash
git status
# Check for uncommitted changes
```

### Step 2: Create/Switch Branch (if needed)

```bash
# If branch-name provided and not on it
git checkout -b <branch-name>
# Or switch to existing
git checkout <branch-name>
```

### Step 3: Stage Changes

```bash
git add -A
# Or stage specific files if prompted
```

### Step 4: Generate Commit

Use /pop:commit flow:
- Analyze changes
- Generate conventional commit message
- Commit with attribution

### Step 5: Push Branch

```bash
git push -u origin <branch-name>
```

### Step 6: Create PR

```bash
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
<2-3 bullets of what changed>

## Changes
- <file changes>

## Test Plan
- [ ] <verification steps>

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

### Step 7: Report

```
PR created: <url>

Branch: <branch-name>
Commits: <count>
Files changed: <count>

Ready for review.
```

## Options

```
/pop:commit-push-pr                    # Use current branch
/pop:commit-push-pr feature/auth       # Create/use specific branch
/pop:commit-push-pr --draft            # Create as draft PR
/pop:commit-push-pr --no-verify        # Skip pre-commit hooks
```

## Safety

- Won't push to main/master directly
- Warns if branch already has open PR
- Confirms before force push
