#!/usr/bin/env python3
"""
LandWise Obsidian Vault MCP Server
===================================

Serves MCP (Model Context Protocol) endpoints for reading and writing to the Obsidian vault.

Features:
- Read markdown files from vault
- Query vault structure
- Write logs and memory updates
- Health check endpoint
- CORS support for JARVIS bridge

Run: python3 mcp_server.py
Port: 3000
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import json
from pathlib import Path
from datetime import datetime, timezone
import asyncio

# ── CONFIG ──────────────────────────────────────────────────────────

VAULT_PATH = "/Users/shaunducker/Desktop/LandWise/Obsidian-Vault"
PORT = 3000
HOST = "localhost"

# Read .mcpvault.json if it exists
CONFIG_FILE = os.path.join(VAULT_PATH, ".mcpvault.json")
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
        VAULT_PATH = config.get("vaultPath", VAULT_PATH)
        PORT = config.get("port", PORT)
        HOST = config.get("host", HOST)

app = FastAPI(title="LandWise Vault MCP Server", version="1.0.0")

# ── CORS ────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── HELPERS ─────────────────────────────────────────────────────────

def get_vault_path():
    """Return the vault path."""
    return VAULT_PATH

def safe_path(vault_path, file_path):
    """Ensure path is within vault (security check)."""
    vault_abs = os.path.abspath(vault_path)
    file_abs = os.path.abspath(os.path.join(vault_abs, file_path))
    if not file_abs.startswith(vault_abs):
        raise ValueError("Path traversal attack detected")
    return file_abs

def list_vault_structure(path=None):
    """Recursively list vault structure."""
    if path is None:
        path = get_vault_path()

    structure = []
    try:
        for item in sorted(os.listdir(path)):
            if item.startswith("."):
                continue  # Skip hidden files except .obsidian
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                structure.append({
                    "type": "dir",
                    "name": item,
                    "path": item_path
                })
            elif item.endswith(".md"):
                structure.append({
                    "type": "file",
                    "name": item,
                    "path": item_path
                })
    except Exception as e:
        print(f"Error listing vault: {e}")

    return structure

# ── ENDPOINTS ───────────────────────────────────────────────────────

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "vault": VAULT_PATH,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": "1.0.0"
    }

@app.get("/vault/structure")
async def vault_structure():
    """List vault directory structure."""
    try:
        structure = list_vault_structure()
        return {
            "status": "ok",
            "vault": VAULT_PATH,
            "structure": structure
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vault/read/{file_path:path}")
async def read_file(file_path: str):
    """Read a markdown file from the vault."""
    try:
        file_abs = safe_path(VAULT_PATH, file_path)

        if not file_abs.endswith(".md"):
            # Append .md if not present
            if os.path.exists(file_abs + ".md"):
                file_abs = file_abs + ".md"

        if not os.path.exists(file_abs):
            raise HTTPException(status_code=404, detail="File not found")

        with open(file_abs, "r", encoding="utf-8") as f:
            content = f.read()

        return {
            "status": "ok",
            "file": file_path,
            "path": file_abs,
            "size": len(content),
            "content": content,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/vault/append/{file_path:path}")
async def append_file(file_path: str, request: Request):
    """Append content to a markdown file."""
    try:
        body = await request.json()
        content = body.get("content", "")

        file_abs = safe_path(VAULT_PATH, file_path)
        if not file_abs.endswith(".md"):
            file_abs = file_abs + ".md"

        # Ensure directory exists
        os.makedirs(os.path.dirname(file_abs), exist_ok=True)

        # Append content
        with open(file_abs, "a", encoding="utf-8") as f:
            f.write("\n" + content + "\n")

        return {
            "status": "ok",
            "file": file_path,
            "action": "append",
            "size": len(content),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/vault/write/{file_path:path}")
async def write_file(file_path: str, request: Request):
    """Write (overwrite) a markdown file."""
    try:
        body = await request.json()
        content = body.get("content", "")

        file_abs = safe_path(VAULT_PATH, file_path)
        if not file_abs.endswith(".md"):
            file_abs = file_abs + ".md"

        # Ensure directory exists
        os.makedirs(os.path.dirname(file_abs), exist_ok=True)

        # Write content (overwrite)
        with open(file_abs, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "ok",
            "file": file_path,
            "action": "write",
            "size": len(content),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vault/search")
async def search(q: str):
    """Search for files by name or content."""
    try:
        results = []
        vault_abs = os.path.abspath(VAULT_PATH)

        for root, dirs, files in os.walk(vault_abs):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith(".")]

            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, vault_abs)

                    # Search filename
                    if q.lower() in file.lower():
                        results.append({
                            "type": "file",
                            "path": rel_path,
                            "name": file
                        })

        return {
            "status": "ok",
            "query": q,
            "results": results,
            "count": len(results)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── STARTUP ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    print(f"Starting LandWise Vault MCP Server")
    print(f"Vault: {VAULT_PATH}")
    print(f"Port: {PORT}")
    print(f"URL: http://{HOST}:{PORT}")

    uvicorn.run(app, host=HOST, port=PORT)
