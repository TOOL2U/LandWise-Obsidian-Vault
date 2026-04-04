# JARVIS Orchestrator Folder

JARVIS state, prompt templates, integration configuration, and operational logs.

## Files

- **soul.md** — (See root) JARVIS identity and operating principles
- **integration.md** — How vault integrates with JARVIS bridge
- **system-prompt-template.md** — Template for JARVIS system prompt (with vault context)
- **dispatch-routing.md** — How JARVIS routes tasks to agents
- **logs/activity.md** — JARVIS activity log

## Quick Links

- JARVIS Bridge Code: `/Users/shaunducker/Desktop/LandWise/Jarvis/bridge/main.py`
- JARVIS Dashboard: http://localhost:8000/dashboard
- JARVIS Voice UI: http://localhost:8000/voice
- JARVIS Status: GET http://localhost:8000/status

## Agent Roster

See [[../soul.md#AGENT_ROSTER]] for the full roster and current status.

## Key Concepts

**JARVIS is the GM** — General Manager. Not an "agent" in the OpenClaw sense. JARVIS is the orchestrator that:
- Routes inbound requests to appropriate agents
- Tracks pipeline and lead status
- Monitors agent performance
- Synthesizes insights for Shaun
- Maintains vault memory

**11 Agent Crew** — JARVIS coordinates these 11 specialist agents:
1. agent_crm — Pipeline tracking, lead status
2. agent_lead_research — Finding prospects, qualifying
3. agent_outreach — Drafting messages, follow-ups
4. agent_content — Instagram, social media, content
5. agent_reporting — KPIs, pipeline reports
6. agent_marketing — Campaigns, email sequences
7. agent_finance — Invoicing, P&L, Thai tax
8. agent_operations — SOPs, survey scheduling
9. agent_strategy — Growth planning, OKRs
10. agent_admin — Scheduling, approvals
11. landwise_orchestrator — Fallback coordination

See [[dispatch-routing.md]] for routing logic.
