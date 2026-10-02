#!/bin/bash
# askohm — file a request to the sandbox skill team from your phone.
# Usage: askohm <skill> <question...>
# Example: askohm ohmfront "is my checkout button accessible? grey small text"
# Skills: ohmarch ohmfront ohmqa ohmsec ohmdev
set -u
SKILL="${1:-ohmdev}"; shift || true
Q="$*"
if [ -z "$Q" ]; then
  echo "Usage: askohm <skill> <question...>"; exit 1
fi
cd ~/ramir-intern 2>/dev/null || cd ~/argi-bot/.. 2>/dev/null || true
STAMP=$(date +%Y%m%d-%H%M%S)
F="mailbox/requests/${STAMP}-${SKILL}.md"
mkdir -p mailbox/requests
{
  echo "# skill: $SKILL"
  echo "# asked: $(date '+%Y-%m-%d %H:%M')"
  echo "# from: phone"
  echo ""
  echo "$Q"
} > "$F"
git add "$F" && git commit -qm "mailbox: $SKILL request $STAMP" && git push origin HEAD && \
  echo "Sent ($F). Tell OhmDev: check mailbox."
