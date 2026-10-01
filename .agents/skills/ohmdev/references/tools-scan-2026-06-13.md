# Referensi — Scan 6 Tools dari Forum (13 Juni 2026)

> Dikumpulkan Master dari forum, didalami OhmDev. Status: **Scrapling & Understand Anything = DIUJI & DIADOPSI**; sisanya = referensi + penanda gap.
> Pasangan dok: gap di HUB2 P7 sudah ditandai di `02_Projects/BAH Hub/docs/superpowers/specs/2026-06-12-bah-hub-v2-design.md` (§P7).

---

## ✅ 1. Scrapling — DIADOPSI (Epsilon)
- **Apa:** Framework scraping Python adaptif. StealthyFetcher tembus Cloudflare Turnstile out-of-the-box; selector auto-relocate saat layout berubah; JSON 10× cepat; spider concurrent + proxy rotation + pause/resume.
- **Lisensi:** Open source, gratis. Repo: `D4Vinci/Scrapling`.
- **Uji (13 Jun):** ✅ LULUS. `scrapling 0.4.9` + `patchright 1.60` + `browserforge` terpasang. Fetcher/StealthyFetcher/DynamicFetcher import OK; StealthyFetcher headless **status 200**, parse 10 elemen.
- **Aksi:** masuk skill `hard-target-recon` Epsilon (Tier 2-4), ditandai TERVERIFIKASI + catatan API v0.4.9.
- **Zona:** 🟡 — bikin scraping lebih gampang, justru disiplin zona legal lebih ketat (🟢 publik no-auth saja).
- **Sentimen:** 🟢 teknis kuat. ⚠️ media sorot "dipakai bypass anti-bot"; preseden Reddit-gugat-Perplexity → tetap di pagar Master.

## ✅ 2. Understand Anything — DIADOPSI (OhmDev)
- **Apa:** Claude Code plugin → codebase jadi knowledge graph interaktif. 8 command (`/understand*`). Plain-English summary per node.
- **Lisensi:** MIT. Repo: `Egonex-AI/Understand-Anything`. Lokal-only.
- **Uji (13 Jun):** ✅ LULUS inspeksi. Clone + bedah: semua `fetch()` ke file lokal (`knowledge-graph.json` dll), `TokenGate` cuma proteksi akses lokal, **no data keluar**. 8 skill command valid. tree-sitter parsing lokal.
- **Aksi:** masuk arsenal OhmDev + 2 peran: (a) understand-before-harden, (b) 🗝️ **penerjemah teknis untuk Master non-programmer** (dashboard + chat bahasa awam).
- **Install:** Master ketik `/plugin marketplace add Egonex-AI/Understand-Anything` lalu `/plugin install understand-anything`.
- **Sentimen:** 🟢 positif, privacy-friendly.

---

## 📋 3. TurboVec — REFERENSI (kandidat P7, belum)
- **Apa:** Vector index Rust+Python (algoritma Google TurboQuant, ICLR 2026). 10jt vektor 31GB→4GB (−87%), lebih cepat dari FAISS, zero-training, jalan tanpa GPU.
- **Lisensi:** MIT, gratis. Bukan vector DB managed — library ANN search (no dashboard/query-language).
- **Verdict:** 🥈 HUB2 sudah putuskan **pgvector** (nol infra baru, cukup untuk skala BAH ~50 buku finance). TurboVec hemat RAM tapi +dependency Rust & non-persisten. **Catat sebagai opsi kalau RAG membengkak besar, bukan sekarang.**

## 📋 4. GraphRAG / Cognee — REFERENSI (lengkapi P7)
- **Apa:** RAG berbasis graph (MS GraphRAG: +35% presisi vs vector-only, menang 70-80% complex sensemaking). Library: **Neo4j, Memgraph, Cognee** (memory engine graph+vector), RAGFlow (GraphRAG+UI).
- **Lisensi:** open source (cek per-tool).
- **Verdict:** 🥈 HUB2 P7 sudah rencana Mem0 + RAG 3-tingkat. GraphRAG/**Cognee** = lapisan **reasoning relasional** di atasnya — mis. hubungkan lead↔perusahaan↔industri↔kontak di market DB (3.038 lead). **Melengkapi pgvector, bukan ganti. Untuk P7 fase Full.**
- **Arah industri 2026:** RAG=retrieval luas · Memory=kontinuitas sesi · **Graph=reasoning relasional**.

## ⚠️ 5. Claude Mail / Claude for Outlook — REFERENSI (inspirasi, jangan jadi dependency)
- **Apa:** Add-in Outlook (beta 7 Mei 2026) — triage unread 3 bucket + draft balasan. Konektor Gmail/M365 di semua plan.
- **Lisensi:** ⚠️ Proprietary Anthropic, berbayar/plan-gated.
- **Verdict:** 🥈 Pola **email-triage agent** relevan (klien AI CS + ops internal). ⚠️ Ranjau sama Cowork: produk proprietary, bukan jalur API yang kita kontrol. **BAH bisa bikin sendiri pakai DeepSeek/GLM + IMAP (ban-safe, gratis)** — selaras prinsip P6 HUB2. Jadikan inspirasi fitur, BUKAN dependency.

## 🔴 6. Fincept Terminal — REFERENSI (belajar pola, JANGAN adopsi kode)
- **Apa:** "Bloomberg open-source" — C++20+Qt6+Python, 423rb instrumen, 100+ connector, analitik CFA (DCF/VaR/Sharpe/portfolio-opt), AI agent workbench.
- **Lisensi:** 🔴🔴 **AGPL-3.0 + komersial $10.200/thn.** Internal use di organisasi for-profit = Commercial Use (wajib bayar). Klausa **JOINT-AND-SEVERAL LIABILITY**: kalau Ramir kontrak developer (BAH) untuk fork/deploy/customize → **Ramir ikut tanggung jawab hukum penuh.**
- **Verdict:** 🥉 **JANGAN adopsi/fork kodenya** (Ramir for-profit → kena lisensi + liability). 🟢 Boleh **bedah pola arsitektur** untuk Iolanthe/Fiona (DCF/VaR/Sharpe sudah jadi skill BAH). Masuk daftar ranjau lisensi sama dengan Typebot/Dify/Erxes/n8n di HUB2 §X5.

---

## RINGKASAN PRIORITAS

| Tool | Fit | Status | Lisensi |
|------|-----|--------|---------|
| 🕷️ Scrapling | 🥇 | ✅ diuji + masuk Epsilon | gratis |
| 🕸️ Understand Anything | 🥇 | ✅ diuji + masuk OhmDev | MIT |
| 🔗 GraphRAG/Cognee | 🥈 | 📋 referensi → P7 Full | open |
| ⚡ TurboVec | 🥈 | 📋 referensi → opsi cadangan | MIT |
| 📧 Claude Mail | 🥈 | ⚠️ inspirasi, build sendiri | proprietary |
| 📊 Fincept | 🥉 | 🔴 belajar pola, jangan adopsi | AGPL+$10k |

**Catatan:** lihat juga `playbook-adopsi-aplikasi-orang.md` (cara baku BAH evaluasi/uji/adopsi repo orang — bahasa awam untuk Master).
