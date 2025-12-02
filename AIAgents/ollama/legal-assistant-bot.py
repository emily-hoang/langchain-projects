import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for assisting with legal document generation using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"
LEGAL_TEMPLATE = {
  "order tracking": "Generate a legal document for order tracking between {party_1} and {party_2}.",
  "return policy": "Generate a legal document for return policy between {party_1} and {party_2}.",
  "customer support contact": "Generate a legal document for customer support contact between {party_1} and {party_2}.",
  "payment methods": "Generate a legal document for payment methods between {party_1} and {party_2}.",
  "shipping details": "Generate a legal document for shipping details between {party_1} and {party_2}."
}

def generate_legal_document(doc_type, party_1, party_2, duration="", salary=""):
  if doc_type not in LEGAL_TEMPLATE:
    return "Sorry, I don't have a template for that document type. Available types are: " + ", ".join(LEGAL_TEMPLATE.keys())
  prompt = LEGAL_TEMPLATE[doc_type].format(party_1=party_1, party_2=party_2, duration=duration, salary=salary)
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't generate the document! Please try selecting a different type!")
    return ai_response
  else:
    return f"Sorry, I couldn't process your request."

# Create Gradio interface
interface = gr.Interface(
  fn=generate_legal_document,
  inputs=[
    gr.Textbox(label="Document Type", placeholder="Enter the type of legal document"),
    gr.Textbox(label="Party 1", placeholder="Enter the name of the first party"),
    gr.Textbox(label="Party 2", placeholder="Enter the name of the second party"),
    gr.Textbox(label="Duration (optional)", placeholder="Enter the duration if applicable"),
    gr.Textbox(label="Salary (optional)", placeholder="Enter the salary if applicable")
  ],
  outputs=gr.Textbox(lines=10, label="Result"),
  title="AI-powered Legal Document Assistant",
  description="Enter details to generate a legal document"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python legal-assistant-bot.py and go to http://127.0.0.1:7860 for Gradio interface