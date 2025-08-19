"""ADC agent module for time and weather queries.

This module provides the ADC (Agent Development Center) agent implementation
that can answer questions about time and weather in various cities.
"""

from google.adk.agents import Agent


def create_agent() -> Agent:
    """Create and return the ADC root agent."""
    return Agent(
        name="adc_agent",
        model="gemini-2.0-flash",
        description=(
            "Agent to answer questions about the time and weather in a city."
        ),
        instruction=(
            "You are a helpful agent who can answer user questions about "
            "the time and weather in a city."
        ),
    )


root_agent = create_agent()
