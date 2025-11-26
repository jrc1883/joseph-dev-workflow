---
name: nightly-summary
description: End of day cleanup and status summary
---

# Nightly Summary Style

## Format

```
┌─────────────────────────────────────────────────────────────┐
│ 🌙 Nightly Summary - [Project Name]                         │
│ [Date] [Time]                                               │
├─────────────────────────────────────────────────────────────┤
│ Sleep Score: [XX/100]                                       │
├─────────────────────────────────────────────────────────────┤
│ Session Summary                                              │
│ Duration: 4h 32m                                            │
│ Commits: 8                                                  │
│ PRs: 1 created, 1 merged                                    │
│ Issues: 2 closed                                            │
├─────────────────────────────────────────────────────────────┤
│ Work Completed                                               │
│ ✓ Implemented user authentication                           │
│ ✓ Added OAuth support                                       │
│ ✓ Fixed login bug (#45)                                     │
├─────────────────────────────────────────────────────────────┤
│ Work In Progress                                             │
│ ⏳ Password reset flow (60%)                                 │
│ ⏳ Email templates (30%)                                     │
├─────────────────────────────────────────────────────────────┤
│ Uncommitted Changes                                          │
│ ⚠ 3 files with uncommitted changes                          │
│   - src/auth/reset.ts                                       │
│   - src/auth/reset.test.ts                                  │
│   - src/templates/reset-email.html                          │
├─────────────────────────────────────────────────────────────┤
│ Cleanup Performed                                            │
│ ✓ Logs rotated (removed 5 old files)                        │
│ ✓ Test artifacts cleaned                                    │
│ ✓ Git maintenance run                                       │
├─────────────────────────────────────────────────────────────┤
│ Tomorrow's Focus                                             │
│ 1. Complete password reset flow                             │
│ 2. Email template styling                                   │
│ 3. Integration testing                                      │
├─────────────────────────────────────────────────────────────┤
│ Safe to Close: [Yes/No]                                     │
│ [Reason if No]                                              │
└─────────────────────────────────────────────────────────────┘
```

## Sleep Score

| Score | Status | Meaning |
|-------|--------|---------|
| 90-100 | 🟢 Safe | Can close, all saved |
| 70-89 | 🟡 Caution | Uncommitted changes |
| 50-69 | 🟠 Warning | Important work not saved |
| 0-49 | 🔴 Danger | Risk of losing work |

## Checks Performed

### Session Summary
- Session duration
- Commits made
- PRs created/merged
- Issues closed

### Work Status
- Completed tasks
- In-progress tasks with %
- Blocked tasks

### Uncommitted Changes
- Files modified
- Nature of changes
- Risk assessment

### Cleanup
- Log rotation
- Artifact cleanup
- Cache pruning
- Git maintenance

## Tomorrow's Focus

Generated from:
- In-progress tasks
- STATUS.json nextAction
- Open issues assigned

## Safe to Close

Conditions for "Yes":
- No uncommitted changes
- No running processes that need data
- Session state saved to STATUS.json

Conditions for "No":
- Uncommitted changes exist
- Background processes running
- Unsaved work detected
