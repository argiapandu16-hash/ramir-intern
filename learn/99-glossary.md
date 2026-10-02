# 99 — Visual Glossary: 30 Terms (Definition + Ramir Example + Visual Cue)

> Source for NotebookLM Mind Map + Quiz. Format: Term — 1-line def. Example. Visual cue.

## Design / Frontend (1–10)

1. **Design token** — Named value for color/type/space. Example: `navy #022135`. Visual: color swatch card.
2. **Type scale** — Stepped font sizes with roles. Example: H1 36/44, body 15/24. Visual: scale ladder.
3. **Spacing rhythm** — 8pt grid (8/16/24/48/80). Example: section 80, card 24. Visual: grid overlay.
4. **Responsive breakpoint** — Layout switch point. Example: `md: 768, lg: 1024`. Visual: 360/768/1280 frames.
5. **Dark mode** — Alternate theme via class. Example: `dark:bg-navydeep`. Visual: light/dark split.
6. **Focus-visible** — Keyboard focus ring. Example: 2px outline offset 3px. Visual: Tab ring on CTA.
7. **Contrast ratio** — Text vs bg luminance. Example: 4.5:1 for body. Visual: contrast checker.
8. **CLS (Cumulative Layout Shift)** — Visual jump score. Example: <0.1. Visual: before/after filmstrip.
9. **CTA** — Primary action. Example: Konsultasi Gratis → WhatsApp. Visual: pill button.
10. **Wireframe → Prototype** — Low-fi to clickable. Example: Pricing list → HTML. Visual: gray boxes → real UI.

## Backend / Data / AI (11–20)

11. **API** — Contract for data exchange. Example: form POST → WhatsApp link. Visual: plug diagram.
12. **Auth** — Prove who you are. Example: future LMS login. Visual: lock + key.
13. **RLS (Row Level Security)** — DB rule per user. Example: Supabase lesson — missing RLS exposed 16k DBs. Visual: table with lock rows.
14. **Migration** — Move data/schema safely. Example: bah-agent split. Visual: boxes moving with rollback arrow.
15. **RAG** — Retrieve + generate with docs. Example: NotebookLM over learn/. Visual: docs → answer with citations.
16. **MCP Server** — Tool port for agents. Example: expose Figma tokens to agent. Visual: USB hub for AI.
17. **Agent orchestration** — Lead directs 5 agents. Example: OhmDev splits build/test/deploy. Visual: conductor + players.
18. **Prompt vs Brief** — Ask vs lead with bar + proof. Example: file 03 templates. Visual: one-liner vs checklist.
19. **Eval / Harness** — Score AI output. Example: Lighthouse + a11y as eval. Visual: scorecard.
20. **Vector DB** — Search by meaning. Example: future glossary search. Visual: dots clustered by topic.

## Delivery / Quality (21–30)

21. **TDD (Red-Green-Refactor)** — Fail test → pass → clean. Example: empty-submit error test first. Visual: red→green badges.
22. **E2E (Playwright)** — Test like a user. Example: book consult flow. Visual: browser robot clicking.
23. **Contract test** — API promise check. Example: form payload shape. Visual: handshake doc.
24. **OWASP Top 10** — Common web risks. Example: injection, broken access. Visual: shield list.
25. **Secret scan** — Find leaked keys. Example: pre-push grep for `ghp_`, `AKIA`. Visual: metal detector.
26. **Preview deploy** — Temporary live URL. Example: Netlify/Vercel preview of Pricing v2. Visual: draft link icon.
27. **Prod deploy (VPS Netcup Titan)** — Live for users. Example: needs Argi go + rollback. Visual: rocket + parachute.
28. **Rollback** — Undo to last good. Example: `git revert` + redeploy. Visual: rewind button.
29. **SLO / Error budget** — Allowed downtime. Example: 99.9% = 43m/mo. Visual: fuel gauge.
30. **Post-mortem (blameless)** — Learn without blame. Example: 5 Whys on missed CTA. Visual: timeline + lessons.

## Quiz Starters for NotebookLM

- Which 3 terms prove enterprise trust fastest? (contrast, proof, SLO)
- Explain RLS using the Supabase lesson in 1 sentence.
- Draw the design-to-code pipeline from memory with 5 stages.
