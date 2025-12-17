# Ensure ollama server and Qwen 2.5 is installed, running and accessible via:
# `brew install ollama`, `ollama serve`
# `ollama pull qwen2.5`, `ollama run qwen2.5`
# And dependencies are installed via `pip install fastapi uvicorn ollama pydantic`
# A simple web interface for generating SQL queries, suggestion using Ollama model available at http://127.0.0.1:7860
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()
# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
  message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ollama.chat(
            model="qwen2.5",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answer user requests."},
                {"role": "user", "content": request.message}
            ]
        )
        return {"response": response['choices'][0]['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Qwen 2.5 Chatbot is running."}
  
# Run the app with: uvicorn simple-chatbot:app --reload --host 0.0.0.0 --port 8000
# Access the chatbot at http://127.0.0.1:8000 or via commandline using curl `curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d "{\"message\":\"Hello, what can you do?\"}"`