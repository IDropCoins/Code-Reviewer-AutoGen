import autogen
import os
import re
config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY")
}

def extract_code_block(text: str) -> str:
    match = re.search(r"```python\n(.*?)\n```", text, re.DOTALL)
    return match.group(1).strip() if match else "No code block found"

# Create function map for tools
function_map = {
    "extract_code_block": extract_code_block
}



tutor = autogen.AssistantAgent(
    name="tutor",
    llm_config=config,
    system_message="You are a Python tutor. When asked, write clear and correct Python code."
)

reviewer = autogen.AssistantAgent(
    name="reviewer",
    llm_config=config,
    system_message="You are a Python code reviewer. Check the tutor's code for correctness, readability, and suggest improvements briefly.",
    function_map=function_map
)

student = autogen.UserProxyAgent(
    name="student",
    human_input_mode="NEVER",
    default_auto_reply="Thank you, I'm done.",      
    max_consecutive_auto_reply=1,                   
    code_execution_config={
        "work_dir": "sandbox",
        "use_docker": False,
        "timeout": 120
    }
)

# Step 1: Tutor answers
chat1=student.initiate_chat(
    tutor,
    message="Write a function that prints n factorial for n to be any number",
    max_rounds=1
)

# Extract and save the code - look for the message with code blocks
tutor_response = None
for message in reversed(chat1.chat_history):
    if message["role"] == "user" and "```python" in message["content"]:
        tutor_response = message["content"]
        break

if tutor_response:
    extracted_code = extract_code_block(tutor_response)
else:
    print("No tutor response with code found")
    extracted_code = "No code block found"
if extracted_code and "No code block found" not in extracted_code:
    with open("final_code.txt","w",encoding="utf-8") as f:
        f.write(extracted_code)
    print("Code saved to final_code.txt")
    
    # Step 2: Reviewer critiques with the actual code
    review_message = f"Please review this Python code for correctness, readability, and suggest improvements:\n\n```python\n{extracted_code}\n```"
    chat2=student.initiate_chat(
        reviewer,
        message=review_message,
        max_rounds=1
    )
else:
    print("No code block found in tutor's response")
    chat2 = None

full_history = chat1.chat_history
if chat2:
    full_history += chat2.chat_history



with open("chat_log.txt","w",encoding="utf-8") as f:
    for turn in full_history:
        f.write(f"{turn['role'].capitalize()}: {turn['content']}\n")
print("Full conversation saved to chat_log.txt")