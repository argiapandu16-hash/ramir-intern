---
name: incident-commander
description: >-
  Incident Commander Framework — full lifecycle dari detection sampai
  resolution + post-incident. Kemampuan: (1) Severity classification (SEV-1
  to SEV-4), (2) Incident Commander role & responsibility, (3) War room
  protocol (who, where, what), (4) Communication cascade (internal, customer,
  status page, external), (5) Resolution coordination (parallel workstream:
  fix, comms, investigation), (6) Stand-down criteria, (7) Post-incident
  review handoff. Pakai saat: "incident", "outage", "down", "broken
  production", "customer impact", "war room", "page on-call", "SEV1", "status
  page", "incident commander", "IC".
metadata:
  owner: alpha
  tier: critical
---

# INCIDENT COMMANDER — Active Incident Management
**Owner**: Alpha | **Tier**: 🔴 Critical

Incident saat real-time = chaos. Incident commander brings structure: clear severity, clear roles, clear comms, clear stand-down. Tanpa IC: 10 orang bicara, nothing decided.

## Severity Levels

```
SEV-1 CRITICAL
- Customer-facing outage atau data loss
- Revenue impact > $10K/jam OR safety risk
- All-hands response, executive notification
- Status page UPDATE required dalam 15 min
- Page on-call immediately

SEV-2 MAJOR
- Significant degradation (>20% users affected)
- Workaround exists tapi painful
- War room within 30 min
- Status page update within 30 min
- Page on-call dalam 15 min

SEV-3 MINOR
- Limited impact (<5% users)
- Acceptable workaround
- No war room — ticket queue
- Status page optional
- Address within 24 hour

SEV-4 LOW
- Cosmetic, no functional impact
- Backlog, address in regular sprint
- No paging needed
```

## Incident Commander Role

```
IC adalah ORCHESTRATOR — bukan technical fixer.

IC RESPONSIBILITIES:
- Declare severity level
- Run the war room (not silent observer)
- Coordinate parallel workstream (tech fix + comms + investigation)
- Make decision on rollback/escalate
- Update stakeholders (internal + external)
- Decide stand-down criteria
- Hand off to post-mortem

IC DOES NOT:
- Personally fix the technical issue (let SME do that)
- Get into deep technical debate (refocus to action)
- Make code changes
- Communicate externally without aligned messaging

Who can be IC?
- Senior engineer atau engineering manager
- Pre-designated on-call rotation
- IC role can rotate untuk long incident (>4 hours)
- Junior IC for SEV-3/4 to build skill
```

## War Room Protocol

```
WHO (mandatory):
- Incident Commander (1)
- Technical SMEs (engineer yang fix)
- Customer Success representative (untuk impact monitoring)
- Comms lead (internal & external messaging)

WHO (optional based on severity):
- Engineering Manager (SEV-1/2)
- VP Engineering (SEV-1)
- CEO (SEV-1 dengan revenue/reputation impact)
- Legal (kalau data breach atau regulated industry)
- PR (kalau public-facing)

WHERE:
- Dedicated Slack channel (#incident-YYYY-MM-DD-shortname)
- Voice/video bridge (Zoom room atau Slack huddle)
- Status page dashboard visible

WHAT:
- IC declares: "Incident XYZ declared SEV-X at HH:MM"
- Pinned message: current status + next update time
- Threaded discussion (avoid main channel noise)
- Decision log (IC tracks key decision dengan timestamp)
```

## Communication Cascade

```
T+0 (incident detected)
- Page on-call engineer
- IC assigned

T+15 min (SEV-1) atau T+30 min (SEV-2)
- War room assembled
- Initial assessment dari SME
- Severity classification confirmed
- Internal notification (Slack #engineering)
- Status page initial update: "investigating"

T+30 min
- Customer Success briefed on impact
- Internal status update (every 30 min for SEV-1, hourly for SEV-2)

T+1 hour (kalau belum resolved)
- Executive notification (SEV-1)
- Status page update: "identified issue, working on fix"
- Customer email kalau impact significant

T+resolution
- Final status page update: "resolved"
- Customer notification dengan brief explanation
- Internal all-hands brief (kalau SEV-1)
- Schedule post-mortem within 48 hour
```

## Parallel Workstream Coordination

```
IC coordinate 3 parallel tracks (don't sequence them):

TRACK 1: TECHNICAL FIX
- Lead: Engineering SME
- Goal: restore service
- Update IC every 15 min

TRACK 2: CUSTOMER IMPACT
- Lead: CS representative
- Goal: monitor affected customers, prep messaging
- Update IC every 30 min

TRACK 3: INVESTIGATION
- Lead: Senior engineer (different dari fix lead)
- Goal: understand root cause untuk post-mortem
- Don't block fix — parallel investigation
- Capture logs, metrics, evidence

IC ensures track stay parallel. Common mistake:
- IC over-focus pada Technical, kehilangan Customer Impact track
- Investigation deferred → kehilangan evidence saat post-mortem
```

## Stand-Down Criteria

```
Before declaring incident resolved, verify ALL:
- [ ] Functional health check passed (service responding)
- [ ] User-facing test passed (real workflow)
- [ ] No error spike in last 15 min vs baseline
- [ ] Affected customers acknowledged restoration
- [ ] No regression introduced by fix
- [ ] Monitoring confirms green dashboard
- [ ] Status page updated to "resolved"
- [ ] Communication closure sent

STAND-DOWN MESSAGE format:
"Incident XYZ resolved at HH:MM. Total duration: X hours.
Root cause: [brief]. Detailed post-mortem to follow within 48h.
Thanks to [team] for response."
```

## Post-Incident Handoff

```
Within 24 hours:
- Schedule post-mortem meeting (target 48 hours after resolution)
- Assign post-mortem facilitator (often the IC)
- Gather artifacts:
  - Timeline log (dari Slack channel + decision log)
  - Metrics snapshot (before/during/after)
  - Customer impact data (CS report)
  - System logs preserved
  
Within 1 week:
- Run post-mortem (using /post-mortem skill)
- Publish post-mortem doc
- Action items assigned dengan due date
- Share lessons cross-team
```

## Output — Incident Log

```
## INCIDENT REPORT — [Short title]
Date: [date]
Severity: SEV-X
IC: [name]
Duration: HH:MM (HH:MM-HH:MM)

### IMPACT
- Customers affected: X (or %)
- Revenue impact: $Y (kalau quantifiable)
- Services affected: [list]
- SLA breach: [yes/no, kalau yes berapa]

### TIMELINE (key decision points)
- T+0 (HH:MM): Incident detected via [source]
- T+5: SEV-X declared
- T+15: War room assembled, [people] in
- T+30: Root cause hypothesis: [...]
- T+45: Fix identified: [...]
- T+60: Fix deployed
- T+65: Verification: [...]
- T+75: Stand-down

### RESOLUTION
[Brief: what fixed it]

### CUSTOMER COMMUNICATION
- Status page: [link]
- Email sent: [time, recipient count]
- Public comm: [Twitter, blog kalau ada]

### FOLLOW-UP
- Post-mortem scheduled: [date]
- Lead: [facilitator]
- Action item review: [date]
```

## Anti-Pattern

```
❌ No IC declared → 5 orang bicara, nothing decided
❌ IC trying to fix → kehilangan oversight
❌ Skip status page update → customer in dark, support overwhelmed
❌ "Hopeful resolution" tanpa verification → re-open incident
❌ Long debate di war room tentang root cause → fix first, investigate second
❌ Skip post-mortem karena "we know what happened" → no system improvement
❌ Page everyone instead of on-call → diluted ownership
```

## Koordinasi

- **Runbook-generator**: incident runbook (per common scenario)
- **Post-mortem**: setiap SEV-1/2 trigger mandatory post-mortem
- **Release-manager**: incident karena deploy → rollback coordination
- **Crisis-comms**: kalau incident jadi public, hand off external comms
