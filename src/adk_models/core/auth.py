"""Shared authentication utilities for OpenAI-compatible agents.

This module provides common authentication and model creation functions
for agents that use Google's OpenAI-compatible endpoint via ADC credentials.
"""

import os

import google.auth
import google.auth.transport.requests
from google.adk.models.lite_llm import LiteLlm
from google.auth.credentials import Credentials


def create_adc_credentials() -> Credentials:
    """Obtain Google ADC credentials for authenticating API requests.

    Returns:
        Credentials: An authorized credentials object with cloud-platform scope.

    Raises:
        google.auth.exceptions.DefaultCredentialsError: If ADC credentials
            cannot be found or loaded.
    """
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    return credentials


def get_adc_token() -> str:
    """Get a fresh access token from ADC credentials.

    Returns:
        str: A valid access token for Google Cloud APIs.

    Raises:
        google.auth.exceptions.RefreshError: If token refresh fails.
        google.auth.exceptions.DefaultCredentialsError: If ADC credentials
            cannot be found or loaded.
    """
    credentials = create_adc_credentials()
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    token = credentials.token
    if token is None:
        msg = "Failed to obtain access token from credentials"
        raise ValueError(msg)
    return token


def build_openai_api_base() -> str:
    """Build the OpenAI-compatible API base URL for Vertex AI.

    Returns:
        str: The complete API base URL for the OpenAI-compatible endpoint.

    Raises:
        ValueError: If required environment variables are not set.
    """
    project = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")

    if not project:
        msg = "GOOGLE_CLOUD_PROJECT environment variable is required"
        raise ValueError(msg)

    if not location:
        msg = "GOOGLE_CLOUD_LOCATION environment variable is required"
        raise ValueError(msg)

    return (
        f"https://{location}-aiplatform.googleapis.com/v1/"
        f"projects/{project}/locations/{location}/endpoints/openapi"
    )
