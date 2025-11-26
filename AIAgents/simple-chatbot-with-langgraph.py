# pip install langchain langgraph openai

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict

llm = ChatOpenAI(
  model="gpt-5",
  temperature=0.1,
  max_tokens=1000,
  timeout=30,
  api_key="your-openai-api-key")

class State(TypedDict):
    name: str
    greeting: str
    response: str

def greet_node(state: State):
    name = state.get("name", "there")
    return {"greeting": f"Hello, {name}!"}

def chat_node(state: State):
    greeting = state.get("greeting", "")
    prompt = f"{greeting} How are you feeling today?"
    response = llm(prompt)
    return {"response": response}

# Connect nodes in a graph
graph = StateGraph(State)
graph.add_node("greet", greet_node)
graph.add_node("chat", chat_node)
graph.add_edge("greet", "chat")
graph.add_edge("chat", END)
graph.set_entry_point("greet")

# Run the graph
app = graph.compile()
result = app.invoke({"name": "Emily"})
print(result["response"])
