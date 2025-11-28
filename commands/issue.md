---
name: pop:issue
description: GitHub issue management - create, list, view, close, comment with AI-executable format
---

# /issue - GitHub Issue Management

Manage GitHub issues with AI-optimized formatting.

## Usage

```
/issue <subcommand> [options]
```

## Subcommands

### create

Create new issue with AI-executable format:

```
/issue create <title>
/issue create "Add user authentication"
/issue create --template bug
/issue create --template feature
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
/issue list                    # Open issues
/issue list --state all        # All issues
/issue list --label bug        # Filtered by label
/issue list --assignee @me     # Assigned to me
/issue list --milestone v1.0   # By milestone
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
/issue view 45
/issue view 45 --comments
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
/issue close 45
/issue close 45 --comment "Fixed in #PR"
/issue close 45 --reason completed
/issue close 45 --reason not_planned
```

### comment

Add comment to issue:

```
/issue comment 45 "Working on this"
/issue comment 45 --file notes.md
```

### edit

Update issue:

```
/issue edit 45 --title "New title"
/issue edit 45 --label add:priority:high
/issue edit 45 --assignee @username
/issue edit 45 --milestone v1.0
```

### link

Link issue to PR:

```
/issue link 45 --pr 67
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
/issue create "Login button unresponsive" --template bug

# List my assigned issues
/issue list --assignee @me --state open

# Close with comment
/issue close 45 --comment "Resolved in commit abc123"

# Add work note
/issue comment 45 "Started investigation, found potential race condition"
```
