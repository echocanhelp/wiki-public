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
import json
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

# SWARM-GUARD-1 (t_0cb42501): fail-closed backlog gate before every create.
sys.path.insert(0, os.path.expanduser('~/.hermes/scripts'))
from mint_guard import gated_once, budget_args  # noqa: E402

REPO = Path('/home/leedt/echo-system')
OUT = REPO / 'knowledge/operational'
SLICE = int(os.environ.get('DEEPEN_SLICE', '1'))
NCARDS = int(os.environ.get('DEEPEN_NCARDS', '32'))
DRY = os.environ.get('DEEPEN_DRY') == '1'
# 2026-10-15: 8 files/card fit the 2400s contract at width 3 (28 min median),
# but at width 5-7 the engine thrashes KV (measured 200% occupancy, per-worker
# prefill 3.5k tok/s vs 21k peak) and 8-file cards stretch past 40 min, batch-
# time out, and re-mint -- 1 close/hr instead of 7. Halved the contract: a
# 4-file card closes in ~20 min under contention. Tunable via DEEPEN_LIST_CAP.
LIST_CAP = int(os.environ.get('DEEPEN_LIST_CAP', '4'))
CORPUS_DIRS = ('works', 'articles', 'sources', 'events', 'topics')
SATURATED_RE = re.compile(r'(hits.?hash|verified.?saturat|SATURATION)', re.I)
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
        # 2026-11-18 (t_1c4fa3b9 class): navigation index pages are not absorbable
        # corpus — an index.md as a card's only "corpus file" is a fat-card bug that
        # wastes a worker run (DEEPEN-X11180809-1 shipped with target=people/index).
        if Path(f).stem == 'index':
            continue
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


_QC_CACHE = None


def corpus_quote_candidates(slug: str):
    """Attributed-speech candidates from scripts/quote-scan.py (corpus-wide,
    high = name+verb adjacent to the quote). Loaded once per build; never
    pasted without confirmation — the card asks the worker to verify."""
    global _QC_CACHE
    if _QC_CACHE is None:
        _QC_CACHE = {}
        p = REPO / "knowledge" / "research" / "quote-candidates.jsonl"
        if p.exists():
            for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                _QC_CACHE.setdefault(r["slug"], []).append(r)
    return sorted(_QC_CACHE.get(slug, []), key=lambda r: r.get("conf") != "high")


def card_body(page: str, text: str, files: list[str], stamp: str, card_no: int,
              today: str, task_id: str) -> str:
    zh = fm(text, 'name_zh') or '(none)'
    en = fm(text, 'name_en') or '(none)'
    shown = files[:LIST_CAP]
    extra = len(files) - len(shown)
    file_lines = '\n'.join(f'- [[{p}|source]]' for p in shown)
    if extra:
        file_lines += (f'\n- and {extra} more — STOP: they are NOT this card. '
                       f'Absorb only the {len(shown)} listed above. Do not grep, list, '
                       f'or enumerate the rest.')
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
    elif not has_quote(text) and (cands := corpus_quote_candidates(Path(page).stem)):
        c = cands[0]
        gap = (
            "ONE GAP: this page has no quote. The candidate below was found by a "
            "corpus-wide attributed-speech scan (" + c.get("conf", "medium") +
            " confidence) — open the source file and confirm the SPEAKER before "
            "pasting; if it is not this person, do not paste it. Either way, "
            "absorb the listed files as dated facts under ## From the record, "
            "one wikilink each."
        )
        src_path = c["path"]
        if src_path.startswith("content/"):
            src_path = src_path[len("content/"):]
        if src_path.endswith(".md"):
            src_path = src_path[:-3]
        qblock = (f'\nQUOTE CANDIDATE (corpus scan, {c.get("conf")} — verify '
                  f'speaker before pasting):\n> {c["quote"]}\nsource: '
                  f'[[{src_path}|source]]\n')
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
        "No web. No new pages. No invented biography. A dated fact with a "
        "wikilink is sourced; a fact you cannot wikilink to a listed file is "
        "inferred or unknown and does not belong on this card. A date bump or a note with no "
        "new [[wikilink]] is 0 deepened — the feeder reads the diff. "
        "HOLD conflicts; never auto-merge dates. "
        f"On a true skip, add one line BELOW the closing --- fence, never inside YAML: "
        f"verified-saturation: {today}. An HTML comment inside frontmatter breaks the build. "
        "Never git add -A, git add ., or git commit -a. Stage only this page. "
        f"Commit subject must be exactly: deepen-x slice {stamp}-{card_no}: N deepened, M skipped. "
        "N = 1 if this page gained substantive content (new wikilinks/dated facts), else 0. "
        "M = 1 only if you verified saturation and wrote the stamp below the fence. "
        "This card is ONE page — never count files into N. Put the file count in the commit body: "
        "'files absorbed: K'. "
        f"Then call the kanban_complete tool on {task_id}. "
        "The hermes kanban CLI complete is rejected inside a worker and does not close the card. "
        "Do NOT publish."
    )


def traffic_weights():
    """GoatCounter 7d per-path visits -> {slug: weight in [0,1]}. Empty if stale/absent.
    Freshness gate: file mtime must be < 7 days, else ranking silently trusts old data."""
    p = REPO / "knowledge" / "research" / "gc-path-counts.json"
    if not p.exists():
        return {}
    import time as _t
    if (_t.time() - p.stat().st_mtime) > 7 * 86400:
        return {}
    try:
        counts = json.loads(p.read_text()).get("counts", {})
    except (ValueError, OSError):
        return {}
    per_slug = {}
    for path, n in counts.items():
        seg = [s for s in path.split("/") if s and s not in ("wiki-public", "people", "organizations", "topics", "works")]
        if seg:
            per_slug[seg[-1]] = per_slug.get(seg[-1], 0) + n
    if not per_slug:
        return {}
    mx = max(per_slug.values())
    return {k: v / mx for k, v in per_slug.items()}


def gap_score(text: str) -> float:
    """Voice/label gap in [0,1] — what the page lacks BEYOND dated content
    (census 2026-10-14: 95% of pages are date-dense, Story=1, Quotes=3%).
    no Story .3 | no Quotes .2 | record facts with zero labels .3 | <10 dates .2.
    Deterministic; feeds the attention-weighted rank per LEONARD-2026-10-15."""
    g = 0.0
    if not re.search(r"^## Story\s*$", text, re.M):
        g += 0.3
    if not re.search(r"^## Quotes", text, re.M):
        g += 0.2
    rec = re.search(r"^## From the record\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if rec:
        facts = [l for l in rec.group(1).splitlines()
                 if re.match(r"\s*(\||- \*\*|\*\*)", l) and re.search(r"\d{4}|n\.d\.", l)]
        if facts and not any(re.search(r"sourced|inferred|alleged|unknown", l, re.I)
                             for l in facts):
            g += 0.3
    if len(re.findall(r"\b(19[4-9]\d|20[0-2]\d)\b", text)) < 10:
        g += 0.2
    return min(g, 1.0)


def absorb_universe(mention_files):
    """Pages with at least one unabsorbed corpus file, ranked by
    count * (1 + 3*traffic) * (1 + gap) — traffic tiebreak per DEEPRANK ruling,
    gap bonus per attention-weighted deepening (2026-10-15): among pages with
    equal absorbable material, the ones missing voice/labels come first.
    (weight 0 = count-only, same order as before; weight 1 = 4x.)"""
    weights = traffic_weights()
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
            score = len(files) * (1 + 3 * weights.get(slug, 0.0)) * (1 + gap_score(text))
            rows.append((-score, rel, files, text))
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


def timed_out_paths(hours: int = 12) -> set[str]:
    """Pages inside DEEPEN cards that timed out within `hours`.

    A timeout is not a verdict on the page -- it says the card was too big for
    the runtime contract at that width. Re-minting the identical card
    guarantees another timeout (observed 2026-10-15: five attempts on three
    pages, zero closes). Cool those pages for `hours` so the queue moves past
    them instead of burning attempts. Fail open.
    """
    import time as _t
    try:
        con = sqlite3.connect(
            f"file:{Path.home() / '.hermes/kanban.db'}?mode=ro", uri=True)
        try:
            rows = con.execute(
                "select t.body from tasks t join task_events e on e.task_id = t.id "
                "where e.kind = 'timed_out' and e.created_at > ? "
                "and t.title like 'DEEPEN%'", (_t.time() - hours * 3600,)).fetchall()
        finally:
            con.close()
    except sqlite3.Error:
        return set()
    paths: set[str] = set()
    for (body,) in rows:
        for m in re.finditer(r'deepen-x-slice(?:-\d+)?-\d+\.txt', body or ''):
            sp = OUT / m.group(0)
            if sp.is_file():
                paths.update(ln.strip() for ln in sp.read_text().splitlines() if ln.strip())
    return paths


def main():
    mention_files = demand_files()
    universe, saturated, no_delta = absorb_universe(mention_files)
    closed = recent_zero_yield_paths('deepen-x')
    cooled = [rel for _n, rel, _f, _t in universe if rel in closed and still_closed(rel, closed[rel])]
    cooled_set = set(cooled) | timed_out_paths()
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
        if not gated_once('deepen-x-build', key=title):  # SWARM-GUARD-1
            print('BACKLOG|SKIP', title)
            continue
        r = subprocess.run(['hermes', 'kanban', 'create', title,
                            '--assignee', 'pinto', '--body', 'pending',
                            '--max-runtime', '2400',
                            *budget_args('DEEPEN-X')],  # SWARM-GUARD-3 t_418565a8: was NULL -> silent 30/30 deaths
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
