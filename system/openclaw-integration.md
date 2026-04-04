# OpenClaw Integration with Vault

**Status:** Ready for configuration
**MCP Server URL:** http://localhost:3000
**Vault Path:** /Users/shaunducker/Desktop/LandWise/Obsidian-Vault

---

## OVERVIEW

OpenClaw WhatsApp agents can query the vault to:
- Check daily priorities before acting
- See what other agents are doing
- Read agent souls for coordination
- Get status updates before sending to Shaun

---

## INTEGRATION POINTS

### 1. Agent Souls in Vault

Each OpenClaw agent can have a corresponding soul file in vault:
- `agents/agent_crm-soul.md` — agent_crm identity and rules
- `agents/agent_outreach-soul.md` — agent_outreach identity and rules
- `agents/agent_marketing-soul.md` — agent_marketing identity and rules
- etc.

Agents read these on startup to load identity and operating principles.

### 2. MCP Server Endpoints

OpenClaw can query vault via HTTP:

**Read a file:**
```bash
GET http://localhost:3000/vault/read/memory/daily-brief.md
```

**Search vault:**
```bash
GET http://localhost:3000/vault/search?q=lead
```

**Append to log:**
```bash
POST http://localhost:3000/vault/append/logs/agent-activity.md
{
  "content": "[2026-04-04T09:00:00Z] agent_crm: Logged Denis into CRM"
}
```

### 3. OpenClaw Agent Prompts

Update agent prompts to include vault awareness:

```markdown
# Agent: agent_crm (CRM Manager)

## Current Status (from vault)

Read from vault at the start of every task:
1. Check memory/daily-brief.md for today's priorities
2. Check memory/dispatch-queue.md to avoid duplicate work
3. Check status.md for known blockers

## Vault Access

You can READ from vault:
GET http://localhost:3000/vault/read/memory/daily-brief.md
GET http://localhost:3000/vault/read/status.md
GET http://localhost:3000/vault/read/memory/dispatch-queue.md

You can APPEND to logs:
POST http://localhost:3000/vault/append/logs/agent-activity.md
```

---

## IMPLEMENTATION STEPS

### Step 1: Create agent soul files in vault

For each agent, create a soul file:

**agents/agent_crm-soul.md:**
```markdown
# Soul: agent_crm (CRM Manager)

**Role:** Pipeline tracking, lead status, CRM updates
**Authority:** Can log leads, update lead status, generate CRM reports
**Reporting:** Append to logs/agent-activity.md after major actions

## Operating Principles

1. Read memory/daily-brief.md before starting work
2. Check status.md for known blockers
3. Log all CRM updates to logs/agent-activity.md
4. Escalate to JARVIS if lead status is uncertain
5. Never send external communication without Shaun approval
```

### Step 2: Update OpenClaw Docker container

Add MCP server to allowed origins in openclaw config:

```json
{
  "allowedOrigins": [
    "http://localhost:8000",  // JARVIS bridge
    "http://localhost:3000",  // MCP vault server
    "http://localhost:2026"   // DeerFlow
  ],
  "skills": [
    {
      "name": "vault-query",
      "description": "Query Obsidian vault for system state",
      "url": "http://localhost:3000/vault/"
    }
  ]
}
```

### Step 3: Test vault query from OpenClaw

In OpenClaw test console:
```bash
# Should return daily-brief.md content
curl http://localhost:3000/vault/read/memory/daily-brief.md

# Should return 200 OK
curl http://localhost:3000/health
```

### Step 4: Add vault query to agent workflows

Update agent prompts in OpenClaw to query vault before acting:

Example for agent_outreach:
```
Before sending any message:
1. Query vault: GET http://localhost:3000/vault/read/memory/daily-brief.md
2. Check if this lead is already being worked on
3. Check if there are known blockers for this lead
4. Proceed only if clear to go
```

---

## WORKFLOW EXAMPLE

**Scenario:** OpenClaw agent_outreach wants to send a message to Denis

1. Agent queries vault:
   ```
   GET http://localhost:3000/vault/read/memory/dispatch-queue.md
   GET http://localhost:3000/vault/read/status.md
   ```

2. Agent sees: "No blocker for Denis. Ready to send."

3. Agent drafts message and prepares to send

4. Agent queries vault:
   ```
   POST http://localhost:3000/vault/append/logs/agent-activity.md
   {
     "content": "[2026-04-04T09:15:00Z] agent_outreach: Ready to send message to Denis (HOT lead)"
   }
   ```

5. Agent sends message to Shaun via WhatsApp for approval (normal approval flow)

---

## TROUBLESHOOTING

### MCP server not reachable from OpenClaw
**Error:** Connection refused on http://localhost:3000
**Solution:** Ensure MCP server is running:
```bash
python3 /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/mcp_server.py &
```

### Agent soul files not found
**Error:** 404 Not Found for agents/agent_crm-soul.md
**Solution:** Create agent soul files in vault:
```bash
touch /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/agent_crm-soul.md
```

### Vault queries slow down agent
**Issue:** Agent waits for vault query to complete
**Solution:** Add timeout to MCP requests (default: 5 seconds)

---

## NEXT STEPS

1. **Create agent soul files** — One for each OpenClaw agent
2. **Update agent prompts** — Add vault query logic
3. **Test vault access** — Verify agents can query MCP server
4. **Monitor vault logs** — Check logs/agent-activity.md for agent activity
5. **Phase 7+:** Integrate DeerFlow with vault

---

## SEE ALSO

- MCP Server: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/mcp_server.py
- Vault Query Skill: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/obsidian.md
- JARVIS Integration: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/system/integration.md
