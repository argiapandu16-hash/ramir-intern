# 05 — Decision Log: Oct 1–2, 2026 (Story for Your Deck)

> Source for NotebookLM timeline + slide narrative. Facts only, no secrets.

## Timeline

| Date | Decision | Why | Outcome |
|------|----------|-----|---------|
| Oct 1 | Practice Ramir landing rebuild (light + dark) | Learn Pricing/CTA/FAQ + dark toggle without FOUC | `ramir-consulting-light.html` (329 lines), `ramir-landing-dark.html` live locally |
| Oct 1 | Adopt House BAH: OhmDev + 5 agents | Need lead model for enterprise work | Roles defined, gates defined |
| Oct 1 | GitHub SSH via `~/.ssh/id_ed25519` (600) | Safe auth without token in repo | `Hi argiapandu16-hash` auth OK |
| Oct 1 | Supabase leak review (UpGuard Sep 25 2026, 16,326 DBs) | Learn RLS lesson before backend | Checklist: RLS on, no anon-key misuse, no service key in frontend |
| Oct 1 | Split `bah-agent` from `ramir-intern` | Keep shared agent clean, personal work separate | `bah-agent` commit `1631993`, 30 skills, pushed to personal + org |
| Oct 2 | Push `bah-agent` to `Tim-tech-Ramir-2026/bah-agent` | Mentor invite to org | `org/main` = `1631993`, diff origin vs org = 0, personal repo kept |
| Oct 2 | Enterprise NotebookLM package | Turn work into learnable sources | `learn/` 7 files (this set) |
| Oct 2 | Re-anchor case study to REAL ramirconsulting.com | Trial pricing table too thin; real diagnostic funnel + 7 services + 3 products more rigorous | `04` rewritten from 6 live pages, `01/05/99` updated, pushed as `learn/` v2 |

## Remotes (Public Info Only)

- Personal practice: `git@github.com:argiapandu16-hash/ramir-intern.git` (main + agent-only)
- Shared agent personal: `git@github.com:argiapandu16-hash/bah-agent.git` (main `1631993`)
- Org shared agent: `git@github.com:Tim-tech-Ramir-2026/bah-agent.git` (main `1631993`)
- Local clean agent: `~/bah-agent/`, work: `~/workspace/`

## Competitor Notes (For Deck Context)

- Szeto Consultants: corporate trust via client logos + process depth
- BizBlueprint: education-led, templates + playbooks
- Konsulbisnis: local SMB proximity, WhatsApp-first
- Ramir edge (REAL, verified Oct 2 2026): diagnostic speed (10-day avg reconstruction, 94% SAK accuracy) + WhatsApp concierge with per-service prefill + tooling proof (KURVA OS, SERAFIRA, INSIDERA, Supernova ERP option) + I-CARE values + Mekari Jurnal & Qontak partnership

## Real-Site Sources (Fetched Oct 2 2026, Public Pages Only)

- Homepage: https://ramirconsulting.com/ (hero, 4 solutions, stages, stats 100+/10d/94%/15-30%, clients, partners, testimonials, Free Check form)
- Financial: https://ramirconsulting.com/consulting-service/financial-accounting/ (KURVA, 4 scopes, 4-step method)
- ERP: https://ramirconsulting.com/consulting-service/erp-solutions/ (KURVA + Supernova option, multi-branch dashboard)
- Market: https://ramirconsulting.com/consulting-service/market-intelligence/ (INSIDERA + SERAFIRA, lead/CRM/sales)
- AI: https://ramirconsulting.com/consulting-service/ai-techstack/ (BAH Assistant, Auto Finance, SERA Portal, human-review rule)
- About: https://ramirconsulting.com/about/ (I-CARE, 100+, 99.9%, 6 industries)

## Slide Narrative (Use in Deck)

1. Problem: template landing cannot help a buyer decide
2. Bar: 8 pillars of enterprise (file 01)
3. System: design-to-code pipeline (file 02)
4. Proof: Ramir vs Stripe vs Linear (file 04)
5. Method: how Argi directs agents (file 03)
6. Terms: visual glossary fluency (file 99)
7. Next: Pricing v2 + compiled prod + case metrics

## FAQ for NotebookLM

**Q: Why split bah-agent from ramir-intern?**
A: Shared agent must stay clean and reusable. Personal practice must stay free to experiment.

**Q: What proves the org push succeeded?**
A: Same SHA on origin and org, zero diff, empty org repo filled with 1 branch main.

**Q: What is the next measurable win?**
A: Pricing v2 with 3 tiers + stat band + Lighthouse >90.
