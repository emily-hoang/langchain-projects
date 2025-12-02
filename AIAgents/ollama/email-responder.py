import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for email response generation using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_legal_document(email_content, tone="professional"):
  prompt = f"Generate a {tone} response to the following email:\n\n{email_content}" \
            "Ensure the response is clear, concise, and addresses all points raised in the email."
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't generate a response! Please try again with different email content.")
    return ai_response
  else:
    return f"Sorry, I couldn't process your request."

# Create Gradio interface
interface = gr.Interface(
  fn=generate_legal_document,
  inputs=gr.Textbox(lines=10, label="Email Content", placeholder="Enter the email content you want to respond to"),
  outputs=gr.Textbox(lines=10, label="Response"),
  title="AI-powered Email Responder",
  description="Enter the email content to generate a professional response"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python email-responder.py and go to http://127.0.0.1:7860 for Gradio interface