
from flask import Flask, render_template, request, jsonify
import sys
import os
import markdown

# Ensure we can import from tools
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
from generate_test_cases import generate_test_cases

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('user_input')
    
    if not user_input:
        return jsonify({"status": "error", "message": "No input provided"}), 400

    # Call our internal tool
    result = generate_test_cases(user_input)
    
    # Convert markdown to HTML for display
    if result["status"] == "success":
        result["html_content"] = markdown.markdown(
            result["test_cases"],
            extensions=['tables', 'fenced_code']
        )
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
