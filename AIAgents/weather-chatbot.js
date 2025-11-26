import { OllamaChatModel } from "bee-agent-framework/adapters/ollama/backend/chat";
import { TokenMemory } from "bee-agent-framework/memory/tokenMemory";
import { OpenMeteoTool } from "bee-agent-framework/tools/weather/openMeteo";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import * as readline from "readline";

// Ensure Ollama is installed via `brew install ollama` and the Ollama daemon is running via `ollama serve`
// Ollama chatbot (using llama3.1 model) - Natural Language Understanding & Generation for processing user queries
const llm = new OllamaChatModel("llama3.1");
const memory = new TokenMemory({ llm });

// Weather Information (via OpenMeteoTool agent)
const tools = [new OpenMeteoTool()];

const agent = new BeeAgent({
  llm,
  memory,
  tools,
});

// Create readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Helper function to get user input
const askQuestion = (query) => {
  return new Promise((resolve) => rl.question(query, resolve));
};

// Main conversation loop
async function chatWithAgent() {
  console.log("\n🌤️  Weather Chatbot powered by IBM Bee Agent Framework");
  console.log("=" .repeat(60));
  console.log("");
  console.log("     \\   /    ");
  console.log("       .-.      ");
  console.log("   ‒ (     ) ‒   ");
  console.log("       `-'      ");
  console.log("     /    \\     ");
  console.log("Ask me anything about weather!");
  console.log("Examples:");
  console.log("  - What's the weather in Melbourne, Australia tomorrow?");
  console.log("  - Will it rain in Sydney, Australia next week?");
  console.log("  - Is it good weather for hiking in Mount Buffalo, Victoria, Australia this weekend?");
  console.log("\nType 'exit' or 'quit' to end the conversation.");
  console.log("=" .repeat(60) + "\n");

  while (true) {
    try {
      const userInput = await askQuestion("You: ");

      if (userInput.toLowerCase().trim() === "exit" || 
          userInput.toLowerCase().trim() === "quit") {
        console.log("\n👋 Thanks for chatting! Goodbye!\n");
        rl.close();
        process.exit(0);
      }

      // Skip empty input
      if (!userInput.trim()) {
        console.log("⚠️  Please enter a question.\n");
        continue;
      }

      console.log("\n🤔 Thinking...\n");

      const response = await agent.run({ 
        prompt: userInput
      }).observe(emitter => {
        emitter.on("update", async ({ update }) => {
          // Show agent's thinking process
          if (update.key === "thought") {
            console.log(`💭 Agent thinking: ${update.value}`);
          }
          // if (update.key === "tool_name") {
          //   console.log(`🔧 Using tool: ${update.value}`);
          // }
          // if (update.key === "tool_input") {
          //   console.log(`📥 Tool input: ${JSON.stringify(update.value, null, 2)}`);
          // }
          // if (update.key === "tool_output") {
          //   console.log(`📤 Tool output received`);
          // }
        });
        
        emitter.on("error", (error) => {
          console.error(`❌ Error: ${error.message}`);
        });
      });

      // Display the final answer
      console.log("\n" + "=".repeat(60));
      console.log("🤖 Agent: \n");
      console.log(response.result.text);
      console.log("=".repeat(60) + "\n");

    } catch (error) {
      console.error(`\n❌ Error: ${error.message}`);
      console.log("Please try rephrasing your question again.\n");
    }
  }
}

// Start the chatbot
chatWithAgent().catch((error) => {
  console.error("Fatal error:", error);
  rl.close();
  process.exit(1);
});