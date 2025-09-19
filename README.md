# Code Reviewer with AutoGen

This project demonstrates how to build a simple **multi-agent system using AutoGen** where:
- A **Tutor Agent** writes Python code based on user queries.
- A **Reviewer Agent** critiques the code for correctness, readability, and improvements.
- A **Student Proxy Agent** manages the conversation flow, executes code safely in a sandbox, and stores logs.

The system also:
- Saves the **entire chat transcript** into `chat_log.txt`.
- Extracts the **Tutor’s final code block** and saves it into `final_code.txt` for testing or reuse.

---

## 🚀 Features
- **Tutor Agent**: Generates clear, correct Python solutions.
- **Reviewer Agent**: Reviews Tutor’s solutions and suggests improvements.
- **Student Proxy Agent**: Automates interaction, prevents infinite loops, and runs code in a sandbox.
- **Conversation Logging**: Full transcript saved to `chat_log.txt`.
- **Code Extraction**: Clean Python code saved to `final_code.txt`.

---

## 📂 Project Structure
```

code-reviewer-autogen/
│── sandbox/             # Safe environment for code execution
│── chat\_log.txt         # Full transcript of Tutor & Reviewer conversation
│── final\_code.txt       # Extracted Python code from Tutor
│── main.py              # Main script (agents + logic)
│── requirements.txt     # Python dependencies
│── .gitignore
│── README.md

````

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/code-reviewer-autogen.git
   cd code-reviewer-autogen
    ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 OpenAI API Key

This project requires an OpenAI API key. The script loads it from **system environment variables** using:

```python
import os

config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY")
}
```

### Setting the key in system variables:

* **macOS/Linux (bash/zsh):**

  ```bash
  export OPENAI_API_KEY="your_api_key_here"
  ```
* **Windows (PowerShell):**

  ```powershell
  setx OPENAI_API_KEY "your_api_key_here"
  ```

### Alternative: Set directly in code (not recommended for production)

If you don’t want to use environment variables, you can hardcode it:

```python
config = {
    "model": "gpt-4o-mini",
    "api_key": "your_api_key_here"
}
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

After execution:

* `chat_log.txt` will contain the **full conversation** (Tutor + Reviewer).
* `final_code.txt` will contain the **clean extracted Python code**.

---

## 🛠️ Example Flow

1. Student asks Tutor: *"Write a function that prints n factorial for n to be any number"*
2. Tutor generates the Python code.
3. Student executes it inside the sandbox.
4. Reviewer critiques the Tutor’s code and suggests improvements.
5. Logs and final code are saved for review.

---

## 📌 Future Improvements

* Add a **Critic Agent** to review the Reviewer’s feedback.
* Integrate with **linters** (e.g., Pylint/Flake8) as tools for Reviewer.
* Extend pipeline to support multiple rounds of refinement.
* Store logs in a **database** instead of flat files.

## Author 👤

**Shivay Bajaj**

- GitHub: https://github.com/IDropCoins
