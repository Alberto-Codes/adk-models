# ADK Models

A Google Agent Development Kit (ADK) project featuring agents that can answer questions about time and weather using Google's Gemini models.

## Overview

This project demonstrates how to build AI agents using the Google Agent Development Kit (ADK). The ADC (Agent Development Center) agent uses Google's Gemini models with the default authentication method (Application Default Credentials) to respond to user queries about time and weather in various cities.

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

If you prefer to use Google AI Studio instead of Vertex AI:

1. Get an API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Set environment variables:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   export GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

### Environment Variables (.env file)

Create a `.env` file in the project root to persist your environment variables:

```env
# For Vertex AI (recommended for production)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=TRUE

# Alternative: For Google AI Studio
# GOOGLE_API_KEY=your-api-key-here
# GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

## Installation

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
   pip install google-adk
   # Or install all dependencies including dev tools:
   pip install -e .[dev]
   ```

## Usage

### Running the Agent

There are several ways to interact with your ADK agent:

#### 1. Interactive Web UI (Recommended)

Launch the development web interface:
```bash
adk web
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
│               └── adc/
│                   ├── __init__.py
│                   └── agent.py          # Main agent implementation
├── pyproject.toml                        # Project configuration
├── README.md                            # This file
├── .env                                 # Environment variables (create this)
└── uv.lock                             # Dependency lock file
```

## Agent Details

The ADC agent (`src/adk_models/core/agents/adc/agent.py`) demonstrates ADK's **default authentication approach**:

- **Model**: `"gemini-2.0-flash"` - passed as a simple string to the Agent constructor
- **Authentication**: Automatic via ADK's internal registry and Application Default Credentials
- **Connection Method**: ADK automatically routes Gemini model requests through the `google-genai` library
- **No Explicit Auth Code**: No need to manually configure authentication clients or credentials in your agent code
- **Capabilities**: Ready to handle time and weather queries (tools can be added as needed)

The agent leverages ADK's built-in model integration, where you simply specify the model name and ADK handles all the authentication and connection details behind the scenes.

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

To extend the agent with new capabilities, you can add custom tools while keeping the same default authentication approach:

```python
def get_current_weather(city: str) -> dict:
    """Your tool implementation here"""
    pass

root_agent = Agent(
    name="adc_agent",
    model="gemini-2.0-flash",  # Same default model string
    tools=[get_current_weather],  # Add your tools here
    description="Agent with weather capabilities",
    instruction="You can help with weather and other queries",
)
```

The authentication remains automatic - ADK handles all the Gemini model connectivity behind the scenes.

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
