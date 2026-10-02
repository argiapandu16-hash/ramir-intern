# 10 — NotebookLM Playbook: Upload Once, Get Deck + Map + Podcast

> Read this after uploading the other 6 files to NotebookLM (notebooklm.google.com → New Notebook → Upload all MDs).

## 1. Upload Checklist

Upload these 6 as sources:
- [ ] 01-enterprise-bar.md
- [ ] 02-design-to-code.md
- [ ] 03-agent-briefing.md
- [ ] 04-ramir-pricing-case.md
- [ ] 05-decision-log.md
- [ ] 99-glossary.md

Keep this playbook OUT of sources (it is instructions, not knowledge).

## 2. Prompt — 10-Slide Video Deck Outline

```
Create a 10-slide outline for Argi, Product Designer aiming for Anthropic-level.
Audience: mentor + intern peers. Tone: confident, specific, visual.
Slides: 1 Title (Argi + 60-second decision thesis), 2 Problem (template fails decisions),
3 Bar (8 pillars table), 4 Pipeline (design-to-code 5 stages), 5 Case Ramir today,
6 Benchmark Stripe (steal 3), 7 Benchmark Linear (steal 3), 8 Target Pricing v2 mock description,
9 Method (how I direct agents + gates), 10 Next (1 metric + 1 date).
For each slide give: title, 3 bullets max, visual idea, speaker note 30s. Cite sources.
```

## 3. Prompt — Mind Map

```
Generate a mind map with central node "Enterprise Product Designer (Argi)".
Branches: Bar (8 pillars), Pipeline (5 stages), Agents (5 roles + vetoes),
Case (Ramir vs Stripe vs Linear table), Glossary (30 terms grouped in 3 clusters).
Keep labels under 4 words. Cite sources per branch.
```

## 4. Prompt — Audio Overview (Podcast)

```
Generate an Audio Overview as 2 hosts (7–9 min).
Story: Argi rebuilds Ramir Pricing from template to enterprise by studying Stripe and Linear
and learning to direct 5 AI agents. Cover: 60-second decision, 1 recommended tier,
proof near price, dark mode craft, gates before prod. End with 1 next step: Pricing v2.
Use file 04 for examples, file 05 for timeline. No filler.
```

## 5. Prompt — Study Guide + Quiz

```
Create a Study Guide + 10-question Quiz.
Guide: key ideas per file with 1 Ramir example each.
Quiz: 6 multiple choice (glossary + pillars), 2 compare (Stripe vs Ramir),
2 scenario (brief an agent for Pricing v2). Provide answer key with citations.
```

## 6. After NotebookLM — Share Checklist

- [ ] Download Audio (mp3) + Mind Map (png) + Doc (study guide)
- [ ] Screenshot 10-slide outline into slides (Canva / Pitch / Figma Slides)
- [ ] Record 60s Loom walking through Pricing v2 plan
- [ ] Post to mentor: 3 bullets + 1 link + 1 question (not a dump)

## FAQ

**Q: How many sources is ideal?**
A: 6 is sweet spot. More than 12 dilutes citations.

**Q: What if Audio hallucinates?**
A: Regenerate with "Use only uploaded sources, cite file + section" appended.
