#!/usr/bin/env python3
"""Bulk photo rollout — HIGH matches only, largest image per person.

Same block as the 5-page pilot (verified live 2026-10-11): ## 照片 + caption +
provenance label. Skips pages that already have ## 照片. Copies image into
content/images/ (Assets emitter ships it; publish.sh tree-copies images/).
"""
import json, os, re, shutil

REPO = '/home/leedt/echo-system'
PLAN = os.path.join(REPO, '.staging/photo-links/plan.json')
LABEL = ('📷 照片取自公開檔案（來源：taiwanjustice.net，Wayback 存檔 {ts}）。'
         '圖說為原始來源所提供，Echo 未經人工逐張查證——若您認得圖中人，歡迎回報修正。')

plan = json.load(open(PLAN))
by = {}
for p in plan:
    by.setdefault(p['person'], []).append(p)

linked, skipped = [], []
for slug, cands in sorted(by.items()):
    md = os.path.join(REPO, 'content', slug + '.md')
    if not os.path.exists(md):
        skipped.append((slug, 'no-page'))
        continue
    t = open(md, encoding='utf-8').read()
    if '## 照片' in t:
        skipped.append((slug, 'already'))
        continue
    big = [c for c in cands if c.get('w', 0) * c.get('h', 1) >= 20000]
    if not big:
        big = cands
    img = max(big, key=lambda c: c.get('w', 0) * c.get('h', 1))
    ext = os.path.splitext(img['src'])[1].lower()
    base = slug.replace('/', '--')
    dest = f"content/images/{base}{ext}"
    shutil.copyfile(os.path.join(REPO, img['src']), os.path.join(REPO, dest))
    cap = re.sub(r'[-_]\d{2,4}[xX]\d{2,4}$', '', img.get('caption', '')).replace('_', ' ').strip()
    if not cap:
        cap = os.path.splitext(os.path.basename(img['src']))[0][:60]
    block = (f"\n## 照片\n\n![{cap}](../images/{base}{ext})\n\n"
             f"{LABEL.format(ts=img.get('archive_ts', ''))}\n")
    open(md, 'w', encoding='utf-8').write(t.rstrip('\n') + '\n' + block)
    linked.append(slug)

print(f"linked: {len(linked)}  skipped: {len(skipped)}")
for s, why in skipped[:10]:
    print(f"  skip {s}: {why}")
