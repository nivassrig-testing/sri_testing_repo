# 🧪 Local Test Case Generator (B.L.A.S.T.)

![Status](https://img.shields.io/badge/Status-Active-success)
![LLM](https://img.shields.io/badge/Model-Llama3.2-blue)
![Backend](https://img.shields.io/badge/Backend-Flask-green)

A deterministic, self-healing test case generator powered by a local **Ollama** LLM (`llama3.2`). This tool allows QA engineers to input requirements, user stories, or code snippets and receive comprehensive, structured test cases instantly—without sending data to the cloud.

---

## 🏗️ Architecture

The system follows a strict **3-Layer Architecture** designed for reliability and separation of concerns.

```mermaid
graph TD
    User((User))
    
    subgraph "Frontend (UI)"
        Ui[Web Interface]
        Script[Client Script]
    end
    
    subgraph "Backend (Flask)"
        App[app.py]
        Endpoint[/generate]
    end
    
    subgraph "Layer 3: Tools"
        Tool[generate_test_cases.py]
        Func[generate_test_cases()]
    end
    
    subgraph "Layer 1: Architecture"
        SOP[TEST_GENERATION_SOP.md]
        Prompt[Golden Prompt Template]
    end
    
    subgraph "Local LLM"
        Ollama[Ollama Service]
        Model[llama3.2]
    end

    User -->|Type Requirement| Ui
    Ui -->|POST request| App
    App -->|Route| Endpoint
    Endpoint -->|Call Tool| Tool
    Tool -->|Read Logic| SOP
    SOP -.->|Inject Template| Tool
    Tool -->|API Call| Ollama
    Ollama -->|Inference| Model
    Model -->|Markdown Response| Ollama
    Ollama -->|JSON Response| Tool
    Tool -->|Structured Data| Endpoint
    Endpoint -->|HTML Response| Ui
    Ui -->|Display Test Cases| User
```

### 1. **Layer 1: Architecture (`architecture/`)**
- **SOP (`TEST_GENERATION_SOP.md`)**: The "Brain". Definitions of prompt templates, logic rules, and error handling strategies.
- **Golden Prompt**: A carefully engineered prompt that forces the LLM to output only structured Markdown tables.

### 2. **Layer 2: Navigation (App Layer)**
- **Flask App (`app.py`)**: The "Nervous System". Routes user requests from the UI to the appropriate tool.
- **UI (`templates/index.html`)**: A premium, dark-themed chat interface for interaction.

### 3. **Layer 3: Tools (`tools/`)**
- **Generator (`generate_test_cases.py`)**: The "Muscle". Executes the logic defined in the SOP. It handles the connection to Ollama, error handling, and response formatting.

---

## 🚀 Getting Started

### Prerequisites
1.  **Python 3.8+**
2.  **Ollama** installed and running.
3.  **Llama3.2** model pulled:
    ```bash
    ollama pull llama3.2
    ```

### Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/nivassrig-testing/sri_testing_repo.git
    cd sri_testing_repo/Project1-LocalTestCaseGenerator
    ```
2.  Install dependencies:
    ```bash
    pip install flask requests markdown
    ```

### Usage
1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your browser and navigate to:
    `http://localhost:5000`
3.  Enter your test requirement (e.g., "Login page for a banking app") and hit send!

---

## 📂 Project Structure

```plaintext
Project1-LocalTestCaseGenerator/
├── app.py                  # Flask Application Entry Point
├── architecture/           # Layer 1: SOPs & prompt logic
│   └── TEST_GENERATION_SOP.md
├── tools/                  # Layer 3: Python execution scripts
│   ├── generate_test_cases.py
│   └── verify_ollama.py
├── templates/              # HTML Templates
│   └── index.html
├── static/                 # CSS & JS Assets
│   ├── style.css
│   └── script.js
├── gemini.md               # Project Constitution & Data Schemas
├── task_plan.md            # Project Roadmap
├── findings.md             # Research & Discovery Log
└── requirements.txt        # Python Dependencies
```
