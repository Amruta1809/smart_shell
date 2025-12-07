import json

def detect_tool(llm_response: str):
    """
    Expected response format from LLM:
    {"tool": "LIST_FILES", "args": {}}
    OR
    {"tool": "CREATE_FILE", "args": {"filename": "notes.txt", "content": "Milk, Bread"}}
    OR
    {"tool": "NONE"}
    """
    try:
        return json.loads(llm_response)
    except json.JSONDecodeError:
        return {"tool": "NONE", "args": {}}
