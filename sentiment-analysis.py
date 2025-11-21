from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']
    return label, score 
  
text = "I love using LangChain for building applications with large language models!"
sentiment, score = analyze_sentiment(text)
print(f"Text: {text}")
print(f"Sentiment: {sentiment} (Score: {score:.2f})")