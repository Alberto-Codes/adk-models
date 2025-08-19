"""OpenAI-compatible Pirate Agent module.

This module provides a pirate-themed agent that uses Google's OpenAI-compatible
endpoint for Gemini models with ADC authentication, arr!
"""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from adk_models.core.auth import build_openai_api_base, get_adc_token
from adk_models.core.constants import (
    PIRATE_AGENT_DESCRIPTION,
    PIRATE_AGENT_INSTRUCTION,
)


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
    """Create a swashbucklin' OpenAI-compatible pirate agent, arrr!

    The agent be configured to assist users with a wide range of questions and
    tasks with a hearty pirate spirit, using the Gemini model accessed via
    Vertex AI's OpenAI-compatible endpoint.

    Returns:
        Agent: A fully configured pirate agent ready to sail the digital seas!
    """
    model = create_litellm_model()
    return Agent(
        name="openai_pirate_agent",
        model=model,
        description=PIRATE_AGENT_DESCRIPTION,
        instruction=PIRATE_AGENT_INSTRUCTION,
    )


root_agent = create_agent()
