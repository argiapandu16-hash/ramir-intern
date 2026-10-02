# 04 — Ramir Pricing Case: Anchor + Benchmarks (Ramir vs Stripe vs Linear)

> Source for NotebookLM. Main case study. Comparative = best for mind map + quiz generation.

## Part A — Ramir Pricing Today (Your Anchor)

- **File:** `ramir-intern/ramir-consulting-light.html` + `ramir-landing-dark.html`
- **Buyer:** UMKM owner (omset Rp 50Jt–1M) deciding: book free consult vs leave. Must decide in 60 seconds.
- **Current state:** Hero + Cara Kerja + CTA with omset dropdown + WhatsApp CTA. No tier table, no price anchoring, no ROI proof.
- **What works:** Clear CTA, dark mode toggle with no FOUC, skip link, mobile nav, Inter + navy system.
- **Gaps (enterprise lens):**
  1. No tiers → user cannot self-select
  2. No recommendation → omset data not mapped to a tier
  3. No proof near CTA → no stats band, no case link
  4. Copy is generic in places → needs verbs + numbers + days

### Proposed Ramir Tiers (Draft for Approval)

| Tier | For whom | Promise | Proof needed |
|------|----------|---------|--------------|
| Starter Diagnostic (Rp 4.9Jt one-time) | <Rp 50Jt omset | Audit + quick wins in 7 days | 1 mini case |
| Growth Sprint (Rp 15Jt / 30 days) | Rp 50Jt–1M, MOST POPULAR | Audit + SOP + 90-day roadmap in 14 days | 2 cases + stat band |
| Enterprise Retainer (Custom) | >Rp 1M / multi-branch | Embedded ops + monthly review | Logo + compliance note |

Recommendation logic: omset dropdown auto-highlights tier. CTA per tier goes to WhatsApp with prefilled text including tier name.

## Part B — Benchmark 1: Stripe Pricing (Transparency Gold)

- **URL pattern:** stripe.com/pricing — single metric per product (e.g. 2.9% + 30¢), calculator, regional switcher.
- **What to steal:**
  1. One metric per tier, no hidden math
  2. FAQ that kills objections ( refunds, migration, support SLA )
  3. Code-like precision: numbers first, adjectives last
  4. Secondary CTA: "Talk to sales" vs "Start now" — matches buyer intent
- **Apply to Ramir:** Price + days + deliverables in every tier header. E.g. "Rp 15Jt — 14 hari — Audit + SOP + Roadmap". FAQ: "Bagaimana jika tidak cocok?", "Apakah data saya aman?", "Berapa lama sampai hasil?"

## Part C — Benchmark 2: Linear (Craft Gold)

- **Pattern:** linear.app — fast (<1s), keyboard-first, subtle motion, dark excellence, changelog as proof.
- **What to steal:**
  1. Spacing rhythm: 80/48/24, max-w-6xl, one idea per section
  2. Motion with purpose: hover lifts CTA 1px, no decorative parallax
  3. Dark mode is first-class, not inverted
  4. Performance as feature: instant page, no CLS
- **Apply to Ramir:** Compile Tailwind for prod (drop CDN), WebP hero, `font-display: swap`, reduce motion respect, 360px perfect before desktop polish.

## Part D — Comparative Table (NotebookLM Favorite)

| Dimension | Ramir today | Stripe | Linear | Ramir target (v2) |
|-----------|-------------|--------|--------|-------------------|
| Decision in 60s | No (no tiers) | Yes (calculator) | Yes (1 CTA) | Yes (quiz → tier) |
| Proof near price | No | Yes (logos + numbers) | Yes (changelog) | Stat band + 1 case/tier |
| Copy precision | Mixed | High | High | Verbs + days everywhere |
| Mobile 360px | Good | Excellent | Excellent | No h-scroll, big tap targets |
| A11y | Partial | Full | Full | Table semantics + errors |
| Performance | CDN (practice OK) | Compiled | Compiled | Compiled CSS, WebP |

## Part E — Before / After Copy Swaps

- Before: "Solusi terbaik untuk bisnis Anda" → After: "Audit operasional + roadmap 90 hari dalam 14 hari"
- Before: "Konsultasi Gratis" → After: "Dapatkan diagnosis gratis 30 menit + estimasi ROI" (keep short CTA label, expand helper)
- Before: omset dropdown dead-end → After: "Omset Rp 250Jt–1M → Growth Sprint paling cocok untuk Anda [Lihat paket]"

## FAQ for NotebookLM

**Q: Why is Stripe the pricing benchmark?**
A: It reduces pricing to one understandable metric and answers every objection within 2 scrolls.

**Q: Why is Linear the craft benchmark?**
A: It proves speed, spacing, and restraint convert better than decoration.

**Q: What is the one change that lifts Ramir most?**
A: Add 3 tiers with recommendation badge + stat band. No redesign required.
