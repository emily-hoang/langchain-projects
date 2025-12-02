import requests
import gradio as gr
from fpdf import FPDF

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests`

# A simple web interface for resume generation using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_legal_document(name, email, phone, personal_website, summary, experience, education, skills, certifications):
  prompt = f"Generate a professional resume template including sections for Contact Information, Summary, Experience, Education, Skills, and Certifications.:n" \
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nPersonal Website: {personal_website}\nSummary: {summary}\nExperience: {experience}\nEducation: {education}\nSkills: {skills}\nCertifications: {certifications}\n" \
            "Format the resume in a clear and organized manner suitable for job applications, ATS-friendly."
  payload = {
    "model": "llama3.1",
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(OLLAMA_URL, json=payload)
  
  if response.status_code == 200:
    ai_response = response.json().get("response", "Sorry, I couldn't generate a resume! Please try again with different information.")
    return ai_response
  else:
    return f"Sorry, I couldn't process your request."

# Create Gradio interface
interface = gr.Interface(
  fn=generate_legal_document,
  inputs=[
    gr.Textbox(lines=1, label="Name", placeholder="Enter your full name"),
    gr.Textbox(lines=1, label="Email", placeholder="Enter your email address"),
    gr.Textbox(lines=1, label="Phone", placeholder="Enter your phone number"),
    gr.Textbox(lines=1, label="Personal Website", placeholder="Enter your personal website URL"),
    gr.Textbox(lines=5, label="Summary", placeholder="Enter a brief summary about yourself"),
    gr.Textbox(lines=5, label="Experience", placeholder="Enter your work experience"),
    gr.Textbox(lines=5, label="Education", placeholder="Enter your educational background"),
    gr.Textbox(lines=5, label="Skills", placeholder="Enter your skills"),
    gr.Textbox(lines=5, label="Certifications", placeholder="Enter your certifications")
  ],
  outputs=gr.Textbox(lines=10, label="Resume"),
  title="AI-powered Resume Generator",
  description="Enter your information to generate a professional resume"
)
if __name__ == "__main__":
  interface.launch()

# Run the script: python resume-generator.py and go to http://127.0.0.1:7860 for Gradio interface