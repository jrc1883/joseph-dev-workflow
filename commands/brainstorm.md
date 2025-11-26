---
name: brainstorm
description: Interactive design refinement using Socratic method - turn rough ideas into detailed designs
---

# /brainstorm - Interactive Design Session

Refine rough ideas into fully-formed designs through collaborative questioning.

## Usage

```
/brainstorm [topic]
```

## Process

Invokes the **brainstorming** skill:

1. **Understand context** - Review project state, docs, recent commits
2. **Ask questions** - One at a time, prefer multiple choice
3. **Explore approaches** - Present 2-3 options with trade-offs
4. **Present design** - In 200-300 word sections, validate each
5. **Document** - Save to `docs/plans/YYYY-MM-DD-<topic>-design.md`
6. **Implementation** - Offer worktree setup and plan creation

## Example Session

```
/brainstorm user authentication

Claude: Let me check the current project state...

Found: Next.js 14, Supabase, no existing auth

First question: What type of authentication do you need?
1. Email/password only
2. OAuth providers (Google, GitHub, etc.)
3. Magic link (passwordless)
4. Multiple options for users

> 2

Which OAuth providers should we support initially?
1. Google only (fastest to implement)
2. Google + GitHub
3. All major providers (Google, GitHub, Apple, Microsoft)

> 2

Let me present the design in sections...

## Section 1: Architecture
We'll use NextAuth.js with Supabase adapter for session management...

Does this section look right so far?

> yes

## Section 2: Components...
```

## Output

Creates design document:

```markdown
# User Authentication Design

> Created: 2025-01-15 via /brainstorm

## Summary
OAuth authentication with Google and GitHub providers...

## Architecture
[Validated design sections]

## Components
[Component breakdown]

## Implementation Notes
[Technical decisions made during brainstorm]
```

## Integration

After design approval, offers:
- Create worktree for implementation
- Generate implementation plan via /write-plan
