---
name: harness-gate
description: Layered anti-hallucination verification gates (mutation tracking + defect scan + completion block). Use when enforcing zero-defect execution, porting the OpenCode harness verdicts ([VERIFIED CLEAN]/[DEFECT ALERT]/[MUTATION REGISTERED]) to DeepSeek/DSH sessions, or running gate.py --wrap/--check.
---

# Harness Gate (portable, DeepSeek/DSH-ready)

Siklus mekanis per turn: **edit/write → MUTATION REGISTERED (UNVERIFIED) →
bash verifikasi → VERIFIED CLEAN / DEFECT ALERT**. Dilarang klaim selesai
sebelum verdict CLEAN; todo `completed` saat mutasi belum terverifikasi =
dipaksa `in_progress`.

Engine: `X:\Antigravity T01\03_Workspace\harness-gate\gate.py` (stdlib only).
Doktrin + bukti lintas sesi: `HARNESS-GATE-SYSTEM.md` di folder yang sama.

- Bungkus command: `python .../gate.py --wrap -- pytest -q`
- Cek output: `python .../gate.py --check --file out.txt` (exit 0 bersih / 1 defect)
- State machine multi-step: `Gate().register_mutation() / .check_command() / .block_completed()`
- Self-test: `test_gate.py` (9/9 PASS) — wajib hijau sebelum klaim adopsi beres.
