import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for code auto completion, suggestion using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def auto_complete_code(code_snippet, language="python"):
  prompt = f"Complete the following {language} code snippet:\n\n{code_snippet}" \
            "Provide the missing code to make it functional and efficient."
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't generate a code completion! Please try again with different query.")
    return ai_response
  else:
    return f"Sorry, an error occurred while processing your request: {response.status_code}."

# Create Gradio interface
interface = gr.Interface(
  fn=auto_complete_code,
  inputs=gr.Textbox(lines=10, label="Code Snippet", placeholder="Enter your code snippet here"),
  outputs=gr.Textbox(lines=10, label="Code Completion"),
  title="AI-powered Code Auto Completion",
  description="Enter your code snippet to get auto completion suggestions"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python resume-generator.py and go to http://127.0.0.1:7860 for Gradio interface