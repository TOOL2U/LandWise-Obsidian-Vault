# Skill: Obsidian Vault Query

**Type:** Read-only vault query tool
**Requires:** MCP server running on http://localhost:3000
**Use Cases:** Check vault status, read agent souls, check daily priorities, check dispatch queue

---

## DESCRIPTION

Query the Obsidian knowledge vault for current system state. Use this when you need to:
- Check today's priorities (memory/daily-brief.md)
- Read agent souls and memory
- Check current blockers (status.md)
- See what Claude is working on (memory/dispatch-queue.md)
- Search vault for specific information

---

## SYNTAX

```
/vault read <file>
/vault status
/vault search <term>
```

---

## EXAMPLES

**Check today's priorities:**
```
/vault read memory/daily-brief.md
```

**Check current blockers:**
```
/vault read status.md
```

**Check dispatch queue:**
```
/vault read memory/dispatch-queue.md
```

**Check agent soul:**
```
/vault read agents/agent_crm-soul.md
```

**Search for a file:**
```
/vault search lead
```

---

## RESPONSE FORMAT

Vault returns:
```json
{
  "status": "ok",
  "file": "memory/daily-brief.md",
  "content": "...",
  "timestamp": "2026-04-04T09:00:00Z"
}
```

---

## LIMITATIONS

- Read-only (for OpenClaw use)
- MCP server must be running
- Files must exist in vault
- Max file size: 1 MB (can be extended if needed)

---

## CONFIGURATION

OpenClaw agents can call this skill via:
```bash
curl http://localhost:3000/vault/read/memory/daily-brief.md
```

---

## SEE ALSO

- MCP Server: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/mcp_server.py
- Vault Integration: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/system/integration.md
