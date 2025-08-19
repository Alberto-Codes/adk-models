"""OpenAI-compatible agent for answering time and weather questions.

This module provides an agent that leverages Google ADC credentials to
authenticate and interact with the Gemini model through an OpenAI-compatible
API endpoint.
"""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from adk_models.core.agents.constants import (
    DEFAULT_AGENT_DESCRIPTION,
    DEFAULT_AGENT_INSTRUCTION,
)
from adk_models.core.auth import build_openai_api_base, get_adc_token


def create_litellm_model(
    model_name: str = "openai/google/gemini-2.0-flash",
) -> LiteLlm:
    """Create a LiteLLM model configured for Google's OpenAI endpoint.

    Args:
        model_name: The model identifier to use. Defaults to
            "openai/google/gemini-2.0-flash".

    Returns:
        LiteLlm: A configured LiteLLM model instance.

    Raises:
        ValueError: If required environment variables are not set.
        google.auth.exceptions.RefreshError: If token refresh fails.
        google.auth.exceptions.DefaultCredentialsError: If ADC credentials
            cannot be found or loaded.
    """
    api_base = build_openai_api_base()
    api_key = get_adc_token()

    return LiteLlm(
        api_base=api_base,
        api_key=api_key,
        model=model_name,
    )


def create_agent() -> Agent:
    """Instantiate an OpenAI-compatible agent using Google's Gemini model.

    The agent is configured to answer questions about the time and weather in a
    city, using the Gemini model accessed via Vertex AI's OpenAI-compatible
    endpoint. Credentials are automatically refreshed and used as the API key.

    Returns:
        Agent: A fully configured agent ready to handle user queries.
    """
    model = create_litellm_model()
    return Agent(
        name="openai_agent",
        model=model,
        description=DEFAULT_AGENT_DESCRIPTION,
        instruction=DEFAULT_AGENT_INSTRUCTION,
    )


root_agent = create_agent()
