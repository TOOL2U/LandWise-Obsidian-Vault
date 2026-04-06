# Workflow: Booking a Meeting

**Trigger:** A client requests a site visit or survey, OR Shaun says "book a meeting with [name]"
**Owner:** agent_admin (primary), agent_operations (for surveys)
**Tools required:** `read_calendar`, `book_meeting` (via JARVIS)

---

## Steps

### 1. Check Availability
```
Call: read_calendar (period: "week")
Purpose: See what's already on Shaun's calendar before proposing a slot
```
- Never propose a time without checking first
- Look for gaps of at least 2 hours for site visits (travel included)
- Avoid: early mornings (before 9am), late evenings (after 7pm), known survey days

### 2. Confirm Slot with Shaun

Say to Shaun (via Telegram or WhatsApp):
> "I've checked your calendar — you're free [day] at [time]. Want me to book that with [client name]?"

Wait for approval before proceeding.

### 3. Get Event Details

Confirm the following before calling `book_meeting`:
- **Title:** e.g. "Site visit — Denis Lantheaume, Thong Nai Pan plot"
- **Date & time:** confirmed by Shaun
- **Duration:** default 60 min (120 min for site surveys)
- **Location / description:** plot address, client phone number
- **Client name:** for the event title and description

### 4. Book the Meeting
```
Call: book_meeting
Input:
  title: "Site visit — [Client Name], [Plot Location]"
  date: "YYYY-MM-DD"
  time: "HH:MM"
  duration_minutes: 60
  description: "[Client name] | [Phone] | [Plot address] | [Package interest]"
```

### 5. Confirm Booking

After `book_meeting` succeeds:
- Tell Shaun: "Done — [event title] is in your calendar for [day] at [time]."
- The Obsidian plugin will create a vault note for the event within 10 minutes.
- If the client needs confirmation, draft a WhatsApp/email via agent_outreach (approval required).

---

## Decision Points

| Situation | Action |
|---|---|
| No suitable slot this week | Propose next week. Ask Shaun if he wants to suggest 2-3 options to client. |
| Client needs travel directions | Include in booking description; agent_outreach can send separately |
| Survey booking (not just call) | Involves agent_operations — check survey equipment availability too |
| Calendar API not configured | Inform Shaun: "Calendar isn't connected yet — go to Obsidian-Vault/memory/calendar.md manually or run calendar_auth.py" |

---

## Approval Gates

- ✅ **Step 2:** Shaun must confirm the proposed time slot before booking
- ✅ **Step 4:** Explicit "yes" or "go ahead" before calling `book_meeting`
- ✅ Any outbound confirmation to the client requires approval

---

## Success Criteria

- Event appears in Obsidian vault (memory/calendar.md) within 10 minutes of booking
- Shaun has confirmed the slot
- Client has been notified (if applicable)

---

## Related Workflows

- [[survey-scheduling.md]] — Full survey ops flow once meeting is booked
- [[approval-request.md]] — Standard approval pattern
- [[new-lead-intake.md]] — If this is the first meeting with a new lead

---

*Google Calendar is connected via Obsidian plugin + JARVIS Calendar API.*
*Events sync every 10 minutes to memory/calendar.md.*
