---
description: GitHub issue management - create, list, view, close, comment with AI-executable format
---

# /popkit:issue - GitHub Issue Management

Manage GitHub issues with AI-optimized formatting.

## Usage

```
/popkit:issue <subcommand> [options]
```

## Subcommands

### create

Create new issue with AI-executable format:

```
/popkit:issue create <title>
/popkit:issue create "Add user authentication"
/popkit:issue create --template bug
/popkit:issue create --template feature
```

**AI-Executable Format:**
```markdown
## Context
[Background information for understanding]

## Objective
[Clear statement of what needs to be done]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Technical Notes
[Implementation hints, relevant files, patterns]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Agent Routing
Suggested agents: [agent-names based on content]
```

Templates:
- **bug**: Bug report with reproduction steps
- **feature**: Feature request with user story
- **task**: Implementation task with checklist
- **research**: Investigation task

### list

List repository issues:

```
/popkit:issue list                    # Open issues
/popkit:issue list --state all        # All issues
/popkit:issue list --label bug        # Filtered by label
/popkit:issue list --assignee @me     # Assigned to me
/popkit:issue list --milestone v1.0   # By milestone
```

Output:
```
Open Issues (12):
#45 [bug] Login fails on mobile - @user - 2 days ago
#44 [feature] Add dark mode - @user - 3 days ago
#43 [task] Update dependencies - unassigned - 1 week ago
...
```

### view

View issue details:

```
/popkit:issue view 45
/popkit:issue view 45 --comments
```

Output:
```
#45: Login fails on mobile
State: open
Labels: bug, priority:high
Assignee: @username
Created: 2 days ago by @reporter

Description:
[Full issue body]

Comments (3):
...
```

### close

Close issue:

```
/popkit:issue close 45
/popkit:issue close 45 --comment "Fixed in #PR"
/popkit:issue close 45 --reason completed
/popkit:issue close 45 --reason not_planned
```

### comment

Add comment to issue:

```
/popkit:issue comment 45 "Working on this"
/popkit:issue comment 45 --file notes.md
```

### edit

Update issue:

```
/popkit:issue edit 45 --title "New title"
/popkit:issue edit 45 --label add:priority:high
/popkit:issue edit 45 --assignee @username
/popkit:issue edit 45 --milestone v1.0
```

### link

Link issue to PR:

```
/popkit:issue link 45 --pr 67
```

## Agent Routing

When creating issues, suggest appropriate agents:
- Bug issues → bug-whisperer, test-writer-fixer
- Security issues → security-auditor
- Performance issues → performance-optimizer
- API issues → api-designer
- Database issues → query-optimizer

## GitHub CLI Integration

All commands use `gh` CLI:
```bash
gh issue create --title "..." --body "..."
gh issue list --state open
gh issue view 45
gh issue close 45
gh issue comment 45 --body "..."
```

## Examples

```
# Create bug report
/popkit:issue create "Login button unresponsive" --template bug

# List my assigned issues
/popkit:issue list --assignee @me --state open

# Close with comment
/popkit:issue close 45 --comment "Resolved in commit abc123"

# Add work note
/popkit:issue comment 45 "Started investigation, found potential race condition"
```
