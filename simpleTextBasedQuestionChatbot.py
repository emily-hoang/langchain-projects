from transformers import pipeline
knowledge_base = """
LangChain is an open-source framework designed to make it easier to build applications powered by **large language models (LLMs)**. It provides a suite of tools and abstractions that help developers create applications that can interact with LLMs in a more structured and efficient way.
Key features of LangChain include:
1. **Chains**: LangChain allows developers to create chains of calls to LLMs and other utilities, enabling complex workflows and interactions.
2. **Data Augmentation**: It provides tools to augment LLMs with external data sources, such as databases, APIs, and documents, allowing for more informed and context-aware responses.
3. **Prompt Management**: LangChain offers utilities for managing and optimizing prompts, helping developers craft effective prompts for their applications.
4. **Integration with Other Tools**: LangChain can be integrated with various tools and services, such as vector databases, web scraping tools, and more, to enhance the capabilities of LLM-powered applications.
5. **Extensibility**: The framework is designed to be extensible, allowing developers to build custom components and integrate them into the LangChain ecosystem.
Overall, LangChain aims to simplify the process of building applications that leverage large language models, making it accessible for developers to create sophisticated AI-driven solutions.
"""

chatbot_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context=knowledge_base):
    response = chatbot_pipeline(question=question, context=context)
    answer = response['answer']
    score = response['score']

    return answer, score
  
def main():
    while True:
        user_question = input("Please enter your question (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break
        answer, score = answer_question(user_question)
        print(f"Answer: {answer} (Score: {score:.2f})")
if __name__ == "__main__":
    main()
  
question = "What is Langchain?"
answer, score = answer_question(question)
print(f"Question: {question}")
print(f"Answer: {answer} (Score: {score:.2f})")
