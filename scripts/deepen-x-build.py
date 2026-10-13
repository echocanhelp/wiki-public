#!/usr/bin/env python3
"""Build DEEPEN-X cards for pages that still have unabsorbed archive files.

A corpus file that wikilinks this page, which this page does not wikilink back,
is the work. Mention count is not. A page whose corpus links are already on it
is not a card — measured 2026-10-12, 20 of 32 demand-ranked cards had zero such
files and would only have reshuffled headings.

The card names one gap and lists the files. It does not ask for Works, Timeline,
Network, and Quotes. It does not search the web. Web is a later lane, only after
this delta is zero.

Dedupe keys on the page path, never the card title.

Already-saturated pages (hits-hash / verified-saturation stamp) are excluded.
Pages whose latest deepen-x commit in 7 days was a zero-yield close are excluded
unless the file was edited after that commit. See scripts/feeder_recent_closes.py.

Env:
  DEEPEN_SLICE   pages per card    (default 1)
  DEEPEN_NCARDS  max cards per run (default 32)
  DEEPEN_DRY     1 = print the plan, write nothing
"""
import glob
import os
import re
import sqlite3
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from feeder_recent_closes import recent_zero_yield_paths, still_closed

REPO = Path('/home/leedt/echo-system')
OUT = REPO / 'knowledge/operational'
SLICE = int(os.environ.get('DEEPEN_SLICE', '1'))
NCARDS = int(os.environ.get('DEEPEN_NCARDS', '32'))
DRY = os.environ.get('DEEPEN_DRY') == '1'
LIST_CAP = 8
CORPUS_DIRS = ('works', 'articles', 'sources', 'events', 'topics')
SATURATED_RE = re.compile(r'(hits.?hash|verified.?saturation|SATURATION)', re.I)
LINK_RE = re.compile(r'\[\[([^\]|#]+)')
WIKI_RE = re.compile(r'\[\[(?:people|organizations)/([^\]|#]+)')
ROSTER_LINE = re.compile(r'^\s*- \[\[(?:people|organizations)/')


def countable_slugs(text: str) -> set[str]:
    """Person/org links that are not a copied columnist roster.

    Tag-archive pages carry the same 14-name bullet list, then a nav. That is
    not a mention. A run of more than 6 consecutive `- [[people/` lines is that
    roster. A real ## Subjects block is shorter and still counts. A slug that
    also appears outside the roster still counts.
    """
    lines = text.splitlines()
    roster = set()
    i = 0
    n = len(lines)
    while i < n:
        if ROSTER_LINE.match(lines[i]):
            j = i + 1
            while j < n and ROSTER_LINE.match(lines[j]):
                j += 1
            if j - i > 6:
                roster.update(range(i, j))
            i = j
        else:
            i += 1
    slugs = set()
    for i, ln in enumerate(lines):
        if i in roster:
            continue
        for m in WIKI_RE.finditer(ln):
            slugs.add(m.group(1).strip().removesuffix('.md'))
    return slugs


def demand_files():
    """slug -> set of content-relative corpus paths (no .md) that wikilink it.

    One walk. The old counter threw the paths away, so the card could not name
    the work and the selector could not tell absorbed from leftover.
    """
    files = defaultdict(set)
    content_root = REPO / 'content'
    for f in glob.glob(str(content_root / '**/*.md'), recursive=True):
        rel = Path(f).relative_to(content_root)
        if not rel.parts or rel.parts[0] not in CORPUS_DIRS:
            continue
        try:
            text = Path(f).read_text(errors='replace')
        except OSError:
            continue
        key = str(rel.with_suffix(''))
        for slug in countable_slugs(text):
            if Path(f).stem == slug:
                continue
            files[slug].add(key)
    return files


def page_links(text: str) -> set[str]:
    return {m.group(1).strip().removesuffix('.md') for m in LINK_RE.finditer(text)}


def fm(text: str, key: str) -> str:
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', text, re.M)
    return m.group(1).strip() if m else ''


def unabsorbed(text: str, slug: str, mention_files) -> list[str]:
    linked = page_links(text)
    files = [p for p in mention_files.get(slug, ())
             if p not in linked and not p.endswith('/index') and p != 'index']
    # A publisher org is linked from nearly every page in its own works tree.
    # That is a catalog stamp, not a subject. 9,733 such links on
    # taiwaneseamericanhistory-org is not a deepen.
    if len(files) >= 200:
        works = sum(1 for p in files if p.startswith('works/'))
        if works / len(files) >= 0.8:
            return []
    return sorted(files)


def quote_candidate(page_text: str, files: list[str]):
    """One sentence from an unabsorbed file that contains the full name.

    Prefer a quoted span. Reject Tag: lines. None if the name is too short to
    be safe — a surname match is a different person.
    """
    zh = fm(page_text, 'name_zh')
    en = fm(page_text, 'name_en')
    names = []
    if len(zh) >= 2:
        names.append(zh)
    if len(en) >= 8 and ' ' in en:
        names.append(en)
    if not names:
        return None
    for rel in files[:4]:
        path = REPO / 'content' / (rel + '.md')
        try:
            blob = path.read_text(errors='replace')[:8000]
        except OSError:
            continue
        for name in names:
            for m in re.finditer('「([^」]{0,80}' + re.escape(name) + '[^」]{0,80})」', blob):
                sent = m.group(1).strip()
                if 'Tag:' not in sent and len(sent) >= 12:
                    return sent[:220], rel
        for name in names:
            idx = blob.find(name)
            if idx < 0:
                continue
            start = max(blob.rfind('\n', 0, idx), blob.rfind('。', 0, idx)) + 1
            end = blob.find('。', idx)
            if end < 0:
                end = min(len(blob), idx + 140)
            else:
                end += 1
            sent = ' '.join(blob[start:end].split())
            if 24 <= len(sent) <= 220 and 'Tag:' not in sent and not sent.startswith('#'):
                return sent[:220], rel
    return None


def has_quote(text: str) -> bool:
    return '## Quotes' in text or bool(re.search(r'^>\s+\S', text, re.M))


def card_body(page: str, text: str, files: list[str], stamp: str, card_no: int,
              today: str, task_id: str) -> str:
    zh = fm(text, 'name_zh') or '(none)'
    en = fm(text, 'name_en') or '(none)'
    shown = files[:LIST_CAP]
    extra = len(files) - len(shown)
    file_lines = '\n'.join(f'- [[{p}|source]]' for p in shown)
    if extra:
        file_lines += f'\n- and {extra} more — absorb the listed ones; the rest wait'
    quote = None if has_quote(text) else quote_candidate(text, files)
    if quote:
        sent, src = quote
        gap = (
            "ONE GAP: this page has no quote. If the sentence below is this person, "
            "paste it under ## Quotes with a wikilink to its source. If it is not "
            "this person, do not paste it. Either way, absorb the listed files as "
            "dated facts under ## From the record, one wikilink each."
        )
        qblock = f'\nQUOTE CANDIDATE (confirm, do not invent):\n> {sent}\nsource: [[{src}|source]]\n'
    else:
        gap = (
            "ONE GAP: absorb the listed files. Add one dated fact per file under "
            "## From the record, each with a wikilink to that file. That is the "
            "whole card. Do not add ## Works / ## Timeline / ## Network / ## Quotes "
            "unless a listed file is actually that kind of record."
        )
        qblock = '\n'
    return (
        f"Deepen 1 page. Slice: knowledge/operational/deepen-x-slice-{stamp}-{card_no}.txt. "
        f"Page: {page}. name_zh: {zh}. name_en: {en}. "
        "Use these exact names. A surname-only hit is not this person. "
        f"{gap}\n"
        f"FILES THAT LINK HERE AND ARE NOT LINKED BACK ({len(files)}):\n{file_lines}\n"
        f"{qblock}"
        "No web. No new pages. No invented biography. A date bump or a note with no "
        "new [[wikilink]] is 0 deepened — the feeder reads the diff. "
        "HOLD conflicts; never auto-merge dates. "
        f"On a true skip, add one line BELOW the closing --- fence, never inside YAML: "
        f"verified-saturation: {today}. An HTML comment inside frontmatter breaks the build. "
        "Never git add -A, git add ., or git commit -a. Stage only this page. "
        f"Commit subject must be exactly: deepen-x slice {stamp}-{card_no}: N deepened, M skipped. "
        f"Then call the kanban_complete tool on {task_id}. "
        "The hermes kanban CLI complete is rejected inside a worker and does not close the card. "
        "Do NOT publish."
    )


def absorb_universe(mention_files):
    """Pages with at least one unabsorbed corpus file, ranked by that count."""
    rows = []
    saturated = 0
    no_delta = 0
    for pat in ('content/people/*.md', 'content/organizations/*.md'):
        for f in glob.glob(str(REPO / pat)):
            rel = os.path.relpath(f, REPO / 'content')
            slug = Path(f).stem
            text = Path(f).read_text(errors='replace')
            if SATURATED_RE.search(text):
                saturated += 1
                continue
            files = unabsorbed(text, slug, mention_files)
            if not files:
                no_delta += 1
                continue
            rows.append((-len(files), rel, files, text))
    rows.sort(key=lambda r: (r[0], r[1]))
    return rows, saturated, no_delta


def open_card_paths():
    con = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
    try:
        bodies = con.execute(
            "select body from tasks "
            "where status not in ('done','archived') and title like 'DEEPEN%'"
        ).fetchall()
    finally:
        con.close()
    paths = set()
    for (body,) in bodies:
        for m in re.finditer(r'deepen-x-slice(?:-\d+)?-\d+\.txt', body or ''):
            sp = OUT / m.group(0)
            if sp.is_file():
                # slice file is the page path only; never the absorb list
                paths.update(ln.strip() for ln in sp.read_text().splitlines() if ln.strip())
    return paths


def main():
    mention_files = demand_files()
    universe, saturated, no_delta = absorb_universe(mention_files)
    closed = recent_zero_yield_paths('deepen-x')
    cooled = [rel for _n, rel, _f, _t in universe if rel in closed and still_closed(rel, closed[rel])]
    cooled_set = set(cooled)
    claimed = open_card_paths()
    top = [row for row in universe if row[1] not in cooled_set and row[1] not in claimed][:SLICE * NCARDS]
    today = date.today().isoformat()

    if DRY:
        print(f"dry: universe={len(universe)} saturated_excluded={saturated} "
              f"no_delta_excluded={no_delta} cooled={len(cooled)} "
              f"claimed_by_open={len(claimed)} planned={len(top)}")
        for i, (_n, rel, files, text) in enumerate(top, 1):
            q = quote_candidate(text, files) if not has_quote(text) else None
            print(f"  card {i}: {rel} unabsorbed={len(files)} "
                  f"quote={'yes' if q else 'no'} names={fm(text,'name_zh') or '-'}|{fm(text,'name_en') or '-'}")
        return

    OUT.mkdir(parents=True, exist_ok=True)
    stamp = subprocess.run(['date', '+%m%d%H%M'], capture_output=True, text=True).stdout.strip()
    made = 0
    for i, (_n, rel, files, text) in enumerate(top):
        card_no = i + 1
        slice_path = OUT / f'deepen-x-slice-{stamp}-{card_no}.txt'
        slice_path.write_text(rel + '\n')
        title = f'DEEPEN-X{stamp}-{card_no}: absorb {min(len(files), LIST_CAP)} corpus files'
        r = subprocess.run(['hermes', 'kanban', 'create', title,
                            '--assignee', 'pinto', '--body', 'pending',
                            '--max-runtime', '2400'],
                           capture_output=True, text=True)
        tid = re.search(r't_[0-9a-f]+', r.stdout)
        if not tid:
            print('create failed:', r.stdout.strip() or r.stderr.strip())
            continue
        body = card_body(rel, text, files, stamp, card_no, today, tid.group(0))
        con = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
        con.execute('update tasks set body=? where id=?', (body, tid.group(0)))
        con.commit()
        con.close()
        subprocess.run(['hermes', 'kanban', 'promote', tid.group(0)], capture_output=True)
        made += 1
        print('created', tid.group(0), slice_path.name, rel, 'files', len(files))
    print(f'cards: {made}  universe: {len(universe)}  no_delta: {no_delta}  '
          f'cooled: {len(cooled)}  excluded(claimed): {len(claimed)}')


if __name__ == '__main__':
    main()
