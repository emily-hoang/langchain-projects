from autogen import AssistantAgent, UserProxyAgent

llm_config = {
  "model": "gpt-4o-mini",
  "temperature": 0.7,
  "api_key": "your_openai_api_key_here"  # Replace with your actual OpenAI API key
}

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_enabled=False)

user_proxy.initiate_chat(assistant, message="Tell me a joke about artificial intelligence.")
