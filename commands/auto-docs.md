---
name: pop:auto-docs
description: "Automatically generate and update plugin documentation"
---

# /auto-docs - Automatic Documentation Generator

Generate and synchronize plugin documentation by analyzing the codebase.

## Usage

```
/auto-docs              # Full documentation generation
/auto-docs check        # Check for documentation drift
/auto-docs claude       # Update CLAUDE.md only
/auto-docs readme       # Update README.md only
/auto-docs components   # Generate component reference
```

## Process

1. **Use the auto-docs skill** to generate documentation
2. **Scan the plugin structure:**
   - Count agents in `agents/` directories
   - Extract skill descriptions from `skills/*/SKILL.md`
   - List commands from `commands/`
   - Document hooks from `hooks/`
3. **Generate or update documentation files:**
   - CLAUDE.md - Project instructions
   - README.md - User documentation
   - docs/components.md - Component reference
4. **Report any drift** between code and documentation

## Flags

| Flag | Description |
|------|-------------|
| `check` | Only check for drift, don't update files |
| `claude` | Update CLAUDE.md only |
| `readme` | Update README.md only |
| `components` | Generate component reference only |

## Output

- Updated documentation files
- Drift report showing discrepancies
- Summary of changes made

## Example

```
> /auto-docs

Scanning plugin structure...
- Agents: 29 (11 tier-1, 15 tier-2, 3 feature-workflow)
- Skills: 22 (21 + auto-docs)
- Commands: 18 (17 + auto-docs)
- Hooks: 10

Updating CLAUDE.md...
✓ Repository structure updated
✓ Component counts updated

Updating README.md...
✓ Feature counts updated
✓ Installation section current

No documentation drift detected.
```
