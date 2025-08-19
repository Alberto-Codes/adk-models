"""OpenAI-compatible Sequential Agent package.

This module provides the SequentialAgent implementation that uses Google's
OpenAI-compatible endpoint for Gemini models.
"""

from google.adk.agents import SequentialAgent

from adk_models.core.agents.open_ai import root_agent as openai_agent
from adk_models.core.agents.open_ai_pirate import (
    root_agent as openai_pirate_agent,
)


def create_agent() -> SequentialAgent:
    """Create a SequentialAgent that combines OpenAI and Pirate agents."""
    return SequentialAgent(
        name="openai_sequential_agent",
        sub_agents=[openai_agent, openai_pirate_agent],
    )


root_agent: SequentialAgent = create_agent()
