import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for text summarization using DeepSeek model available at http://127.0.0.1:7860
# DeepSeek API endpoint and headers
OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(input_text):
    if not input_text.strip():
        return "Please provide some text to summarize."

    prompt = f"Summarize the following text in a concise manner:\n\n{input_text}\n\nSummary:"
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 0.9,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        summary = data.get("text", "No summary generated.")
        return summary.strip()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
      
if __name__ == "__main__":
    iface = gr.Interface(
        fn=summarize_text,
        inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize here..."),
        outputs="text",
        title="Text Summarizer",
        description="Enter text and get a concise summary using DeepSeek model."
    )
iface.launch()