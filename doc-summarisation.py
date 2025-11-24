from transformers import pipeline

# Load the document summarization pipeline
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_document(text, max_length=150, min_length=30):
    summary = summarization_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
    return summary
  
text = """"LangChain is an open-source framework designed to make it easier to build applications powered by large language models (LLMs). It provides a suite of tools and abstractions that help developers create applications that can interact with LLMs in a more structured and efficient way.
Key features of LangChain include:
1. Chains: LangChain allows developers to create chains of calls to LLMs and other utilities, enabling complex workflows and interactions.
2. Data Augmentation: It provides tools to augment LLMs with external data sources, such as databases, APIs, and documents, allowing for more informed and context-aware responses.
3. Prompt Management: LangChain offers utilities for managing and optimizing prompts, helping developers craft effective prompts for their applications.
4. Integration with Other Tools: LangChain can be integrated with various tools and services, such as vector databases, web scraping tools, and more, to enhance the capabilities of LLM-powered applications.
5. Extensibility: The framework is designed to be extensible, allowing developers to build custom components and integrate them into the LangChain ecosystem.
Overall, LangChain aims to simplify the process of building applications that leverage large language models, making it accessible for developers to create sophisticated AI-driven solutions."""

summary = summarize_document(text)
print("Example Document Summary: \n")
print("Original Document: \n", text)
print("Summarised Document: \n", summary)
print("\n")
print("===============================================================================================================")


def main():
  while True:
    user_input = input("Please enter the document text to summarize (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the document summarization tool. Goodbye!")
        break
    summary = summarize_document(user_input)
    print("Summarised Document: ", summary)
 
# Only run the main function if this script is executed directly, not when imported   
if __name__ == "__main__":
    main()