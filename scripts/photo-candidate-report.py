#!/usr/bin/env python3
"""Photo candidate report — page <-> image matches with provenance + confidence.

Design (Leonard 2026-10-11): we do NOT claim the photo is verified. Every
linkable match ships with a standing label that states provenance and the
unverified-but-high-probability status, so the reader, not Echo, is the final
checker. The report is the deliverable; linking is a separate, human-GO step.

Confidence tiers
  HIGH  full hanzi name appears in the image caption, exactly one person
        candidate matched, caption has no other known person's name
  MED   name matched but caption also names another known person (左/右 style)
        OR only given-name (2-char) match
  LOW   everything else that matched at all (skip linking)

Ambiguity is a hard veto, not a penalty: if two different person pages match
one caption, the pair goes to LOW and the report says why.
"""
import json, os, re, sys, glob, collections

VAULT = '/home/leedt/echo-system'
IMG_ROOTS = [
    os.path.join(VAULT, 'knowledge/web-archives/taiwanjustice-net/raw-html'),
    os.path.join(VAULT, 'knowledge/interactions/photos'),
    os.path.join(VAULT, 'knowledge/interactions/onboarding'),
]
OUT_JSON = os.path.join(VAULT, 'knowledge/operational/photo-candidates.jsonl')
OUT_MD = os.path.join(VAULT, 'knowledge/operational/photo-candidates.md')

HANZI = r'[\u4e00-\u9fff]'

def load_people():
    """name_zh (and any hanzi inside title) -> slug. Ambiguous names are dropped."""
    by_name = collections.defaultdict(set)
    for p in glob.glob(os.path.join(VAULT, 'content/people/*.md')):
        slug = 'people/' + os.path.basename(p)[:-3]
        try:
            head = open(p, encoding='utf-8', errors='ignore').read(1200)
        except Exception:
            continue
        names = set()
        m = re.search(r'name_zh:\s*"?([^"\n]+)', head)
        if m:
            names.add(m.group(1).strip())
        m = re.search(r'title:\s*"?([^"\n]+)', head)
        if m:
            for h in re.findall(HANZI + r'{2,4}', m.group(1)):
                names.add(h)
        for n in names:
            if re.fullmatch(HANZI + '{2,4}', n):
                by_name[n].add(slug)
    # a name owned by 2+ pages is vault ambiguity, not our matching problem
    return {n: next(iter(s)) for n, s in by_name.items() if len(s) == 1}, \
           {n: sorted(s) for n, s in by_name.items() if len(s) > 1}

def caption_from_path(p):
    base = os.path.basename(p)
    # strip timestamp/hash/size-suffix noise, keep the caption run
    base = re.sub(r'^\d{14}_', '', base)
    base = re.sub(r'[-_][0-9a-f]{16}\.(jpe?g|png|webp)$', '', base, flags=re.I)
    base = re.sub(r'[-_]\d{2,4}[xX]\d{2,4}\.(jpe?g|png|webp)$', '', base, flags=re.I)
    base = re.sub(r'\.(jpe?g|png|webp)$', '', base, flags=re.I)
    base = re.sub(r'wp-content_uploads_\d{2,4}_\d{2}_', '', base)
    return base

def provenance(img):
    j = img + '.json'
    if os.path.exists(j):
        try:
            d = json.load(open(j))
            return dict(source_url=d.get('source_url', ''),
                        archive_url=d.get('archive_url', ''),
                        archive_ts=d.get('archive_ts', ''),
                        sha256=d.get('sha256', '')[:12])
        except Exception:
            pass
    return {}

def main():
    names, ambiguous_names = load_people()
    print(f"person names indexed: {len(names)} unique, {len(ambiguous_names)} ambiguous-in-vault")

    imgs = []
    for root in IMG_ROOTS:
        for ext in ('jpg', 'jpeg', 'png', 'webp'):
            imgs += glob.glob(os.path.join(root, '**', '*.' + ext), recursive=True)
            imgs += glob.glob(os.path.join(root, '**', '*.' + ext.upper()), recursive=True)
    imgs = sorted(set(imgs))
    print(f"images scanned: {len(imgs)}")

    matches = []
    for img in imgs:
        cap = caption_from_path(img)
        hits = {n: s for n, s in names.items() if n in cap}
        amb = {n: sl for n, sl in ambiguous_names.items() if n in cap}
        if not hits and not amb:
            continue
        # count how many OTHER known names appear (multi-person caption?)
        others = [n for n in names if n in cap and n not in hits] + list(amb)
        if len(hits) == 1 and not others:
            tier = 'HIGH'
            slug = next(iter(hits.values()))
        elif len(hits) == 1 and others:
            tier = 'MED'   # 左/右 style: subject probably here, but who is who?
            slug = next(iter(hits.values()))
        else:
            tier = 'LOW'
            slug = sorted(hits.values())[0] if hits else None
        matches.append(dict(image=os.path.relpath(img, VAULT), caption=cap[:120],
                            person=slug, tier=tier, **provenance(img)))

    order = {'HIGH': 0, 'MED': 1, 'LOW': 2}
    matches.sort(key=lambda m: (order[m['tier']], m.get('person') or 'zz'))
    with open(OUT_JSON, 'w') as f:
        for m in matches:
            f.write(json.dumps(m, ensure_ascii=False) + '\n')

    c = collections.Counter(m['tier'] for m in matches)
    pages = collections.Counter(m['person'] for m in matches if m['tier'] == 'HIGH')
    print(f"matched images: {len(matches)}  HIGH={c['HIGH']} MED={c['MED']} LOW={c['LOW']}")
    print(f"person pages with >=1 HIGH match: {len(pages)}")

    with open(OUT_MD, 'w') as f:
        f.write("# Photo candidate report\n\n")
        f.write(f"- images scanned: {len(imgs)}\n")
        f.write(f"- matched: {len(matches)} (HIGH {c['HIGH']} / MED {c['MED']} / LOW {c['LOW']})\n")
        f.write(f"- person pages with a HIGH match: {len(pages)}\n\n")
        f.write("HIGH = full hanzi name, single-person caption. MED = caption also names\n")
        f.write("another known person (who-is-who ambiguity). LOW = do not link.\n\n")
        f.write("## HIGH — linkable with standing unverified-photo label\n\n")
        for m in matches:
            if m['tier'] != 'HIGH':
                break
            f.write(f"- `{m['person']}` ← `{m['image']}`\n")
            if m.get('source_url'):
                f.write(f"  - src: {m['source_url'][:110]}  (wayback {m.get('archive_ts','')})\n")
        f.write("\n## MED — needs a human who-is-who call\n\n")
        for m in matches:
            if m['tier'] != 'MED':
                break
            f.write(f"- `{m['person']}` ← `{m['image']}`\n  - caption: {m['caption']}\n")
    print("wrote:", OUT_MD)

if __name__ == '__main__':
    main()
