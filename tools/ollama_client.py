import ollama
import json
import os

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "architecture", "prompt_template.md")

def load_template():
    with open(TEMPLATE_PATH, "r") as f:
        return f.read()

def generate_test_cases(user_input, model="llama3.2"):
    """
    Generates test cases based on user input using Ollama.
    """
    system_prompt = load_template()
    
    full_prompt = f"""
    {system_prompt}
    
    **USER INPUT:**
    {user_input}
    """
    
    print(f"Sending request to {model}...")
    try:
        response = ollama.chat(model=model, messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ], format='json') # Enforce JSON mode if supported by model/library or just prompt engineering
        
        content = response['message']['content']
        
        # Simple validation just to check parsing
        try:
            data = json.loads(content)
            return data
        except json.JSONDecodeError:
            print("Failed to parse JSON. Raw output:")
            print(content)
            return {"error": "Invalid JSON response", "raw": content}
            
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Test run
    sample_input = "Login page: Username and Password fields. Button to submit."
    result = generate_test_cases(sample_input)
    import pprint
    pprint.pprint(result)
