#!/usr/bin/env python3
"""taiwandaily-slice-prep.py — deterministic slicer for TAIWANDAILY-ABSORB cards.

Runs OUTSIDE the worker's 30-iteration budget (SSOT: ~/knowledge/swarm-churn/
SSOT.md, piece S1). Selection + hanzi identity pre-filter are string matching,
not judgment — the worker only judges the shortlist.

  prep <YYYYMM> [--batch N]   -> JSON on stdout:
    {batches: [[{url,file,title,names,candidates:[page...],tag}...], ...],
     stats: {...}}
    tag: hit | collision | nohit  (from page-title index; worker has final say)
  ledger-coverage <YYYYMM>     -> JSON: {ym, total, decided, uncovered:[...]}
    A ledger line counts as coverage only if decision is decided AND, for
    absorbed, the page path exists in git HEAD (ops-doctrine inv.12: a line
    appended before a lost commit must not fake coverage).

Ledger: knowledge/web-archives/tdm-<ym>-absorb-ledger.jsonl (append-only,
written ONLY via taiwandaily-absorb-ledger.py).
"""
import json, re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path.home() / 'echo-system'
ARCH = REPO / 'knowledge/web-archives'
CONTENT = REPO / 'content'
INDEX = REPO / 'knowledge/research/tdm-page-title-index.json'

HANZI = re.compile(r'[一-鿿]{2,4}')

def _is_settled():
    """SSOT = the fetcher's own is_settled (status vocabulary drifted across
    fetcher generations: ok/exists/ok-direct/ok-existing/ok-video — a local
    ('ok','exists') tuple silently zeroed 27 months, probe 2026-10-20)."""
    try:
        import importlib.util
        sp = importlib.util.spec_from_file_location(
            'tdm_fetch', str(REPO / 'scripts/taiwandaily-month-fetch.py'))
        m = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(m)
        return m.is_settled
    except Exception:
        return lambda s: str(s).startswith(('ok', 'exists'))
IS_SETTLED = _is_settled()
# titles that are pure wire/ads even when they name people
SKIP_TITLE = re.compile(r'廣告|促銷|徵才|目錄|活動海報|照片集')
NAME_STOP = {'即時新聞','台灣','美國','中國','日本','總統','立委','市長','市長選','記者','消息','報導','表示','指出','認為'}
NAME_STOP |= {'台灣人','台灣人','美國人','本報','中央社記者','中央社記者陳'}

def article_title(md_path: Path) -> str:
    try:
        head = md_path.read_text(encoding='utf-8', errors='replace')[:600]
    except OSError:
        return ''
    m = re.search(r'^title:\s*"?([^"\n]+)', head, re.M)
    return (m.group(1) if m else '').strip()

def page_title_index(force=False) -> dict:
    """{normalized_title_or_stem: [relpaths]} cached by content/ mtime."""
    stamp = ARCH / '.tdm-index-mtime'
    cur = str(CONTENT.stat().st_mtime)
    if not force and INDEX.exists() and stamp.exists() and stamp.read_text().strip() == cur:
        try:
            return json.loads(INDEX.read_text())
        except Exception:
            pass
    idx: dict[str, list[str]] = {}
    # PEOPLE pages: content/people/*.md (2.4k, front-matter name_zh is the
    # authoritative identity field). NOT articles/ (news copies -> false
    # collisions, probe 1) and NOT content/*.md depth-1 (just index.md,
    # probe 2). Index = name_zh + H1 + hanzi 2-4grams of the page head —
    # what the old worker's "grep hanzi across content/" gate approximated.
    from collections import defaultdict
    tmp: dict[str, list[str]] = defaultdict(list)
    for p in (CONTENT / 'people').glob('*.md'):
        rel = str(p.relative_to(CONTENT))
        keys = {p.stem.lower().replace('-', ' ')}
        try:
            head = p.read_text(encoding='utf-8', errors='replace')[:600]
        except OSError:
            head = ''
        m = re.search(r'^name_zh:\s*"?([^"\n]+)', head, re.M)
        if m:
            nz = m.group(1).strip()
            if nz and nz != 'null':
                keys.add(nz)
        for m in re.finditer(r'^#\s+(.+)$', head, re.M):
            keys.add(re.sub(r'\s+', ' ', m.group(1)).strip().lower())
        for run in HANZI.findall(head):
            for n in range(2, min(4, len(run)) + 1):
                for i in range(len(run) - n + 1):
                    keys.add(run[i:i+n])
        for k in keys:
            tmp[k].append(rel)
    idx = {k: sorted(set(v))[:20] for k, v in tmp.items()}
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(idx, ensure_ascii=False))
    stamp.write_text(cur)
    return idx

def candidate_names(title: str) -> list[str]:
    out = []
    for seg in re.split(r'[：:，,、\s|「」『』（）()【】\[\]！!？?]+', title):
        for n in HANZI.findall(seg):
            if n in NAME_STOP or SKIP_TITLE.search(n):
                continue
            if n not in out:
                out.append(n)
    return out[:6]

def match_pages(name: str, idx: dict) -> list[str]:
    # exact n-gram key only — the index already contains every 2-4gram from
    # page heads; the old bidirectional substring fallback matched place
    # names inside news titles and flooded 'collision' (probe 2026-10-19).
    seen, out = set(), []
    for h in idx.get(name, []):
        if h not in seen:
            seen.add(h); out.append(h)
    return out[:5]

def prep(ym: str, batch: int):
    mf = ARCH / f'tdm-{ym}.json'
    if not mf.exists():
        print(json.dumps({'error': f'no manifest for {ym}'})); return 1
    d = json.loads(mf.read_text())
    results = d.get('results') or []
    decided = set()
    led = ARCH / f'tdm-{ym}-absorb-ledger.jsonl'
    if led.exists():
        for line in led.read_text().splitlines():
            try:
                decided.add(json.loads(line)['url'])
            except Exception:
                continue
    idx = page_title_index()
    items = []
    n_skip = n_hit = n_coll = n_settled = 0
    for r in results:
        if not IS_SETTLED(str(r.get('status', ''))) or not r.get('file'):
            continue
        n_settled += 1
        url = r['url']
        if url in decided:
            continue
        # file may be absolute (old fetcher) or ARCH-relative (new fetcher) —
        # Path() on a relative string resolves against CWD and silently read
        # 0 titles, skipping a whole month (probe 2026-10-20, 202511).
        f = Path(r['file'])
        if not f.is_absolute():
            f = ARCH / r['file']
        title = article_title(f)
        if not title or SKIP_TITLE.search(title):
            n_skip += 1
            continue
        names = candidate_names(title)
        if not names and unquote(url).find('台美人物') < 0:
            n_skip += 1
            continue
        cands = []
        for n in names:
            for p in match_pages(n, idx):
                if p not in cands:
                    cands.append(p)
        tag = 'nohit' if not cands else ('hit' if len(cands) <= 3 else 'collision')
        n_hit += tag == 'hit'; n_coll += tag == 'collision'
        items.append({'url': url, 'file': str(f), 'title': title,
                      'names': names, 'candidates': cands, 'tag': tag})
    # judgment-heavy first: collisions and hits before nohits (worker may
    # still absorb a nohit by creating a page — but they are the rare path)
    order = {'collision': 0, 'hit': 1, 'nohit': 2}
    items.sort(key=lambda x: order[x['tag']])
    batches = [items[i:i+batch] for i in range(0, len(items), batch)]
    print(json.dumps({'ym': ym, 'batch_size': batch,
                      'stats': {'settled': n_settled, 'undecided': len(items),
                                'prefilter_skipped': n_skip,
                                'hit': n_hit, 'collision': n_coll},
                      'batches': batches}, ensure_ascii=False))
    return 0

def ledger_coverage(ym: str):
    led = ARCH / f'tdm-{ym}-absorb-ledger.jsonl'
    mf = ARCH / f'tdm-{ym}.json'
    if not mf.exists():
        print(json.dumps({'ym': ym, 'error': 'no manifest'})); return 1
    urls = [r['url'] for r in (json.loads(mf.read_text()).get('results') or [])
            if IS_SETTLED(str(r.get('status', '')))]
    decided: dict[str, dict] = {}
    if led.exists():
        for line in led.read_text().splitlines():
            try:
                e = json.loads(line)
                decided[e['url']] = e
            except Exception:
                continue
    # git-HEAD check for absorbed pages — HEAD, not the index: a git-add
    # without a commit must NOT fake coverage (Grok F2)
    head_paths = set()
    absorbed_pages = sorted({e.get('page') for e in decided.values()
                             if e.get('decision') == 'absorbed' and e.get('page')})
    if absorbed_pages:
        r = subprocess.run(['git', '-C', str(REPO), 'ls-tree', '-r', 'HEAD',
                            '--name-only', '--'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(json.dumps({'ym': ym, 'error': 'git-error', 'complete': False}))
            return 1
        head_paths = {l for l in r.stdout.splitlines() if l}
    covered, uncovered = 0, []
    for u in urls:
        e = decided.get(u)
        if not e or e.get('decision') not in ('absorbed', 'skipped', 'hold'):
            uncovered.append(u); continue
        if e['decision'] == 'absorbed':
            page = e.get('page')
            if not page or page not in head_paths:
                uncovered.append(u); continue
        covered += 1
    print(json.dumps({'ym': ym, 'total': len(urls), 'decided': covered,
                      'complete': covered == len(urls) and bool(urls),
                      'uncovered': uncovered[:50], 'uncovered_n': len(uncovered)},
                     ensure_ascii=False))
    return 0 if covered == len(urls) else 2

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    if args[0] == 'prep':
        ym = args[1]
        b = 8
        if '--batch' in args:
            b = int(args[args.index('--batch') + 1])
        sys.exit(prep(ym, b))
    elif args[0] == 'ledger-coverage':
        sys.exit(ledger_coverage(args[1]))
    print(f'unknown verb {args[0]}'); sys.exit(1)
