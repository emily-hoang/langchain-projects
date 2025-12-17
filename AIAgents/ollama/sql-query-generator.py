import requests
import gradio as gr

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`
# A simple web interface for generating SQL queries, suggestion using Ollama model available at http://127.0.0.1:7860

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_sql_query(natural_language_query, database_type="MySQL", database_schema="employee(name, salary, department)"):
  prompt = f"Generate a SQL query for the following request on a {database_type} database with this schema: {database_schema}\n\nRequest: {natural_language_query}"
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't generate a SQL query! Please try again with a different request.")
    return ai_response
  else:
    return f"Sorry, an error occurred while processing your request: {response.status_code}."
  
# Create Gradio interface
interface = gr.Interface(
  fn=generate_sql_query,
  inputs=[
    gr.Textbox(lines=5, label="Natural Language Query", placeholder="Enter your request in natural language"),
    gr.Textbox(label="Database Type", placeholder="Enter the type of database (e.g., MySQL, PostgreSQL)"),
    gr.Textbox(lines=5, label="Database Schema", placeholder="Enter the database schema")
  ],
  outputs=gr.Textbox(lines=10, label="Generated SQL Query"),
  title="AI-powered SQL Query Generator",
  description="Enter a natural language request to generate a SQL query"
)
if __name__ == "__main__":
  interface.launch()
  
# Run the script: python sql-query-generator.py and go to http://127.0.0.1:7860 for Gradio interface