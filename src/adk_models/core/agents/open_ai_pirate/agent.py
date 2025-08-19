"""Arrr! This be the OpenAI-compatible Pirate Agent for answerin' time and
weather questions.

This here module provides a pirate agent that leverages Google ADC credentials
to parley with the Gemini model through an OpenAI-compatible API endpoint,
matey!
"""

import os

import google.auth
import google.auth.transport.requests
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.auth.credentials import Credentials

from adk_models.core.agents.constants import (
    PIRATE_AGENT_DESCRIPTION,
    PIRATE_AGENT_INSTRUCTION,
)


def create_api_key() -> Credentials:
    """Obtain Google ADC credentials for authenticatin' API requests, arrr!

    Returns:
        Credentials: An authorized credentials object with cloud-platform
        scope.
    """
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    return credentials


def create_agent() -> Agent:
    """Summon an OpenAI-compatible pirate agent usin' Google's Gemini model, arrr!

    This agent be ready to answer yer questions about time and weather in any
    city, usin' the Gemini model via Vertex AI's OpenAI-compatible endpoint.
    Credentials be refreshed and used as the API key, just like a true
    buccaneer!

    Returns:
        Agent: A swashbucklin' agent ready to handle user queries.
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
        name="openai_pirate_agent",
        model=model,
        description=PIRATE_AGENT_DESCRIPTION,
        instruction=PIRATE_AGENT_INSTRUCTION,
    )


root_agent = create_agent()
