#!/usr/bin/env python3
"""
OPTIMUS Agent Observability Hook
Sends agent telemetry data to OPTIMUS Command Center
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path

# OPTIMUS WebSocket server endpoint
OPTIMUS_WS_URL = "http://localhost:3051"
OPTIMUS_TELEMETRY_ENDPOINT = f"{OPTIMUS_WS_URL}/api/agent/activity"
OPTIMUS_COLLABORATION_ENDPOINT = f"{OPTIMUS_WS_URL}/api/agent/collaboration"

def send_to_optimus(endpoint, data):
    """Send data to OPTIMUS telemetry endpoint"""
    try:
        response = requests.post(
            endpoint,
            json=data,
            timeout=2,
            headers={'Content-Type': 'application/json'}
        )
        return response.status_code == 200
    except Exception as e:
        # Fail silently to not disrupt Claude's workflow
        return False

def track_tool_use(tool_name, tool_args, tool_result=None, execution_time=0):
    """Track tool usage in OPTIMUS"""
    activity_data = {
        "agentName": os.environ.get('CLAUDE_AGENT_NAME', 'claude'),
        "activity": f"tool_use:{tool_name}",
        "metadata": {
            "toolName": tool_name,
            "toolArgs": tool_args,
            "executionTime": execution_time,
            "success": tool_result is not None,
            "sessionId": os.environ.get('CLAUDE_SESSION_ID', 'unknown'),
            "timestamp": datetime.now().isoformat(),
            "projectPath": os.getcwd()
        }
    }
    
    send_to_optimus(OPTIMUS_TELEMETRY_ENDPOINT, activity_data)

def track_agent_activation(agent_name, task_type, context=None):
    """Track agent activation in OPTIMUS"""
    activity_data = {
        "agentName": agent_name,
        "activity": f"activation:{task_type}",
        "metadata": {
            "taskType": task_type,
            "context": context or {},
            "sessionId": os.environ.get('CLAUDE_SESSION_ID', 'unknown'),
            "timestamp": datetime.now().isoformat(),
            "projectPath": os.getcwd()
        }
    }
    
    send_to_optimus(OPTIMUS_TELEMETRY_ENDPOINT, activity_data)

def track_collaboration(from_agent, to_agent, collaboration_type, metadata=None):
    """Track agent collaboration in OPTIMUS"""
    collab_data = {
        "agentName": from_agent,
        "partnerAgent": to_agent,
        "collaborationType": collaboration_type,
        "metadata": metadata or {}
    }
    
    send_to_optimus(OPTIMUS_COLLABORATION_ENDPOINT, collab_data)

def main():
    """Main hook entry point"""
    if len(sys.argv) < 2:
        return
    
    hook_type = sys.argv[1]
    
    if hook_type == "post-tool-use" and len(sys.argv) >= 4:
        tool_name = sys.argv[2]
        try:
            tool_args = json.loads(sys.argv[3]) if sys.argv[3] else {}
            tool_result = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None
            execution_time = float(sys.argv[5]) if len(sys.argv) > 5 else 0
            
            track_tool_use(tool_name, tool_args, tool_result, execution_time)
        except:
            pass
    
    elif hook_type == "agent-activation" and len(sys.argv) >= 4:
        agent_name = sys.argv[2]
        task_type = sys.argv[3]
        context = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None
        
        track_agent_activation(agent_name, task_type, context)
    
    elif hook_type == "agent-collaboration" and len(sys.argv) >= 5:
        from_agent = sys.argv[2]
        to_agent = sys.argv[3]
        collab_type = sys.argv[4]
        metadata = json.loads(sys.argv[5]) if len(sys.argv) > 5 else None
        
        track_collaboration(from_agent, to_agent, collab_type, metadata)

if __name__ == "__main__":
    main()