---
description: Create detailed implementation plan with bite-sized tasks for engineers with zero codebase context
---

# /popkit:write-plan - Implementation Planning

Generate comprehensive implementation plans with exact file paths, code examples, and verification steps.

## Usage

```
/popkit:write-plan [feature-name]
/popkit:write-plan                    # Interactive
/popkit:write-plan user-auth          # From topic
/popkit:write-plan --from design.md   # From design doc
```

## Process

Invokes the **popkit:writing-plans** skill:

1. Load design document or gather requirements
2. Break into bite-sized tasks (2-5 minutes each)
3. Include exact file paths
4. Provide complete code examples
5. Add verification commands
6. Save to `docs/plans/YYYY-MM-DD-<feature>.md`

## Plan Structure

```markdown
# [Feature] Implementation Plan

> **For Claude:** Use popkit:executing-plans skill to implement.

**Goal:** [One sentence]
**Architecture:** [2-3 sentences]
**Tech Stack:** [Technologies]

---

### Task 1: [Component Name]

**Files:**
- Create: `exact/path/to/file.ts`
- Modify: `existing/file.ts:50-75`
- Test: `tests/file.test.ts`

**Step 1: Write the failing test**
\`\`\`typescript
// Complete test code
\`\`\`

**Step 2: Run test to verify it fails**
Run: `npm test -- file.test.ts`
Expected: FAIL

**Step 3: Write minimal implementation**
\`\`\`typescript
// Complete implementation
\`\`\`

**Step 4: Run test to verify it passes**
Run: `npm test -- file.test.ts`
Expected: PASS

**Step 5: Commit**
\`\`\`bash
git commit -m "feat: add component"
\`\`\`

---

### Task 2: ...
```

## Principles

- **DRY** - Don't repeat yourself
- **YAGNI** - You ain't gonna need it
- **TDD** - Test-driven development
- **Frequent commits** - After each task

## Output

Creates plan at `docs/plans/YYYY-MM-DD-<feature>.md`

Then offers execution options:
1. **Subagent-Driven** - Same session, fresh subagent per task
2. **Parallel Session** - New session with /popkit:execute-plan
