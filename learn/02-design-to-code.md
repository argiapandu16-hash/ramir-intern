# 02 — Design to Code: Figma Tokens In, Production UI Out

> Source for NotebookLM. Theme: designer who prototypes in code + directs AI agents.

## 1. The Pipeline (5 Stages)

```
Figma / Tokens / Copy / Assets IN
  -> 1. Spec (designer approves)
  -> 2. ohmfront Build (React/Next.js or static HTML + Tailwind)
  -> 3. ohmarch Integrate (API, data, auth if needed)
  -> 4. ohmqa + ohmsec Check (TDD, Playwright, OWASP, a11y)
  -> 5. ohminfra Preview -> Prod (preview URL -> VPS Netcup Titan)
Designer approves at: spec, visual preview, copy/brand, pre-prod gate
```

## 2. What You Own vs What Agents Own

| Stage | You (Argi) Own | Agent Owns | Done Means |
|-------|----------------|------------|------------|
| Spec | User story, tokens, copy final, acceptance criteria | Drafts spec from your brief | You say "approved" in writing |
| Build | Visual direction, 1 screen anchor | Component code, responsive, dark mode | Preview URL matches Figma within 95% |
| Integrate | Data shape approval (e.g. Ramir Free Check fields: Nama, Perusahaan, WA, Omset 4 bands, Fokus 5 problems) | API wiring, form handling, WA prefill per service | Real data flows, no mock left |
| Test | UX edge approval | Unit + E2E + a11y audit | All checks green, video proof |
| Deploy | Go / no-go | Pipeline, rollback plan | Live URL + rollback command known |

## 3. Input Contract (What Agents Need From You)

To get zero-question builds, always give:
1. **Tokens:** colors (hex), type scale, spacing, radius. Example: `navy #022135, radius 12, Inter 400/600/800`
2. **Copy final:** headlines + CTA + helper + error strings. No lorem.
3. **Assets:** logo SVG, hero WebP, icons. With 1x/2x or SVG.
4. **Acceptance:** "Mobile 360px no scroll, Tab reaches CTA, submit empty shows inline error, Lighthouse >90"

Copy-paste brief starter:
> Build [screen] from [Figma link]. Tokens: [list]. Copy doc: [link]. Must pass: [4 criteria]. Output: preview URL + file list + test proof.

## 4. Static vs Next.js Decision

| Case | Use | Why |
|------|-----|-----|
| Ramir landing today | Static HTML + Tailwind compiled | Fast, cheap, easy preview |
| Ramir LMS / Academi-Z later | Next.js + TypeScript + Tailwind | Auth, routing, data, scale |
| Rule | If no login/data, stay static | Don't pay framework cost early |

## 5. Dark Mode + Responsive Recipe (Your Current Stack)

- `darkMode: 'class'`, pre-paint script from localStorage to avoid FOUC (you already have this — keep it)
- Mobile-first: base = 360px, then `md:` and `lg:` up
- Focus-visible: 2px outline offset 3px, sky color in dark
- Reduced motion: disable animation when `prefers-reduced-motion`

## 6. FAQ for NotebookLM

**Q: What makes a designer "prototype in code" vs "hand off Figma"?**
A: You can open the HTML, change tokens/copy, and approve a preview URL — not just comment on screenshots.

**Q: What is the most common handoff failure?**
A: Missing acceptance criteria. Without it agents guess, you redo.

**Q: When should backend get involved?**
A: Only when real data/auth is needed. Landing with WhatsApp CTA needs no backend.
