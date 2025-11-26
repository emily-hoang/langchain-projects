# Personal Finance Advisor 💰

An intelligent financial advisor chatbot powered by IBM Bee Agent Framework and BeeAI Code Interpreter, capable of complex financial calculations using Python, NumPy, Pandas, and SciPy.

## Features

✨ **Advanced Calculations**
- Compound interest with various compounding frequencies
- Loan amortization schedules
- Net Present Value (NPV) and Internal Rate of Return (IRR)
- Portfolio risk and return analysis
- Statistical financial modeling
- Monte Carlo simulations

🐍 **Python-Powered**
- Execute complex financial formulas using Python
- Access to NumPy, Pandas, SciPy, and Matplotlib
- Automatic library installation on-the-fly
- Sandboxed code execution for security

🧠 **AI Intelligence**
- Natural language understanding via Llama 3.1
- Contextual conversation memory
- Wikipedia integration for financial term definitions
- Step-by-step reasoning transparency

## Prerequisites

1. **Ollama** with Llama 3.1 model
   ```bash
   # Install Ollama
   brew install ollama
   
   # Start Ollama service
   ollama serve
   
   # Pull Llama 3.1 model
   ollama pull llama3.1
   ```

2. **BeeAI Code Interpreter** running on http://localhost:50081
   
   See [SetupBeeAICodeInterpreter](./SetupBeeAICodeInterpreter.md) for detailed setup instructions.

## Quick Start

### 1. Verify BeeAI Code Interpreter is Running

```bash
# Test the connection
./test-beeai-connection.sh
```

Expected output:
```
✅ BeeAI Code Interpreter is running!
✅ All tests passed! BeeAI Code Interpreter is ready.
```

### 2. Install Dependencies

```bash
cd /Users/nhunghoang/AIProjects/chatbot/AIAgents
npm install
```

### 3. Run the Finance Advisor

```bash
node personal-finance-advisor.js
```

## Usage Examples

### Example 1: Compound Interest Calculation

```
You: Calculate compound interest on $10,000 at 5% annual rate for 10 years

🐍 Executing Python code via BeeAI Code Interpreter...

📝 Python Code:
────────────────────────────────────────────────────────────
principal = 10000
rate = 0.05
years = 10
amount = principal * (1 + rate) ** years
interest = amount - principal
print(f"Future Value: ${amount:,.2f}")
print(f"Interest Earned: ${interest:,.2f}")
────────────────────────────────────────────────────────────

✅ Python Output:
────────────────────────────────────────────────────────────
Future Value: $16,288.95
Interest Earned: $6,288.95
────────────────────────────────────────────────────────────

🤖 Finance Advisor: 
Your $10,000 investment at 5% annual rate will grow to $16,288.95 
in 10 years, earning $6,288.95 in interest.
```

### Example 2: Mortgage Calculation

```
You: What's the monthly payment for a $300,000 mortgage at 4.5% for 30 years?

🤖 Finance Advisor: 
The monthly payment would be $1,520.06
```

### Example 3: Portfolio Analysis

```
You: Calculate expected return for portfolio: 60% stocks (10% return, 15% risk), 
     40% bonds (4% return, 5% risk)

🤖 Finance Advisor:
Portfolio Expected Return: 7.6%
Portfolio Risk (Standard Deviation): 10.1%
Sharpe Ratio: 0.75
```

### Example 4: NPV Calculation

```
You: What's the NPV of cash flows [-50000, 15000, 20000, 25000, 30000] at 8% discount rate?

🤖 Finance Advisor:
NPV: $19,277.56
This is a good investment with positive NPV.
```

### Example 5: Financial Term Definition

```
You: What is an ETF?

🤖 Finance Advisor:
An ETF (Exchange-Traded Fund) is an investment fund that holds multiple assets 
like stocks or bonds and trades on stock exchanges throughout the day...
[Uses Wikipedia for detailed explanation]
```

## Advanced Features

### Python Libraries Available

- **NumPy**: Numerical computing and array operations
- **Pandas**: Data analysis and manipulation
- **SciPy**: Scientific computing (optimization, statistics)
- **Matplotlib**: Data visualization and plotting
- **SymPy**: Symbolic mathematics
- **PyPDF2, pikepdf**: PDF manipulation
- **Pillow**: Image processing
- **MoviePy**: Video processing
- **FFmpeg**: Media conversion
- **And more**: Libraries auto-installed on demand

### Custom Calculations

You can request complex custom calculations:

```
You: Create a Monte Carlo simulation with 10,000 iterations to estimate 
     retirement savings with $500/month investment, 7% return, 30 years, 
     assuming 15% volatility
```

### Data Visualization

```
You: Plot the growth of $10,000 invested at 6% over 30 years
```

## Environment Variables

```bash
# Optional: Override Code Interpreter URL (defaults to http://localhost:50081)
export CODE_INTERPRETER_URL=http://localhost:50081

# Run the advisor
node personal-finance-advisor.js
```

## Troubleshooting

### Connection Error to Code Interpreter

```bash
# Check if BeeAI Code Interpreter is running
curl http://localhost:50081/health

# If not running, start it:
cd ~/AIProjects/bee-code-interpreter
bash scripts/run-pull.sh
```

### Ollama Connection Error

```bash
# Check Ollama status
ollama list

# Start Ollama service
ollama serve

# Verify model is available
ollama pull llama3.1
```

### Python Execution Errors

- Code Interpreter automatically installs missing libraries
- Execution timeout is 30 seconds by default
- Check BeeAI Code Interpreter logs for detailed errors

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│         Personal Finance Advisor (Node.js)              │
│                                                          │
│  ┌────────────────┐         ┌──────────────────┐       │
│  │  Ollama Chat   │         │   Bee Agent      │       │
│  │  (Llama 3.1)   │────────▶│   Framework      │       │
│  └────────────────┘         └──────────────────┘       │
│                                      │                   │
│                                      ▼                   │
│                    ┌──────────────────────────────┐     │
│                    │      Tool Orchestration      │     │
│                    └──────────────────────────────┘     │
│                              │      │                    │
│                    ┌─────────┘      └──────────┐        │
│                    ▼                            ▼        │
│          ┌──────────────────┐        ┌──────────────┐   │
│          │   PythonTool     │        │ WikipediaTool│   │
│          └──────────────────┘        └──────────────┘   │
│                    │                                     │
└────────────────────┼─────────────────────────────────────┘
                     ▼
        ┌────────────────────────────┐
        │  BeeAI Code Interpreter    │
        │  (Kubernetes + Docker)     │
        │                            │
        │  • Python Executor         │
        │  • NumPy, Pandas, SciPy    │
        │  • Sandboxed Execution     │
        │  • Auto Library Install    │
        └────────────────────────────┘
```

## Security Considerations

- All Python code runs in isolated Kubernetes pods
- Code Interpreter uses sandboxed execution
- No direct filesystem access
- Network isolation enforced
- Resource limits prevent abuse

## Contributing

Contributions welcome! Areas for improvement:

- Additional financial calculation templates
- Custom plotting styles for charts
- Integration with real-time market data APIs
- Tax calculation modules
- Investment strategy backtesting

## License

MIT


