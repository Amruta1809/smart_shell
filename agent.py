from llm import query_llm
from tools import list_files, get_time, create_file
from parser import detect_tool

SYSTEM_PROMPT = """
You are a Smart Shell AI agent.

Your job is to decide whether a user's request should use a tool or just be answered normally.

RULES:
1. If the user asks to execute something on the computer (file commands, listing, time, write, read directory, create/edit files), respond ONLY with JSON:
   {"tool": "TOOL_NAME", "args": {...}}

2. If the user is chatting or asking general knowledge, DO NOT return JSON.
   Instead, reply normally.

AVAILABLE TOOLS:
- LIST_FILES
- GET_TIME
- CREATE_FILE
"""

def run_agent():
    print("\n🤖 Smart Shell AI Ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        try:
            # Get response from LLM
            llm_reply = query_llm(SYSTEM_PROMPT, user_input).strip()

            # Attempt to detect JSON tool command
            parsed = detect_tool(llm_reply)
            tool = parsed.get("tool", "NONE")

            # --- Tool Execution ---
            if tool == "LIST_FILES":
                result = list_files()
                print("📂 Files in directory:\n" + "\n".join(result))

            elif tool == "GET_TIME":
                result = get_time()
                print("⏰ Current time:", result)

            elif tool == "CREATE_FILE":
                args = parsed.get("args", {})
                filename = args.get("filename", "untitled.txt").strip()
                content = args.get("content", "").strip()
                create_file(filename, content)
                print(f"✅ File '{filename}' created successfully.")

            else:
                # Normal Chat Response
                print(f"💬 {llm_reply}")

        except Exception as e:
            print("❌ Error:", str(e))


if __name__ == "__main__":
    run_agent()
