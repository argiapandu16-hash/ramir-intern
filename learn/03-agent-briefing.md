# 03 — Agent Briefing: How to Direct AI Agents Like a Lead

> Source for NotebookLM. Theme: orchestration skill. House BAH: OhmDev + ohmarch, ohmfront, ohminfra, ohmqa, ohmsec.

## 1. The Lead Model

You are not a prompt writer. You are a lead with 5 reports:
- ohmarch: system, API, data, RAG/MCP
- ohmfront: UI, Tailwind, a11y, visual fidelity
- ohminfra: preview/deploy, Docker, VPS, rollback
- ohmqa: tests, E2E, quality gate (veto power)
- ohmsec: OWASP, secrets, privacy (veto power)

OhmDev orchestrates. QA and Sec can block a deploy even if build is done.

## 2. The Brief Formula (R-C-C-A-V)

- **Role:** which agent + what expert lens
- **Context:** links, tokens, constraints (no secrets in repo, mobile-first)
- **Constraints:** what NOT to do (don't change copy, don't add deps)
- **Acceptance:** 3-5 checkable outcomes
- **Verification:** what proof to return (preview URL, test log, diff)

## 3. Three Copy-Paste Templates

### Template A — Build (ohmfront)
> Role: ohmfront senior frontend. Context: Build Ramir Pricing from Figma [link], tokens [list]. Constraints: static HTML + compiled Tailwind, no new deps, keep dark mode. Acceptance: (1) matches Figma 95%, (2) 360px no h-scroll, (3) Tab to CTA works, (4) Lighthouse a11y >95. Verification: return file list + preview steps + screenshots.

### Template B — Polish (ohmqa + ohmfront)
> Role: ohmqa gate + ohmfront fix. Context: Polish [file] for enterprise bar checklist in 01. Constraints: don't change copy. Acceptance: contrast 4.5:1, focus visible, empty-submit error, CLS <0.1. Verification: before/after diff + Lighthouse scores.

### Template C — Handoff (ohminfra + ohmsec)
> Role: ohminfra deploy + ohmsec scan. Context: Deploy [folder] to preview. Constraints: no secrets in repo, no prod without approval. Acceptance: preview URL live, secret scan clean, rollback known. Verification: URL + scan log + rollback command.

## 4. Gates You Must Enforce (Non-Negotiable)

1. Spec approval — you approve in writing before build
2. No prod deploy without your go — preview first
3. No real data migration without backup + rollback
4. No secrets/credentials in repo or chat — use env + vault
5. Big architecture choice — needs trade-off note (build vs buy, cost, risk)

## 5. Anti-Patterns

| Anti-pattern | What happens | Fix |
|--------------|--------------|-----|
| Vague brief ("make it nice") | 3 rewrites | Use R-C-C-A-V |
| No acceptance | Endless polish | 3-5 checks max |
| Skipping QA/Sec | Bug in demo | QA+Sec veto by default |
| Chat-only approval | Lost decisions | Write to decision-log |

## 6. FAQ for NotebookLM

**Q: How is directing agents different from prompting?**
A: Prompting asks for output. Directing sets bar, constraints, and verification — like managing humans.

**Q: Who can block a deploy?**
A: ohmqa and ohmsec. Even OhmDev cannot override a veto without your explicit risk acceptance.

**Q: What is the smallest great brief?**
A: 5 lines: role, link, don't-do, 3 checks, proof required.
