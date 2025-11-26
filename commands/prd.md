---
name: prd
description: Create Product Requirements Document from brainstorming session
---

# /prd - Product Requirements Document

Generate a PRD from a brainstorming session or feature description.

## Usage

```
/prd [topic]
/prd "task management app"
/prd --from design.md          # Generate from design doc
```

## Process

1. Run brainstorming session (if not provided)
2. Extract requirements
3. Structure as PRD
4. Save to `docs/prd/YYYY-MM-DD-<topic>.md`

## PRD Template

```markdown
# Product Requirements Document: [Product Name]

**Version:** 1.0
**Date:** YYYY-MM-DD
**Author:** [Name]

---

## Executive Summary

[2-3 sentences describing the product/feature]

## Problem Statement

### Current Pain Points
- [Pain point 1]
- [Pain point 2]

### Target Users
- [User persona 1]
- [User persona 2]

## Goals and Objectives

### Primary Goals
1. [Goal 1]
2. [Goal 2]

### Success Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| [Metric] | [Value] | [How measured] |

## Requirements

### Functional Requirements

#### Must Have (P0)
- [ ] [Requirement 1]
- [ ] [Requirement 2]

#### Should Have (P1)
- [ ] [Requirement 3]

#### Nice to Have (P2)
- [ ] [Requirement 4]

### Non-Functional Requirements

- **Performance:** [Requirements]
- **Security:** [Requirements]
- **Accessibility:** [Requirements]
- **Scalability:** [Requirements]

## User Stories

### Epic: [Epic Name]

**Story 1:** As a [user], I want to [action] so that [benefit]
- Acceptance Criteria:
  - [ ] [Criterion 1]
  - [ ] [Criterion 2]

## Technical Considerations

### Architecture
[High-level architecture decisions]

### Dependencies
- [Dependency 1]
- [Dependency 2]

### Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [Impact] | [Mitigation] |

## Timeline

### Phase 1: MVP
- Duration: [X weeks]
- Deliverables: [List]

### Phase 2: Enhancement
- Duration: [X weeks]
- Deliverables: [List]

## Appendix

### Glossary
- **Term:** Definition

### References
- [Reference 1]
```

## Example

```
/prd task management app

Starting brainstorming session...
[Interactive session to gather requirements]

Generating PRD...

PRD created: docs/prd/2025-01-15-task-management.md

Summary:
- 5 P0 requirements
- 8 P1 requirements
- 3 P2 requirements
- 12 user stories
- 3-phase timeline

Would you like to:
1. Review and edit the PRD
2. Generate implementation plan
3. Create GitHub issues from requirements
```
