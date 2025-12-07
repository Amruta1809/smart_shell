from parser import detect_tool

def test_detect_list_files():
    response = '{"tool":"LIST_FILES"}'
    parsed = detect_tool(response)
    assert parsed["tool"] == "LIST_FILES"

def test_detect_get_time():
    response = '{"tool":"GET_TIME"}'
    parsed = detect_tool(response)
    assert parsed["tool"] == "GET_TIME"

def test_detect_create_file():
    response = '{"tool":"CREATE_FILE","args":{"filename":"a.txt","content":"hi"}}'
    parsed = detect_tool(response)
    assert parsed["tool"] == "CREATE_FILE"
    assert parsed["args"]["filename"] == "a.txt"
