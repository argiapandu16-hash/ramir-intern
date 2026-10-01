# Playbook — Cara BAH Adopsi / Contek Aplikasi Orang (untuk Master)

> **Untuk siapa:** Master (bukan programmer). Ini cara OhmDev & tim ngevaluasi dan memutuskan saat Master nemu tool/repo/aplikasi keren di forum dan tanya "ini bisa perkuat kita nggak?".
> **Janji OhmDev:** Master nggak perlu paham kode. Master cukup lempar nama/link, OhmDev jalankan playbook ini dan lapor balik dalam **bahasa awam + verdict jelas**.
> **Dibuat:** 13 Juni 2026, dari sesi scan 6 tools (Scrapling, Understand Anything, dst).

---

## 🎯 Inti: 3 cara "ambil" punya orang (beda banget konsekuensinya)

Master sering bilang "adopsi" atau "contek" — padahal ada **3 level** yang risikonya beda jauh:

| Cara | Maksud | Contoh | Risiko |
|------|--------|--------|--------|
| **1. PAKAI** (install apa adanya) | Pasang & jalankan tool orang | Scrapling, Understand Anything | 🟢 Rendah — asal lisensi izinkan |
| **2. CONTEK POLA** (belajar caranya, tulis ulang sendiri) | Lihat cara mereka bikin, kita bikin versi sendiri | Belajar DCF dari Fincept, bikin di Iolanthe | 🟢 Aman — ide tak bisa dipatenkan |
| **3. FORK / ADOPSI KODE** (ambil kodenya, modif) | Copy codebase orang, ubah, deploy | Fork Fincept jadi produk Ramir | 🔴 Bisa bahaya — lisensi mengikat |

**Aturan emas Master:** *"Pakai boleh, contek pola selalu aman, fork kode hati-hati."*

---

## 🚦 Lampu Lisensi (yang OhmDev cek PERTAMA — paling sering jadi ranjau)

Setiap repo punya "surat izin" namanya **lisensi**. OhmDev selalu cek ini duluan. Disederhanakan:

| Lisensi | Artinya buat Ramir (perusahaan for-profit) | Lampu |
|---------|---------------------------------------------|-------|
| **MIT / Apache / BSD** | Bebas pakai, modif, jual. Cukup sebut kreditnya. | 🟢 AMAN |
| **GPL / AGPL** | Kalau dipakai/deploy, **kode kita ikut wajib dibuka** ke publik. AGPL paling ketat (bahkan SaaS). | 🟡 HATI-HATI |
| **AGPL + lisensi komersial** (mis. Fincept) | Pakai internal di perusahaan = **wajib bayar** (Fincept: $10.200/thn). Kadang ada klausa **Ramir ikut kena tuntutan** kalau developer-nya (BAH) yang deploy. | 🔴 RANJAU |
| **Proprietary** (mis. Claude Mail) | Punya orang, berbayar, kita nggak bisa kontrol/modif. Cuma bisa langganan. | 🟡 Boleh pakai, jangan jadi tulang punggung |
| **"No license"** (kosong) | Secara hukum = hak cipta penuh pemilik. Diam-diam pakai = melanggar. | 🔴 Tanya dulu |

> **Kenapa ini penting buat Master:** Ramir itu **for-profit**. Banyak tool "gratis" ternyata gratis cuma buat hobi/perorangan — begitu dipakai bisnis, kena biaya atau kewajiban hukum. OhmDev selalu cek ini SEBELUM ngoding apa-apa.

---

## 📋 7 Langkah Baku OhmDev (yang Master akan lihat hasilnya)

Tiap kali Master lempar tool baru, OhmDev jalankan ini:

1. **Cari & pahami** — apa ini, siapa bikin, dipakai berapa orang (bintang GitHub = popularitas).
2. **Cek lisensi** — lampu hijau/kuning/merah di atas. Kalau 🔴 → stop di sini, lapor Master.
3. **Cek privasi** — apakah tool ini kirim data kita keluar diam-diam? (OhmDev bedah kodenya: cari panggilan ke internet.)
4. **Uji terpisah** — install di "ruang karantina" (folder `03_Workspace`), jalankan, lihat beneran kerja atau nggak. **TIDAK langsung dicampur ke sistem hidup.**
5. **Cek sentimen** — orang lain bilang apa? Ada keluhan/bug/risiko hukum?
6. **Petakan gap & fit** — ini nutup lubang apa di BAH? Tumpang-tindih dengan yang sudah ada nggak?
7. **Verdict + gate** — laporan bahasa awam: 🥇 adopsi / 🥈 catat dulu / 🔴 hindari. Kalau adopsi → minta izin Master sebelum masuk sistem nyata.

> Master cukup baca **langkah 7**. Sisanya OhmDev kerjakan sendiri (autopilot).

---

## 🗝️ Cara Master "Lihat" yang Kami Bangun (tanpa baca kode)

Master minta bisa paham bahasa teknis kami. Caranya: **Understand Anything** (sudah dipasang ke OhmDev).

- Tiap OhmDev bangun/ubah sesuatu → OhmDev bisa bikin **peta visual** (knowledge graph) dari kode itu.
- Master buka `/understand-dashboard` → lihat kotak-kotak (tiap kotak = satu bagian sistem) + penjelasan bahasa Inggris/Indonesia sederhana.
- Master bisa **tanya langsung** lewat `/understand-chat`: *"bagian mana yang ngurus pembayaran?"* → dijawab tanpa Master baca kode.

> Ini jendela transparansi Master ke dalam mesin BAH. OhmDev akan **tawarkan graph** tiap kali habis bangun sesuatu yang penting.

---

## ⚖️ Garis Merah (OhmDev TIDAK akan lakukan tanpa izin Master)

```
🔴 Fork/deploy kode berlisensi mengikat (GPL/AGPL/komersial) untuk produk Ramir
🔴 Pakai tool yang kirim data klien/Master keluar tanpa kontrol
🔴 Bypass auth/login sistem orang (beda dari scrape data publik)
🔴 Install ke sistem PRODUKSI (VPS Contabo) tanpa uji terpisah + approval
🔴 Adopsi repo "no license" diam-diam
```

OhmDev selalu **uji di karantina dulu**, **cek lisensi dulu**, **lapor verdict dulu** — baru sentuh sistem nyata.

---

## Contoh Nyata (sesi 13 Jun 2026)

| Tool | Apa yang OhmDev lakukan | Hasil ke Master |
|------|--------------------------|------------------|
| **Scrapling** | Install di karantina → uji fetch+anti-bot (status 200 ✅) → lisensi gratis 🟢 | 🥇 Adopsi → masuk Epsilon |
| **Understand Anything** | Clone → bedah privasi (no data keluar ✅) → MIT 🟢 | 🥇 Adopsi → masuk OhmDev (+ jendela Master) |
| **Fincept Terminal** | Cek lisensi → AGPL + $10.200/thn + klausa Ramir ikut kena tuntutan 🔴 | 🔴 Jangan adopsi kode; boleh contek pola DCF saja |
| **Claude Mail** | Cek → proprietary Anthropic 🟡 | 🥈 Inspirasi; BAH bikin versi sendiri (ban-safe) |

> Pola ini berlaku untuk SEMUA tool/repo/aplikasi yang Master temukan ke depan. Lempar saja namanya — OhmDev jalankan playbook ini.
