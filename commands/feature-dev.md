---
description: 7-phase feature development workflow - Discovery through Summary
---

# /popkit:feature-dev - Complete Feature Development

End-to-end feature development using the 7-phase workflow.

## Usage

```
/popkit:feature-dev [feature-name]
/popkit:feature-dev "user authentication"
```

## The 7 Phases

### Phase 1: Discovery

**Goal:** Understand what to build

```
What feature would you like to build?
> User authentication with OAuth

Let me gather context about the project...
- Project: Next.js 14 with Supabase
- Existing auth: None
- Related: User model exists
```

### Phase 2: Exploration

**Goal:** Understand the codebase

Uses **code-explorer** agent:

```
Exploring codebase for similar features...

Entry Points:
- `src/app/api/auth/route.ts` (new)
- `src/components/auth/` (to create)

Patterns Found:
- API routes use standard Response format
- Components use server actions
- Database uses Supabase client

Files to Read:
- `src/lib/supabase.ts` - Client setup
- `src/types/user.ts` - User model
```

### Phase 3: Questions

**Goal:** Clarify requirements

```
A few questions to clarify the implementation:

1. Which OAuth providers should we support?
   a) Google only
   b) Google + GitHub
   c) All major providers

2. Should we support email/password as well?
   a) Yes
   b) No, OAuth only

3. Where should users be redirected after login?
   a) Dashboard
   b) Previous page
   c) Custom URL

> 1b, 2a, 3a
```

### Phase 4: Architecture

**Goal:** Design the implementation

Uses **code-architect** agent:

```
Designing architecture...

## Architecture Design: User Authentication

### Approach: Pragmatic Balance

### Component Design

| Component | Purpose | Location |
|-----------|---------|----------|
| AuthProvider | Context for auth state | `src/providers/` |
| LoginForm | Email/password form | `src/components/auth/` |
| OAuthButtons | Google/GitHub buttons | `src/components/auth/` |

### Implementation Map

Phase 1: Setup Supabase Auth
Phase 2: Create components
Phase 3: Add API routes
Phase 4: Wire up providers

Do you approve this architecture? [y/N]
```

### Phase 5: Implementation

**Goal:** Build the feature

```
Creating worktree for isolated development...
✓ .worktrees/feature-user-auth created
✓ npm install complete
✓ Tests passing (baseline)

Generating implementation plan...
✓ Plan saved to docs/plans/2025-01-15-user-auth.md

Executing plan...
[Task-by-task implementation with TDD]
```

### Phase 6: Review

**Goal:** Verify quality

Uses **code-reviewer** agent:

```
Reviewing implementation...

## Code Review: User Authentication

### Summary
Clean implementation with 95% test coverage.

### Critical Issues: 0
### Important Issues: 1
- Token refresh could be more robust

### Assessment
Ready to merge with minor improvements.

Quality Score: 8/10
```

### Phase 7: Summary

**Goal:** Complete and document

```
Feature development complete!

## Summary

### What Was Built
- OAuth login (Google, GitHub)
- Email/password authentication
- Session management
- Protected routes

### Files Created
- 8 new files
- 3 files modified
- 47 tests added

### Next Steps
Options:
1. Merge to main
2. Create PR for review
3. Keep branch for more work
4. Discard

Which option?
```

## Integration

The workflow uses these agents and skills:
- **code-explorer** - Phase 2
- **code-architect** - Phase 4
- **code-reviewer** - Phase 6
- **popkit:brainstorming** - Phase 1
- **popkit:writing-plans** - Phase 5
- **popkit:executing-plans** - Phase 5
- **popkit:finishing-a-development-branch** - Phase 7
