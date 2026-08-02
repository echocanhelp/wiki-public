#!/usr/bin/env python3
"""No-op featured regen stub — inject skipped if markers missing."""
import argparse
from pathlib import Path
ap = argparse.ArgumentParser()
ap.add_argument('--root', default='.')
ap.add_argument('--inject', action='store_true')
ap.add_argument('--recency-window', type=int, default=30)
ap.add_argument('--max-people', type=int, default=6)
ap.add_argument('--max-orgs', type=int, default=3)
ap.add_argument('--dry-run', action='store_true')
args = ap.parse_args()
root = Path(args.root)
for name in ('index.html', 'public/index.html'):
    p = root / name
    if not p.exists():
        print(f'featured-regen: skip missing {p}')
        continue
    t = p.read_text(errors='replace')
    if '<!-- featured-start -->' not in t:
        print(f'featured-regen: no markers in {p}, skip')
        continue
    print(f'featured-regen: markers present in {p} (no-op keep)')
print('featured-regen: done')
