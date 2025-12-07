import os
from datetime import datetime

def list_files():
    return "\n".join(os.listdir("."))

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return f"📄 File '{filename}' created."

