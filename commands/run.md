---
description: GitHub Actions workflow management - list, view, rerun workflows and check statuses
---

# /popkit:run - GitHub Actions Management

Monitor and manage GitHub Actions workflows.

## Usage

```
/popkit:run <subcommand> [options]
```

## Subcommands

### list

List workflow runs:

```
/popkit:run list                      # Recent runs
/popkit:run list --workflow ci.yml    # Specific workflow
/popkit:run list --branch main        # By branch
/popkit:run list --status failure     # Failed only
/popkit:run list --limit 20           # More results
```

Output:
```
Recent Workflow Runs:
✓ CI #234 - main - 2m ago - 3m 45s
✗ CI #233 - feature/auth - 1h ago - 2m 12s
✓ Deploy #89 - main - 2h ago - 5m 30s
⏳ CI #235 - fix/bug - running - 1m 20s
...
```

### view

View run details:

```
/popkit:run view 234
/popkit:run view 234 --log
/popkit:run view 234 --job build
```

Output:
```
Run #234: CI
Status: success
Workflow: ci.yml
Branch: main
Commit: abc123 - "feat: add auth"
Duration: 3m 45s
Triggered: push

Jobs:
✓ build (1m 20s)
✓ test (2m 15s)
✓ lint (45s)
```

### rerun

Rerun workflow:

```
/popkit:run rerun 233                 # Rerun all jobs
/popkit:run rerun 233 --failed        # Rerun failed jobs only
/popkit:run rerun 233 --job test      # Rerun specific job
```

### watch

Watch running workflow:

```
/popkit:run watch 235
```

Live output:
```
Watching run #235...
⏳ build: running (45s)
   → Installing dependencies...

[Updates in real-time]

✓ build: completed (1m 20s)
⏳ test: running...
```

### cancel

Cancel running workflow:

```
/popkit:run cancel 235
```

### download

Download artifacts:

```
/popkit:run download 234              # All artifacts
/popkit:run download 234 --name dist  # Specific artifact
```

### logs

View logs:

```
/popkit:run logs 234                  # All logs
/popkit:run logs 234 --job build      # Specific job
/popkit:run logs 234 --failed         # Failed steps only
```

## GitHub CLI Integration

All commands use `gh` CLI:
```bash
gh run list
gh run view 234
gh run rerun 233 --failed
gh run watch 235
gh run cancel 235
gh run download 234
```

## Workflow Status Icons

- ✓ success
- ✗ failure
- ⏳ in_progress
- ○ queued
- ⊘ cancelled
- ⚠ skipped

## Examples

```
# Check why CI failed
/popkit:run list --status failure
/popkit:run view 233 --log

# Rerun failed tests
/popkit:run rerun 233 --failed

# Watch current run
/popkit:run watch

# Download build artifacts
/popkit:run download 234 --name build-output
```
