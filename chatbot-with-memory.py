from transformers import pipeline

chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

memory = {}

def chat_with_memory(user_input):
  # Check if the user mentions their name to personalize the response
  if "my name is" in user_input.lower():
    name_part = user_input.lower().split("my name is")[-1].strip().split()[0].capitalize()
    memory['name'] = name_part
    return f"Nice to meet you, {name_part}!"
  if 'name' in memory:
    response = chatbot_pipeline(f"Hello {memory['name']}, How can I assist you today?")
  else:
    response = chatbot_pipeline(user_input)
  return response[0]['generated_text']

def main():
  while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
      print("Exiting the chatbot. Goodbye!")
      break
    print("\n")
    print("Bot: ", chat_with_memory(user_input))

if __name__ == "__main__":
  main()