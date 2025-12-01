import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def check_grammar(input_text):
    prompt = f"Check the grammar of the following text and provide corrections if necessary:\n\n{input_text}\n\nCorrected Text:"
    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        corrected_text = data.get("response", "No corrections made.")  # Note: key is "response" not "text"
        return corrected_text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=check_grammar,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to check grammar..."),
    outputs="text",
    title="Grammar Checker",
    description="Enter text and get grammar corrections using Ollama's llama3.1 model."
)

if __name__ == "__main__":
    iface.launch()