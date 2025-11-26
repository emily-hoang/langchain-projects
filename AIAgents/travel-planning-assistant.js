import { OllamaChatModel } from "bee-agent-framework/adapters/ollama/backend/chat";
import { TokenMemory } from "bee-agent-framework/memory/tokenMemory";
import { OpenMeteoTool } from "bee-agent-framework/tools/weather/openMeteo";
import { WikipediaTool } from "bee-agent-framework/tools/search/wikipedia";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import * as readline from "readline";

// Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
const llm = new OllamaChatModel("llama3.1");
const memory = new TokenMemory({ llm });
const tools = [
  new OpenMeteoTool(),
  new WikipediaTool()
];

const agent = new BeeAgent({
  llm,
  memory,
  tools,
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const askQuestion = (query) => {
  return new Promise((resolve) => rl.question(query, resolve));
};

async function chatWithAgent() {
  console.log("\n✈️  Travel Itinerary Planner");
  console.log("=".repeat(60));
  console.log("     ✈️");
  console.log("    🗺️  🏖️");
  console.log("   🎒 📸");
  console.log("Plan your perfect trip with weather and destination info!");
  console.log("Examples:");
  console.log("  - Plan a 3-day trip to Rome starting next Monday");
  console.log("  - What's the weather in Bali in December?");
  console.log("  - Tell me about attractions in Barcelona");
  console.log("\nType 'exit' or 'quit' to end.");
  console.log("=".repeat(60) + "\n");

  while (true) {
    try {
      const userInput = await askQuestion("You: ");

      if (userInput.toLowerCase().trim() === "exit" || 
          userInput.toLowerCase().trim() === "quit") {
        console.log("\n👋 Bon voyage! Safe travels!\n");
        rl.close();
        process.exit(0);
      }

      if (!userInput.trim()) {
        console.log("⚠️  Please enter a question.\n");
        continue;
      }

      console.log("\n🗺️  Planning your trip...\n");

      const response = await agent.run({ 
        prompt: userInput
      });

      console.log("\n" + "=".repeat(60));
      console.log("🤖 Travel Planner: \n");
      console.log(response.result.text);
      console.log("=".repeat(60) + "\n");

    } catch (error) {
      console.error(`\n❌ Error: ${error.message}\n`);
    }
  }
}

chatWithAgent().catch((error) => {
  console.error("Fatal error:", error);
  rl.close();
  process.exit(1);
});