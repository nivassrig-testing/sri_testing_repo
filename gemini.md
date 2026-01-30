# Project Constitution (gemini.md)

## Data Schemas

### Core Payload: Test Case Generation
**Input (Prompt Request):**
```json
{
  "user_input": "string",  // The scenario, requirements, or code snippet from the user
  "model": "llama3.2"      // Fixed model requirement
}
```

**Output (Structured Test Cases):**
```json
{
  "test_cases": [
    {
      "id": "TC_001",
      "title": "string",
      "description": "string",
      "pre_conditions": "string",
      "steps": [
        "1. Step one..."
      ],
      "expected_result": "string",
      "type": "positive|negative|edge_case"
    }
  ],
  "summary": "string"
}
```

## Behavioral Rules
1. **Model**: STRICTLY use `llama3.2`.
2. **Determinism**: Output must always follow the JSON schema.
3. **Template**: Use a predefined "System Template" stored in code to guide the LLM.
4. **Interface**: Modern, aesthetic Web UI (Chat interface).

## Architectural Invariants
1. **Data-First**: Schema compliance is mandatory.
2. **Local-First**: All processing happens on localhost via Ollama.
3. **3-Layer**: 
    - `architecture/` (Prompt Templates & Logic)
    - `tools/` (Ollama Client & Parsers)
    - `ui/` (Frontend)
