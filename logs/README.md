# Logs Folder

System logs, integration events, and audit trails.

## Log Files

- **jarvis-activity.md** — JARVIS decisions, dispatch events, hourly syncs
- **bridge-events.md** — JARVIS bridge API calls, errors, webhook events
- **agent-activity.md** — Agent decisions and task completions
- **vault-access.md** — Vault read/write access log (for audit)
- **integration-tests.md** — Results of integration tests (Phase 10)

## Log Retention

- Keep logs for 90 days minimum
- Archive old logs to logs/archive/ after 6 months
- Monthly summary: Last Sunday of month → summary to memory/

## Log Format

All logs use ISO 8601 timestamp:
```
[2026-04-04T09:30:00Z] JARVIS: Routed lead-intake task to agent_crm
[2026-04-04T09:31:15Z] agent_crm: Logged Denis Lantheaume into CRM, score: 75
[2026-04-04T09:32:00Z] JARVIS: Waiting for Shaun approval to proceed with quote
```

## Querying Logs

To find all JARVIS decisions today:
```
grep "JARVIS:" logs/jarvis-activity.md
```

To find all errors:
```
grep -E "ERROR|BLOCKED|FAILED" logs/bridge-events.md logs/agent-activity.md
```

## Integration Events

JARVIS bridge logs all API calls:
- Incoming webhook events
- Outgoing email/WhatsApp sends
- DeerFlow agent requests
- OpenClaw dispatch updates
- CRM updates

This helps debug integrations.
