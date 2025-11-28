---
name: pop:plugin-test
description: "Run plugin self-tests to verify component integrity"
---

# /plugin-test - Plugin Self-Testing

Run comprehensive tests on plugin components to ensure everything works correctly.

## Usage

```
/plugin-test              # Run all tests
/plugin-test hooks        # Test hooks only
/plugin-test agents       # Test agents only
/plugin-test skills       # Test skills only
/plugin-test routing      # Test agent routing
/plugin-test structure    # Test file structure
```

## Process

1. **Use the plugin-test skill** to run tests
2. **Load test definitions** from tests/ directory
3. **Execute tests by category:**
   - Structure: Validate files exist and are properly formatted
   - Hooks: Test JSON protocol compliance
   - Agents: Verify definitions and routing
   - Skills: Check SKILL.md format and dependencies
4. **Report results** with pass/fail summary

## Categories

| Category | What It Tests |
|----------|---------------|
| `hooks` | JSON stdin/stdout, error handling, timeouts |
| `agents` | Definitions, tools, routing keywords |
| `skills` | SKILL.md format, descriptions, dependencies |
| `routing` | Agent selection based on prompts |
| `structure` | File existence, YAML validity, references |

## Output

```
Running plugin self-tests...

[Structure Tests]
✓ agents/config.json valid
✓ hooks/hooks.json valid
✓ All 29 agents have definitions
✓ All 22 skills have SKILL.md

[Hook Tests]
✓ pre-tool-use: JSON protocol
✓ post-tool-use: JSON protocol
✓ session-start: JSON protocol
...

[Agent Tests]
✓ bug-whisperer: definition valid
✓ code-reviewer: routing keywords work
...

[Routing Tests]
✓ "fix bug" → bug-whisperer (0.8 confidence)
✓ "review code" → code-reviewer (0.9 confidence)
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Results: 54 passed, 0 failed, 2 skipped
Time: 12.3s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Test Files

Test definitions are stored in:
- `tests/hooks/` - Hook input/output tests
- `tests/agents/` - Agent definition tests
- `tests/skills/` - Skill structure tests
- `tests/routing/` - Agent routing tests

## Flags

| Flag | Description |
|------|-------------|
| `--verbose` | Show detailed test output |
| `--fail-fast` | Stop on first failure |
| `--json` | Output results as JSON |
