# LangChain & IBM Bee Agent Examples

This repository contains example chatbots and utilities demonstrating natural language, agent tools, and integrations using Python and Node.js. The examples are organized under the `AIAgents/` folder and include both Ollama-backed Python scripts and JavaScript agent examples using the `bee-agent-framework`.

## Contents (selected from AIAgents/)
- academic-research-assistant.js — Interactive research assistant (Wikipedia + LLM)
- travel-planning-assistant.js — Travel planning chatbot (OpenMeteo + LLM)
- weather-chatbot.js — Weather-focused agent using OpenMeteoTool
- personal-finance-advisor.js (in `financial-advisor/`) — Interactive finance advisor (may use PythonTool)
- ollama/ — Collection of Python scripts that use Ollama and local tools:
  - pdf-extractor.py — PDF text extraction + summarisation (PyMuPDF / OCR / Ollama)
  - text-summariser.py, meeting_summariser-bot.py, grammar-checker.py, etc.
- Qwen2.5-and-ollama/ — Additional simple chatbot examples

## Prerequisites
- Node.js (16+) and npm
- Python 3.8+
- For Ollama-backed examples: Ollama installed and running (`ollama serve`)
- Optional: Docker (for code interpreter container), `poppler` and `tesseract` for PDF/OCR

## Setup — Node (JavaScript examples)
1. Open a terminal in `AIAgents/`:
   ```bash
   cd AIAgents
   npm install
   ```
2. Run an example:
   ```bash
   node academic-research-assistant.js
   ```
   - Many JS examples expect the `bee-agent-framework` to be installed (this repo contains package.json in the AIAgents folder). Ensure dependencies are installed via `npm install`.

## Setup — Python (virtual environment and dependencies)
It is recommended to isolate Python dependencies per-project using a virtual environment.

1. Create a virtual environment (recommended name: `.venv`):
   ```bash
   cd AIAgents/ollama
   python3 -m venv .venv
   ```
2. Activate the virtual environment:
   - macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
3. Install required Python packages:
   - Create `requirements.txt` (example):
     ```
     gradio
     requests
     PyMuPDF
     pdf2image
     pytesseract
     pillow
     ```
   - Install:
     ```bash
     pip install -r requirements.txt
     ```
4. System-level dependencies (macOS Homebrew):
   ```bash
   brew install poppler      # required by pdf2image
   brew install tesseract    # required by pytesseract
   ```
5. Deactivate virtual environment when done:
   ```bash
   deactivate
   ```

Notes:
- If `PyMuPDF` import fails (e.g., `ModuleNotFoundError: No module named 'frontend'`), reinstall properly:
  ```bash
  pip uninstall PyMuPDF fitz -y
  pip install PyMuPDF
  ```

## Ollama & Code Interpreter
- Many Python examples (under `AIAgents/ollama`) and some agent flows expect an Ollama server:
  ```bash
  ollama serve
  ```
- Verify Ollama is reachable:
  ```bash
  curl http://localhost:11434/api/tags
  ```
- The `PythonTool` in `bee-agent-framework` requires a separate Code Interpreter service (or appropriate configuration). To run code-interpreter (example via Docker), follow the repo docs or use:
  ```bash
  # example: run a code interpreter container (if available)
  docker run -p 50081:50081 quay.io/aevo98765/bee-code-interpreter:latest
  ```
  Then configure the PythonTool with:
  ```js
  new PythonTool({
    codeInterpreter: { url: "http://127.0.0.1:50081" },
    storage: new PythonStorage()
  })
  ```

## Run common examples

- Academic Research Assistant (Node):
  ```bash
  cd AIAgents
  node academic-research-assistant.js
  ```
  - If ArXiv tool is missing in your `bee-agent-framework` version, the script falls back to Wikipedia-only behavior.

- Personal Finance Advisor (Node):
  ```bash
  cd AIAgents/financial-advisor
  node personal-finance-advisor.js
  ```
  - If you see errors about `PythonTool` or `codeInterpreter`, either start the Code Interpreter service or remove/comment out `PythonTool` from the `tools` array to use only LLM capabilities.

- PDF Extractor (Python + Gradio):
  ```bash
  cd AIAgents/ollama
  source .venv/bin/activate        # activate your venv
  python pdf-extractor.py
  ```
  - Visit http://127.0.0.1:7860 to use the Gradio UI.
  - Ensure `poppler` and `tesseract` are installed on the system.

## Troubleshooting
- 404 from Ollama `/api/generate`: verify Ollama version and use the correct endpoint (`/api/chat` vs `/api/generate`). Configure Ollama client baseURL if needed.
- `ModuleNotFoundError: No module named 'frontend'` for `fitz`: reinstall PyMuPDF as shown above.
- `TypeError: Cannot read properties of undefined (reading 'codeInterpreter')`: PythonTool requires options with `codeInterpreter.url`.
- DuckDuckGo rate-limit errors: avoid rapid repeated requests, add retry/delay logic, or remove DuckDuckGo tool.

## Contributing / Extending
- Add new examples under `AIAgents/` and document them in this README.
- For Python scripts, include a `requirements.txt` alongside each script for reproducibility.
- Keep Node examples' dependencies in `AIAgents/package.json`.

## License & Notes
- This repository provides example code and integration patterns. Review third-party licenses for any included packages or models you download.
- When using LLMs and external tools, handle sensitive data carefully.
