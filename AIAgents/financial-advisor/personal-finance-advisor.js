import { OllamaChatModel } from "bee-agent-framework/adapters/ollama/backend/chat";
import { TokenMemory } from "bee-agent-framework/memory/tokenMemory";
import { PythonTool } from "bee-agent-framework/tools/python/python";
import { PythonStorage } from "bee-agent-framework/tools/python/storage";
import { WikipediaTool } from "bee-agent-framework/tools/search/wikipedia";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import * as readline from "readline";

const llm = new OllamaChatModel("llama3.1");
const memory = new TokenMemory({ llm });

// Initialize PythonTool with BeeAI Code Interpreter
// Folow instructions at FinancialAdvisor.md
const pythonTool = new PythonTool({
  codeInterpreter: {
    url: process.env.CODE_INTERPRETER_URL || "http://localhost:50081"
  },
  storage: new PythonStorage()
});

const tools = [
  pythonTool,         // For advanced financial calculations with numpy, pandas, scipy
  new WikipediaTool() // For financial terms/concepts
];

const agent = new BeeAgent({
  llm,
  memory,
  tools,
  meta: {
    name: "Finance Advisor",
    description: "Expert financial advisor with Python capabilities for complex calculations including compound interest, NPV, IRR, portfolio analysis, and statistical modeling using numpy, pandas, and scipy."
  }
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const askQuestion = (query) => {
  return new Promise((resolve) => rl.question(query, resolve));
};

async function chatWithAgent() {
  console.log("\n💰 Personal Finance Advisor");
  console.log("=".repeat(60));
  console.log("     💵");
  console.log("    📊📈");
  console.log("   💳 🏦");
  console.log("Powered by BeeAI Code Interpreter for advanced calculations!");
  console.log("\nCapabilities:");
  console.log("  ✓ Compound interest & investment calculations");
  console.log("  ✓ Portfolio analysis & risk assessment");
  console.log("  ✓ Loan amortization schedules");
  console.log("  ✓ Statistical financial modeling");
  console.log("  ✓ Data visualization with matplotlib");
  console.log("\nExamples:");
  console.log("  - Calculate compound interest on $10,000 at 5% for 10 years");
  console.log("  - Create a 30-year mortgage amortization for $300,000 at 4.5%");
  console.log("  - Analyze portfolio with stocks: [AAPL, GOOGL, MSFT]");
  console.log("  - What's the NPV of cash flows: [-10000, 3000, 4000, 5000]?");
  console.log("  - Explain what an ETF is");
  console.log("\nType 'exit' or 'quit' to end.");
  console.log("=".repeat(60) + "\n");

  while (true) {
    try {
      const userInput = await askQuestion("You: ");

      if (userInput.toLowerCase().trim() === "exit" || 
          userInput.toLowerCase().trim() === "quit") {
        console.log("\n👋 Happy investing! Goodbye!\n");
        rl.close();
        process.exit(0);
      }

      if (!userInput.trim()) {
        console.log("⚠️  Please enter a question.\n");
        continue;
      }

      console.log("\n💭 Calculating...\n");

      const response = await agent.run({ 
        prompt: userInput
      }).observe(emitter => {
        emitter.on("update", async ({ data, update, meta }) => {
          // Show agent's thinking process
          if (update.key === "thought") {
            console.log(`💭 Thinking: ${update.value}`);
          }
          
          // Show when Python code is being executed
          if (update.key === "tool_name" && update.value === "Python") {
            console.log(`🐍 Executing Python code via BeeAI Code Interpreter...`);
          }
          
          // Show the Python code being executed
          if (update.key === "tool_input" && data.tool_name === "Python") {
            console.log(`\n📝 Python Code:\n${"─".repeat(60)}`);
            console.log(update.value.code);
            console.log("─".repeat(60));
          }
          
          // Show Python execution results
          if (update.key === "tool_output" && data.tool_name === "Python") {
            console.log(`\n✅ Python Output:\n${"─".repeat(60)}`);
            console.log(update.value);
            console.log("─".repeat(60) + "\n");
          }
        });
        
        emitter.on("error", (error) => {
          console.error(`❌ Error: ${error.message}`);
        });
      });

      console.log("\n" + "=".repeat(60));
      console.log("🤖 Finance Advisor: \n");
      console.log(response.result.text);
      console.log("=".repeat(60) + "\n");

    } catch (error) {
      console.error(`\n❌ Error: ${error.message}`);
      console.log("Please try rephrasing your question.\n");
    }
  }
}

chatWithAgent().catch((error) => {
  console.error("Fatal error:", error);
  rl.close();
  process.exit(1);
});