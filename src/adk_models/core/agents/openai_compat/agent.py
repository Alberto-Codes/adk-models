"""OpenAI-compatible agent using Google's Vertex AI endpoint.

This module provides an agent that uses Google's OpenAI-compatible endpoint
for Gemini models, demonstrating how to connect to Gemini through the
OpenAI protocol.
"""

import os

import google.auth
from google.auth.credentials import Credentials
import google.auth.transport.requests
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def create_api_key()-> Credentials:
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    print("Using ADC credentials:", credentials)
    return credentials





def create_agent() -> Agent:
    """Create and return the ADC agent using OpenAI-compatible endpoint.

    This agent uses Google's OpenAI-compatible endpoint for Gemini models,
    demonstrating how to connect to Gemini through the OpenAI protocol
    without using LiteLLM.

    Returns:
        Agent: Configured ADC agent using OpenAI-compatible endpoint.
    """
    credentials = create_api_key()
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    adc_token = credentials.token
    model = LiteLlm(
        api_key=adc_token,
        model="openai/google/gemini-2.0-flash",
    )
    return Agent(
        name="adc_openai_compat_agent",
        model=model,
        description=(
            "Agent to answer questions about the time and weather in a city "
            "using Google's OpenAI-compatible endpoint."
        ),
        instruction=(
            "You are a helpful agent who can answer user questions about "
            "the time and weather in a city. You are powered by Google's "
            "Gemini model accessed through the OpenAI-compatible API."
        ),
    )


root_agent = create_agent()
