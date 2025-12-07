import requests
import os
from dotenv import load_dotenv

# Load .env variables safely
load_dotenv(override=True)

API_KEY = os.getenv("OPENROUTER_API_KEY")

# Available free models on OpenRouter
FREE_MODELS = [
    "meta-llama/llama-3.3-70b-instruct:free",
    "tngtech/deepseek-r1t2-chimera:free",
    "amazon/nova-2-lite-v1:free",
    "google/gemma-3-27b-it:free",
    "openai/gpt-oss-20b:free",
    "google/gemini-2.0-flash-exp:free"
]

DEFAULT_MODEL = FREE_MODELS[1]   # auto-selected free model


def query_llm(system_prompt, user_input, model=DEFAULT_MODEL):
    """Send a message to the OpenRouter model."""

    if not API_KEY:
        return "❌ Missing API key in .env file!"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Smart Shell AI"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=25
        )

        if response.status_code != 200:
            return f"⚠️ HTTP {response.status_code}: {response.text}"

        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Running directly (optional for debugging only)
if __name__ == "__main__":
    print(query_llm("You are a helpful assistant.", "Hello! Tell me something cool."))
