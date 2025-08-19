"""OpenAI-compatible agent for answering time and weather questions.

This module provides an agent that leverages Google ADC credentials to
authenticate and interact with the Gemini model through an OpenAI-compatible
API endpoint.
"""

import os

import google.auth
import google.auth.transport.requests
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.auth.credentials import Credentials

from adk_models.core.agents.constants import (
    DEFAULT_AGENT_DESCRIPTION,
    DEFAULT_AGENT_INSTRUCTION,
)


def create_api_key() -> Credentials:
    """Obtain Google ADC credentials for authenticating API requests.

    Returns:
        Credentials: An authorized credentials object with cloud-platform scope.
    """
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    return credentials


def create_agent() -> Agent:
    """Instantiate an OpenAI-compatible agent using Google's Gemini model.

    The agent is configured to answer questions about the time and weather in a
    city, using the Gemini model accessed via Vertex AI's OpenAI-compatible
    endpoint. Credentials are automatically refreshed and used as the API key.

    Returns:
        Agent: A fully configured agent ready to handle user queries.
    """
    credentials = create_api_key()
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    adc_token = credentials.token
    api_base = (
        f"https://{os.getenv('GOOGLE_CLOUD_LOCATION')}-aiplatform.googleapis.com/v1/"
        f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}/locations/"
        f"{os.getenv('GOOGLE_CLOUD_LOCATION')}/endpoints/openapi"
    )
    model = LiteLlm(
        api_base=api_base,
        api_key=adc_token,
        model="openai/google/gemini-2.0-flash",
    )
    return Agent(
        name="openai_agent",
        model=model,
        description=DEFAULT_AGENT_DESCRIPTION,
        instruction=DEFAULT_AGENT_INSTRUCTION,
    )


root_agent = create_agent()
