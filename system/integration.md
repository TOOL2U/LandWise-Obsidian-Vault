# Vault Integration with JARVIS Bridge

**Purpose:** JARVIS reads vault state on startup and periodically syncs with memory files.

---

## JARVIS Startup Sequence

1. Load .env and OPENCLAW_URL, DEERFLOW_URL, etc.
2. Load vault path from .env: VAULT_PATH=/Users/shaunducker/Desktop/LandWise/Obsidian-Vault
3. Read soul.md → Load identity, agent roster, operating principles
4. Read status.md → Load integration status, pending actions, current pipeline
5. Read CRM store from crm_store.json
6. Start background tasks: Telegram poll loop, vault refresh loop, Gmail lead poll loop (every 5 min)
7. Initialize JARVIS endpoints and dashboards
8. Listen for dispatch queue, webhook events

---

## Recall-Stack Layers (Context Injection Order)

JARVIS assembles context in this order on every request:

| Layer | Source | Purpose |
|-------|--------|---------|
| 1 | Live CRM + pending actions | Real-time business state |
| 2 | `primer.md` (BASE_DIR/../primer.md) | Session state — active phase, blockers, next step |
| 3 | Obsidian vault: daily-brief.md | Today's priorities |
| 4 | Obsidian vault: calendar.md | Schedule awareness |
| 5 | Obsidian vault: status.md | Integration status |
| 6 | Obsidian vault: soul.md | Company identity |
| 7 | Recent Telegram history (last 10 messages) | Conversation continuity |

**primer.md** is rewritten at the end of every Claude Code session to capture project phase, open blockers, and exact next step. JARVIS reads it on every request so it always knows current context without needing re-briefing.

---

## Vault Context in JARVIS System Prompt

```
## VAULT CONTEXT

You have access to a persistent Obsidian knowledge vault located at:
/Users/shaunducker/Desktop/LandWise/Obsidian-Vault

**Key Memory Files:**
- soul.md — Your identity, operating principles, agent roster
- status.md — Current integration status, pending actions, blockers
- memory/daily-brief.md — Today's priorities and lead status
- memory/dispatch-queue.md — Active Claude tasks and their status
- memory/calendar.md — Google Calendar events (synced by sync_vault.py)

**Read-only Integration:**
On startup and every hour:
1. Read soul.md for current identity/focus
2. Read status.md for integration status
3. Check memory/daily-brief.md for today's actions
4. Check memory/dispatch-queue.md to know what Claude is working on
5. Check memory/calendar.md for today's schedule

**DO NOT** modify soul.md or status.md programmatically. Manual updates only.
**DO** append logs to logs/jarvis-activity.md and logs/bridge-events.md after significant events.
```

---

## New Capabilities (Session 7 wired — 2026-04-05)

| Capability | Wired Into | Status |
|---|---|---|
| WhatsApp autodiscover (port 18789) | main.py send_whatsapp() | ✅ |
| Gmail auto-polling every 5 min | main.py _gmail_poll_loop() | ✅ |
| Google Calendar API (read + book) | main.py /calendar/* endpoints + JARVIS tools | ✅ |
| recall-stack primer.md | main.py _load_primer() + _write_primer() | ✅ |
| Calendar vault sync | sync_vault.py sync_calendar() | ✅ |
| DeerFlow agents read primer.md | deerflow-integration.md Step 4 | ✅ Documented |
| OpenClaw new tool awareness | soul.md BRIDGE CONFIG section | ✅ Documented |
| GSD / Ralph slash commands | .claude/commands/ | ✅ |

---

## New Integrations (Session 7 — 2026-04-05)

### Gmail Auto-Polling
- `_check_gmail_for_leads()` — checks INBOX for lead emails since `_gmail_last_checked`
- Uses `_is_lead_enquiry()` to classify: 14 lead keywords, skips no-reply/own address/threads
- Sends Telegram notification per match: `📧 New lead enquiry detected`
- `_gmail_poll_loop()` runs every 5 minutes in background
- Manual trigger: `GET /gmail/check-leads`
- JARVIS tool: `check_new_leads`

### Google Calendar API
- Credentials: `calendar_credentials/token.json` + `client_secret.json`
- Helper: `_get_calendar_service()` — auto-refreshes expired tokens, fails gracefully
- Endpoints: `GET /calendar/today`, `GET /calendar/week`, `POST /calendar/book`
- JARVIS tools: `read_calendar` (period: today/week), `book_meeting`
- Vault sync: `sync_calendar()` in sync_vault.py writes to memory/calendar.md
- Setup: run `python3 calendar_auth.py` once to generate token.json

### WhatsApp Port Auto-Discovery
- `send_whatsapp()` now tries ports in order: cached URL → 18789 (WebSocket gateway) → 8080 (OPENCLAW_URL) → 3000
- `_wa_working_url` caches the first successful port across calls
- Endpoint: `POST /whatsapp/autodiscover` — probes all known ports and returns working URL

---

## Data Sync Schedule

| Interval | Action |
|---|---|
| On startup | Read soul.md, status.md, memory/daily-brief.md |
| Every 5 min | Gmail lead poll (background loop) |
| Every 5 min | sync_vault.py daemon (if running) |
| Every 30 min | Vault refresh loop |
| Every 24 hours | Generate daily brief, update memory/ folder |
| Weekly (Mon 9am) | Generate weekly report, update BACKLOG.md |

---

## Vault Write Rules

JARVIS can append to (but not overwrite):
- memory/jarvis-activity.md — Log of decisions and dispatch events
- logs/bridge-events.md — Record of API calls, errors, completions
- logs/jarvis-activity.md — Hourly sync notes

sync_vault.py writes (overwrites on each run):
- memory/crm-snapshot.md
- memory/pending-actions.md
- memory/content-calendar.md
- memory/daily-brief.md
- memory/calendar.md

JARVIS CANNOT modify:
- soul.md — Shaun updates manually
- status.md — Shaun updates manually
- agents/SOUL.md — Agent-specific; agents update via OpenClaw

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
