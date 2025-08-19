"""ADC agent module for general conversational AI.

This module provides the ADC (Agent Development Center) agent implementation
that can assist users with a wide range of questions and tasks.
"""

from google.adk.agents import Agent

from adk_models.core.constants import (
    DEFAULT_AGENT_DESCRIPTION,
    DEFAULT_AGENT_INSTRUCTION,
)


def create_agent() -> Agent:
    """Create and return the ADC root agent."""
    return Agent(
        name="adc_agent",
        model="gemini-2.0-flash",
        description=DEFAULT_AGENT_DESCRIPTION,
        instruction=DEFAULT_AGENT_INSTRUCTION,
    )


root_agent: Agent = create_agent()
