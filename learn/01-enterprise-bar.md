# 01 — Enterprise Bar: What Separates Template vs Anthropic-Level Product

> Source for NotebookLM. Theme: craft bar for a Product Designer who prototypes in code.
> Pattern used throughout: Key Idea > Why It Matters > Example from Ramir.

## 1. The Enterprise Bar in 1 Paragraph

Enterprise bar = a user can decide in 60 seconds, trust in 10 seconds, and complete the task with zero confusion. Everything else (visual polish, motion, copy) serves those three outcomes. Templates look finished but fail decisions. Enterprise products make decisions easy.

## 2. The 8 Pillars

| # | Pillar | Template Trap | Enterprise Bar | How to Check in Code |
|---|--------|---------------|----------------|----------------------|
| 1 | Decision clarity | 3 vague tiers, no guidance | 1 recommended path + quiz / calculator | Can a first-time buyer pick in 60s without asking? |
| 2 | Trust signals | Generic testimonials | Named logos, numbers, case link, compliance | Is proof within 1 scroll of CTA? |
| 3 | Copy precision | "Best solution for your business" | Verbs + numbers: "Audit in 7 days, roadmap in 14" | Does every headline contain a verb or number? |
| 4 | Accessibility WCAG 2.2 AA | Low contrast, div-buttons | 4.5:1 contrast, real buttons, focus visible, skip link | Tab through page, can you complete CTA blind? |
| 5 | Performance budget | 5MB hero video | <200KB critical, lazy below fold, no layout shift | Lighthouse mobile >90, CLS <0.1 |
| 6 | Responsive + states | Desktop-only, happy path only | Mobile-first, loading / empty / error states | Resize to 360px, throttle to 3G, break the form |
| 7 | Error prevention | Silent fail | Inline validation, confirm step, undo | Submit empty form — is guidance instant? |
| 8 | Handoff discipline | Figma only | Tokens + copy + assets + acceptance criteria | Can an agent rebuild it without asking you? |

## 3. Key Idea Deep Dives

### 3.1 Decision Clarity > Visual Variety
- Key Idea: Pricing is a decision UI, not a price list. For consultative sales, the quiz + diagnostic IS the pricing UI.
- Why It Matters: UMKM owners compare consulting vs doing nothing. Enterprise leads compare vendor risk.
- Example from Ramir (REAL site ramirconsulting.com, Oct 2 2026): no public tiers. Decision UI = omset selector (4 bands) + problem selector (5 focuses) → Free 30-min Business & Financial Check via WhatsApp +62 852-8551-3366. Enterprise upgrade = keep diagnostic, add scope transparency per service (days + deliverables + outcome range, e.g. `Rekonstruksi 12 bulan + laporan SAK dalam 10 hari`).

### 3.2 Trust in 10 Seconds
- Key Idea: Trust = specificity.
- Why It Matters: "Trusted by many" converts at ~0%. `FMCG Surabaya: laporan laba rugi tiap tgl 5, buka 3 cabang baru` converts.
- Example from Ramir (REAL): stat band `100+ UMKM & Menengah / 10 Hari rata-rata / 94% akurasi SAK / 15-30% margin dicegah` + logos FishLog, Telkom Indonesia, Pertamina Patra Niaga, Bella Food, D'Burger + partners Mekari Jurnal & Qontak + I-CARE values. Gap = cases anonymized; upgrade = add scope+duration+outcome even when name hidden.

### 3.3 Copy Is Interface
- Key Idea: Every headline is a button label for the brain.
- Why It Matters: Vague copy forces the user to think. Precise copy lets them act.
- Before: "Solusi terbaik untuk bisnis Anda"
- After: "Dapatkan audit operasional + roadmap 90 hari dalam 14 hari"

### 3.4 Accessibility Is Enterprise Entry Ticket
- Checklist: contrast 4.5:1, focus-visible outline, real `<button>`/`<a>`, labels on all inputs, skip-to-content, `prefers-reduced-motion`, keyboard-only CTA completion.
- Ramir status: skip link OK, focus-visible OK, theme toggle OK. Missing: pricing table semantics (`<table>` or list with aria), form error association.

### 3.5 Performance Is Design
- Budget: HTML+CSS+JS critical <200KB, images WebP/AVIF, fonts display=swap, no render-blocking Tailwind CDN in prod (use compiled CSS).
- Current Ramir uses Tailwind CDN — fine for practice, must compile for prod.

## 4. Self-Review Checklist (Use Before Any Handoff)

- [ ] Can a stranger pick a tier in 60 seconds?
- [ ] Is there 1 recommended option?
- [ ] Is proof within 1 scroll of price?
- [ ] Does mobile 360px work without horizontal scroll?
- [ ] Can you Tab from header to CTA without getting lost?
- [ ] Does empty-submit give instant helpful error?
- [ ] Lighthouse mobile Performance >90, Accessibility >95?

## 5. FAQ for NotebookLM

**Q: What is the single biggest gap between template and enterprise?**
A: Decision support. Templates show options. Enterprise recommends one and proves why.

**Q: What is the fastest way to raise craft bar this week?**
A: Fix copy verbs + add 1 proof band + make mobile 360px perfect. No redesign needed.

**Q: How does this connect to agent work?**
A: Agents can only build to the bar you define. If acceptance criteria lists the 8 pillars, output jumps from template to enterprise automatically.
