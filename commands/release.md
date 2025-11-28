---
description: GitHub release management - create releases, generate changelogs, tag versions
---

# /popkit:release - Release Management

Create and manage GitHub releases with auto-generated changelogs.

## Usage

```
/popkit:release <subcommand> [options]
```

## Subcommands

### create

Create new release:

```
/popkit:release create <version>
/popkit:release create v1.2.0
/popkit:release create v1.2.0 --draft
/popkit:release create v1.2.0 --prerelease
```

Process:
1. Generate changelog from commits since last release
2. Create git tag
3. Create GitHub release with notes

**Release Notes Template:**
```markdown
## What's Changed

### Features
- feat: Add user authentication (#45)
- feat: Add dark mode support (#43)

### Bug Fixes
- fix: Resolve login validation issue (#44)
- fix: Fix memory leak in dashboard (#42)

### Other Changes
- chore: Update dependencies
- docs: Improve API documentation

## Full Changelog
https://github.com/owner/repo/compare/v1.1.0...v1.2.0

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### list

List releases:

```
/popkit:release list                  # All releases
/popkit:release list --limit 5        # Recent 5
/popkit:release list --draft          # Include drafts
```

Output:
```
Releases:
v1.2.0 - 2 days ago - Latest
v1.1.0 - 2 weeks ago
v1.0.0 - 1 month ago
v0.9.0-beta - 2 months ago (prerelease)
```

### view

View release details:

```
/popkit:release view v1.2.0
```

Output:
```
Release v1.2.0
Tag: v1.2.0
Published: 2 days ago
Author: @username

Assets:
- source.zip (1.2 MB)
- source.tar.gz (1.1 MB)

Notes:
[Full release notes]
```

### edit

Edit release:

```
/popkit:release edit v1.2.0 --notes "Updated notes"
/popkit:release edit v1.2.0 --draft false
/popkit:release edit v1.2.0 --prerelease true
```

### delete

Delete release:

```
/popkit:release delete v1.2.0
/popkit:release delete v1.2.0 --tag  # Also delete tag
```

### changelog

Generate changelog without creating release:

```
/popkit:release changelog             # Since last release
/popkit:release changelog v1.1.0      # Since specific version
/popkit:release changelog --format md # Markdown output
```

## Version Detection

Automatically detects version from:
1. Command argument
2. package.json version
3. Cargo.toml version
4. Latest tag + increment

## Changelog Generation

Analyzes commits for:
- **feat**: New features
- **fix**: Bug fixes
- **docs**: Documentation
- **perf**: Performance
- **refactor**: Code changes
- **test**: Tests
- **chore**: Maintenance

Groups by type and includes PR/issue links.

## GitHub CLI Integration

All commands use `gh` CLI:
```bash
gh release create v1.2.0 --notes "..."
gh release list
gh release view v1.2.0
gh release edit v1.2.0
gh release delete v1.2.0
```

## Examples

```
# Create release with auto-generated notes
/popkit:release create v1.2.0

# Create draft release for review
/popkit:release create v1.3.0 --draft

# View what would be in changelog
/popkit:release changelog

# Edit release notes
/popkit:release edit v1.2.0 --notes "$(cat CHANGELOG.md)"
```
