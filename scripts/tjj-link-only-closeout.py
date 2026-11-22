#!/usr/bin/env python3
"""Deterministic link-only closeout for a TJJ article (lane policy 1103).

Gates (recomputed from git HEAD, never from worker last_output):
  1. own EOF comment count == 1 and comment is pure ASCII
  2. verified-saturation line present (below closing fence)
  3. every [[people/...]] link in the file resolves to an existing page
Exit 0 = all gates pass (card may be closed); exit 1 = defect (report lines).
Usage: tjj-link-only-closeout.py <repo-relative-article-path> <card-title-prefix>
"""
import os
import re
import subprocess
import sys

def main():
    path, prefix = sys.argv[1], sys.argv[2]
    repo = os.path.expanduser('~/echo-system')
    txt = subprocess.run(['git', '-C', repo, 'show', f'HEAD:{path}'],
                         capture_output=True, text=True, check=True).stdout
    fails = []

    own = re.findall(rf'<!-- {re.escape(prefix)}.*?-->', txt, re.S)
    if len(own) != 1:
        fails.append(f'own-comment count={len(own)} (want 1)')
    elif not all(ord(c) < 0x80 for c in own[0]):
        bad = sorted({hex(ord(c)) for c in own[0] if ord(c) >= 0x80})
        fails.append(f'own-comment not ASCII, codepoints={bad[:8]}')

    if not re.search(r'(?m)^verified-saturation: \d{4}-\d{2}-\d{2}$', txt):
        fails.append('verified-saturation line missing')

    people = re.findall(r'\[\[people/([^|\]]+)', txt)
    def _page(p):
        # Subjects lines carry the .md suffix (people/x.md), frontmatter authors do not;
        # strip it before resolving so both forms gate clean.
        stem = p[:-3] if p.endswith('.md') else p
        return os.path.exists(os.path.join(repo, 'content', 'people', f'{stem}.md'))
    missing = sorted({p for p in people if not _page(p)})
    if missing:
        fails.append(f'people links with no page: {missing}')

    print(f'{"PASS" if not fails else "FAIL"} {path} [{prefix}] '
          f'people_links={len(people)} own_comments={len(own)}')
    for f in fails:
        print('  -', f)
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
