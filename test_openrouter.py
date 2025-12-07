import requests

# Replace with your actual API key
API_KEY = "sk-or-v1-58312f910320e72f4195071a86b72eb6bd248e026fb9c8ee04ad9852a"

# OpenRouter test endpoint (basic models info)
url = "https://api.openrouter.ai/v1/models"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("✅ API key is valid. Response:")
        print(response.json())
    elif response.status_code == 401:
        print("❌ Unauthorized. Check your API key or account.")
    else:
        print(f"⚠️ Unexpected status code {response.status_code}: {response.text}")
except Exception as e:
    print("⚠️ Error connecting to OpenRouter:", e)
