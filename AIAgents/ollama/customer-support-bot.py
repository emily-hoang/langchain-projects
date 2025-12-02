import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for identitifying named entities using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"
FAQ_DB = {
  "oder tracking": "You can track your order by loggin into your account and navigating to",
  "return policy": "We accept returns within 30 days. Visit our Returns page to initiate a help request",
  "customer support contact": "You can reach customer support at support@example.com or call 8989375000",
  "payment methods": "We accept Visa, Mastercard, Paypal, and Apple Pay for secure transactions",
  "shipping details": "Orders are processed within 24 hours. Standard shipping takes 3-5 business days"
}

def extract_named_entities(text):
  prompt = f"Find the best match from the FAQ database for this customer query: {text}" \
            f"Available FAQs: {list(FAQ_DB.keys())}" \
            f"Provide a response based on the closest matching FAQ."
  
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I don't have an answer for this question! Please contact us at sample@support.com")
    return FAQ_DB.get(ai_response.lower(), ai_response)
  else:
    return f"Sorry, I couldn't process your request."

# Create Gradio interface
interface = gr.Interface(
  fn=extract_named_entities,
  inputs=gr.Textbox(lines=10, placeholder="Enter your request for support"),
  outputs=gr.Textbox(lines=10, label="Result"),
  title="AI-powered Customer Support",
  description="Enter your request to get support"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python name-entity-extractor.py and go to http://127.0.0.1:7860 for Gradio interface