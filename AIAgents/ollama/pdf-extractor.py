import requests
import gradio as gr
import fitz # PyMuPDF
from pdf2image import convert_from_path
import pytesseract

# Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
# and dependencies are installed via `pip install gradio requests PyMuPDF pdf2image pytesseract`
# brew install poppler  # Required for pdf2image
# brew install tesseract  # Required for pytesseract

# A simple web interface for PDF text extraction using Ollama model available at http://127.0.0.1:7860
# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_text_from_pdf(pdf_file_path):
  text = ""
  with fitz.open(pdf_file_path) as doc:
    for page in doc:
      text += page.get_text("text") + "\n"
      return text if text.strip() else "No text found in the PDF."
    
# OCR (Optical Character Recognition) is the technology that converts images of printed or handwritten text into machine-readable text.
def extract_text_with_ocr(pdf_file):
  images = convert_from_path(pdf_file)
  extracted_text = "\n".join(pytesseract.image_to_string(image) for image in images)
  return extracted_text if extracted_text.strip() else "No text found in the PDF."
  
def sumarise_text(text):
  prompt = f"Summarise the following text extracted from a PDF document:\n\n{text}"
  
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
  

# Create Gradio interface
interface = gr.Interface(
  fn=extract_text_from_pdf,
  inputs=[
      gr.File(label="Upload PDF file")
  ],
  outputs=gr.Textbox(lines=10, label="Extracted Text"),
  title="AI-powered PDF Text Extractor",
  description="Upload a PDF file to extract its text content"
)
if __name__ == "__main__":
  interface.launch()

# Test PDF Text Extraction + Sumarisation
def process_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    if "No text found" in text:
        text = extract_text_with_ocr(pdf_file)
    if "No text found" in text:
        return "No text could be extracted from the PDF."
    return sumarise_text(text)

# if __name == "__main__":
#     pdf_path = "sample.pdf"  # Replace with your PDF file path
#     summary = process_pdf(pdf_path)
#     print("Summary of PDF content:")
#     print(summary)
  
# Run the script: python pdf-extractor.py and go to http://127.0.0.1:7860 for Gradio interface