#!/usr/bin/env python3
import sys
import os
import sqlite3
import json
from datetime import datetime

DB_PATH = os.path.expanduser("~/workspace/.workgraph/workgraph-intern.db")
SNAPSHOT_PATH = os.path.expanduser("~/workspace/.workgraph/snapshot.json")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def update_snapshot():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, status, priority FROM tasks ORDER BY id DESC LIMIT 10")
    tasks = [dict(row) for row in cur.fetchall()]
    
    snapshot = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "active_intent": "OpenCode Dedicated Intern Sandbox Workspace",
        "total_tasks": len(tasks),
        "recent_tasks": tasks
    }
    
    os.makedirs(os.path.dirname(SNAPSHOT_PATH), exist_ok=True)
    with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    conn.close()

def add_task(title, priority="medium"):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, status, priority) VALUES (?, 'pending', ?)", (title, priority))
    conn.commit()
    task_id = cur.lastrowid
    conn.close()
    update_snapshot()
    print(f"✅ Task #{task_id} berhasil ditambahkan: '{title}' [{priority}]")

def list_tasks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, status, priority, created_at FROM tasks ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()
    print("=== DAFTAR TUGAS WORKGRAPH INTERN ===")
    if not rows:
        print("Belum ada tugas tercatat. Tambahkan dengan: workgraph add 'Nama Tugas'")
        return
    for r in rows:
        status_icon = "🟢 [DONE]" if r["status"] == "done" else "🟡 [PENDING]"
        print(f"#{r['id']} {status_icon} ({r['priority']}) {r['title']} - {r['created_at']}")

def complete_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status='done', updated_at=CURRENT_TIMESTAMP WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    update_snapshot()
    print(f"✅ Task #{task_id} ditandai selesai (DONE)!")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h", "help"]:
        print("Penggunaan CLI WorkGraph Intern:")
        print("  workgraph add 'Nama Tugas' [priority]")
        print("  workgraph list")
        print("  workgraph done <id>")
        print("  workgraph status")
        return

    cmd = sys.argv[1].lower()
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Error: Harap masukkan judul tugas. Contoh: workgraph add 'Setup API'")
            return
        title = sys.argv[2]
        priority = sys.argv[3] if len(sys.argv) > 3 else "medium"
        add_task(title, priority)
    elif cmd in ["list", "ls"]:
        list_tasks()
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Error: Harap masukkan ID tugas. Contoh: workgraph done 1")
            return
        complete_task(int(sys.argv[2]))
    elif cmd in ["status", "snapshot"]:
        update_snapshot()
        print("✅ Snapshot WorkGraph berhasil diperbarui ke .workgraph/snapshot.json")
        list_tasks()
    else:
        print(f"Perintah tidak dikenal: {cmd}")

if __name__ == "__main__":
    main()
