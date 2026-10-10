#!/usr/bin/env python3
"""Rewrite bloated ## Timeline sections: life events visible, news mentions collapsed.

Rule (Leonard 2026-10-11: long pages are noisy — 75% of timeline bullets corpus-wide
are 📰 wire/tag noise):
  - life events (no 📰 marker) stay visible, chronological
  - 📰 mentions move into a collapsed <details> fold whose summary states the count
    and year range — nothing deleted, labeling does the work
  - inside the fold, dedupe by normalized title (Tag: prefix stripped, whitespace/
    punctuation folded): same story twice becomes one line with (xN)
Nothing outside ## Timeline is touched. Idempotent: running twice is a no-op.
Usage: python3 timeline-fold-noise.py [--dry] [slug ...]   (default: all pages with >50 bullets)
"""
import os, re, sys, glob

CONTENT = '/home/leedt/echo-system/content'
THRESH = 50

def norm_title(t):
    t = re.sub(r"^'?\s*Tag:\s*", '', t)
    t = re.sub(r"[『「\"'']|[_\-—－]", '', t)
    t = re.sub(r"\s+", '', t)
    return t[:60].lower()

def fold(section_body):
    """section_body = text after '## Timeline' header to next '## '."""
    bullets = re.findall(r'^\s*[-*]\s+.+$', section_body, re.M)
    if len(bullets) <= THRESH:
        return None
    # noise = 'Tag:' lines ANY emoji: the builder keyword-matches article text,
    # so tag-noise arrives as 🗳️/🏥/🕯️ just as often as 📰. Emoji is not the
    # discriminator — the Tag: prefix is (measured: 85% of heavy-page bullets).
    life, news = [], []
    for b in bullets:
        if re.search(r"'?\s*Tag:", b):
            news.append(b)
        else:
            life.append(b)
    # dedupe news by normalized title, keep first date + count
    seen = {}
    order = []
    for b in news:
        m = re.match(r"^(\s*[-*]\s+\*\*\d{4}-\d{2}-\d{2}\*\*)\s*(?:📰\s*)?['\"]?\s*Tag:\s*(.*)$", b)
        if m:
            key = norm_title(m.group(2))
        else:
            key = norm_title(re.sub(r'^.*?Tag:\s*', '', b))
        if key in seen:
            seen[key]['n'] += 1
            continue
        seen[key] = {'raw': b, 'n': 1}
        order.append(key)
    dedup = []
    for k in order:
        line = seen[k]['raw']
        if seen[k]['n'] > 1:
            line = re.sub(r'\s*$', f"  ({seen[k]['n']}×)", line)
        dedup.append(line)
    years = [re.search(r'\*\*(\d{4})-', b).group(1) for b in news if re.search(r'\*\*(\d{4})-', b)]
    yr = f"{min(years)}–{max(years)}" if years else "n.d."
    out = "## Timeline\n\n"
    if life:
        out += "\n".join(life) + "\n"
    else:
        out += "_（無可確認生平事件；以下為新聞紀錄）_\n"
    icon = "📰" if any("📰" in l for l in news) else "🗂"
    out += f"\n<details>\n<summary>{icon} 檔案紀錄 — {len(news)} 則提及（{yr}），去重後 {len(dedup)} 條</summary>\n\n"
    out += "\n".join(dedup) + "\n\n</details>\n"
    return out

def process(path, dry=False):
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^##\s+Timeline\s*\n(.*?)(?=^## |\Z)', t, flags=re.M | re.S)
    if not m:
        return 'no-timeline'
    new = fold(m.group(1))
    if new is None:
        return 'below-threshold'
    if '<details>' in m.group(1):
        return 'already-folded'
    if not dry:
        t = t[:m.start()] + new + '\n' + t[m.end():]
        open(path, 'w', encoding='utf-8').write(t)
    return 'folded'

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry' in sys.argv
    if args:
        paths = [os.path.join(CONTENT, p if p.endswith('.md') else p + '.md') for p in args]
    else:
        paths = glob.glob(CONTENT + '/people/*.md') + glob.glob(CONTENT + '/organizations/*.md')
    counts = {}
    for p in paths:
        r = process(p, dry)
        counts[r] = counts.get(r, 0) + 1
        if r == 'folded' and not dry:
            pass
    print(counts)
