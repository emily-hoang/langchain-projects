import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for identitifying named entities using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_named_entities(text):
  prompt = f"Extract all named entities (persons, organisations, locations, dates) from the input {text}"
  
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    return response.json().get("response", "No entities detected.")
  else:
    return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
  fn=extract_named_entities,
  inputs=gr.Textbox(lines=10, placeholder="Enter text for entity recognition"),
  outputs=gr.Textbox(lines=10, label="Extracted Entities"),
  title="AI-powered Named Entity Recognition (NER)",
  description="Enter a paragraph and Ollama AI will extract the persons, organisations, locations, and dates"
)
if __name__ == "__main__":
  interface.launch()
  
# Run the script: python name-entity-extractor.py and go to http://127.0.0.1:7860 for Gradio interface