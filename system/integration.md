# Vault Integration with JARVIS Bridge

**Purpose:** JARVIS reads vault state on startup and periodically syncs with memory files.

---

## JARVIS Startup Sequence

1. Load .env and OPENCLAW_URL, DEERFLOW_URL, etc.
2. **NEW:** Load vault path from .env: VAULT_PATH=/Users/shaunducker/Desktop/LandWise/Obsidian-Vault
3. **NEW:** Read soul.md → Load identity, agent roster, operating principles
4. **NEW:** Read status.md → Load integration status, pending actions, current pipeline
5. Read CRM store from crm_store.json
6. Initialize JARVIS endpoints and dashboards
7. Listen for dispatch queue, webhook events

---

## Vault Context in JARVIS System Prompt

Add this block to the JARVIS system prompt:

```
## VAULT CONTEXT

You have access to a persistent Obsidian knowledge vault located at:
/Users/shaunducker/Desktop/LandWise/Obsidian-Vault

**Key Memory Files:**
- soul.md — Your identity, operating principles, agent roster
- status.md — Current integration status, pending actions, blockers
- memory/daily-brief.md — Today's priorities and lead status
- memory/dispatch-queue.md — Active Claude tasks and their status

**Read-only Integration:**
On startup and every hour:
1. Read soul.md for current identity/focus
2. Read status.md for integration status
3. Check memory/daily-brief.md for today's actions
4. Check memory/dispatch-queue.md to know what Claude is working on

**DO NOT** modify soul.md or status.md programmatically. Manual updates only by Shaun via CLAUDE.md instructions.

**DO** append logs to logs/jarvis-activity.md and logs/bridge-events.md after significant events.
```

---

## Data Sync Schedule

| Interval | Action |
|---|---|
| On startup | Read soul.md, status.md, memory/daily-brief.md |
| Every 1 hour | Sync lead status, check pending actions |
| Every 24 hours | Generate daily brief, update memory/ folder |
| Weekly (Mon 9am) | Generate weekly report, update BACKLOG.md |

---

## Vault Write Rules

JARVIS can append to (but not overwrite):

- memory/jarvis-activity.md — Log of decisions and dispatch events
- logs/bridge-events.md — Record of API calls, errors, completions
- logs/jarvis-activity.md — Hourly sync notes

JARVIS CANNOT modify:
- soul.md — Shaun updates manually
- status.md — Shaun updates manually
- agent souls in agents/ — Agent-specific; agents update via OpenClaw

---

## MCP Server Integration

Once MCP server is running on localhost:3000, JARVIS can query vault via HTTP:

```python
# In JARVIS bridge main.py
async def load_vault_context():
    async with httpx.AsyncClient() as client:
        soul = await client.get("http://localhost:3000/vault/read/soul.md")
        status = await client.get("http://localhost:3000/vault/read/status.md")
        return {
            "soul": soul.json(),
            "status": status.json()
        }
```

See [[mcp-config.md]] for MCP server details.

---

## Dispatch Queue Integration

When Claude Dispatch picks up a task:
1. Claude writes task to memory/dispatch-queue.md
2. JARVIS reads memory/dispatch-queue.md every hour
3. JARVIS knows what Claude is working on, can coordinate hand-offs
4. When Claude finishes, JARVIS updates memory/completed-tasks.md

See [[../memory/dispatch-queue.md]] template.
