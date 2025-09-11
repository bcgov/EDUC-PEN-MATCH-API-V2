from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Get credentials from .env
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Configure OpenAI client
openai.api_type = "azure"
openai.api_key = api_key
openai.api_base = endpoint
openai.api_version = api_version

# Test call
response = openai.ChatCompletion.create(
    engine=deployment,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response["choices"][0]["message"]["content"])
