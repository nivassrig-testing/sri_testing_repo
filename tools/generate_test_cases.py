
import requests
import json
import sys

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3.2"

def generate_test_cases(user_input, model=DEFAULT_MODEL):
    """
    Generates test cases from user input using Ollama.
    Follows architecture/TEST_GENERATION_SOP.md.
    """
    
    # 1. Construct Prompt (The Golden Prompt)
    prompt_template = f"""
You are an expert QA Automation Engineer. Your task is to generate comprehensive test cases based on the following input.

---
INPUT:
{user_input}
---

INSTRUCTIONS:
1. Analyze the input to understand the functionality and requirements.
2. Identify happy paths, edge cases, and potential error scenarios.
3. Output the test cases in a clean Markdown table format with the following columns:
   - Test Case ID (e.g., TC001)
   - Description
   - Pre-conditions
   - Test Steps (Numbered list)
   - Expected Result
   - Priority (High/Medium/Low)
4. Do not include introductory filler. Provide only the Markdown output.

OUTPUT:
"""

    payload = {
        "model": model,
        "prompt": prompt_template,
        "stream": False
    }

    try:
        print(f"Generating test cases with model '{model}'...")
        response_obj = requests.post(OLLAMA_URL, json=payload)
        response_obj.raise_for_status()
        
        result = response_obj.json()
        generated_text = result.get("response", "")
        
        if not generated_text:
            return {"status": "error", "message": "Ollama returned an empty response."}

        return {
            "status": "success",
            "test_cases": generated_text,
            "metadata": {
                "model": model,
                "duration": result.get("total_duration", 0) / 1e9 # Convert nanoseconds to seconds
            }
        }

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Connection error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}

if __name__ == "__main__":
    # Simple CLI test
    if len(sys.argv) > 1:
        user_input_arg = " ".join(sys.argv[1:])
    else:
        user_input_arg = "Login for Gmail" # Default test input

    result = generate_test_cases(user_input_arg)
    
    if result["status"] == "success":
        print("\n--- Generated Test Cases ---\n")
        print(result["test_cases"])
        print("\n----------------------------")
    else:
        print(f"Error: {result.get('message')}")
