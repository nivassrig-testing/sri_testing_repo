# Project Constitution (Gemini)

## Data Schemas

### Core Payload
**Input Object (User Request):**
```json
{
  "user_input": "string", // The description or code snippet provided by the user
  "model": "llama3.2"     // Default model
}
```

**Output Object (System Response):**
```json
{
  "test_cases": "string", // Generated test cases in Markdown format
  "status": "success" | "error",
  "error_message": "string" | null, // Optional error details
  "metadata": {
    "model_used": "string",
    "generation_time": "number" // Time in seconds
  }
}
```

## Behavioral Rules
1. **Model**: strictly use `llama3.2` via Ollama.
2. **Template**: Logic must use a pre-defined prompt template stored in the code to ensure consistent high-quality output.
3. **UI**: Provide a Chat Interface for interaction.
4. **Local Execution**: All processing must happen locally; no external API calls to cloud LLMs.

## Architectural Invariants
- 3-layer architecture: Architecture -> Navigation -> Tools
- Deterministic business logic.
- Self-healing via "Self-Annealing" protocol.
