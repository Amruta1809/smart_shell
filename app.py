import streamlit as st
from llm import query_llm
from tools import list_files, get_time, create_file
from parser import detect_tool

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# (Optional debug check – only shows in terminal, not UI)
API_KEY = os.getenv("OPENROUTER_API_KEY")


# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = """
You are a Smart Shell AI agent.

RULES:
- If the user asks a system command (files, time, create file), respond ONLY with JSON.
- If the user asks a normal question or general conversation, reply normally.
- Do NOT invent new tools. Allowed tools are ONLY:

TOOLS:
- LIST_FILES
- GET_TIME
- CREATE_FILE

FORMAT:
If a tool is needed:
{"tool":"TOOL_NAME","args":{...}}

If no tool is needed:
Respond normally as a helpful assistant.

EXAMPLES:

User: "Create a file named test.txt with: milk, eggs"
→ {"tool":"CREATE_FILE","args":{"filename":"test.txt","content":"milk, eggs"}}

User: "What files are here?"
→ {"tool":"LIST_FILES"}

User: "What is the capital of France?"
→ "Paris."

User: "Search file content"
→ "Sorry, I cannot search inside files yet."
"""

# --- UI Setup ---
st.set_page_config(page_title="Smart Shell AI", page_icon="🤖")
st.title("🧠 Smart Shell AI (Web Version)")
st.write("Type something and I'll decide whether to talk or perform an action.")

# --- Session-based chat history ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Input box ---
user_input = st.text_input("Enter command:")

# --- Handle request when button clicked ---
if st.button("Run"):
    if user_input.strip():

        llm_reply = query_llm(SYSTEM_PROMPT, user_input)
        parsed = detect_tool(llm_reply)

        tool = parsed.get("tool", "NONE")

        if tool == "LIST_FILES":
            result = list_files()
            response = f"📂 **Files:**\n```\n{result}\n```"

        elif tool == "GET_TIME":
            result = get_time()
            response = f"🕒 Current Time: **{result}**"

        elif tool == "CREATE_FILE":
            filename = parsed.get("args", {}).get("filename", "untitled.txt")
            content = parsed.get("args", {}).get("content", "")
            result = create_file(filename, content)
            response = f"📄 {result}"

        else:
            response = f"💬 {llm_reply}"

        # Save to chat history
        st.session_state.history.append((user_input, response))

# --- Display chat history ---
for user, reply in reversed(st.session_state.history):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(reply)
    st.markdown("---")
