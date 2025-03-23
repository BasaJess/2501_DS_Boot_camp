## Retrieval Augmented Generation with LangChain

This lesson shows how with LangChain framework one could perfor Retrieval Augmented Generation, i.e., augment a Language Large Model with document retrieval
There are two parallel notebooks
- `llama_rag` shows the use of completely open-sorce Huggingface and Llmma models
- `openai_rag` shows the use of OpenAi models  

Either notebook requires credentials to be loaded from a '.env' file, which should contain respectively either of the following lines, if not both:
```
GROQ_API_KEY=<your groq api key>
OPENAI_API_KEY=<your openai api key>
```

## Environment


Use the requirements file to create a new environment for this task. 

```Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

    For `PowerShell` CLI :

    ```PowerShell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt