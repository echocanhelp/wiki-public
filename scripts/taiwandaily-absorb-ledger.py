#!/usr/bin/env python3
"""taiwandaily-absorb-ledger.py — the ONLY writer of the absorb ledger.

Workers call this after each page write; it appends one JSON line and fsyncs,
so a SIGKILL loses at most the in-flight article. Never edit or rewrite the
ledger by hand; duplicates are tolerated (last wins) because append-only +
fsync is what makes the card resumable.

usage: taiwandaily-absorb-ledger.py <YYYYMM> --url URL \
        --decision absorbed|skipped|hold [--page content/people/x.md] [--note TEXT]

Exit 0 + prints the appended line. Refuses unknown decisions and empty urls.
The page path is stored repo-relative (knowledge/... or content/...) so
ledger-coverage can check it against git HEAD.
"""
import argparse, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

ARCH = Path.home() / 'echo-system/knowledge/web-archives'
DECISIONS = ('absorbed', 'skipped', 'hold')

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('ym')
    ap.add_argument('--url', required=True)
    ap.add_argument('--decision', required=True, choices=DECISIONS)
    ap.add_argument('--page', default=None)
    ap.add_argument('--note', default=None)
    a = ap.parse_args()
    if not a.url.startswith('http'):
        print('REFUSE: url must be absolute', file=sys.stderr); return 1
    if a.decision == 'absorbed' and not a.page:
        print('REFUSE: absorbed requires --page (repo-relative)', file=sys.stderr); return 1
    if a.page and a.page.startswith('/'):
        try:
            a.page = str(Path(a.page).relative_to(Path.home() / 'echo-system'))
        except ValueError:
            print('REFUSE: --page must live under ~/echo-system', file=sys.stderr); return 1
    ARCH.mkdir(parents=True, exist_ok=True)
    if not re.fullmatch(r'\d{6}', a.ym):
        print('bad ym (want 6 digits)', a.ym, file=sys.stderr)
        return 2
    led = ARCH / f'tdm-{a.ym}-absorb-ledger.jsonl'
    line = json.dumps({'url': a.url, 'decision': a.decision, 'page': a.page,
                       'note': a.note, 'ts': datetime.now(timezone.utc).isoformat()},
                      ensure_ascii=False)
    new_file = not led.exists()
    fd = os.open(led, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        want = len((line + '\n').encode('utf-8'))
        if os.write(fd, (line + '\n').encode('utf-8')) != want:
            print('REFUSE: short write, ledger line not durable', file=sys.stderr)
            return 3
        os.fsync(fd)
    finally:
        os.close(fd)
    if new_file:  # first create: fsync the dir so the entry itself is durable
        dfd = os.open(ARCH, os.O_RDONLY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    print(line)
    return 0

if __name__ == '__main__':
    sys.exit(main())
