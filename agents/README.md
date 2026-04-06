# Agents Folder

Individual agent souls and memory files. Each agent has its own persistent memory and operating principles.

## Agent Files

Each agent has:
- **[agent-id]-soul.md** — Identity, operating principles, authority
- **[agent-id]-memory.md** — Persistent memory (conversations, decisions, learned patterns)
- **[agent-id]-skills.md** — Available skills and tools (for OpenClaw/DeerFlow)

## Agent Roster

1. **agent_crm** — CRM Manager (lead tracking, pipeline status)
2. **agent_lead_research** — Lead Researcher (prospect finding, qualification)
3. **agent_outreach** — Outreach Specialist (message drafting, follow-ups)
4. **agent_content** — Content Creator (Instagram, social media, content calendar)
5. **agent_reporting** — Analytics & Reporting (KPIs, pipeline reports)
6. **agent_marketing** — Marketing Strategist (campaigns, email sequences, SEO)
7. **agent_finance** — CFO / Finance (invoicing, P&L, cash flow, Thai tax)
8. **agent_operations** — Head of Operations (SOPs, survey scheduling, drone regs)
9. **agent_strategy** — Chief Strategy (growth planning, OKRs, market analysis)
10. **agent_admin** — Executive Assistant (scheduling, approvals, document coordination)
11. **landwise_orchestrator** — General Orchestrator (fallback routing, synthesis)

## Soul Files

See individual agent files. Key principles:
- Each agent is autonomous within their domain
- All external comms require Shaun's WhatsApp approval (via JARVIS/OpenClaw)
- Agents read this vault for context on company status, leads, blockers
- Agents append logs to their memory files

## Integration

- **OpenClaw:** Each agent has corresponding soul/prompt in OpenClaw configuration
- **DeerFlow:** Agent skills live in vault/agents/ (see workflows for details)
- **JARVIS:** Routes requests to agents via dispatch rules
- **Claude Dispatch:** Can invoke agents directly for multi-step tasks

## Calendar Access (Google Calendar is LIVE)

Google Calendar is connected via Obsidian plugin (syncs every 10 min) and JARVIS Calendar API.

**Agents that should check calendar before acting:**
- **agent_admin** — always check calendar before scheduling; use JARVIS `book_meeting` tool
- **agent_operations** — check for survey conflicts before scheduling site visits
- **agent_crm** — check calendar when a lead asks about timing or availability

**How to check schedule:**
1. Read `Obsidian-Vault/memory/calendar.md` — updated every 10 min by Obsidian plugin
2. Or ask JARVIS to call `read_calendar` tool for live API data

**How to book:**
- Route booking requests through JARVIS — it has the `book_meeting` tool
- Always confirm with Shaun before creating events
- Include: client name, plot address/location, duration (default 60 min)

---

## Memory Access

Agents can READ:
- soul.md (identity)
- status.md (blockers, integration status)
- daily-brief.md (priorities, lead status)
- **memory/calendar.md** — Shaun's live calendar (Google Calendar via Obsidian plugin)
- Other agent souls (for coordination)

Agents can WRITE (append only):
- [agent-id]-memory.md (their own memory)
- logs/agent-activity.md (shared activity log)

Agents CANNOT modify:
- soul.md, status.md (Shaun updates these)
- Other agent souls
