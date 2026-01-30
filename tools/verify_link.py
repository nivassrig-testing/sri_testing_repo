import ollama
import sys
import pprint

def verify_ollama():
    print("Testing Ollama Connection...")
    try:
        # Check available models
        models = ollama.list()
        print(f"Ollama connected. Found {len(models['models'])} models.")
        print("Models response debug:")
        pprint.pprint(models)
        
        target_model = "llama3.2"
        # Adjusted to handle potential difference in key names, though 'name' is standard. 
        # Usually it is 'name' or 'model'.
        found = False
        for m in models['models']:
            # The python library returns objects sometimes, or dicts.
            # Let's handle both.
            name = m.get('name') if isinstance(m, dict) else getattr(m, 'model', getattr(m, 'name', ''))
            if target_model in name:
                found = True
                break
        
        if not found:
            print(f"[X] Model '{target_model}' not found in Ollama library.")
            print("Please run: ollama pull llama3.2")
            return False
        else:
            print(f"[OK] Model '{target_model}' is available.")
            
        print(f"Attempting generation with {target_model}...")
        response = ollama.chat(model=target_model, messages=[
            {'role': 'user', 'content': 'Say "B.L.A.S.T. verified" if you can hear me.'},
        ])
        print(f"Response: {response['message']['content']}")
        return True

    except Exception as e:
        print(f"[X] Error connecting to Ollama: {e}")
        print("Ensure Ollama is running (e.g., in system tray or via 'ollama serve').")
        return False

if __name__ == "__main__":
    success = verify_ollama()
    if not success:
        sys.exit(1)
