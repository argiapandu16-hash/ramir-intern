# Mailbox — phone ↔ sandbox async pipe (v1, manual)

Two folders, one rule: **phone writes requests, sandbox writes answers.**

- `mailbox/requests/<timestamp>-<skill>.md` — created on phone via `askohm`.
- `mailbox/answers/<same-name>.md` — created by OhmDev in sandbox, pushed to Telegram too.

## Request format

```markdown
# skill: ohmarch
# asked: 2026-10-02 14:00
# from: phone

<your question + context>
```

Valid skills: `ohmarch` (architecture/backend), `ohmfront` (UI/UX),
`ohmqa` (testing), `ohmsec` (security), `ohmdev` (anything else).

## Flow

1. Phone: `askohm ohmfront "is my checkout button accessible?"` → pushes.
2. Tell OhmDev (here or via any chat): `check mailbox`.
3. OhmDev answers with the full skill → writes `mailbox/answers/...`
   → pushes the answer AND forwards it to your Telegram (Pipe 2).
4. Phone: `git pull` → read `mailbox/answers/...` anytime.

v1 latency: same session/day (sandbox processes on demand).
v2 (later): auto-watcher for minute-level replies.
