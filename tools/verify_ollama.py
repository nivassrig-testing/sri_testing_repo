
import requests
import json
import sys

def verify_ollama():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",
        "prompt": "Hello, are you ready to test?",
        "stream": False
    }
    
    try:
        print("Testing Ollama connection...")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        print("Success! Response from Ollama:")
        print(result.get("response"))
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama: {e}")
        return False

if __name__ == "__main__":
    if verify_ollama():
        sys.exit(0)
    else:
        sys.exit(1)
