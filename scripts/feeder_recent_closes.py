#!/usr/bin/env python3
"""Paths whose latest feeder commit was a zero-yield close.

Workers record saturation in the commit subject and do not write the
verified-saturation stamp the builders already know how to skip. So the same
page is re-carded every hour. This module re-reads git once per feeder tick.

A later edit (file mtime newer than that commit) puts the path back immediately.
After COOLDOWN_DAYS the path is eligible again even if mtime did not move:
new corpus articles do not touch the entity page, and a permanent mtime gate
would hide them forever.

Fail open. A git error returns no exclusions so a broken log cannot starve
the swarm.
"""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

REPO = Path('/home/leedt/echo-system')
COOLDOWN_DAYS = 7

# A positive deepen count means the card did the work. Do not let a trailing
# "0 skipped" or a saturation aside exclude that path.
_REAL = re.compile(r'(?<![0-9])[1-9]\d*\s+deepened', re.I)
_ZERO = re.compile(
    r'(?<![0-9])0\s+deepened'
    r'|verified[-\s]saturat'
    r'|\bsaturated\b'
    r'|(?<![0-9])0\s+touched'
    r'|(?<![0-9])0\s+changed'
    r'|no content edits'
    r'|no new mater',
    re.I)


def date_bump_hashes(days: int = COOLDOWN_DAYS) -> set[str]:
    """Feeder commits that claim a deepen but add no wikilink, quote, or image.

    A last_reviewed bump is not work. The subject line cannot be trusted.
    Cached on HEAD so a dry run and the following live tick do not pay twice.
    A git error returns an empty set (fail open).
    """
    cache = Path.home() / '.hermes' / 'cache' / 'feeder-date-bumps.json'
    head = subprocess.run(
        ['git', '-C', str(REPO), 'rev-parse', 'HEAD'],
        capture_output=True, text=True).stdout.strip()
    if cache.is_file() and head:
        try:
            import json
            saved = json.loads(cache.read_text())
            if saved.get('head') == head and saved.get('days') == days:
                return set(saved.get('bumps') or [])
        except (OSError, ValueError):
            pass
    claimed = subprocess.run(
        ['git', '-C', str(REPO), 'log', f'--since={days} days ago',
         '--format=%H%x09%s', '--', 'content/'],
        capture_output=True, text=True)
    if claimed.returncode != 0:
        return set()
    real = set()
    for line in claimed.stdout.splitlines():
        h, _, subj = line.partition('\t')
        if h and _REAL.search(subj) and subj.lstrip().lower().startswith(('deepen-x', 'tjj')):
            real.add(h)
    added: set[str] = set()
    for pattern in (r'\[\[', r'^> ', r'!\['):
        r = subprocess.run(
            ['git', '-c', 'core.quotepath=false', '-C', str(REPO), 'log',
             f'--since={days} days ago', '-G', pattern, '--format=%H', '--', 'content/'],
            capture_output=True, text=True)
        if r.returncode != 0:
            return set()
        added.update(x.strip() for x in r.stdout.splitlines() if x.strip())
    bumps = real - added
    try:
        import json
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps({'head': head, 'days': days, 'bumps': sorted(bumps)}))
    except OSError:
        pass
    return bumps


def is_zero_yield(subject: str) -> bool:
    if _REAL.search(subject):
        return False
    return bool(_ZERO.search(subject))


def recent_zero_yield_paths(prefix: str, days: int = COOLDOWN_DAYS) -> dict[str, int]:
    """content-relative path -> unix time of the latest matching feeder commit,
    if that commit was a zero-yield close.

    `prefix` is `deepen-x` or `tjj`. A TJJ saturation commit also lists the
    person pages it stamped; those must not be excluded from the deepen queue,
    and a later TJJ touch must not clear a deepen-x zero-yield close. Newest
    matching commit wins.
    """
    r = subprocess.run(
        ['git', '-c', 'core.quotepath=false', '-C', str(REPO), 'log',
         f'--since={days} days ago', '--format=%H %ct%x09%s', '--name-only',
         '--', 'content/'],
        capture_output=True, text=True)
    if r.returncode != 0:
        return {}
    out: dict[str, int] = {}
    seen: set[str] = set()
    bumps = date_bump_hashes(days)
    ct = 0
    zero = False
    match = False
    buf: list[str] = []
    in_commit = False
    want = prefix.lower()

    def flush() -> None:
        if not match:
            return
        for raw in buf:
            rel = raw.strip().strip('"')
            if not rel or rel.endswith('/'):
                continue
            if rel.startswith('content/'):
                rel = rel[len('content/'):]
            if rel in seen:
                continue
            seen.add(rel)
            if zero:
                out[rel] = ct

    for line in r.stdout.splitlines():
        head, sep, subj = line.partition('\t')
        hm = re.match(r'^([0-9a-f]{7,40}) (\d+)$', head)
        if sep and hm and subj:
            if in_commit:
                flush()
            commit_hash = hm.group(1)
            ct = int(hm.group(2))
            match = subj.lstrip().lower().startswith(want)
            zero = is_zero_yield(subj) if match else False
            if match and commit_hash in bumps:
                zero = True
            buf = []
            in_commit = True
            continue
        # git puts a blank line between the subject and the file list. It is
        # not a commit boundary — the next subject line is.
        if not line.strip() or not in_commit:
            continue
        buf.append(line)
    if in_commit:
        flush()
    return out


def still_closed(rel: str, closed_at: int) -> bool:
    """True when nobody has edited the page since the zero-yield close.

    The worker writes, then commits, so mtime is at or before the commit.
    A later touch (mtime > commit) means the page changed and must be eligible.
    """
    try:
        return os.path.getmtime(REPO / 'content' / rel) <= closed_at + 2
    except OSError:
        return False


if __name__ == '__main__':
    deepen = recent_zero_yield_paths('deepen-x')
    tjj = recent_zero_yield_paths('tjj')
    d_held = sum(1 for rel, ts in deepen.items() if still_closed(rel, ts))
    t_held = sum(1 for rel, ts in tjj.items() if still_closed(rel, ts))
    print(f'deepen-x zero-yield: {len(deepen)} still-closed: {d_held}')
    print(f'tjj zero-yield: {len(tjj)} still-closed: {t_held}')
    # a known zero-yield page from 2026-10-12 must be in the deepen set
    probe = 'people/dean-chang.md'
    print(f'probe {probe}:', probe in deepen)
