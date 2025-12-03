import requests
import gradio as gr
import speech_recognition as sr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for meeting summarisation using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_legal_document(transcript):
  # prompt = f"Summarise the following meeting transcript into key points and action items:\n\n{transcript}" \
  prompt = "Provide a concise summary highlighting the main topics discussed and any decisions made."
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't generate a summary! Please try again with different transcript.")
    return ai_response
  else:
    return f"Sorry, I couldn't process your request."

def transcribe_audio(file_path):
    # Transcribe an audio file at file_path and return plain text (empty string on failure)
    if not file_path:
        return ""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return ""
# Create Gradio interface
def process_input(audio, transcript):
    # If audio uploaded, attempt transcription; otherwise use provided transcript.
    # Priority: transcribed audio > manual transcript if audio was provided and transcribed.
    text = transcript or ""
    if audio:
        transcribed = transcribe_audio(audio)
        if transcribed:
            text = transcribed
    if not text or not text.strip():
        return "No transcript provided or audio could not be transcribed."
    return generate_legal_document(text)

interface = gr.Interface(
  fn=process_input,
  inputs=[
      gr.Audio(type="filepath", label="Upload audio (optional)"),
      gr.Textbox(lines=5, label="Transcript", placeholder="Enter the meeting transcript (optional)")
  ],
  outputs=gr.Textbox(lines=10, label="Summary"),
  title="AI-powered Meeting Summariser",
  description="Upload an audio file or paste the meeting transcript to generate a concise summary"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python meeting_summariser-bot.py and go to http://127.0.0.1:7860 for Gradio interface