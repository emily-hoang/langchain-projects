from transformers import pipeline

# Initialize the keyword extraction pipeline
keyword_extractor = pipeline("text2text-generation", model="Voicelab/vlt5-base-keywords")
# keyword_extractor = pipeline("ner", model="ml6team/keyphrase-extraction-distilbert-inspec") - Alternative model

def extract_keywords(text, max_keywords=10):
  if not text or not text.strip():
          return []
      
  try:
    # Limit the token to 64 for keyword extraction
    result = keyword_extractor(text, max_length=64)[0]['generated_text']
    keywords = [kw.strip() for kw in result.split(',') if kw.strip()]
    return keywords[:max_keywords]
  except (IndexError, KeyError, TypeError) as e:
    print(f"Error extracting keywords: {e}")
    return []

if __name__ == "__main__":
  # Example usage
  sample_text = """
  Artificial intelligence and machine learning are transforming the technology industry.
  Deep learning models have achieved remarkable success in natural language processing tasks.
  """
  
  keywords = extract_keywords(sample_text)
  print("Extracted Keywords:", keywords)