# LangChain Project

This project contains Python scripts that demonstrate natural language processing capabilities using the Hugging Face Transformers library.

## Scripts

1. **sentiment-analysis.py** - Analyzes the sentiment of text input
2. **simpleTextBasedQuestionChatbot.py** - A question-answering chatbot with knowledge about LangChain

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone or download this repository**

2. **Create a virtual environment**
   ```bash
   python3 -m venv langchain_env
   ```

3. **Activate the virtual environment**
   ```bash
   source langchain_env/bin/activate
   ```

4. **Install required dependencies**
   ```bash
   pip install transformers torch
   ```

## Running the Scripts

### Sentiment Analysis

This script analyzes the sentiment of a given text.

```bash
python sentiment-analysis.py
```

**Output Example:**
```
Text: I love using LangChain for building applications with large language models!
Sentiment: POSITIVE (Score: 0.99)
```

### Question-Answering Chatbot

This interactive chatbot answers questions based on a built-in knowledge base about LangChain.

```bash
python simpleTextBasedQuestionChatbot.py
```

**Usage:**
- Enter your questions when prompted
- Type 'exit' to quit the chatbot

**Example Interaction:**
```
Please enter your question (or type 'exit' to quit): What is Langchain?
Answer: an open-source framework (Score: 0.54)
```

## Dependencies

- `transformers` - Hugging Face Transformers library for NLP models
- `torch` - PyTorch for running the models

## Models Used

- **Sentiment Analysis**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Question Answering**: `distilbert-base-cased-distilled-squad`

## Notes

- The first time you run each script, the models will be downloaded automatically (this may take a few minutes)
- Models are cached locally for subsequent runs
- The chatbot's knowledge is limited to the predefined context about LangChain

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```
