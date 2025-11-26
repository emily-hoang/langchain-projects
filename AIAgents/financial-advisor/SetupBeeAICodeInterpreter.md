# BeeAI Code Interpreter Setup Guide

## Prerequisites

1. **Rancher Desktop** (recommended) or Docker Desktop
2. **kubectl** command-line tool
3. **Git** with submodules support

## Installation Steps

### Option 1: Quick Start with Pre-built Image (Recommended)

```bash
# 1. Clone BeeAI Code Interpreter with submodules
cd ~/AIProjects
git clone --recurse-submodules https://github.com/i-am-bee/bee-code-interpreter.git
cd bee-code-interpreter

# 2. Run with pre-built image (fastest method)
bash scripts/run-pull.sh
```

### Option 2: Build Image Locally (for customization)

```bash
# 1. Clone BeeAI Code Interpreter with submodules
cd ~/AIProjects
git clone --recurse-submodules https://github.com/i-am-bee/bee-code-interpreter.git
cd bee-code-interpreter

# 2. Build and run locally (may take 1-2 hours)
bash scripts/run-build.sh
```

### Option 3: Using BeeAI Framework Starter (Easiest)

```bash
# Clone the TypeScript starter template
git clone https://github.com/i-am-bee/beeai-framework-ts-starter.git
cd beeai-framework-ts-starter

# Follow the README instructions - it sets up everything automatically
```

## Verify Installation

### Check if the service is running

```bash
# Test with curl
curl -X POST http://localhost:50081/v1/execute \
  -H "Content-Type: application/json" \
  -d '{"source_code":"print(\"Hello from BeeAI Code Interpreter!\")"}'
```

**Expected Output:**
```json
{
  "stdout": "Hello from BeeAI Code Interpreter!\n",
  "stderr": "",
  "exit_code": 0,
  "files": {}
}
```

### Check health

```bash
# If you have Python and the code interpreter installed
python -m code_interpreter.health_check
```

## Configuration

### Environment Variables

You can override configuration using environment variables with `APP_` prefix:

```bash
# Example: Change the executor image
export APP_EXECUTOR_IMAGE=custom-executor:latest

# Example: Change the namespace
export APP_NAMESPACE=my-namespace
```

### Common Configuration Options

Located in `src/code_interpreter/config.py`:

- `executor_image`: Docker image for code execution
- `namespace`: Kubernetes namespace for executor pods
- `host`: Service host (default: 0.0.0.0)
- `port`: Service port (default: 50081)

## Running Your Finance Advisor

Once BeeAI Code Interpreter is running:

```bash
cd /Users/nhunghoang/AIProjects/chatbot/AIAgents

# Set the Code Interpreter URL (optional, defaults to localhost:50081)
export CODE_INTERPRETER_URL=http://localhost:50081

# Run the finance advisor
node personal-finance-advisor.js
```

## Example Queries

Try these with your Personal Finance Advisor:

### 1. Compound Interest Calculation
```
Calculate compound interest on $50,000 at 6% annual rate for 20 years with monthly compounding
```

### 2. Mortgage Amortization
```
Create a 30-year mortgage amortization schedule for $400,000 at 4.5% interest
```

### 3. Portfolio Analysis
```
Calculate the expected return and risk of a portfolio with:
- 40% stocks (12% return, 18% volatility)
- 30% bonds (5% return, 6% volatility)
- 30% cash (2% return, 1% volatility)
```

### 4. NPV Calculation
```
What's the NPV of an investment with initial cost $100,000 and cash flows:
Year 1: $30,000
Year 2: $35,000
Year 3: $40,000
Year 4: $45,000
Discount rate: 8%
```

### 5. Retirement Savings
```
If I invest $500/month for 30 years with 7% annual return, how much will I have?
Plot the growth over time.
```

## Troubleshooting

### Port 50081 already in use
```bash
# Find the process using port 50081
lsof -i :50081

# Kill the process if needed
kill -9 <PID>
```

### Kubernetes context issues
```bash
# Check current context
kubectl config current-context

# List all contexts
kubectl config get-contexts

# Switch context if needed
kubectl config use-context rancher-desktop
```

### Service not starting
```bash
# Check Rancher Desktop is running
# Check kubectl can connect
kubectl get pods --all-namespaces

# Check logs
kubectl logs -n <namespace> <pod-name>
```

### Connection refused errors
```bash
# Verify service is accessible
curl http://localhost:50081/health

# Check port forwarding
kubectl port-forward -n <namespace> <pod-name> 50081:50081
```

## Production Considerations

For production deployment:

1. **Use secure container runtime**: gVisor, Kata Containers, or Firecracker
2. **Configure service account**: With proper RBAC permissions
3. **Set up file storage cleanup**: Auto-delete old objects from shared storage
4. **Use S3 bucket**: For file sharing instead of local filesystem
5. **Monitor resource usage**: Set appropriate limits for executor pods
6. **Enable logging**: Capture execution logs for debugging
7. **Implement rate limiting**: Prevent abuse of code execution

## Resources

- [BeeAI Code Interpreter GitHub](https://github.com/i-am-bee/bee-code-interpreter)
- [BeeAI Framework Docs](https://i-am-bee.github.io/bee-agent-framework/)
- [Rancher Desktop](https://rancherdesktop.io/)
- [TypeScript Starter](https://github.com/i-am-bee/beeai-framework-ts-starter)
- [Python Starter](https://github.com/i-am-bee/beeai-framework-py-starter)
