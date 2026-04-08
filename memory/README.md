# Memory Folder

Persistent vault memory — agent memory, conversation logs, session state, dispatch queue tracking.

## Files

- **daily-brief.md** — Today's priorities, lead status, actions
- **dispatch-queue.md** — Active Claude tasks and their status
- **completed-tasks.md** — Completed Claude tasks (archive)
- **agent-memory/** — Per-agent persistent memory (agent-created)
- **sync-schedule.md** — Memory sync schedule and automation
- **ai-history/** — Shaun's AI conversation knowledge base (imported 2026-04-07)
  - shaun-profile.md — Owner identity, skills, preferences
  - property-business.md — Sia Moon business model, services, pipeline
  - web-development.md — Tech stack, GitHub repos, projects
  - land-survey-gis.md — QGIS drainage analysis, land survey
  - legal-contracts.md — Thai lease, company registration, legal
  - design-branding.md — Logos, uniforms, website design, brand
  - ai-team-structure.md — Multi-agent AI team, JARVIS, automation vision
  - thailand-context.md — Thailand living, construction, banking, language

## Sync Automation

JARVIS syncs memory files hourly:
1. Reads daily-brief.md
2. Checks dispatch-queue.md for active tasks
3. Appends new activity to jarvis-activity.md
4. Updates status indicators

## Manual Updates

Shaun can manually add notes to any file in memory/. They are read by JARVIS on next sync.

Example:
```markdown
# Note for Claude
Please prioritize Denis's quote by EOD today. He's expecting it.
```

JARVIS reads this and can route it to appropriate agent.

## Access Control

- JARVIS: Read-only
- Shaun: Read-write
- Agents: Can append only (not overwrite)
- Claude Dispatch: Read-write (only to dispatch-queue.md)
