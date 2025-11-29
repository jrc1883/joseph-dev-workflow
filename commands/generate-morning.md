---
description: Generate project-specific morning health check command by analyzing tech stack
---

# /popkit:generate-morning - Morning Command Generator

Analyze the project and generate a customized morning health check command.

## Usage

```
/popkit:generate-morning              # Generate for current project
/popkit:generate-morning --nightly    # Also generate nightly cleanup
```

## Process

Invokes the **morning-generator** skill:

1. Detect tech stack (frameworks, databases, services)
2. Identify health check requirements
3. Determine project command prefix
4. Generate `.claude/commands/[prefix]:morning.md`
5. Report findings and offer customization

## What Gets Detected

| Category | Examples |
|----------|----------|
| Frameworks | Next.js, Express, Vue, Django, FastAPI |
| Databases | PostgreSQL, MongoDB, Supabase, Prisma |
| Cache | Redis, Memcached |
| Services | Docker, eBay API, Stripe, AWS |
| Quality | TypeScript, ESLint, Jest, Pytest |

## Example Output

```
/popkit:generate-morning

Analyzing project...

Tech Stack Detected:
  Framework: Next.js 14
  Database: Supabase (local, port 54322)
  Cache: Redis (port 6379)
  Quality: TypeScript, ESLint, Jest

Project Prefix: "genesis" (from package.json)

Generating .claude/commands/genesis:morning.md...

Health checks configured:
  ✓ Next.js dev server (port 3000)
  ✓ Supabase services (ports 54321-54334)
  ✓ Redis connection
  ✓ TypeScript validation
  ✓ Jest test suite

Command created!

You can now run:
  /genesis:morning         # Full report
  /genesis:morning quick   # Quick status

Would you like me to also generate /genesis:nightly?
```

## Generated Command Features

The generated command includes:

### Service Health Checks
- Port availability
- Process status
- Connection testing

### Git Integration
- Branch info
- Uncommitted changes
- Remote sync status

### Quality Gates
- TypeScript errors
- Lint status
- Test results

### Ready to Code Score
- 0-100 scoring
- Color-coded status
- Actionable recommendations

## Customization

After generation, you can customize:
- Add additional services
- Adjust port numbers
- Include API key validations
- Add project-specific checks

## Related

- `/popkit:morning` - Generic morning check (works without generation)
- `/popkit:init-project` - Full project initialization (includes morning)
- `pop-morning-generator` - The underlying skill
