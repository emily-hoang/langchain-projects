import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for text summarization using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(input_text):
    if not input_text.strip():
        return "Please provide some text to summarize."

    prompt = f"Summarize the following text in a concise manner:\n\n{input_text}\n\nSummary:"
    
    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        summary = data.get("response", "No summary generated.")  # Fixed: changed "text" to "response"
        return summary.strip()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Create Gradio interface
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize here..."),
    outputs=gr.Textbox(lines=10, placeholder="Result"),
    title="Text Summarizer",
    description="Enter text and get a concise summary using Ollama's llama3.1 model."
)

if __name__ == "__main__":
    iface.launch()
    
# Run the script: python text-summariser.py and go to http://127.0.0.1:7860 for Gradio interface