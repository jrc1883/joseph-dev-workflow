#!/usr/bin/env python3
"""
Subagent Stop Hook
Handles subagent completion with logging and optional TTS notifications.
"""

import sys
import json
import argparse
import shutil
from pathlib import Path

def create_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir

def get_tts_script_path():
    """Determine the best TTS script to use based on available API keys."""
    utils_dir = Path(".claude/hooks/utils/tts")
    
    # Check for API keys and return appropriate TTS script
    tts_options = [
        ("ELEVENLABS_API_KEY", utils_dir / "elevenlabs.py"),
        ("OPENAI_API_KEY", utils_dir / "openai_tts.py"),
        (None, utils_dir / "pyttsx3_tts.py")  # Local fallback
    ]
    
    for env_key, script_path in tts_options:
        if env_key is None or (env_key and env_key in os.environ):
            if script_path.exists():
                return script_path
    
    return None

def announce_subagent_completion():
    """Announce subagent completion using TTS if available."""
    try:
        import os
        import subprocess
        tts_script = get_tts_script_path()
        
        if tts_script:
            subprocess.run([
                sys.executable, str(tts_script), 
                "Subagent Complete"
            ], check=False, capture_output=True)
    except Exception:
        pass  # Silent failure for TTS

def main():
    parser = argparse.ArgumentParser(description="Subagent Stop Hook")
    parser.add_argument('--chat', action='store_true', 
                       help='Copy transcript to chat.json')
    
    args = parser.parse_args()
    
    try:
        # Read input data from stdin
        input_data = sys.stdin.read()
        data = json.loads(input_data) if input_data.strip() else {}
        
        # Create logs directory
        logs_dir = create_logs_directory()
        
        # Log subagent stop event
        log_file = logs_dir / "subagent_stop.json"
        log_data = []
        if log_file.exists():
            try:
                with open(log_file, 'r') as f:
                    log_data = json.load(f)
            except json.JSONDecodeError:
                log_data = []
        
        log_data.append(data)
        
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        # Copy transcript to chat.json if requested
        if args.chat and 'transcript' in data:
            chat_file = logs_dir / "chat.json"
            with open(chat_file, 'w') as f:
                json.dump(data['transcript'], f, indent=2)
        
        # Announce completion
        announce_subagent_completion()
        
    except Exception as e:
        print(f"Error in subagent_stop hook: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block on errors

if __name__ == "__main__":
    main()