# Referensi — Anthropic "The Founder's Playbook: Building an AI-Native Startup"

> **Sumber:** Anthropic / Claude, rilis **14 Mei 2026**, 34 halaman.
> Blog: `claude.com/blog/the-founders-playbook` · PDF gratis (no sign-in).
> **Tidak ada repo GitHub resmi** — hanya terjemahan Mandarin tidak resmi (`yangliu2060/founders-playbook-zh`).
> **Diekstrak & disesuaikan:** 13 Juni 2026 oleh OhmDev untuk BAH.
>
> **Sifat dokumen ini:** referensi terkurasi — konten playbook **+ kolom "Status di HUB2"** yang menandai mana yang Master sudah punya (✅), mana yang diserap (📥), mana yang ranjau (⚠️). BUKAN copy mentah. Lihat juga: `02_Projects/BAH Hub/PRD_BAH_Hub_v1.md` + `docs/superpowers/specs/2026-06-12-bah-hub-v2-design.md`.

---

## ⚠️ Disclaimer Pemakaian (WAJIB BACA)

Playbook ini **genuinely useful TAPI juga dokumen marketing** Anthropic. Dirilis **1 hari setelah** launch *Claude for Small Business* — corong konversi ke revenue berulang. Anthropic raise $30B @ valuasi $380B; tesis ke investor: "Claude = infrastruktur wajib", dan playbook ini mengaktifkan tesis itu di titik paling awal (founder baru).

**Cara pakai untuk BAH/Ramir:**
- Ambil **kerangka stage-gating + exit criteria + failure modes** (itu padat & nyata).
- **Buang** dorongan "pakai Claude Cowork/Code untuk segalanya" — di BAH, otak murah (GLM/DeepSeek/OR) tetap default; Claude untuk task berat (prinsip P6 HUB2 "ban-safe").
- **Ranjau utama (⚠️):** playbook menyarankan **Claude Cowork untuk compliance/security workstream** di Launch stage — padahal dokumentasi Anthropic SENDIRI bilang Cowork activity TIDAK tercatat di audit log / Compliance API / data export, dan **jangan untuk regulated workloads** (SOC2/HIPAA/PCI/GDPR). Untuk P6 (AI CS+CRM jual ke klien), JANGAN ikut saran ini.

---

## Tesis Inti — "Founder = Orchestrator of Agents"

AI menghapus 3 gerbang lama company-building: **modal, headcount, skill teknis**. Founder bergeser dari *individual contributor* (nulis kode, manage orang, ops harian) → **orchestrator**: mengarahkan agent + tools + tim kecil. Perhatian founder naik ke *higher-order work* — generate ide & arahkan sistem.

> **"The bottlenecks are no longer what you can build, but what you choose to build."**

Tiga area AI mengangkat startup jadi seperti org besar:
1. **Conversational intelligence & research** — on-call expert (deep research, document drafting, devil's advocate).
2. **Agentic coding** — engineer yang selalu available, never blocked.
3. **Workflow automation** — automated ops team (CRM, report, compliance tracking, integrasi antar-tool).

> **Status di HUB2:** ✅ **SUDAH INTI.** Ini persis tesis HUB2 — "rumah perang agent autonomous", Master di titik keputusan, agent kerja autonomous (PRD v1 §1, v2 §0). Master praktikkan duluan; playbook baru *deskripsikan*. **Validasi eksternal**, bukan info baru.

---

## Pilihan Permukaan Claude (Chat / Cowork / Code)

| Kalau task… | Pakai | Kenapa |
|-------------|-------|--------|
| Pertanyaan, rewrite, brainstorm cepat | **Chat** | Cepat, percakapan, no setup |
| Riset/analisis, dokumen jadi dari file & sistem | **Cowork** | Folder access, connector, skills, scheduled runs |
| Nulis/test/ship software | **Code** | Codebase access, diff, git, dev env |

> "Ketiganya share Claude yang sama; yang beda cuma workspace di sekitarnya."

> **Status di HUB2:** 📥 **Adaptasi.** Padanan BAH: **Chat→** dispatch chat 1-on-1 (Telegram/Lobby) · **Cowork→** Arena + skill orchestration (creative-sop, research, dll) · **Code→** OhmLoop coding arena. Tapi **engine BAH multi-provider** (GLM/DeepSeek/OR + Claude), bukan Claude-only.

---

# 4 STAGE — Goal · Exit Criteria · Failure Modes · Exercise

## STAGE 1 — IDEA
**Goal:** *Research-oriented validation* — kumpulkan bukti solid bahwa masalah nyata ada (& solusi-mu menjawabnya) SEBELUM commit resource ke building. Tahan diri: *"don't build until the evidence justifies it."*

**Exit criteria — jawab YA ke 3 ini:**
1. **Masalah real & spesifik?** Bisa sebut siapa persis kena, seberapa sering, seberapa parah, & apa yang mereka lakukan sekarang.
2. **Solusimu menjawab masalah aktual?** (yang validasi ungkap — kadang ≠ asumsi awal).
3. **Cukup sinyal untuk justify building?** Tak akan pernah 100% pasti; butuh bukti kualitatif bahwa commit ke MVP = keputusan beralasan, bukan lompatan iman buta.

**Failure modes:**
- **Mistaking building for validating** — 42% startup gagal karena bikin yang tak diinginkan. Prototype cepat ≠ bukti; prototype = *alat pressure-test percakapan*, bukan bukti itu sendiri.
- **Premature scaling** — scale eksekusi mendahului validasi business demand.
- **Loss of objectivity** — *confirmation bias kini punya research engine.* Minta AI cari bukti yang dukung keyakinanmu → pasti ketemu. Antidot: arahkan AI sebaliknya — **pressure-test ide setajam saat memvalidasinya**.

**Exercises kunci:**
- Pertajam problem statement jadi *testable* ("Contract review takes too long" ❌ → "In-house legal di mid-market spend 3+ hari/siklus karena redline dikelola via email, bukan satu dokumen ber-versi" ✅).
- Minta AI **argue against** ide-mu (devil's advocate) — surface sinyal pasar negatif, kompetitor gagal, hambatan struktural.
- Bangun TAM/SAM/SOM dari data publik + pressure-test asumsinya.
- Identifikasi 3 tren eksternal (regulatory/tech/demographic) 2 tahun ke depan — tailwind atau headwind?
- Customer discovery: target profile presisi > daftar kontak panjang; tanya masa lalu ("ceritakan terakhir kali kamu hadapi masalah ini") bukan hipotetis ("akankah kamu pakai…").
- **Lightweight prototype**: bangun *satu* core interaction, taruh di depan 5 orang dari target profile tervalidasi → tentukan lanjut atau balik.

**Tool:** Chat (brainstorm) → Cowork (riset/sintesis) → Code (prototype akhir).

> **Status di HUB2:** 📥 **Diserap sebagian.** Konsep "Q0 → testable hypothesis" sudah ada di skill `/diagnose` (Ramir Diagnostic). Yang LAYAK serap: **3 exit criteria + "AI as structured devil's advocate"** sebagai pola baku sebelum BAH commit build apapun. Sudah selaras dgn prinsip P5 HUB2 (anti-halusinasi by design).

---

## STAGE 2 — MVP
**Goal:** Terjemahkan *validated problem* → working product (iterasi terkecil paling fokus, bukan versi penuh) yang generate bukti **product-market fit**. Goal kedua sama penting: **moving fast tanpa menumpuk technical debt**, + **investasi di persistent context (CLAUDE.md)** sejak hari satu.

**Exit criteria:** bukti genuine PMF — grup spesifik & teridentifikasi menemukan produk cukup bernilai untuk **kembali (retention), bayar (revenue), dan/atau cerita ke orang (referral)**.

**Failure modes:**
- **Agentic technical debt** — AI re-derive keputusan fondasi tiap sesi → drift. Tanpa spec & architectural constraint tertulis, codebase tak punya *coherent mental model*. Beda dari debt biasa: **ini compound & muncul telat.**
- **False PMF** — angka awal mengesankan tapi bukan jaminan pasar butuh produkmu. Traksi awal (teman, portfolio investor, spike Hacker News) = ephemeral; tak prediksi minggu ke-6/12.
- **Zero-friction scope creep** — tiap fitur defensible & murah dibikin → produk melar lewat batas. Antidot: **scope definition tertulis sebelum building** ("should we build this?" → "apakah cukup banyak user bilang mereka tak dapat value tanpa ini?").
- **Insecure by inexperience** — agentic coding generate kode yang *works*, bukan *secure*. Tak ada feedback loop natural yang peringatkan founder pemula. **Security review wajib sebelum user pertama sentuh.**

**Exercises kunci:**
- **Define architecture before build** → simpan output sebagai **CLAUDE.md** (persistent "memory" project, dibaca otomatis Agent SDK).
- Template sesi Code: (1) revisit scope doc, (2) kasih CLAUDE.md; **akhir sesi: update log** (apa dibangun, keputusan, asumsi). *5 menit dok/sesi = asuransi murah lawan architectural drift.*
- **Security review** sebelum deploy: auth & session handling, data exposure di API response, input validation & injection, dependency rentan. (Claude Code Security — beta saat itu — scan & saran patch.)
- **Measurement framework SEBELUM launch:** retention benchmark, activation criteria, target Day-7 & Day-30. Definisikan juga *false positive* (signups tanpa activation, revenue tanpa retention).
  - **Sean Ellis test:** "Seberapa kecewa kalau tak bisa pakai ini lagi?" — **>40% "sangat kecewa" = indikator PMF bermakna.**
  - **Effort test:** kalau retention butuh intervensi konstan (outreach, insentif, follow-up heroik) = belum PMF. Post-PMF, produk mulai *menarik* sendiri, bukan didorong.
- **Pivot when evidence demands:** kalau ≥3 siklus iterasi tanpa gerak ke PMF → diagnostic: (a) ada segmen yang respons beda? (b) gap value = positioning atau product problem? (c) apa yang harus benar agar produk ini temukan PMF, & realistis?

**Tool:** Code (build, primary) + Cowork (feedback logistics, sintesis).

> **Status di HUB2:** 📥 **Insight #1 & #2 layak serap.**
> - **CLAUDE.md sebagai architectural context** — BAH sudah pakai (`CLAUDE.md` global + project). Validasi praktik.
> - 📥 **Measurement framework PMF (Sean Ellis 40% + effort test + false-positive def)** → **belum ada di HUB2**; relevan untuk **P6 (AI CS+CRM SaaS jual klien)**. Catat sebagai modul metrik P6.
> - ✅ "Scope tertulis dulu" = selaras prinsip P2 HUB2 ("jantung dulu, hiasan nyusul") + spec-gate Workflow C OhmDev.
> - ⚠️ "Security review wajib pra-user" — HUB2 punya gate ohmsec (5 CTO), tapi pertajam: jadikan **gate eksplisit pra-deploy P6**.

---

## STAGE 3 — LAUNCH
**Goal:** Ubah traksi awal → *repeatable, sustainable growth engine*; harden infrastruktur; bangun perusahaan nyata di sekitar produk. **Bangun operational system yang membebaskan perhatian founder** (bukan mengeluarkan founder dari perusahaan).

**Exit criteria — 3 elemen:**
1. **Growth repeatable & channel-driven** — bukan sekadar retain; akuisisi prediktabel via channel spesifik dengan unit economics dipahami: **CAC, LTV, payback period** — angka yang kamu tahu & bisa defend.
2. **Produk handle production workloads** — infra di-harden, security & compliance beres, reliability tahan kondisi produksi nyata.
3. **Ops jalan tanpa founder bottleneck** — proses & automation ada; founder bukan lagi yang pegang support, triage, sprint planning, reporting.

**Failure modes:**
- **Technical debt comes due** — debt MVP (untuk velocity) mulai berbunga. Solusi: **architectural audit sistematis** → refactor terarah → perluas test coverage agar ronde fitur berikut tak reintroduce masalah sama.
- **Founder becomes the bottleneck** — instinct "ada di tiap loop" (aset di MVP) jadi constraint di Launch. Remedy: **all-out audit semua yang founder pegang** → klasifikasi: bisa di-automate / bisa delegate / genuinely butuh founder.
- **Security & compliance no longer deferrable** — user nyata + data nyata + kontrak enterprise → kerentanan teoritis jadi exposure nyata. **Security & compliance review = remediation wajib, bukan saran.**
- **Expansion before you're ready** — pasar/funding baru tampak peluang growth, padahal bisa tempat PMF mati. Ekspansi terlalu dini ke pasar beda → variabel baru, kehilangan kemampuan baca data sendiri, abaikan basis user awal.

**Exercises kunci:**
- Code: audit codebase MVP → daftar prioritas kelemahan struktural, gap test coverage, kandidat refactor → sequence lintas sprint. Dokumentasikan keputusan arsitektur (yang tadinya di kepala) ke **CLAUDE.md**.
- Cowork: audit operasional terstruktur (tiap task berulang, keputusan, workflow yang jalan hanya karena founder ingat) → kategorikan automate/human-not-you/founder-judgment → bangun automation layer.
- Security: code-level review berorientasi framework target market (SOC2/GDPR/HIPAA) → 2 output: sequence remediasi prioritas + daftar dokumentasi/control untuk compliance review. **Note Anthropic: "AI scan = bantuan, BUKAN pengganti qualified compliance review."**
- Stand up product management process ringan: sprint cadence, spec template minimum, decision-tree triage bug, weekly metrics brief dari data nyata.

**Tool:** ketiganya penuh & saling suapi output. ⚠️ Cowork untuk compliance/ops layer — **lihat disclaimer ranjau di atas**.

> **Status di HUB2:** 📥 **Insight #3 (exit criteria CAC/LTV/payback) + ⚠️ ranjau Cowork.**
> - 📥 **Tiga exit criteria Launch konkret** (growth repeatable + production-ready + no-founder-bottleneck) → **pertajam tangga HUB2** X4 (MVP→Fondasi→Full→Jual saat ini belum punya exit criteria setajam ini).
> - ✅ "Founder bottleneck → audit & delegate" = persis misi HUB2 (dispatch dari HP, watcher, agent autonomous).
> - ⚠️ **TAMBAH ke X5 Risiko HUB2:** "Jangan pakai Cowork-class tool (no audit log) untuk compliance/regulated workload P6." Ini ranjau nyata yang playbook sendiri kontradiksi.

---

## STAGE 4 — SCALE
**Goal:** Founder re-center dari builder → *public-facing executive* (analyst briefing, IPO roadshow). Scale infra teknis **+ scale organisasi jadi business matang**. Bangun **defensible moat lewat accumulated depth** (kedalaman integrasi, data proprietary, workflow).

**Exit criteria:** bukan 1 milestone, tapi *threshold event* — perusahaan sustainable meski founder makin lepas ops harian. Pertanyaan kunci: **"Kalau incumbent ber-dana copy produkmu hari ini, user-mu tetap bertahan?"** Wujud praktis (salah satu dari 3): **profitabilitas berkelanjutan tanpa kapital eksternal · IPO-readiness · akuisisi.** Ketiganya butuh growth sistematis & auditable, moat tahan scrutiny, org matang operasional.

**Failure modes:**
- **Delegating the operational layer** — sistem ops Scale harus jalan andal tanpa babysit; transisi ini tantangan psikologis + struktural. Pegang terlalu lama → bottleneck; lepas terlalu cepat ke sistem AI → keputusan kritis tanpa konteks founder.
- **Building a GTM function** — organic growth ada plafonnya; mayoritas founder Scale belum pernah bangun GTM nyata (marketing, sales, analyst relations, brand voice/story).
- **Scaling technical & org functions** — pelanggan besar evaluasi *organisasi*, bukan cuma produk; butuh support infra, dokumentasi, reliability guarantee, + fungsi org (hiring, payroll, accounting, legal).

**Exercises kunci (moat-building):**
- **Bottleneck map** workflow operasional → ekstrapolasi "apa terjadi kalau founder hilang 1 minggu" → yang stall = yang masih butuh handoff.
- **Enterprise gap analysis**: pilih 3 prospek/ideal customer → dokumentasi, SLA, support infra apa yang tim procurement enterprise harap → di mana kurang.
- **Compound user data → defensible advantage**: audit data interaksi → 3 pola behavioral sinyal-tertinggi → feedback loop yang ubah tiap pola jadi product improvement → draft *moat narrative* 1-halaman (cerita data flywheel: kenapa kompetitor mulai hari ini tak bisa replikasi dalam <2 tahun).
- **Workflow lock-in**: petakan customer per *integration depth* → makin banyak integrasi/automation user bangun di atas produkmu, makin mahal switching → bangun API/webhook/SDK agar customer build *on top of* produk (lock-in terdalam).
- **Domain expertise → AI context**: eksternalisasi pengetahuan domain founder via skill/memory → jadi *proprietary knowledge substrate* yang AI generalis tak bisa tandingi.

**Tool:** ketiganya — Code (harden + integrasi + demo env), Cowork (eksekusi taktis GTM: content, outbound, analyst logistics), Chat.

> **Status di HUB2:** ✅ **Mostly N/A untuk sekarang** (BAH belum stage Scale). Tapi 2 konsep relevan strategis Ramir:
> - 📥 **"Moat lewat accumulated depth + workflow lock-in"** → relevan untuk **P6 SaaS** & posisi Ramir (data klien Jatim 3.038 lead = data flywheel yang sudah jalan).
> - 📥 **"Domain expertise → proprietary AI knowledge substrate"** → persis yang BAH lakukan dengan 51 skill custom + memory. Ramir bisa pakai ini sebagai *pitch* (Big-4 × AI: kedalaman domain ter-kodifikasi).

---

## "Same Job, New Rules" (penutup)
Kerja founder tak berubah: temukan masalah nyata, bikin solusi, scale jadi perusahaan. Yang berubah: **AI memampatkan kuartal jadi minggu.** Validasi berbulan → afternoon. Prototype tak butuh co-founder berskill tepat — cukup masalah jelas + beberapa sesi coding agent. **"The bottlenecks are no longer what you can build, but what you choose to build."**

---

## Founder Stories (referensi, dari Resources)
HumanLayer (F24), Ambral (W25), Vulcan Technologies (S25), Carta Healthcare (22rb kasus bedah/thn, −66% waktu abstraksi), Anything (1.5jt user no-code), Cogent (enterprise security agents), Airtree (Cowork = pusat ops), Duvo (procurement/supply-chain agents), Zingage (homecare 24/7), Kindora (matching charity↔funder, Claude Sonnet), GC AI (legal platform).

---

## RINGKASAN AKSI untuk HUB2 (yang OhmDev rekomendasikan serap)

| # | Insight playbook | Aksi konkret di HUB2 | Prioritas |
|---|------------------|----------------------|-----------|
| 1 | Exit criteria + failure mode eksplisit per stage | Pertajam tangga X4 (MVP→Fondasi→Full→Jual) dengan exit criteria gaya playbook | 🟡 Fondasi |
| 2 | Measurement framework PMF (Sean Ellis 40%, effort test, false-positive) | Modul metrik untuk **P6 (AI CS+CRM SaaS)** | 🟡 saat P6 |
| 3 | ⚠️ Cowork JANGAN untuk compliance/regulated (no audit log) | TAMBAH baris ke **X5 Risiko & Mitigasi** HUB2 | 🔴 sekarang |
| 4 | "Start 1 proses repetitif low-creative, bukan AI-kan semua day-1" | ✅ Sudah = prinsip P2. Validasi, no action | ✅ done |
| 5 | Moat = accumulated depth + workflow lock-in + domain substrate | Pitch material Ramir (Big-4×AI) + arah P6 jangka panjang | 🟢 strategis |

**Catatan OhmDev:** HUB2 **sudah lebih dari cukup** sebagai PRD. Playbook ini bukan menambah pekerjaan — ia (a) memvalidasi arah Master dari sumber otoritatif, (b) menyumbang 1 ranjau compliance yang harus dicatat, (c) memberi bahasa *exit-criteria* yang bisa mempertajam tangga build. Tidak ada rombakan arsitektur.
