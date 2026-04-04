# Workflows Folder

Repeatable playbooks for common LandWise tasks. These are referenced by JARVIS and agents.

## Workflow Files

- **new-lead-intake.md** — Process new lead inquiry (intake → qualify → log)
- **lead-followup.md** — Daily follow-up process (check responses, send next steps)
- **quote-generation.md** — Generate and send quote (draft → approval → send)
- **approval-request.md** — Standard pattern for requesting Shaun approval (WhatsApp)
- **partnership-outreach.md** — Outreach to agents and brokers
- **survey-scheduling.md** — Schedule drone survey and coordinate on-site work
- **reporting-kpis.md** — Generate weekly/monthly pipeline and KPI reports

## How to Use

When JARVIS routes a task, the assigned agent follows the corresponding workflow:

1. **New email from potential client** → agent_outreach follows new-lead-intake.md
2. **Check for lead responses** → agent_outreach follows lead-followup.md
3. **Generate quote** → agent_outreach follows quote-generation.md
4. **Need Shaun approval** → Any agent follows approval-request.md
5. **Reach out to agents/brokers** → agent_marketing follows partnership-outreach.md

## Workflow Template

Each workflow includes:
- **Trigger:** When to start this workflow
- **Steps:** Step-by-step actions
- **Decision points:** Where conditional logic applies
- **Approval gates:** Where Shaun approval is needed
- **Success criteria:** How to know the workflow completed
- **Error handling:** What to do if something fails

## Integration with JARVIS

JARVIS reads these workflows to understand available processes. When routing a task, JARVIS says:
"Follow workflow X" — the agent then executes the steps in that workflow.

## Integration with Claude Dispatch

When Claude Dispatch picks up a task, it can reference workflows directly:
"Process these 3 leads using the new-lead-intake workflow" — Claude follows the steps and coordinates hand-offs to agents.

## Updating Workflows

- Workflows are living documents
- After significant process change, update the relevant workflow
- Document why the change was made
- Log to logs/workflow-updates.md

---

## Current Workflows (Status)

- [ ] new-lead-intake.md — Not yet created
- [ ] lead-followup.md — Not yet created
- [ ] quote-generation.md — Not yet created
- [ ] approval-request.md — Not yet created
- [ ] partnership-outreach.md — Not yet created
- [ ] survey-scheduling.md — Not yet created
- [ ] reporting-kpis.md — Not yet created

See [[../../Desktop--LandWise/workflows/]] for existing workflow files in the main LandWise folder.
