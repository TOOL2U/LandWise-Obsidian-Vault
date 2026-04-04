# Memory Sync Schedule

JARVIS automatically syncs vault memory files on this schedule (local machine time):

---

## Hourly Sync (Every Hour at :00)

**Time:** Every hour at :00 minutes (e.g., 9:00, 10:00, 11:00, etc.)

**Actions:**
1. Read memory/daily-brief.md
2. Check memory/dispatch-queue.md for active/blocked tasks
3. Append activity log to logs/jarvis-activity.md
4. Check for manual notes from Shaun in memory/
5. Sync lead status from CRM to daily-brief.md

**Logged to:** logs/jarvis-hourly-sync.md

---

## Daily Sync (Every Day at 8:00 AM)

**Time:** 08:00 AM local time (e.g., 08:00 Bangkok time)

**Actions:**
1. Generate daily-brief.md for the day
2. Check completed tasks from yesterday
3. Archive completed tasks to memory/completed-tasks.md
4. Reset daily-brief priorities
5. Check for blockers from yesterday

**Logged to:** logs/jarvis-daily-sync.md

---

## Weekly Sync (Every Monday at 9:00 AM)

**Time:** 09:00 AM local time, Monday

**Actions:**
1. Generate week report with KPIs
2. Check pipeline progress (quotas, conversions)
3. Update BACKLOG.md with status
4. Check agent performance
5. Escalate blockers to Shaun via WhatsApp

**Logged to:** logs/jarvis-weekly-sync.md

---

## Implementation

Currently, these are MANUAL. To automate, use one of:

**Option 1: JARVIS Scheduler**
Add to JARVIS bridge main.py:
```python
import schedule
import time

def hourly_sync():
    # Read vault files and sync
    pass

schedule.every().hour.at(":00").do(hourly_sync)
```

**Option 2: Cron + Python Script**
```bash
# Run hourly_sync.py every hour
0 * * * * /usr/bin/python3 /Users/shaunducker/Desktop/LandWise/hourly_sync.py
```

**Option 3: Background Task Service**
Use FastAPI BackgroundTasks or APScheduler.

---

## Current Status

- [x] Schedule defined
- [ ] JARVIS scheduler implemented
- [ ] Cron job created

See [[../logs/jarvis-activity.md]] for sync logs.
