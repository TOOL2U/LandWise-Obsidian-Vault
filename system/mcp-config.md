# MCP Server Configuration

**Package:** @bitbonsai/mcpvault
**Version:** Latest
**Port:** 3000 (configurable)
**Vault Path:** /Users/shaunducker/Desktop/LandWise/Obsidian-Vault

---

## Installation

```bash
npm install -g @bitbonsai/mcpvault
# OR if global permission fails:
npx @bitbonsai/mcpvault
```

## Configuration File

Location: `/Users/shaunducker/Desktop/LandWise/Obsidian-Vault/.mcpvault.json`

```json
{
  "vaultPath": "/Users/shaunducker/Desktop/LandWise/Obsidian-Vault",
  "port": 3000,
  "host": "localhost",
  "openaiApiKey": "sk-...",
  "allowedOrigins": [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:2026"
  ],
  "logLevel": "info"
}
```

## Startup

See [[../mcp-startup.sh]] for the startup script.

```bash
chmod +x /Users/shaunducker/Desktop/LandWise/mcp-startup.sh
/Users/shaunducker/Desktop/LandWise/mcp-startup.sh
```

## Health Check

```bash
curl http://localhost:3000/health
```

Expected response:
```json
{
  "status": "ok",
  "vault": "/Users/shaunducker/Desktop/LandWise/Obsidian-Vault",
  "timestamp": "2026-04-04T00:00:00Z"
}
```

## Integration Points

- **JARVIS Bridge:** Reads vault on startup (soul.md, status.md)
- **Dispatch Queue:** Writes task state to memory/
- **OpenClaw:** Can call MCP endpoints via Make.com webhooks
- **DeerFlow:** Skills directory points to vault/agents/

See [[integration.md]] for details.
