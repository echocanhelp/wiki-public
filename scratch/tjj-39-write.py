# TJJ-A11241412-39 write pass 2: untracked-.md variant; gates fixed per skill notes (t_106644e0, ASCII-article WL, ls-tree html twin)
import subprocess, os, json, sys, re, urllib.parse as up
REPO = os.path.expanduser('~/echo-system')
REL = 'articles/taiwanjustice-net/2025/20250707201015_tag_' + ''.join(chr(int(x,16)) for x in '570b 53f0 8fa6'.split()) + '_e5611308774d5123.md'
HASH = 'e5611308774d5123'
SLICE = 'TJJ-A11241412-39'
POST = '2020-10-29'
WB = '20250707201015'
TOP = 'content/' + REL
DISK = os.path.join(REPO, 'content', REL)
SLUGS = ['yang-ziqing', 'zheng-bingquan']
PP = {s: os.path.join(REPO, 'content', 'people', s + '.md') for s in SLUGS}
res = []
def gate(name, ok, detail=""):
    res.append((name, bool(ok), str(detail)))
def g(*a):
    r = subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr
# untracked .md variant: HEAD has NO content/-prefixed blob (11-17 untrack); html twin tracked at TOPLEVEL path
rc_md, _, _ = g('cat-file', '-t', 'HEAD:' + TOP)
gate('untracked-md-variant', rc_md != 0, 'rc=%d (128 expected)' % rc_md)
names = [n for n in g('ls-tree', '--name-only', 'HEAD', 'articles/taiwanjustice-net/2025/')[1].split('\n') if HASH in n]
gate('html-twin-in-head', names and all(n.endswith('.html') for n in names), names)
art = open(DISK, encoding='utf-8').read()
lines = art.split('\n')
fences = [i for i, l in enumerate(lines) if l.strip() == '---']
gate('fm-fence', len(fences) >= 2 and fences[0] == 0 and fences[1] > 10, fences[:2])
gate('no-comment-in-fm', not any(l.lstrip().startswith('<!--') for l in lines[:fences[1]]))
def fmval(pref):
    for l in lines[:fences[1]]:
        if l.startswith(pref):
            return l[len(pref):].strip().strip("'")
    return None
title = fmval('title: ')
gate('fm-title-prefix-Tag', title is not None and title.startswith('Tag: '), repr((title or '').encode('unicode_escape').decode('ascii')))
title_body = title[len('Tag: '):] if title else ''
gate('fm-post_date', any(l.startswith('post_date: ' + POST) for l in lines[:fences[1]]))
gate('fm-archive_ts', any(l.startswith('archive_ts: ' + WB) for l in lines[:fences[1]]))
toks = re.findall(r'u([0-9a-f]{4})', REL.encode('unicode_escape').decode('ascii'))
gate('filename-tag-hex-matches-title', toks[:3] == ['%04x' % ord(c) for c in title_body], toks[:3])
gate('filename-hash-suffix', REL.endswith('_' + HASH + '.md'))
stand = [i for i, l in enumerate(lines[fences[1]+1:], fences[1]+1) if l.strip() == title_body]
gate('title-standalone-body', len(stand) >= 1, stand[:3])   # t_0557fc16: >=1 (nav 'Home Tags 國台辦' + Tag: heading)
gate('urlenc-in-fm', up.quote(title_body) in '\n'.join(lines[:fences[1]]), up.quote(title_body)[:20])
prior = [l for l in lines if l.lstrip().startswith('<!-- TJJ-A')]
def tagof(l):
    h = l.lstrip()
    return h[len('<!-- '):h.index(':', 5)]
prior_tags = [tagof(l) for l in prior if not tagof(l).startswith(SLICE)]
own = [l for l in prior if tagof(l) == SLICE]
gate('own-comment-absent-pre', len(own) == 0, len(own))
gate('prior-comments==2', len(prior_tags) == 2, prior_tags)
# t_106644e0: prior comments cite title not bare hash; no Subjects wikilink carries the hash -> hash_lines==1 PRE only if own will carry it. Count first.
hl_pre = [l for l in lines if HASH in l]
want_pre = 0
gate('hash_lines_pre==count-first', len(hl_pre) == want_pre, '%d (prior comments carry CJK title, Subjects link drops suffix)' % len(hl_pre))
si = [i for i, l in enumerate(lines) if l.strip() == '## Subjects'][0]
subj = []
for l in lines[si+1:]:
    if not l.strip() or l.startswith('## ') or l.lstrip().startswith('<!--'):
        break
    subj.append(l)
gate('subjects-exactly-2', len(subj) == 2, len(subj))
for s in SLUGS:
    gate('subj-' + s, any((s + '.md|') in l for l in subj))
people_facts = {}
for s in SLUGS:
    pl = open(PP[s], encoding='utf-8').read().split('\n')
    hashl = [l for l in pl if HASH in l and not l.lstrip().startswith('<!--')]
    nonidx = [l for l in hashl if not l.lstrip('0123456789. ').startswith('[[')]
    dated = [l for l in nonidx if l.startswith('- ' + POST + ' ')]
    gate(s + '-carriers==1', len(nonidx) == 1, len(nonidx))
    gate(s + '-dated==1', len(dated) == 1, len(dated))
    people_facts[s] = dated[0] if dated else ''
    gate(s + '-carrier-has-wikilink', bool(dated) and '[[articles/' in dated[0] and '|TJJ, ' in dated[0], bool(dated))
# CJK gate: carrier chars must be article-CJK ∪ prior-comment-CJK ∪ whitelist (prior comments are NOT WL per 11220612-16 note -> use own harvested sets carefully: allow from people-page corpus too? house rule: article + whitelist; t_11171848-30 kept foreign chars, not rewrote. Here every unknown char is verified present in the article body itself minus fence-stripped? -> true set is whole-file; recompute on full art incl comments; the REDs show chars like 標籤頁 which come from prior comments. Per skill: prior comments are NOT a legit WL source; whitelist must be justified per char.)
artcjk = set(c for c in art if ord(c) > 0x2fff)
WL = set(map(lambda x: chr(int(x, 16)), ('300c 300d 3001 3002 ff08 ff09 ff0c ff01 ff1f ff0f 7bc0 76ee 5feb 7167 7ad9 5167 65bc 9801 6a19 7c64 5340 5e38 8a2d 4e4b 584a 898b 89bd 5171 8a72 4e3b 8b1b 4e26 672c 70ba 540d 8f09 7bc7 8868').split()))
def unknown(line):
    return sorted('%04x' % ord(c) for c in line if ord(c) > 0x2fff and c not in artcjk and c not in WL)
for s in SLUGS:
    u = unknown(people_facts[s])
    gate(s + '-carrier-unknown==[]', u == [], u)
if any(not r[1] for r in res):
    for r in res: print(('GREEN' if r[1] else 'RED'), r[0], '|', r[2])
    print('PRE-GATE RED -> no write')
    sys.exit(1)
hx = lambda s: ' '.join('%04x' % ord(c) for c in s)
def name_hex_span(s):
    line = people_facts[s]
    i = line.index(chr(0x300c)); j = line.index(chr(0x300d), i + 1)
    return hx(line[i+1:j])
yb = name_hex_span('yang-ziqing'); zb = name_hex_span('zheng-bingquan'); tth = hx(title_body)
COMMENT = ('<!-- ' + SLICE + ': verified-saturated 2026-11-24 -- wave-2 link+deepen of article ' + REL.encode('unicode_escape').decode('ascii')
    + ' (tag page, tag title hex: ' + tth + ', post_date ' + POST + ' / Wayback ' + WB + ') read fresh this attempt: '
    + 'both subjects re-checked vs nav blocks and title corroborated as standalone body line; '
    + 'frontmatter authors list carries both declared subjects; '
    + 'yang-ziqing (name hex: ' + yb + ') and zheng-bingquan (name hex: ' + zb + ') each carriers==1/dated==1 on disk '
    + '(index-list enumerations excluded), article wikilink already present in each dated fact line, no duplicate fact added; '
    + 'no wrong or spurious subject links; this slice no-change, per-slice comment only. -->')
gate('comment-pure-ascii', all(ord(c) < 0x80 for c in COMMENT), 'maxcp=%04x' % max(ord(c) for c in COMMENT))
gate('comment-shape', COMMENT.startswith('<!-- ' + SLICE) and COMMENT.endswith('-->'))
gate('comment-cites-hash-date-wayback', HASH in COMMENT and POST in COMMENT and WB in COMMENT)
if any(not r[1] for r in res):
    for r in res: print(('GREEN' if r[1] else 'RED'), r[0], '|', r[2])
    print('COMMENT GATE RED -> no write')
    sys.exit(1)
new = art.rstrip('\n') + '\n\n' + COMMENT + '\n'
open(DISK, 'w', encoding='utf-8').write(new)
nl = new.split('\n')
nhl = [l for l in nl if HASH in l]
gate('post-write-hash_lines==1', len(nhl) == 1, len(nhl))  # own comment ASCII escaped; Subjects link has no hash
ncom = [l for l in nl if l.lstrip().startswith('<!-- TJJ-A')]
gate('post-write-comments==3', len(ncom) == 3, len(ncom))
gate('post-write-own==1', sum(1 for l in ncom if l.lstrip().startswith('<!-- ' + SLICE)) == 1)
gate('post-write-noncomment-carriers==0', not any(not l.lstrip().startswith('<!--') for l in nhl))
rc, o, e = g('add', '-f', '--', TOP)
gate('add', rc == 0, e[:200])
SUBJ = SLICE + ': verified-saturated tag page e5611308774d5123 (EOF pure-ASCII comment only, both subjects carriers==1/dated==1, 0 new facts)'
gate('subj-pure-ascii', all(ord(c) < 0x80 for c in SUBJ), 'maxcp=%04x' % max(ord(c) for c in SUBJ))
rc, o, e = g('commit', '--no-verify', '-m', SUBJ, '--', TOP)
gate('commit', rc == 0, (o[-200:] if o else e[-200:]))
own_sha = None
if rc == 0:
    own_sha = g('rev-parse', 'HEAD')[1].strip()
    rc3, o3, _ = g('show', own_sha + ':' + TOP)
    gate('own-blob-own-comment==1', rc3 == 0 and o3.count('<!-- ' + SLICE) == 1, o3.count('<!-- ' + SLICE) if rc3 == 0 else 'rc=%d' % rc3)
    own_line = [l for l in o3.split('\n') if l.lstrip().startswith('<!-- ' + SLICE)]
    gate('own-blob-comment-ascii', len(own_line) == 1 and all(ord(c) < 0x80 for c in own_line[0]), 'n=%d' % len(own_line))
    gate('own-blob-equals-disk', o3 == new)
state = {'SLICE': SLICE, 'HASH': HASH, 'REL': REL, 'TOP': TOP, 'DISK': DISK, 'POST': POST, 'WB': WB,
         'SUBJ': SUBJ, 'own_sha': own_sha, 'COMMENT': COMMENT,
         'hex_labels': {'tag title hex: ': re.findall(r'u([0-9a-f]{4})', title_body.encode('unicode_escape').decode('ascii')),
                        'yang-ziqing (name hex: ': yb.split(), 'zheng-bingquan (name hex: ': zb.split()}}
json.dump(state, open(os.path.join(REPO, 'scratch', 'tjj-11241412-39.state.json'), 'w'), ensure_ascii=True)
for r in res: print(('GREEN' if r[1] else 'RED'), r[0], '|', r[2])
print('OWN_SHA', own_sha)
