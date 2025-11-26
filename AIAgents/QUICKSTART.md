# Quick Start Guide: Personal Finance Advisor

## ✅ Integration Complete!

Your `personal-finance-advisor.js` has been successfully integrated with BeeAI Code Interpreter!

## What Changed?

### 1. **Imports Added**
```javascript
import { PythonTool } from "bee-agent-framework/tools/python/python";
import { PythonStorage } from "bee-agent-framework/tools/python/storage";
```

### 2. **PythonTool Initialized**
```javascript
const pythonTool = new PythonTool({
  codeInterpreter: {
    url: process.env.CODE_INTERPRETER_URL || "http://localhost:50081"
  },
  storage: new PythonStorage()
});
```

### 3. **Enhanced Agent Description**
- Added Python calculation capabilities
- Supports NumPy, Pandas, SciPy
- Complex financial modeling enabled

### 4. **Enhanced UI**
- Shows when Python code is executed
- Displays the actual code being run
- Shows Python execution results in real-time

## 🚀 Next Steps

### Step 1: Install BeeAI Code Interpreter

Choose one of these methods:

#### Method A: Using Pre-built Image (Fastest)
```bash
cd ~/AIProjects
git clone --recurse-submodules https://github.com/i-am-bee/bee-code-interpreter.git
cd bee-code-interpreter
bash scripts/run-pull.sh
```

#### Method B: Using BeeAI Framework Starter (Easiest)
```bash
git clone https://github.com/i-am-bee/beeai-framework-ts-starter.git
cd beeai-framework-ts-starter
# Follow README instructions
```

### Step 2: Verify Installation

```bash
cd /Users/nhunghoang/AIProjects/chatbot/AIAgents
./test-beeai-connection.sh
```

You should see:
```
✅ BeeAI Code Interpreter is running!
✅ All tests passed!
```

### Step 3: Start Ollama (if not running)

```bash
# Start Ollama service
ollama serve

# In another terminal, verify model
ollama list
# Should show llama3.1
```

### Step 4: Run Your Finance Advisor

```bash
cd /Users/nhunghoang/AIProjects/chatbot/AIAgents
node personal-finance-advisor.js
```

## 💡 Try These Queries

### Basic Calculations
```
Calculate compound interest on $25,000 at 6% for 15 years
```

### Mortgage Analysis
```
What's the monthly payment for a $500,000 mortgage at 3.5% for 30 years?
Show me the amortization schedule for the first year.
```

### Investment Planning
```
If I invest $1,000/month for 25 years at 8% return, how much will I have?
```

### NPV Analysis
```
Calculate NPV for an investment:
- Initial cost: $100,000
- Year 1-5 cash flows: $30,000, $35,000, $40,000, $45,000, $50,000
- Discount rate: 10%
```

### Portfolio Risk
```
Analyze a portfolio:
- 50% stocks: 11% return, 18% volatility
- 30% bonds: 5% return, 7% volatility  
- 20% cash: 2% return, 1% volatility
Calculate expected return and portfolio risk.
```

### Financial Definitions
```
What is a Roth IRA?
Explain the difference between ETF and mutual fund
```

## 📊 What You Get

### Python Execution Transparency

When you ask a calculation question, you'll see:

```
You: Calculate compound interest on $10,000 at 5% for 10 years

💭 Calculating...

💭 Thinking: I need to calculate compound interest using the formula...
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

============================================================
🤖 Finance Advisor: 

Your $10,000 investment at 5% annual interest will grow to 
$16,288.95 in 10 years, earning you $6,288.95 in interest.
============================================================
```

## 🛠️ Troubleshooting

### BeeAI Code Interpreter Not Running?

```bash
# Check if it's running
curl http://localhost:50081/health

# Start it (choose one method from Step 1 above)
cd ~/AIProjects/bee-code-interpreter
bash scripts/run-pull.sh
```

### Ollama Not Running?

```bash
# Check status
ollama list

# Start service
ollama serve

# Pull model if needed
ollama pull llama3.1
```

### Connection Errors?

```bash
# Test BeeAI connection
./test-beeai-connection.sh

# Check environment variable
echo $CODE_INTERPRETER_URL
# Should show: http://localhost:50081 (or your custom URL)
```

## 📚 Documentation

- **Full Setup Guide**: [SETUP_BEEAI_CODE_INTERPRETER.md](./SETUP_BEEAI_CODE_INTERPRETER.md)
- **Detailed README**: [README_FINANCE_ADVISOR.md](./README_FINANCE_ADVISOR.md)
- **Test Script**: `./test-beeai-connection.sh`

## 🎯 Key Features Enabled

✅ **Advanced Math**: NumPy, SciPy calculations  
✅ **Data Analysis**: Pandas DataFrames  
✅ **Visualizations**: Matplotlib charts  
✅ **Financial Functions**: IRR, NPV, PMT, etc.  
✅ **Statistical Models**: Monte Carlo, regression  
✅ **Secure Execution**: Sandboxed Python environment  
✅ **Auto Library Install**: No manual package management  

## 🔐 Security

All Python code runs in:
- Isolated Kubernetes pods
- Sandboxed containers
- No direct file system access
- Resource-limited environments
- Network-isolated execution

Safe for production use! ✨

---

**Questions?** Check the comprehensive guides:
- `SETUP_BEEAI_CODE_INTERPRETER.md` - Installation details
- `README_FINANCE_ADVISOR.md` - Feature documentation
- Run `./test-beeai-connection.sh` - Diagnostic tool
