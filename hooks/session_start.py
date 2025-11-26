#!/usr/bin/env python3
"""
Session Start Hook
Handles session initialization and setup.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

def create_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir

def log_session_start(data):
    """Log session start data to JSON file."""
    logs_dir = create_logs_directory()
    log_file = logs_dir / "session_start.json"
    
    # Add timestamp
    data['timestamp'] = datetime.now().isoformat()
    
    # Read existing log data
    log_data = []
    if log_file.exists():
        try:
            with open(log_file, 'r') as f:
                log_data = json.load(f)
        except json.JSONDecodeError:
            log_data = []
    
    # Append new data
    log_data.append(data)
    
    # Write updated log
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=2)

def main():
    try:
        # Read input data from stdin
        input_data = sys.stdin.read()
        data = json.loads(input_data) if input_data.strip() else {}
        
        # Log the session start
        log_session_start(data)
        
        # Print welcome message
        print("Session started - hooks system active", file=sys.stderr)
        
    except Exception as e:
        print(f"Error in session_start hook: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block on errors

if __name__ == "__main__":
    main()