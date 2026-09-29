# AGENTS.md — OpenCode Intern Dedicated Sandbox

Selamat datang di Sandbox OpenCode Dedicated Tim Intern.

## 🧭 Panduan Kerja & Alur Kontinuitas
1. **WorkGraph Lokal**:
   - Seluruh tugas dan progres proyek wajib dicatat menggunakan perintah CLI `workgraph`.
   - Gunakan `workgraph add "Judul Tugas" [priority]` untuk membuat tugas baru.
   - Gunakan `workgraph list` untuk melihat daftar tugas yang sedang aktif.
   - Gunakan `workgraph done <id>` saat suatu tugas selesai dikerjakan.
   - File status kontinuitas tersimpan otomatis di `.workgraph/snapshot.json`.

2. **Dukungan 30 Skill Teknis Dewan 5 CTO**:
   - Kamu didukung oleh 30 skill teknis standar industri di `~/.config/opencode/skills/`.
   - Manfaatkan persona `ohmdev`, `ohmarch`, `ohminfra`, `ohmsec`, `ohmqa`, `ohmfront` untuk arsitektur, backend, frontend, testing TDD, dan keamanan.

3. **Batasan Lingkungan (Isolasi)**:
   - Folder kerja utama kamu berada di `~/workspace/`.
   - Dilarang menyimpan credential atau token privat di repositori publik.
