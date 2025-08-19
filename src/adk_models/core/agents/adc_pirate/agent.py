"""Arrr! This be the ADC Pirate Agent module for time and weather queries.

This here module provides the ADC (Agent Development Center) pirate agent,
ready to answer yer questions about time and weather in any port or city, matey!
"""

from google.adk.agents import Agent

from adk_models.core.constants import (
    PIRATE_AGENT_DESCRIPTION,
    PIRATE_AGENT_INSTRUCTION,
)


def create_agent() -> Agent:
    """Raise the anchor and create the ADC root pirate agent, arrr!"""
    return Agent(
        name="adc_pirate_agent",
        model="gemini-2.0-flash",
        description=PIRATE_AGENT_DESCRIPTION,
        instruction=PIRATE_AGENT_INSTRUCTION,
    )


root_agent = create_agent()
