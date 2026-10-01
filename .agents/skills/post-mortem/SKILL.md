---
name: post-mortem
description: >-
  Post-Mortem Framework — honest retrospective dari decision atau incident.
  Kemampuan: (1) Blameless culture pattern (focus pada system, bukan person),
  (2) 5-Whys root cause analysis, (3) Timeline reconstruction (apa yang
  terjadi kapan), (4) Decision quality scoring (separate dari outcome
  quality), (5) Lesson extraction (apa yang reusable cross-context), (6)
  Action item dengan accountability, (7) Knowledge base contribution. Pakai
  saat: "post-mortem", "postmortem", "retrospective", "lessons learned",
  "incident review", "kenapa kita gagal", "apa yang dipelajari", "root cause",
  "5 whys", "blameless".
metadata:
  owner: alpha
  tier: standard
---

# POST-MORTEM — Honest Retrospective
**Owner**: Alpha | **Tier**: 🟡 Standard

Post-mortem yang work bukan tentang menyalahkan. Tentang extract pelajaran sistemik supaya kesalahan yang sama tidak terulang. Blameless ≠ accountability-less.

## Prinsip Blameless Culture

```
✅ Focus pada SYSTEM yang allow kesalahan
✅ Asumsi: orang made best decision dengan info tersedia saat itu
✅ Goal: improve process, dokumentasi, training, automation
✅ Outcome: lessons untuk org, bukan punishment

❌ Bukan: orang yang salah, lain kali hati-hati
❌ Bukan: blame yang nyata di-cover ("system" sebagai excuse)
❌ Bukan: avoid hard conversation tentang competence atau judgment
```

## Pisahkan Decision Quality dari Outcome Quality

```
Same as /decide skill — but applied post-event:

Good Decision + Bad Outcome = Bad luck (jangan ubah process based on this)
Bad Decision + Good Outcome = Lucky (jangan reinforce bad process)
Good Decision + Good Outcome = Skill (replicate)
Bad Decision + Bad Outcome = Lesson (system improvement)

Most post-mortem mistakes: confuse outcome dengan decision.
"Kita gagal — pasti decision salah" — wrong, sometimes good decision unlucky.
"Kita berhasil — decision pasti benar" — wrong, sometimes bad decision lucky.
```

## Workflow Post-Mortem (60-90 min)

### Step 1 — Timeline Reconstruction (15 min)
```
What happened, chronologically:

T-0    : [Trigger event]
T+5min : [First action]
T+15min: [Decision X made by Y]
T+30min: [Outcome of decision]
...
T+resolution: [End state]

Use timestamp, names, decisions, actions, observations.
Tidak ada interpretasi yet — pure factual.
```

### Step 2 — Root Cause Analysis (5-Whys) (20 min)
```
For each significant issue:

"Why did X happen?"
→ Because Y
"Why did Y happen?"
→ Because Z
"Why did Z happen?"
→ Because W
"Why did W happen?"
→ Because V
"Why did V happen?"
→ Root cause

5-Whys digs past symptom ke system-level cause.
Stop kalau mencapai:
- Process gap (no SOP)
- Training gap (skill missing)
- Tool gap (manual error-prone)
- Visibility gap (didn't know in time)
- Cultural gap (didn't escalate)
```

### Step 3 — Contributing Factors (15 min)
```
Beyond root cause, list factors yang amplify atau enable:

ORGANIZATIONAL
- Unclear ownership
- Conflicting priorities
- Insufficient resource
- Skip review process

TECHNICAL
- Missing monitoring
- Lack of automation
- Tool limitation
- Tech debt

PEOPLE
- Knowledge silo (1 person know all)
- New team member tanpa onboarding
- Burnout / fatigue
- Communication breakdown

EXTERNAL
- Vendor issue
- Customer surprise
- Market change
- Regulatory change

Mostly insiden besar = combination dari 3-5 factor, bukan single cause.
```

### Step 4 — Decision Quality Scoring (10 min)
```
For each key decision di timeline:

| Decision | Info available | Reasoning | Decision quality | Outcome |
|----------|----------------|-----------|-----------------|---------|
| Decision X | Limited (knew A, B) | Sound given info | Good | Bad (unlucky) |
| Decision Y | Full visibility | Skipped reviewing data | Poor | Bad |

This distinguishes "we made the right call but unlucky" dari "we made wrong call".
```

### Step 5 — Lesson Extraction (15 min)
```
3 tipe lesson:

REPLICABLE (apa yang work, do more):
- "Communication channel #incident very effective — formalize use"
- "On-call rotation prevented burnout"

AVOIDABLE (apa yang fail, don't repeat):
- "Skipped pre-deploy check → root cause of issue. Make mandatory."
- "Single point of failure di senior engineer → cross-train"

SURPRISING (apa yang unexpected, investigate further):
- "Customer impact lebih besar dari estimated — recalibrate severity"
- "Vendor responsiveness lebih lambat dari SLA — re-evaluate vendor"
```

### Step 6 — Action Items (15 min)
```
SMART action items:
- Specific (apa yang akan dilakukan)
- Measurable (bagaimana tahu done)
- Assignable (single owner)
- Realistic (dengan resource available)
- Time-bound (deadline)

Format:
| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Add pre-deploy check ke checklist | DevOps Lead | June 15 | TODO |
| Cross-train Junior on payment system | Senior Eng | June 30 | TODO |

Max 5 action items. More than that = nobody will do, lost.
```

### Step 7 — Knowledge Base Contribution
```
Add ke org knowledge base:
- Runbook update (kalau incident, update incident runbook)
- SOP update (kalau process gap, update SOP)
- Anti-pattern documentation (kalau system design issue)
- Onboarding update (kalau new joiner akan benefit)

Buat post-mortem easily searchable. Future engineer harus bisa find ini saat search "kenapa system X fail di Q2 2026".
```

## Output — Post-Mortem Template

```
## POST-MORTEM — [Incident/Decision Title]
Date: [date] | Severity: [SEV-1/2/3]
Facilitator: [name] | Participants: [list]

### TL;DR
[2-3 sentence: what happened, impact, primary lesson]

### IMPACT
- Customer: [number affected, duration, business impact]
- Revenue: $[X] (kalau quantifiable)
- Reputation: [public visibility, social media, press]
- Team: [overtime, morale impact]

### TIMELINE
[Chronological factual]

### ROOT CAUSE
[Result of 5-Whys analysis — system-level, not person]

### CONTRIBUTING FACTORS
- Organizational: ...
- Technical: ...
- People: ...
- External: ...

### DECISION QUALITY ASSESSMENT
[Per key decision: was decision sound given info available]

### WHAT WENT WELL
[Positive observations to replicate]

### WHAT WENT POORLY
[Honest assessment of failure modes]

### ACTION ITEMS
[SMART format, max 5]

### KNOWLEDGE BASE UPDATES
- Updated runbook X
- New SOP for Y
- Anti-pattern documented in Z
```

## Anti-Pattern

```
❌ Blame individual ("X should have known better") → defensive culture
❌ Skip 5-Whys (stop at first cause) → fix symptom not root
❌ Action item terlalu banyak (>5) → nothing done
❌ Tidak share post-mortem cross-team → only this team learns
❌ Skip post-mortem karena "not worth it" → repeat same incident
❌ Post-mortem yang tidak honest (cover untuk hide poor decision) → no learning
❌ Conflate decision quality dengan outcome → wrong lesson extracted
```

## Koordinasi

- **Incident-commander**: incident → trigger post-mortem within 48 hours
- **Decide**: bad decision outcome → post-mortem decision quality
- **Sprint-health**: pattern across sprint = post-mortem candidate
- **Runbook-generator**: lesson → update runbook
- **Process-mapper**: lesson → update SOP
