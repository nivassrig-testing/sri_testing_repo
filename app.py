from flask import Flask, render_template, request, jsonify
from tools.ollama_client import generate_test_cases
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('input')
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    try:
        result = generate_test_cases(user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
