#!/usr/bin/env python3
"""
GitHub Issues Utility
Creates GitHub issues from lessons learned and error tracking data.

Part of the popkit plugin error tracking system.
"""

import subprocess
import json
from datetime import datetime
from pathlib import Path


def create_issue_from_lesson(lesson: dict) -> dict:
    """Create GitHub issue from lesson learned.

    Args:
        lesson: Dict containing lesson data with keys:
            - type: Category of lesson (routing_gap, validation_failure, etc.)
            - context: Where the issue was encountered
            - symptom: What was observed
            - root_cause: Why it happened
            - fix: How it was fixed
            - prevention: How to prevent it

    Returns:
        Dict with status and issue URL if successful
    """
    title = f"[Lesson Learned] {lesson.get('type', 'unknown')}: {lesson.get('symptom', 'No description')[:50]}"

    body = f"""## Context
{lesson.get('context', 'No context provided')}

## Symptom
{lesson.get('symptom', 'No symptom description')}

## Root Cause
{lesson.get('root_cause', 'Root cause not identified')}

## Fix Applied
{lesson.get('fix', 'No fix documented')}

## Prevention
{lesson.get('prevention', 'No prevention measures documented')}

---
*Auto-generated from popkit error tracking on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

    try:
        result = subprocess.run(
            [
                "gh", "issue", "create",
                "--title", title,
                "--body", body,
                "--label", "lesson-learned,automated"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            issue_url = result.stdout.strip()
            return {
                "status": "created",
                "url": issue_url,
                "title": title
            }
        else:
            return {
                "status": "error",
                "error": result.stderr,
                "title": title
            }
    except subprocess.TimeoutExpired:
        return {"status": "error", "error": "Timeout creating issue"}
    except FileNotFoundError:
        return {"status": "error", "error": "gh CLI not installed"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def create_issue_from_validation_failure(validation_result: dict) -> dict:
    """Create GitHub issue from validation failure.

    Args:
        validation_result: Dict containing validation data with keys:
            - agent: Name of the agent that failed
            - output_style: Expected output style
            - missing_fields: List of missing required fields

    Returns:
        Dict with status and issue URL if successful
    """
    agent = validation_result.get('agent', 'unknown')
    output_style = validation_result.get('output_style', 'unknown')
    missing = validation_result.get('missing_fields', [])

    title = f"[Validation Failure] {agent}: Missing {len(missing)} required fields"

    body = f"""## Agent
`{agent}`

## Expected Output Style
`{output_style}`

## Missing Required Fields
{chr(10).join(f'- `{field}`' for field in missing)}

## Context
Agent output did not conform to the declared output_style schema.

## Suggested Fix
Update the agent prompt or implementation to include the required fields.

---
*Auto-generated from popkit output validator on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

    try:
        result = subprocess.run(
            [
                "gh", "issue", "create",
                "--title", title,
                "--body", body,
                "--label", "validation-failure,agent,automated"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            return {
                "status": "created",
                "url": result.stdout.strip(),
                "title": title
            }
        else:
            return {"status": "error", "error": result.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def save_lesson_locally(lesson: dict, status_file: Path = None) -> dict:
    """Save lesson to local STATUS.json file.

    Args:
        lesson: Lesson data to save
        status_file: Path to STATUS.json (default: .claude/STATUS.json)

    Returns:
        Dict with status of operation
    """
    if status_file is None:
        status_file = Path(".claude/STATUS.json")

    try:
        # Load existing status
        status = {}
        if status_file.exists():
            with open(status_file, 'r', encoding='utf-8') as f:
                status = json.load(f)

        # Initialize lessons_learned if not present
        if 'lessons_learned' not in status:
            status['lessons_learned'] = []

        # Add ID and timestamp if not present
        if 'id' not in lesson:
            lesson['id'] = f"LL-{len(status['lessons_learned']) + 1:03d}"
        if 'date' not in lesson:
            lesson['date'] = datetime.now().strftime('%Y-%m-%d')

        # Add lesson
        status['lessons_learned'].append(lesson)

        # Save status
        status_file.parent.mkdir(parents=True, exist_ok=True)
        with open(status_file, 'w', encoding='utf-8') as f:
            json.dump(status, f, indent=2)

        return {
            "status": "saved",
            "id": lesson['id'],
            "file": str(status_file)
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def save_error_locally(error: dict, status_file: Path = None) -> dict:
    """Save error to local STATUS.json error_log.

    Args:
        error: Error data to save
        status_file: Path to STATUS.json (default: .claude/STATUS.json)

    Returns:
        Dict with status of operation
    """
    if status_file is None:
        status_file = Path(".claude/STATUS.json")

    try:
        # Load existing status
        status = {}
        if status_file.exists():
            with open(status_file, 'r', encoding='utf-8') as f:
                status = json.load(f)

        # Initialize error_log if not present
        if 'error_log' not in status:
            status['error_log'] = []

        # Add timestamp if not present
        if 'timestamp' not in error:
            error['timestamp'] = datetime.now().isoformat()

        # Add error
        status['error_log'].append(error)

        # Keep only last 100 errors
        if len(status['error_log']) > 100:
            status['error_log'] = status['error_log'][-100:]

        # Save status
        status_file.parent.mkdir(parents=True, exist_ok=True)
        with open(status_file, 'w', encoding='utf-8') as f:
            json.dump(status, f, indent=2)

        return {"status": "saved", "file": str(status_file)}
    except Exception as e:
        return {"status": "error", "error": str(e)}


if __name__ == "__main__":
    # Test the module
    test_lesson = {
        "type": "routing_gap",
        "context": "ESLint cleanup in test project",
        "symptom": "Specialists not triggered for lint work",
        "root_cause": "Missing 'lint', 'eslint' keywords in routing config",
        "fix": "Added lint keywords to agents/config.json",
        "prevention": "Add routing test cases for new keywords"
    }

    print("Testing save_lesson_locally...")
    result = save_lesson_locally(test_lesson)
    print(json.dumps(result, indent=2))
