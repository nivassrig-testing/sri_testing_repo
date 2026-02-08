
# 🔹 Test Case Generation SOP

**Version:** 1.0
**Context:** This Standard Operating Procedure (SOP) defines the logic for generating test cases from user input using the local Ollama LLM (`llama3.2`).

## 1. Goal
Convert ambiguous or specific user input (requirements, user stories, or code snippets) into a structured markdown table of test cases.

## 2. Inputs
- `user_input` (String): The text provided by the user.
- `model` (String, Default: `llama3.2`): The LLM model to use.

## 3. The Golden Prompt Template
The system must use the following prompt structure. **Do not modify the core instructions without updating this SOP.**

```text
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
(Markdown Table)
```

## 4. Processing Logic
1.  **Receive Input:** API or CLI receives `user_input`.
2.  **Validate:** Ensure input is not empty.
3.  **Construct Prompt:** Inject `user_input` into the Golden Prompt Template.
4.  **Call LLM:** Send request to Ollama (`POST /api/generate`).
5.  **Extract:** efficient response handling (stream=False for v1).
6.  **Return:** The markdown content.

## 5. Error Handling
- **Connection Error:** If Ollama is down, return generic error: "Local LLM service is unavailable."
- **Empty Response:** If LLM returns empty, retry once.
