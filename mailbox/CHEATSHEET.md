# ⚡ Argi's Daily Cheatsheet — pocket product designer

## Morning (2 min)
```
cd ~/argi-bot && python bot.py      # if phone rebooted overnight
```
Telegram → `/standup` → copy-paste to mentor.

## Telegram bot commands (@argi_ohmdev_bot)
| Type | Meaning |
|---|---|
| `/add Draft HMW high` | new task (low/medium/high) |
| `/list` `/status` | board + counts (offline) |
| `/done 3` | complete task #3 |
| `/idea ...` | park inspiration in 5s |
| `/ideas` | inspiration bank |
| `/standup` | standup draft (offline) |
| `/ask ...` | design coach, sees your tasks |
| `/crit ...` | critique: Strengths→Issues→Fixes→Score |
| `/myid` `/help` | your ID / this list |

## Skill team (Termux → sandbox → back to Telegram)
```
cd ~/ramir-intern
askohm <skill> "<question>"
```
| Skill | Call for |
|---|---|
| `ohmfront` | UI/UX, accessibility, **build me a page** |
| `ohmarch` | backend, data, architecture |
| `ohmqa` | testing, review my flow |
| `ohmsec` | security/privacy check |
| `ohmdev` | anything else |

Then say `check mailbox` to OhmDev (here). Answer lands in
`mailbox/answers/` AND your Telegram.

## Build-a-UI flow (designer superpower)
1. `askohm ohmfront "build a pricing page: 3 tiers, dark, CTA WA"`
2. `check mailbox` → OhmDev builds + pushes + sends **preview link**.
3. Open link on phone → screenshot → `/crit <what feels off>`.
4. Iterate: `askohm ohmfront "fix: ..."`.

## Termux survival
| Problem | Fix |
|---|---|
| Bot silent | `cd ~/argi-bot && python bot.py` (rebooted?) |
| `409 Conflict` | two bots polling → stop one (`pkill -f bot.py`) |
| Push rejected | `git pull --rebase origin main` then push |
| New bot version | `curl -L <link> -o bot.py && wc -l bot.py` → restart |
| Keep alive overnight | notification → Acquire wakelock + battery Unrestricted |
| `429` from AI | free-tier limit, wait a minute |

## Rules that protect you
- Secrets live in `~/.env`-style files only. Never paste tokens in chat.
- `origin` (yours) = playground. `org-house` (mentor) = don't touch.
- Defer is always OK: sandbox + phone work without any approval.
