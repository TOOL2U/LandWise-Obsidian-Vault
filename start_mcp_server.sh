#!/bin/bash

# LandWise Vault MCP Server Startup Script
# Runs the MCP server on localhost:3000

set -e

VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_PATH="/Users/shaunducker/Desktop/LandWise/Obsidian-Vault"
PORT=3000

echo "Starting LandWise Vault MCP Server"
echo "Vault: $VAULT_PATH"
echo "Port: $PORT"
echo "URL: http://localhost:$PORT"
echo ""

# Ensure vault path exists
if [ ! -d "$VAULT_PATH" ]; then
    echo "ERROR: Vault path does not exist: $VAULT_PATH"
    exit 1
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 is not installed"
    exit 1
fi

# Check if FastAPI/uvicorn is available
if ! python3 -c "import fastapi, uvicorn" 2>/dev/null; then
    echo "Installing required Python packages..."
    pip3 install fastapi uvicorn
fi

# Start the server
cd "$VAULT_PATH"
python3 mcp_server.py --port $PORT --host localhost

# Keep running until interrupted
wait
