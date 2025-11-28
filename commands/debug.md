---
description: Systematic debugging with root cause analysis - 4-phase framework
---

# /popkit:debug - Systematic Debugging

Systematic approach to finding and fixing bugs with root cause analysis.

## Usage

```
/popkit:debug [issue-description]
/popkit:debug                         # Describe issue interactively
/popkit:debug "login fails on mobile"
/popkit:debug --test failing-test.ts  # Debug specific test
```

## Process

Invokes the **popkit:systematic-debugging** skill:

### Phase 1: Root Cause Investigation

```
Starting systematic debugging...

1. Reading error messages carefully
2. Attempting to reproduce
3. Checking recent changes
4. Tracing data flow

Gathering evidence...
```

**DO NOT** propose fixes until Phase 1 is complete.

### Phase 2: Pattern Analysis

```
Finding patterns...

1. Locating similar working code
2. Comparing against references
3. Identifying differences
4. Understanding dependencies

Pattern found: [description]
```

### Phase 3: Hypothesis Testing

```
Forming hypothesis:
"The issue is caused by X because Y"

Testing minimally...
- Change: [single change]
- Result: [pass/fail]

Hypothesis confirmed/rejected.
```

### Phase 4: Implementation

```
Root cause identified: [cause]

Creating failing test...
Implementing fix...
Verifying fix...

Fixed! Test now passes.
```

## Red Flags

The skill will stop and return to Phase 1 if:
- "Quick fix" is attempted without investigation
- Multiple changes made at once
- Fixes proposed without understanding

## Options

```
/popkit:debug --verbose               # Show all investigation steps
/popkit:debug --skip-phase-1          # If already investigated (rare)
```

## Example Session

```
/popkit:debug "Users getting logged out randomly"

Phase 1: Investigation
- Error: "Token expired" in console
- Reproduces: Inconsistently, after ~30 minutes
- Recent change: Updated auth library 2 days ago
- Data flow: Token -> Storage -> Validation -> Rejection

Phase 2: Pattern Analysis
- Working: Previous version didn't have this
- Difference: New library uses shorter default expiry

Phase 3: Hypothesis
"Token expiry changed from 1 hour to 30 minutes in library update"
Testing: Check library changelog... Confirmed!

Phase 4: Fix
Test: "should maintain 1 hour session"
Fix: Configure explicit token expiry
Verify: Test passes, manual test confirms
```

## Integration

Uses skills:
- **popkit:root-cause-tracing** - When errors are deep in stack
- **popkit:defense-in-depth** - Adding validation layers after fix
- **popkit:test-driven-development** - Creating regression test
