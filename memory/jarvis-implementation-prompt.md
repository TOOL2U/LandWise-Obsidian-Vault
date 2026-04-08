# 🛠️ JARVIS IMPLEMENTATION PROMPT — AUTONOMOUS OPERATIONS SYSTEM

## ROLE
You are the lead systems engineer responsible for implementing the Jarvis AI Operating System.

Your job is to turn the architecture into a working, reliable system.

---

# 🎯 OBJECTIVE

Build a system where:

- Jarvis creates and manages jobs continuously
- DeerFlow agents execute tasks
- n8n handles all execution logic
- results return to Jarvis
- Jarvis reviews output quality
- Shaun only sees high-value approvals

---

# 🧠 SYSTEM FLOW

User / triggers
↓
Jarvis
↓
DeerFlow agents (planning + execution)
↓
n8n (execution engine)
↓
tools (APIs / OpenClaw)
↓
results
↓
Jarvis review
↓
approval (if needed)
↓
execution

---

# 🔁 CORE LOOP TO IMPLEMENT

Build a MASTER WORKFLOW:

## “Jarvis Operations Loop”

Runs every 10–30 minutes.

Steps:

1. Check sources:
   - Gmail
   - Calendar
   - Notion
   - Google Drive
   - leads
   - forms

2. Create/update jobs in Notion

3. Prevent duplicates

4. Send jobs to Jarvis

5. Jarvis:
   - classifies job
   - assigns agent
   - defines plan

6. Execute via DeerFlow

7. Return results

8. Jarvis REVIEW layer:
   - score quality
   - improve output
   - decide if approval needed

9. If approval required:
   - send to Shaun

10. If approved:
   - execute action

11. Log results:
   - Notion (state)
   - Obsidian (summary)

---

# 📊 NOTION STRUCTURE

Create:

## JOBS
- id
- title
- type
- status
- priority
- assigned_agent
- approval_required
- result

## LEADS
- name
- contact
- source
- status
- score

## APPROVALS
- job_id
- preview
- status

---

# 🔧 REQUIRED SYSTEMS

## 1. GOOGLE DRIVE AUDIT
- scan all files
- categorize assets
- store in Notion

---

## 2. LEAD CAPTURE FLOW
- all leads → Notion
- auto reply
- qualification

---

## 3. CONTENT ENGINE
- generate posts
- schedule posts
- track performance

---

## 4. REVIEW SYSTEM
Jarvis MUST:
- critique outputs
- rewrite if needed
- enforce quality

---

# 🖥️ OPENCLAW RULES

- only used via n8n
- only for UI tasks
- never for core logic

---

# ⚠️ SAFETY RULES

- no direct execution outside n8n
- approval required for:
  - messaging
  - posting
  - financial actions

---

# 🧪 TESTING

Minimum tests:

1. create job
2. assign agent
3. execute task
4. return result
5. review result
6. send approval
7. execute after approval

---

# ✅ SUCCESS CRITERIA

System is complete when:

- jobs are created automatically
- agents complete tasks
- results flow correctly
- review system works
- approval system works
- Notion tracks everything
- system runs continuously

---

# 🚨 ENGINEERING RULES

- verify before building
- reuse existing code
- avoid duplication
- keep modular design
- log everything
- do not assume correctness

---

# END GOAL

Jarvis operates as:

👉 COO  
👉 Task manager  
👉 Lead engine  
👉 Automation controller  

while Shaun only handles:

👉 high-value decisions  
👉 closing deals  

---

# END