import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for product recommendation using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"
PRODUCT_DB = {
  "laptop": ["Dell XPS 13 - High performance and sleek design", "MacBook Air - Lightweight, powerful, and great battery life", "HP Spectre x360 - Ideal for versatility with 2-in-1 design"],
  "smartphone": ["iPhone 14 - Great camera and performance", "Samsung Galaxy S22 - High performance and vibrant display", "Google Pixel 7 - Excellent camera and clean Android experience"],
  "headphones": ["Sony WH-1000XM4 - Industry-leading noise cancellation", "Bose QuietComfort 35 II - Comfortable with excellent sound quality", "Apple AirPods Pro - Seamless integration with Apple devices"],
  "smartwatch": ["Apple Watch Series 7 - Advanced health monitoring and seamless integration with iOS", "Samsung Galaxy Watch 4 - Comprehensive fitness tracking and Android compatibility", "Fitbit Versa 3 - Affordable with robust health features"],
  "tablet": ["iPad Pro - Powerful and versatile tablet with Apple Pencil support", "Samsung Galaxy Tab S7 - High performance Android tablet with S Pen", "Microsoft Surface Pro 7 - Versatile 2-in-1 laptop and tablet"]
}

def generate_legal_document(query):
  prompt = f"Analyse the following query and suggest best matching products: {query}" \
            "Available products are: " + ", ".join([item for sublist in PRODUCT_DB.values() for item in sublist]) + ". " \
            "Provide a short list of top recommendations from the product database."
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't find any recommendations! Please try again with a different query.")
    return ai_response
  else:
    return f"Sorry, I couldn't process your request."

# Create Gradio interface
interface = gr.Interface(
  fn=generate_legal_document,
  inputs=gr.Textbox(lines=10, label="Query", placeholder="Enter your product preferences or requirements"),
  outputs=gr.Textbox(lines=10, label="Recommendations"),
  title="AI-powered Product Recommendation",
  description="Enter your product preferences to get top recommendations"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python product-recommendation.py and go to http://127.0.0.1:7860 for Gradio interface