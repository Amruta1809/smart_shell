# 🧠 Smart Shell AI Agent

A CLI agent powered by OpenRouter that can:
- Chat conversationally
- List local files
- Fetch time
- Create files using natural language

## Setup
1. Clone the repository: git clone https://github.com/Amruta1809/smart-shell-ai.git
cd smart-shell-ai
2. Create a virtual environment (optional): python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
3. Install dependencies: pip install -r requirements.txt
4. Set up the OpenRouter API key in .env: OPENROUTER_API_KEY=your_api_key_here

## Model Choice:
Chosen free model: amazon/nova-2-lite-v1
- Lightweight, fast, general-purpose, free to use.

## Usage Examples:
- What files are in this directory?
- What time is it?
- Create a file named notes.txt with: Milk, Eggs
- Who is the capital of France?
- Hello


## Features
- Conversational AI for general knowledge queries.
- Execute local commands: list files, get time, create files.
- Natural language output for tool results (no JSON shown to user).
- Support for multiple free OpenRouter LLM models.




