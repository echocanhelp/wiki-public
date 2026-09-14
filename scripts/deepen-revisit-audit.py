#!/usr/bin/env python3
"""Revisit audit: pages deepened by the swarm (last_reviewed 2026-09-06..) that
have corpus mentions in works/articles but ZERO wikilinks into the corpus.
Those are the gwhyneth-class misses: deepened, but mission layer missed."""
import os, re, glob, subprocess
from pathlib import Path
REPO = Path('/home/leedt/echo-system')
os.chdir(REPO)

# corpus index: for every work/article page, which people/org slugs does it mention?
# cheap proxy: build name->files map from person/org frontmatter names, then one grep pass
corpus_files = []
for pat in ('content/works/**/*.md', 'content/articles/**/*.md'):
    corpus_files.extend(glob.glob(str(REPO/pat), recursive=True))
corpus_blob = {}
for f in corpus_files:
    try:
        t = open(f, encoding='utf-8', errors='ignore').read()
    except Exception:
        continue
    if len(t) > 400:
        corpus_blob[os.path.relpath(f, REPO)] = t

def corpus_hits(names):
    hits = 0
    for f, t in corpus_blob.items():
        for n in names:
            if n and n in t:
                hits += 1
                break
    return hits

flagged, checked = [], 0
for pf in glob.glob('content/people/*.md') + glob.glob('content/organizations/*.md'):
    try:
        txt = (REPO/'content'/os.path.relpath(pf,'content') if False else open(REPO/pf, encoding='utf-8', errors='ignore')).read()
    except Exception:
        continue
    m = re.search(r'last_reviewed:\s*(\d{4}-\d{2}-\d{2})', txt)
    if not (m and m.group(1) >= '2026-09-06'):
        continue
    checked += 1
    names = set()
    for key in ('name_zh', 'name_en', 'title'):
        mm = re.search(rf'^{key}:\s*"?([^"\n]+)"?', txt, re.M)
        if mm:
            v = mm.group(1).strip()
            v = re.split(r'\s*\(', v)[0].strip()
            if len(v) >= 2:
                names.add(v)
    if not names:
        continue
    has_link = re.search(r'\[\[(works/|articles/)', txt)
    if has_link:
        continue
    h = corpus_hits(names)
    if h >= 1:
        flagged.append((h, pf.replace('content/',''), os.path.getsize(REPO/pf)))

flagged.sort(reverse=True)
print(f'swarm-reviewed pages checked: {checked}')
print(f'gwhyneth-class (zero corpus links but >=1 corpus mention): {len(flagged)}')
print('top 15 by mention count (mentions, path, bytes):')
for h, p, s in flagged[:15]:
    print(f'  {h:3d}  {s:6d}B  {p}')
