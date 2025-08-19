

from google.adk.agents import SequentialAgent

from adk_models.core.agents.open_ai import root_agent as openai_agent
from adk_models.core.agents.open_ai_pirate import (
    root_agent as openai_pirate_agent,
)


def create_agent() -> SequentialAgent:
    """Summon an OpenAI-compatible pirate agent usin' Google's Gemini model, arrr!

    This agent be ready to answer yer questions about time and weather in any
    city, usin' the Gemini model via Vertex AI's OpenAI-compatible endpoint.
    Credentials be refreshed and used as the API key, just like a true
    buccaneer!

    Returns:
        Agent: A swashbucklin' agent ready to handle user queries.
    """
    return SequentialAgent(
        name="openai_sequential_agent",
        sub_agents=[openai_agent,
            openai_pirate_agent]
    )


root_agent = create_agent()
