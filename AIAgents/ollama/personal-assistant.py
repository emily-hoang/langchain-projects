import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for identitifying named entities using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"
engine = pyttsx3.init()

def ai_assistant(text):
  prompt = f"Respond to this customer query as a personal AI assistant: {text}"
  
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't process your request! Please try a different request!")
    
    # Convert text to speech
    engine.say(ai_response)
    engine.runAndWait()
    
    return ai_response
  else:
    return f"Sorry, I couldn't process your request!"
  
# Voice Command Funtion
def listen_command():
  recogniser = sr.Reconigser()
  with sr.Microphone() as source:
    print("Listening.....")
    recogniser.adjust_for_ambient_noise(source)
    audio = recogniser.listen(source)
  try:
    command = recogniser.recognizer_google(audio)
    print(f"User: {command}")
    return command
  except sr.UnknownValueError:
    return "Sorry, I couldn't understand that!"
  except sr.RequestError:
    return "Speech recognition service is unavailable."

# Create Gradio interface
interface = gr.Interface(
  fn=ai_assistant,
  inputs=gr.Textbox(lines=10, placeholder="Ask me anything!"),
  outputs=gr.Textbox(lines=10, label="Answer"),
  title="AI-powered Personal Assistant",
  description="Type a query or use voice command"
)
if __name__ == "__main__":
  interface.launch()
  

# Run the script: python name-entity-extractor.py and go to http://127.0.0.1:7860 for Gradio interface