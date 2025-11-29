---
name: sync
description: Validate and synchronize plugin state across all components
---

# /popkit:sync

Validates plugin integrity and offers to fix issues. Uses the Scan → Compare → Report → Recommend/Apply pattern.

## Usage

```bash
/popkit:sync                    # Analyze and report only
/popkit:sync apply              # Automatically apply safe fixes
/popkit:sync --component=agents # Check specific component
```

## Instructions

You are the sync validation engine. Your job is to scan the popkit plugin for integrity issues and report findings.

### Phase 1: Scan

Scan the following components:

1. **Agents** (`agents/`)
   - Check all agent files have valid YAML frontmatter
   - Verify required fields: name, description, tools
   - Check output_style references valid styles
   - Verify agent is listed in config.json

2. **Routing** (`agents/config.json`)
   - Check all keywords have valid agent references
   - Verify file patterns are syntactically valid
   - Ensure error patterns have valid agents
   - Check for orphaned agents (not in any tier)

3. **Output Styles** (`output-styles/`)
   - Check all styles have frontmatter
   - Verify schemas exist for styles with `output_style` references
   - Check example sections are present

4. **Hooks** (`hooks/`)
   - Verify all hooks in hooks.json exist as files
   - Check Python syntax validity
   - Verify stdin/stdout JSON protocol compliance

5. **Skills** (`skills/`)
   - Check all skills have SKILL.md
   - Verify frontmatter format
   - Check for duplicate skill names

6. **Tests** (`tests/`)
   - Verify test files are valid JSON
   - Check test coverage for routing rules
   - Ensure all agent types have routing tests

### Phase 2: Compare

Compare current state against expected:

```typescript
interface ValidationResult {
  component: string;
  status: 'pass' | 'warning' | 'error';
  issues: Issue[];
}

interface Issue {
  severity: 'error' | 'warning' | 'info';
  file: string;
  line?: number;
  message: string;
  autoFixable: boolean;
  fix?: string;
}
```

### Phase 3: Report

Generate a structured report:

```markdown
## Popkit Sync Report

**Scan Date:** [timestamp]
**Components Checked:** [count]
**Issues Found:** [count by severity]

### Summary

| Component | Status | Issues |
|-----------|--------|--------|
| Agents | [pass/warning/error] | [count] |
| Routing | [pass/warning/error] | [count] |
| Output Styles | [pass/warning/error] | [count] |
| Hooks | [pass/warning/error] | [count] |
| Skills | [pass/warning/error] | [count] |
| Tests | [pass/warning/error] | [count] |

### Issues by Severity

#### Errors (Must Fix)
- [issue 1]
- [issue 2]

#### Warnings (Should Fix)
- [issue 1]

#### Info (Nice to Have)
- [issue 1]

### Auto-Fixable Issues

The following issues can be automatically fixed:
1. [issue with fix description]
2. [issue with fix description]

Run `/popkit:sync apply` to apply these fixes.
```

### Phase 4: Recommend/Apply

If `apply` argument provided:
1. Only fix issues marked as `autoFixable: true`
2. Create backup before changes
3. Apply fixes one at a time
4. Report each fix applied
5. Run validation again to confirm

Safe auto-fixes include:
- Adding missing required frontmatter fields with defaults
- Registering orphaned agents in config.json
- Creating missing schema files from output style templates
- Adding missing routing test cases

Never auto-fix:
- Code changes in hooks
- Agent prompt content
- Skill instructions
- Configuration values that require decisions

## Example Output

```markdown
## Popkit Sync Report

**Scan Date:** 2025-01-28T10:00:00Z
**Components Checked:** 6
**Issues Found:** 3 errors, 5 warnings, 2 info

### Summary

| Component | Status | Issues |
|-----------|--------|--------|
| Agents | warning | 2 |
| Routing | pass | 0 |
| Output Styles | error | 1 |
| Hooks | pass | 0 |
| Skills | warning | 3 |
| Tests | info | 2 |

### Issues by Severity

#### Errors (Must Fix)
- `output-styles/agent-handoff.md`: Missing schema file at `output-styles/schemas/agent-handoff.schema.json`

#### Warnings (Should Fix)
- `agents/tier-2-on-demand/new-agent.md`: Missing output_style field
- `agents/tier-2-on-demand/another-agent.md`: Not registered in config.json tiers

#### Info (Nice to Have)
- `tests/routing/test-agent-routing.json`: No test for 'format' keyword routing
- `tests/routing/test-agent-routing.json`: No test for 'style' keyword routing

### Auto-Fixable Issues

1. Missing schema for agent-handoff - Will create from template
2. Missing output_style field - Will add `output_style: agent-handoff`

Run `/popkit:sync apply` to apply these fixes.
```

## Integration

This command uses the `pop-validation-engine` skill pattern:
- Scan: Collect current state
- Compare: Check against schema
- Report: Structured findings
- Recommend/Apply: Suggest or apply fixes

Related commands:
- `/popkit:plugin-test` - Run automated tests
- `/popkit:routing-debug` - Debug agent routing
- `/popkit:auto-docs` - Update documentation
