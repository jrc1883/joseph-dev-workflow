#!/usr/bin/env python3
"""
Agent Context Integration Hook
Integrates project-aware agent loading into Claude Code's agent system.
This hook intercepts agent loading requests and adds project context.
"""

import os
import sys
import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import our context loading system
config_dir = Path.home() / ".claude" / "config"
sys.path.insert(0, str(config_dir))

try:
    from agent_context_loader import agent_context_loader, load_agent, get_agents, recommend_agents, get_project_info
    CONTEXT_SYSTEM_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Agent context system not available: {e}")
    CONTEXT_SYSTEM_AVAILABLE = False

def enhance_agent_loading(agent_name: str, working_directory: str = None) -> dict:
    """
    Enhance agent loading with project context
    This function is called by Claude Code when loading agents
    """
    if not CONTEXT_SYSTEM_AVAILABLE:
        logger.warning("Context system unavailable, falling back to default agent loading")
        return {}
    
    try:
        # Use our context loader to get enhanced agent
        enhanced_agent = load_agent(agent_name, working_directory)
        
        if enhanced_agent:
            logger.info(f"Successfully enhanced agent '{agent_name}' with project context")
            
            # Add metadata about the enhancement
            enhanced_agent['_context_enhanced'] = True
            enhanced_agent['_enhancement_timestamp'] = str(Path().cwd())
            
            return enhanced_agent
        else:
            logger.warning(f"Could not enhance agent '{agent_name}' - not found")
            return {}
            
    except Exception as e:
        logger.error(f"Error enhancing agent '{agent_name}': {e}")
        return {}

def get_agent_suggestions(user_input: str, working_directory: str = None) -> list:
    """
    Get intelligent agent suggestions based on user input
    This helps with automatic agent selection
    """
    if not CONTEXT_SYSTEM_AVAILABLE:
        return []
    
    try:
        recommendations = recommend_agents(user_input, working_directory)
        
        # Format recommendations for Claude Code
        suggestions = []
        for rec in recommendations:
            agent = rec['agent']
            suggestions.append({
                'name': agent.get('name'),
                'score': rec['score'],
                'reasons': rec['reasons'],
                'description': agent.get('description', ''),
                'is_project_specific': agent.get('project_specific', False),
                'is_enhanced': 'project_context' in agent
            })
        
        return suggestions
        
    except Exception as e:
        logger.error(f"Error getting agent suggestions: {e}")
        return []

def get_context_status(working_directory: str = None) -> dict:
    """
    Get current project context status for debugging and user info
    """
    if not CONTEXT_SYSTEM_AVAILABLE:
        return {'status': 'unavailable', 'reason': 'Context system not loaded'}
    
    try:
        status = get_project_info(working_directory)
        return {
            'status': 'available',
            'project_detected': status['detected_project'] is not None,
            'project_info': status['detected_project'],
            'has_overrides': status['has_overrides'],
            'has_custom_agents': status['has_custom_agents'],
            'available_overrides': status['available_overrides'],
            'available_custom_agents': status['available_custom_agents']
        }
        
    except Exception as e:
        logger.error(f"Error getting context status: {e}")
        return {'status': 'error', 'error': str(e)}

def list_all_agents(working_directory: str = None) -> dict:
    """
    List all available agents with project context awareness
    """
    if not CONTEXT_SYSTEM_AVAILABLE:
        return {'global': [], 'project_specific': [], 'enhanced_global': []}
    
    try:
        agents = get_agents(working_directory)
        
        # Add metadata for UI display
        for category, agent_list in agents.items():
            for agent in agent_list:
                agent['_category'] = category
                agent['_has_project_context'] = 'project_context' in agent
        
        return agents
        
    except Exception as e:
        logger.error(f"Error listing agents: {e}")
        return {'global': [], 'project_specific': [], 'enhanced_global': []}

# Main hook function - this is called by Claude Code
def on_agent_request(event_data: dict) -> dict:
    """
    Main hook function called by Claude Code for agent-related requests
    """
    event_type = event_data.get('type')
    working_dir = event_data.get('working_directory', os.getcwd())
    
    if event_type == 'load_agent':
        agent_name = event_data.get('agent_name')
        return enhance_agent_loading(agent_name, working_dir)
    
    elif event_type == 'suggest_agents':
        user_input = event_data.get('user_input', '')
        return {'suggestions': get_agent_suggestions(user_input, working_dir)}
    
    elif event_type == 'list_agents':
        return list_all_agents(working_dir)
    
    elif event_type == 'context_status':
        return get_context_status(working_dir)
    
    else:
        logger.warning(f"Unknown event type: {event_type}")
        return {}

# CLI interface for testing
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Test agent context integration')
    parser.add_argument('command', choices=['status', 'list', 'load', 'suggest'], help='Command to run')
    parser.add_argument('--agent', help='Agent name (for load command)')
    parser.add_argument('--input', help='User input (for suggest command)')
    parser.add_argument('--dir', help='Working directory')
    
    args = parser.parse_args()
    
    if args.command == 'status':
        status = get_context_status(args.dir)
        print("Context Status:")
        print(json.dumps(status, indent=2))
    
    elif args.command == 'list':
        agents = list_all_agents(args.dir)
        print("Available Agents:")
        for category, agent_list in agents.items():
            print(f"\n{category.upper()} ({len(agent_list)} agents):")
            for agent in agent_list:
                name = agent.get('name', 'Unknown')
                desc = agent.get('description', 'No description')[:50]
                enhanced = '✓' if agent.get('_has_project_context') else ' '
                print(f"  {enhanced} {name}: {desc}...")
    
    elif args.command == 'load':
        if not args.agent:
            print("Error: --agent required for load command")
            sys.exit(1)
        
        agent = enhance_agent_loading(args.agent, args.dir)
        if agent:
            print(f"Successfully loaded agent: {args.agent}")
            print(f"Enhanced: {'✓' if agent.get('_context_enhanced') else '✗'}")
            print(f"Instructions length: {len(agent.get('instructions', ''))}")
            print(f"Keywords: {len(agent.get('keywords', []))}")
        else:
            print(f"Failed to load agent: {args.agent}")
    
    elif args.command == 'suggest':
        if not args.input:
            print("Error: --input required for suggest command")
            sys.exit(1)
        
        suggestions = get_agent_suggestions(args.input, args.dir)
        print(f"Agent suggestions for: '{args.input}'")
        for i, sugg in enumerate(suggestions, 1):
            print(f"\n{i}. {sugg['name']} (score: {sugg['score']:.2f})")
            print(f"   {sugg['description'][:60]}...")
            print(f"   Reasons: {', '.join(sugg['reasons'])}")
    
    print(f"\nSystem Status: {'✓ Available' if CONTEXT_SYSTEM_AVAILABLE else '✗ Unavailable'}")