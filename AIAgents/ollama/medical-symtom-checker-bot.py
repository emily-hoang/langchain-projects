import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for assisting with medical symptom checking using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_legal_document(symtoms):
  prompt = f"Analyse the following symtoms and suggest possible medical conditions: {symtoms}" \
            "Provide a short list of possible causes and general advice on next steps."
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't analyze the symptoms! Please try again with different symptoms.")
    return ai_response
  else:
    return f"Sorry, I couldn't process your request."

# Create Gradio interface
interface = gr.Interface(
  fn=generate_legal_document,
  inputs=gr.Textbox(lines=10, label="Symptoms", placeholder="Enter the symptoms you are experiencing"),
  outputs=gr.Textbox(lines=10, label="Result"),
  title="AI-powered Medical Symptom Checker",
  description="Enter your symptoms to get possible medical conditions and advice"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python medical-symptom-checker-bot.py and go to http://127.0.0.1:7860 for Gradio interface