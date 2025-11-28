---
description: Auto-generate commit message matching repository style with conventional commits
---

# /popkit:commit - Smart Commit

Generate commit message from staged changes, following repository conventions.

## Usage

```
/popkit:commit [message]
```

- Without message: Auto-generate from diff
- With message: Use provided message, format appropriately

## Process

### Step 1: Check Status

```bash
git status --porcelain
git diff --cached --stat
```

### Step 2: Analyze Changes

- Count files changed
- Identify change types (new, modified, deleted)
- Detect patterns (feat, fix, refactor, etc.)

### Step 3: Generate Message

Following conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, perf, test, chore, ci, revert

### Step 4: Commit

```bash
git commit -m "$(cat <<'EOF'
<generated message>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

## Examples

**Auto-generated:**
```
/popkit:commit
→ Analyzes diff, generates: "feat(auth): add password reset flow"
```

**With hint:**
```
/popkit:commit fixed the login bug
→ "fix(auth): resolve login validation issue"
```

## Attribution

All commits include:
- Claude Code attribution link
- Co-Authored-By header
