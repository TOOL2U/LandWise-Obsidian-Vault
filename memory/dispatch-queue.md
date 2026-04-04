# Dispatch Queue — Active Claude Tasks

**Last Updated:** 2026-04-04T00:00:00Z

This file tracks active Claude Dispatch tasks. JARVIS reads this hourly to understand what Claude is working on.

---

## Active Tasks

| Task ID | Title | Status | Started | ETA | Notes |
|---|---|---|---|---|---|
| (none yet) | — | — | — | — | — |

---

## Completed This Session

| Task ID | Title | Status | Completed | Duration | Notes |
|---|---|---|---|---|---|
| (none yet) | — | — | — | — | — |

---

## Template for New Task Entry

When Claude Dispatch starts a new task, it should add an entry here:

```markdown
| 2026-04-04-lead-intake-001 | Process 3 Gmail leads | in_progress | 2026-04-04T09:00:00Z | 2 hours | Log Denis, Philémon, Bob into CRM |
```

Update status as: `in_progress` → `blocked` (if issue) → `completed` (if done)

---

## How JARVIS Uses This

1. JARVIS reads this file every hour
2. JARVIS sees which Claude tasks are active
3. If a task is blocked, JARVIS can route to appropriate agent for support
4. When completed, JARVIS can trigger follow-up actions (e.g., send approval request via WhatsApp)

---

## Handoff Requests

If Claude needs JARVIS/agent help, add here:

```markdown
## Blocked: 2026-04-04-lead-intake-001

Reason: Need Shaun WhatsApp approval before sending messages

Action for JARVIS:
- Route approval request to OpenClaw agent
- Send Shaun: "3 leads ready for outreach. Approve messages?"
- Wait for response
- Resume task once approved
```
