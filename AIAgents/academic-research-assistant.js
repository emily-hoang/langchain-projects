import { OllamaChatModel } from "bee-agent-framework/adapters/ollama/backend/chat";
import { TokenMemory } from "bee-agent-framework/memory/tokenMemory";
import { ArXivTool } from "bee-agent-framework/tools/arxiv";
import { WikipediaTool } from "bee-agent-framework/tools/search/wikipedia";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import * as readline from "readline";

// Ensure ollama server is installed, running and accessible via `brew install ollama`, `ollama serve`
const llm = new OllamaChatModel("llama3.1");
const memory = new TokenMemory({ llm });
const tools = [
  new ArXivTool({ maxResults: 5 }),
  new WikipediaTool()
];

const agent = new BeeAgent({
  llm,
  memory,
  tools,
})

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const askQuestion = (query) => {
  return new Promise((resolve) => rl.question(query, resolve));
};

async function chatWithAgent() {
  console.log("\n📚 Academic Research Assistant");
  console.log("=".repeat(60));
  console.log("     📖");
  console.log("    🔬 🧬");
  console.log("   📊 💡");
  console.log("Ask me about research papers and academic topics!");
  console.log("\nFunctionality:");
  console.log("  ✓ Search ArXiv for academic papers and preprints");
  console.log("  ✓ Access Wikipedia for general knowledge");
  console.log("  ✓ Answer questions about research topics");
  console.log("  ✓ Find recent publications in specific fields");
  console.log("  ✓ Provide summaries of academic concepts");
  console.log("\nExamples:");
  console.log("  - Find recent papers on quantum computing");
  console.log("  - What is machine learning?");
  console.log("  - Search for climate change research from 2023");
  console.log("\nType 'exit' or 'quit' to end.");
  console.log("=".repeat(60) + "\n");

  while (true) {
    try {
      const userInput = await askQuestion("You: ");

      if (userInput.toLowerCase().trim() === "exit" || 
          userInput.toLowerCase().trim() === "quit") {
        console.log("\n👋 Happy researching! Goodbye!\n");
        rl.close();
        process.exit(0);
      }

      if (!userInput.trim()) {
        console.log("⚠️  Please enter a question.\n");
        continue;
      }

      console.log("\n🔍 Searching academic databases...\n");

      const response = await agent.run({ 
        prompt: userInput
      }).observe(emitter => {
        emitter.on("update", async ({ update }) => {
          if (update.key === "tool_name") {
            console.log(`📚 Searching: ${update.value}`);
          }
        });
      });

      console.log("\n" + "=".repeat(60));
      console.log("🤖 Research Assistant: \n");
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