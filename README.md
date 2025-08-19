# ADK Models

A Google Agent Development Kit (ADK) project featuring agents that can answer questions about time and weather using Google's Gemini models.

## Overview

This project demonstrates how to build AI agents using the Google Agent Development Kit (ADK). It includes two implementations:

1. **ADC Agent** (`adc/`) - Uses ADK's default authentication method (Application Default Credentials) with Google's Gemini models
2. **OpenAI-Compatible Agent** (`openai/`) - Uses Google's OpenAI-compatible endpoint for Gemini models via the LiteLlm wrapper, authenticating with ADC credentials (not an API key)

Both agents can respond to user queries about time and weather in various cities, showcasing different ways to connect to Google's Gemini models.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

### 1. Google Cloud CLI

Install the Google Cloud CLI to enable authentication with Google Cloud services:

**macOS/Linux:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

**Windows:**
Download and run the installer from [Google Cloud CLI installation guide](https://cloud.google.com/sdk/docs/install-sdk).

### 2. Python 3.12+

This project requires Python 3.12 or higher. Check your Python version:
```bash
python --version
```

### 3. Google Cloud Project

You'll need access to a Google Cloud project with the Vertex AI API enabled. If you don't have one:
1. Create a new project in the [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the Vertex AI API
3. Set up billing if required

## Authentication Setup

This project uses Google ADK's **default authentication mechanism** which relies on **Application Default Credentials (ADC)**. The agent automatically discovers and uses credentials without requiring explicit configuration in your code - you simply pass the model name (e.g., `"gemini-2.0-flash"`) directly to the Agent constructor.

### How ADK Default Authentication Works

When you create an Agent with a Gemini model name like this:

```python
Agent(
    name="adc_agent",
    model="gemini-2.0-flash",  # ADK automatically handles authentication
    # ... other parameters
)
```

ADK's internal registry automatically:
1. Recognizes the `gemini-*` model string
2. Routes the request through the `google-genai` library
3. Uses Application Default Credentials to authenticate with Google Cloud

### Setting Up Application Default Credentials

### For Local Development

1. **Initialize the Google Cloud CLI:**
   ```bash
   gcloud init
   ```
   Follow the prompts to select your Google Cloud project.

2. **Set up Application Default Credentials:**
   ```bash
   gcloud auth application-default login
   ```
   This command will open a browser window where you can sign in with your Google account. Your credentials will be stored locally for use by the ADK agent.

3. **Set required environment variables:**
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   export GOOGLE_CLOUD_LOCATION="us-central1"  # or your preferred region
   export GOOGLE_GENAI_USE_VERTEXAI=TRUE
   ```

### Alternative: Using Google AI Studio (API Key)

**Required for the OpenAI-Compatible Agent:**

If you want to use the OpenAI-compatible agent or prefer Google AI Studio:

1. Get an API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Set environment variables:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   export GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

Note: The OpenAI-compatible agent (`openai_compat/`) requires the Google AI Studio API key and uses Google's OpenAI-compatible endpoint at `https://generativelanguage.googleapis.com/v1beta/openai/`.

### Environment Variables (.env file)

Create a `.env` file in the project root to persist your environment variables:

```env
# For Vertex AI (used by the default ADC agent)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=TRUE

# For Google AI Studio (required for OpenAI-compatible agent)
# GOOGLE_API_KEY=your-api-key-here
# GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

## Installation

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management and running scripts. Please ensure you have `uv` installed:

```bash
pip install uv  # or see uv documentation for other install methods
```

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd adk-models
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   
   # Activate (macOS/Linux):
   source .venv/bin/activate
   
   # Activate (Windows):
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   uv sync --group dev
   ```

> **Note:**
> Due to a breaking change in `openai` version 1.100.0 and above ([see issue #2564](https://github.com/openai/openai-python/issues/2564)), you must use `openai<1.100`. Version 1.100.0 and later moved or removed some internal types, causing import errors in libraries that depend on the previous structure (such as LiteLLM and others). Until upstream dependencies are updated, please avoid `openai>=1.100.0`.

## Usage

### Running the Agent

To launch the development web interface, run:
```bash
uv run adk web src/adk_models/core/agents
```

This will start a local server (usually at `http://localhost:8000`) where you can:
- Chat with your agent through a web interface
- View function call events and traces
- Debug agent responses
- Use voice/video features (with compatible models)

#### 2. Terminal Interface

Run the agent directly in your terminal:
```bash
adk run
```

#### 3. API Server

Start the agent as an API server:
```bash
adk api_server
```

### Example Queries

Try these sample prompts with your agent:
- "What is the weather in New York?"
- "What is the current time in New York?"
- "What is the weather in Paris?"
- "What is the time in Paris?"

## Project Structure

```
adk-models/
├── src/
│   └── adk_models/
│       ├── __init__.py
│       └── core/
│           └── agents/
│               ├── adc/
│               │   ├── __init__.py
│               │   └── agent.py          # Default ADK authentication
│               └── openai/
│                   ├── __init__.py
│                   └── agent.py          # OpenAI-compatible endpoint
├── pyproject.toml                        # Project configuration
├── README.md                            # This file
├── .env                                 # Environment variables (create this)
├── .env.example                         # Environment template
└── uv.lock                             # Dependency lock file
```

## Agent Details

This project includes two different agent implementations:

### 1. ADC Agent (`src/adk_models/core/agents/adc/agent.py`)

Demonstrates ADK's **default authentication approach**:

- **Model**: `"gemini-2.0-flash"` - passed as a simple string to the Agent constructor
- **Authentication**: Automatic via ADK's internal registry and Application Default Credentials
- **Connection Method**: ADK automatically routes Gemini model requests through the `google-genai` library
- **No Explicit Auth Code**: No need to manually configure authentication clients or credentials in your agent code

### 2. OpenAI-Compatible Agent (`src/adk_models/core/agents/openai/agent.py`)

Demonstrates using Google's **OpenAI-compatible endpoint** with ADC credentials:

- **Model**: `LiteLlm` instance configured for the OpenAI-compatible Gemini endpoint
- **Endpoint**: `https://<location>-aiplatform.googleapis.com/v1/projects/<project>/locations/<location>/endpoints/openapi` (set via environment variables)
- **Authentication**: Uses Application Default Credentials (ADC) to obtain a token, not an API key
- **Compatibility**: Standard OpenAI interface for Gemini models via the LiteLlm wrapper
- **Use Case**: Ideal for OpenAI-compatible workflows using Google Gemini with secure ADC authentication
- **Dependencies**: Requires the `google-adk` Python library

Both agents provide the same capabilities but showcase different connection methods to Google's Gemini models.

## Usage Notes for OpenAI-Compatible Agent

- Ensure you have set the following environment variables:
  - `GOOGLE_CLOUD_PROJECT` (your GCP project ID)
  - `GOOGLE_CLOUD_LOCATION` (your GCP region, e.g., `us-central1`)
- The agent will use ADC credentials to authenticate and obtain a token for the OpenAI-compatible endpoint.
- No API key is required for this agent; do not set `GOOGLE_API_KEY` for this workflow.

## Example: OpenAI-Compatible Agent Initialization

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
import google.auth
import google.auth.transport.requests

def create_api_key():
    credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    credentials.refresh(google.auth.transport.requests.Request())
    return credentials.token

model = LiteLlm(
    api_base=(
        f"https://{os.getenv('GOOGLE_CLOUD_LOCATION')}-aiplatform.googleapis.com/v1/"
        f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}/locations/"
        f"{os.getenv('GOOGLE_CLOUD_LOCATION')}/endpoints/openapi"
    ),
    api_key=create_api_key(),
    model="openai/google/gemini-2.0-flash",
)

agent = Agent(
    name="openai_agent",
    model=model,
    description="Agent to answer questions about the time and weather in a city using Google's OpenAI-compatible endpoint.",
    instruction="You are a helpful agent who can answer user questions about the time and weather in a city. You are powered by Google's Gemini model accessed through the OpenAI-compatible API.",
)
```

## Development

### Code Quality Tools

This project uses several tools to maintain code quality:

```bash
# Run linting
ruff check src/

# Format code
ruff format src/

# Type checking
ty check src/

# Run tests
pytest

# Run all quality checks
bash -c "ruff check src/ && ruff format --check src/ && ty check src/ && pytest"
```

### Adding New Tools

Both agents can be extended with new capabilities while maintaining their respective authentication approaches:

**For the default ADC agent:**
```python
def get_current_weather(city: str) -> dict:
    """Your tool implementation here"""
    pass

root_agent = Agent(
    name="adc_agent",
    model="gemini-2.0-flash",  # Default ADK approach
    tools=[get_current_weather],
    description="Agent with weather capabilities",
    instruction="You can help with weather and other queries",
)
```

**For the OpenAI-compatible agent:**
```python
import os
from google.adk.agents import Agent
from openai import OpenAI

class GeminiOpenAIModel:
    def __init__(self, model_name: str = "gemini-2.0-flash"):
        self.model_name = model_name
        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

def get_current_weather(city: str) -> dict:
    """Your tool implementation here"""
    pass

root_agent = Agent(
    name="adc_openai_compat_agent",
    model=GeminiOpenAIModel("gemini-2.0-flash"),
    tools=[get_current_weather],
    description="Agent with weather capabilities via OpenAI endpoint",
    instruction="You can help with weather and other queries",
)
```

## Troubleshooting

### Authentication Issues

**Error: "The Application Default Credentials are not available"**
- Run `gcloud auth application-default login` to set up ADC
- Verify your Google Cloud project is set: `gcloud config get-value project`
- Check that Vertex AI API is enabled in your project

**Error: "User credentials not working"**
- Some APIs require additional configuration for user credentials
- Try using a service account or contact your organization's admin
- Verify the API is enabled and you have proper IAM permissions

### Agent Not Found in Web UI

If your agent doesn't appear in the dropdown:
- Ensure you're running `adk web` from the parent directory of your agent folder
- Check that your agent module structure matches the expected format
- Verify the `__init__.py` files are present and properly configured

### Model Access Issues

**Error: "API not enabled" or "No quota project"**
- Enable the Vertex AI API in your Google Cloud project
- Set the `GOOGLE_CLOUD_PROJECT` environment variable
- Check your project's billing status

## Documentation Links

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Quickstart Guide](https://google.github.io/adk-docs/get-started/quickstart/)
- [ADK Models & Authentication Guide](https://google.github.io/adk-docs/agents/models/) - Explains ADK's default authentication approach
- [ADK Self-Hosted Endpoint Guide](https://google.github.io/adk-docs/agents/models/#self-hosted-endpoint-eg-vllm) - Documentation for using custom model wrappers
- [Google Gemini OpenAI Compatibility](https://ai.google.dev/gemini-api/docs/openai) - Google's OpenAI-compatible endpoint documentation
- [Application Default Credentials Setup](https://cloud.google.com/docs/authentication/provide-credentials-adc)
- [Google Cloud CLI Installation](https://cloud.google.com/sdk/docs/install-sdk)
- [Gemini Models Documentation](https://ai.google.dev/gemini-api/docs/models)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the quality checks
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
