# DeerFlow Integration with Vault

**Status:** Ready for configuration
**DeerFlow URL:** http://localhost:2026
**Vault Skills Path:** /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/

---

## OVERVIEW

DeerFlow agents can have persistent skills stored in the vault. This enables:
- Skills as markdown files (easy to edit)
- Skill versioning via git
- Skills readable by JARVIS and other agents
- Central skill repository shared across the crew

---

## INTEGRATION POINTS

### 1. Vault Skills Directory

DeerFlow skills live in:
```
/Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/
```

Each skill is a markdown file:
- `agent_crm-skills.md` — agent_crm available skills
- `agent_outreach-skills.md` — agent_outreach available skills
- `agent_marketing-skills.md` — agent_marketing available skills
- etc.

### 2. DeerFlow Configuration

Update DeerFlow config to point to vault skills:

**In DeerFlow .env or config.json:**
```json
{
  "skillsPath": "/Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/",
  "skillExtension": ".md",
  "autoReload": true,
  "vaultIntegration": {
    "enabled": true,
    "mcpUrl": "http://localhost:3000"
  }
}
```

### 3. Skill File Format

Each skill file defines available actions:

**agent_crm-skills.md:**
```markdown
# Skills: agent_crm (CRM Manager)

## Skill: log_lead
**Description:** Log a new lead into CRM
**Input:** name, email, phone, source, score
**Output:** lead_id, status
**Error Handling:** Duplicate lead → return existing_lead_id

## Skill: update_lead_status
**Description:** Change lead status in pipeline
**Input:** lead_id, status (NEW, CONTACTED, QUALIFIED, QUOTED, ACTIVE, CLOSED)
**Output:** lead (updated record)

## Skill: get_lead_status
**Description:** Fetch current lead status
**Input:** lead_id
**Output:** lead (full record)

## Skill: generate_crm_report
**Description:** Generate pipeline report
**Input:** date_range (optional), status_filter (optional)
**Output:** report (markdown)
```

---

## IMPLEMENTATION STEPS

### Step 1: Create skill files for each agent

For agent_crm:
```bash
cat > /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/agent_crm-skills.md << 'EOF'
# Skills: agent_crm (CRM Manager)

## Skill: log_lead
**Purpose:** Add new lead to CRM
**Input:** name, email, phone, source, score
**Output:** lead_id, status

## Skill: update_lead_status
**Purpose:** Update lead pipeline status
**Input:** lead_id, new_status
**Output:** lead_record

## Skill: generate_pipeline_report
**Purpose:** Generate current pipeline report
**Input:** (none)
**Output:** report.md
EOF
```

### Step 2: Configure DeerFlow to read from vault

**Location:** Wherever DeerFlow config is
(Typically: /Users/shaunducker/Desktop/LandWise/Deerflow/config.json or similar)

Add:
```json
{
  "skills": {
    "path": "/Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/",
    "extension": ".md",
    "autoReload": true,
    "vaultIntegration": {
      "enabled": true,
      "mcpUrl": "http://localhost:3000",
      "readMemoryOnStartup": true
    }
  }
}
```

### Step 3: Test DeerFlow skill loading

Restart DeerFlow:
```bash
# DeerFlow should load skills from vault
# Check DeerFlow logs for: "Loaded X skills from vault"
```

Query DeerFlow skill list:
```bash
curl http://localhost:2026/skills
# Should list all skills from vault agents/ folder
```

### Step 4: Add vault context to DeerFlow agents

DeerFlow agents should read vault on startup:

**In DeerFlow agent startup:**
```python
async def startup(agent):
    # Read primer.md FIRST — recall-stack Layer 2 (current project state, last action, next step)
    try:
        primer = open("/Users/shaunducker/Desktop/LandWise/primer.md").read()
    except Exception:
        primer = ""

    # Read vault status and today's brief
    vault_status = await http.get("http://localhost:3000/vault/read/status.md")

    # Set agent context — primer is the most important for continuity
    agent.context["primer"]           = primer   # ← recall-stack Layer 2
    agent.context["vault_status"]     = vault_status
    agent.context["today_priorities"] = await http.get(
        "http://localhost:3000/vault/read/memory/daily-brief.md"
    )
```

**IMPORTANT — primer.md is the recall-stack Layer 2 file.**
- **Path:** `/Users/shaunducker/Desktop/LandWise/primer.md`
- **Contents:** active project, last completed JARVIS action, exact next step, system state
- **Rule:** All DeerFlow agents MUST read primer.md before starting work to stay in sync with the JARVIS session state and avoid duplicate or conflicting work.

---

## SKILL FILE EXAMPLES

### agent_outreach-skills.md

```markdown
# Skills: agent_outreach (Outreach Specialist)

## Skill: draft_message
**Purpose:** Draft client message or follow-up
**Input:** client_name, lead_stage, context
**Output:** message (text), tone, approval_needed (bool)

## Skill: schedule_followup
**Purpose:** Schedule follow-up for a lead
**Input:** lead_id, date, action
**Output:** followup_id, status

## Skill: get_pending_responses
**Purpose:** Check for client responses to recent messages
**Input:** (optional: date_since)
**Output:** responses (list)
```

### agent_marketing-skills.md

```markdown
# Skills: agent_marketing (Marketing Strategist)

## Skill: draft_email_sequence
**Purpose:** Create multi-email nurture sequence
**Input:** lead_list, campaign_name, template
**Output:** sequence (list of emails)

## Skill: analyze_pipeline
**Purpose:** Analyze pipeline health and funnel
**Input:** (none)
**Output:** analysis (markdown report)

## Skill: suggest_campaign
**Purpose:** Suggest next marketing campaign
**Input:** current_leads, goals
**Output:** campaign_recommendation
```

---

## VAULT MEMORY INTEGRATION

DeerFlow agents can read from vault memory:

```
GET http://localhost:3000/vault/read/memory/daily-brief.md
GET http://localhost:3000/vault/read/memory/dispatch-queue.md
GET http://localhost:3000/vault/read/logs/agent-activity.md
```

This enables:
- Agents see today's priorities
- Agents know what Claude is working on
- Agents avoid duplicate work
- Coordination across the crew

---

## SKILL VERSIONING & GIT

Skills are markdown files in vault, which is version-controlled:

```bash
cd /Users/shaunducker/Desktop/LandWise/Obsidian-Vault
git log -p agents/agent_crm-skills.md
# See skill changes over time
```

To update a skill:
1. Edit the .md file
2. Commit to git
3. DeerFlow reloads (if autoReload: true)
4. Next agent request uses updated skill

---

## TROUBLESHOOTING

### DeerFlow not finding skills
**Error:** "No skills found in vault"
**Solution:** Check skillsPath in config:
```bash
ls /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/*.md
```

### Skills not reloading after edit
**Error:** Agent uses old skill definition
**Solution:** Ensure autoReload: true in config, or restart DeerFlow

### MCP server slow to respond
**Error:** DeerFlow startup takes 10+ seconds
**Solution:** Increase timeout in config (default: 5s)
```json
{
  "vaultIntegration": {
    "timeout": 10
  }
}
```

---

## NEXT STEPS

1. **Find DeerFlow config** — Locate DeerFlow directory and config file
2. **Create skill files** — agent_[id]-skills.md for each agent
3. **Update DeerFlow config** — Point to vault agents/ folder
4. **Test skill loading** — Restart DeerFlow and check logs
5. **Test agent skills** — Call DeerFlow endpoint and verify skills work
6. **Phase 8+:** Initialize git, create startup sequence

---

## PRIMER.MD AWARENESS

DeerFlow agents should be aware of the session primer at startup:

**Path:** `/Users/shaunducker/Desktop/LandWise/primer.md`

`primer.md` is the **recall-stack layer 2** — rewritten at the end of every Claude Code session to capture:
- Active project phase and completion status
- Open blockers (DALL-E billing, Make.com, etc.)
- Exact next step for the next session
- System state table with current capabilities

**In DeerFlow agent startup, add:**
```python
async def startup(agent):
    # Read session primer for current project state
    try:
        with open("/Users/shaunducker/Desktop/LandWise/primer.md") as f:
            agent.context["session_primer"] = f.read()
    except FileNotFoundError:
        pass

    # Read vault status
    vault_status = await http.get("http://localhost:3000/vault/read/status.md")
    agent.context["vault_status"] = vault_status
    agent.context["today_priorities"] = await http.get(
        "http://localhost:3000/vault/read/memory/daily-brief.md"
    )
```

This ensures agents always know what phase of work is active and avoid duplicating completed work.

---

## SEE ALSO

- MCP Server: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/mcp_server.py
- Vault Skills Index: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/agents/README.md
- JARVIS Integration: /Users/shaunducker/Desktop/LandWise/Obsidian-Vault/system/integration.md
- Session Primer: /Users/shaunducker/Desktop/LandWise/primer.md
