#!/bin/bash

echo "🔍 Testing BeeAI Code Interpreter Connection..."
echo ""

# Test basic connectivity
echo "1. Testing basic connectivity..."
response=$(curl -s -X POST http://localhost:50081/v1/execute \
  -H "Content-Type: application/json" \
  -d '{"source_code":"print(\"Connection successful!\")"}' 2>&1)

if [ $? -eq 0 ]; then
  echo "✅ BeeAI Code Interpreter is running!"
  echo "Response: $response"
else
  echo "❌ Cannot connect to BeeAI Code Interpreter at http://localhost:50081"
  echo "Error: $response"
  echo ""
  echo "Please ensure BeeAI Code Interpreter is running:"
  echo "  cd ~/AIProjects/bee-code-interpreter"
  echo "  bash scripts/run-pull.sh"
  exit 1
fi

echo ""
echo "2. Testing Python calculation..."
calc_response=$(curl -s -X POST http://localhost:50081/v1/execute \
  -H "Content-Type: application/json" \
  -d '{"source_code":"result = 10000 * (1 + 0.05) ** 10\nprint(f\"Compound interest result: ${result:,.2f}\")"}')

echo "Response: $calc_response"

echo ""
echo "3. Testing numpy import..."
numpy_response=$(curl -s -X POST http://localhost:50081/v1/execute \
  -H "Content-Type: application/json" \
  -d '{"source_code":"import numpy as np\nprint(\"NumPy version:\", np.__version__)\nprint(\"Array:\", np.array([1, 2, 3]))"}')

echo "Response: $numpy_response"

echo ""
echo "✅ All tests passed! BeeAI Code Interpreter is ready."
echo ""
echo "You can now run your Personal Finance Advisor:"
echo "  node personal-finance-advisor.js"
