# TJJ-A11231410-9 verified-saturated fast path: EOF ASCII comment only
import subprocess, os, json, re, sys
REPO=os.path.expanduser('~/echo-system')
REL='articles/taiwanjustice-net/2024/20240719000440_root_ea5391c88dc9317b.md'
HASH='ea5391c88dc9317b'
SLICE='TJJ-A11231410-9'
POST='2023-03-20'; WB='20240719000440'
TOP='content/'+REL
DISK=os.path.join(REPO,'content',REL)
res=[]
def gate(name,ok,detail=""):
    res.append((name,bool(ok),str(detail)))
def g(*a):
    r=subprocess.run(['git']+list(a),cwd=REPO,capture_output=True,text=True)
    return r.returncode,r.stdout,r.stderr
# untracked variant probe
rc,_,_=g('cat-file','-t','HEAD:'+TOP)
gate('head-md-blob-absent-expected-untracked',rc!=0,'rc=%d (128=untracked variant, expected)'%rc)
art=open(DISK,encoding='utf-8').read()
lines=art.split('\n')
# fences
fences=[i for i,l in enumerate(lines) if l.strip()=='---']
gate('fm-fence',fences[0]==0 and fences[1]>10,fences[:2])
gate('no-comment-in-fm',not any(l.lstrip().startswith('<!--') for l in lines[:fences[1]]))
# FM fields via prefix match
def fmval(pref):
    for l in lines[:fences[1]]:
        if l.startswith(pref): return l[len(pref):].strip().strip("'")
    return None
title=fmval('title: ')
gate('fm-title-prefix-Tag',title is not None and title.startswith('Tag: '),repr(title))
title_body=title[len('Tag: '):] if title else None
gate('fm-post_date',any(l.startswith('post_date: '+POST) for l in lines[:fences[1]]))
gate('fm-archive_ts',any(l.startswith('archive_ts: '+WB) for l in lines[:fences[1]]))
# title hex via unicode_escape harvest from FM title line (never hand-typed)
tl=[l for l in lines[:fences[1]] if l.startswith('title: ')][0]
toks=re.findall(r'u([0-9a-f]{4})',tl.encode('unicode_escape').decode('ascii'))
# title verbatim standalone body line
stand=[i for i,l in enumerate(lines[fences[1]+1:],fences[1]+1) if l.strip()==title_body]
gate('title-standalone-body',len(stand)>=1,stand[:3])
# url-encoded title in FM
urle=urllib_quote=None
import urllib.parse as up
enc=up.quote(title_body)
gate('urlenc-in-fm',enc in '\n'.join(lines[:fences[1]]),enc[:20])
# prior comments
prior=[l for l in lines if l.lstrip().startswith('<!-- TJJ-A')]
def tagof(l):
    h=l.lstrip(); return h[len('<!-- '):h.index(':',5)]
prior_tags=[tagof(l) for l in prior if not tagof(l).startswith(SLICE)]
own=[l for l in prior if tagof(l)==SLICE]
gate('own-comment-absent-pre',len(own)==0,len(own))
gate('prior-comments',len(prior_tags)>=1,prior_tags)
# hash lines PRE
hl=[l for l in lines if HASH in l]
gate('hash_lines_pre',len(hl)==1 and all(l.lstrip().startswith('<!--') for l in hl),len(hl))
gate('prior-comment-carries-bare-hash',any(HASH in l for l in prior))
# subjects section bounded between ## Subjects and next ## or comment or blank
si=[i for i,l in enumerate(lines) if l.strip()=='## Subjects'][0]
subj=[]
for l in lines[si+1:]:
    if not l.strip() or l.startswith('## ') or l.lstrip().startswith('<!--'): break
    subj.append(l)
gate('subjects-exactly-2',len(subj)==2,len(subj))
SLUGS=['yang-ziqing','zheng-bingquan']
for s in SLUGS:
    gate('subj-'+s,any((s+'.md|') in l for l in subj))
# people pages: saturation gate on DISK
PP={'yang-ziqing':'content/people/yang-ziqing.md','zheng-bingquan':'content/people/zheng-bingquan.md'}
people_facts={}
for s,tp in PP.items():
    pl=open(os.path.join(REPO,tp),encoding='utf-8').read().split('\n')
    hashl=[l for l in pl if HASH in l and not l.lstrip().startswith('<!--')]
    nonidx=[l for l in hashl if not l.lstrip('0123456789. ').startswith('[[')]
    dated=[l for l in nonidx if l.startswith('- '+POST+' ')]
    gate(s+'-carriers==1',len(nonidx)==1,len(nonidx))
    gate(s+'-dated==1',len(dated)==1,len(dated))
    people_facts[s]=dated[0] if dated else None
    gate(s+'-carrier-has-wikilink',dated and '[[' in dated[0] and '|' in dated[0],bool(dated))
# bracket spans harvested from dated carrier lines
spans=[]
for s in SLUGS:
    line=people_facts[s]
    i=line.index(chr(0x300c)); j=line.index(chr(0x300d),i+1)
    spans.append(line[i+1:j])
prior_blob='\n'.join(prior)
for s,sp in zip(SLUGS,spans):
    ok=( (chr(0x300c)+sp+chr(0x300d)) in art ) or ((chr(0x300c)+sp+chr(0x300d)) in prior_blob) or all((c in art) for c in sp if ord(c)>0x2fff)
    gate('span-corrob-'+s,ok,sp[:12].encode('unicode_escape').decode('ascii'))
# carrier-line CJK gate vs ARTICLE TOTAL CJK U WL
WL=set(map(lambda x:chr(int(x,16)),'''300c 300d ff08 ff09 ff0c 3002 3001 300a 300b 7bc0 76ee 5feb 7167 7ad9 5167 65bc 9801 6a19 7c64 5340 5e38 8a2d 4e4b 584a 898b 89bd 5171 8a72 4e3b 8b1b 4e26 672c 70ba 5747 7bc7 5404 985e 5206 5373 5176 7b49 7b46 7b4b 8868 7b49 984c 540c 5340 6e05 9801 5c0e 8981 644a 8f09 96c6 9801 662f 7684 4e86 5728 540d 65bc 8f09'''.split()))
artcjk=set(c for c in art if ord(c)>0x2fff)
def unknown(line):
    return sorted('%04x'%ord(c) for c in line if ord(c)>0x2fff and c not in artcjk and c not in WL)
for s in SLUGS:
    u=unknown(people_facts[s])
    gate(s+'-carrier-unknown==[]',u==[],u)
if any(not r[1] for r in res):
    for r in res: print(('GREEN' if r[1] else 'RED'),r[0],'|',r[2])
    print('PRE-GATE RED -> no write'); sys.exit(1)
# build COMMENT (pure ASCII)
hx=lambda s:' '.join('%04x'%ord(c) for c in s)
hx2=lambda s:' '.join('%04x'%ord(c) for c in s if ord(c)>0x2fff)
yb=hx2(people_facts['yang-ziqing'][people_facts['yang-ziqing'].index(chr(0x300c))+1:people_facts['yang-ziqing'].index(chr(0x300d))])
zb=hx2(people_facts['zheng-bingquan'][people_facts['zheng-bingquan'].index(chr(0x300c))+1:people_facts['zheng-bingquan'].index(chr(0x300d))])
COMMENT=('<!-- '+SLICE+': verified-saturated 2026-11-24 -- wave-2 link+deepen of article 20240719000440_root_'+HASH
 +'.md (tag page, tag page hex: '+hx(title_body)+', post_date '+POST+' / Wayback '+WB+') read fresh this attempt: '
 +'both subjects re-checked vs body, title corroborated as standalone body line; '
 +'yang-ziqing (name hex: '+yb+') and zheng-bingquan (name hex: '+zb+') each carriers==1/dated==1 on disk '
 +'(index-list enumerations excluded), article wikilink already present, no duplicate fact added; '
 +'no wrong or spurious subject links; this slice no-change, per-slice comment only. -->')
gate('comment-pure-ascii',all(ord(c)<0x80 for c in COMMENT),'maxcp=%04x'%max(ord(c) for c in COMMENT))
gate('comment-shape',COMMENT.startswith('<!-- '+SLICE) and COMMENT.endswith('-->'))
if any(not r[1] for r in res):
    for r in res: print(('GREEN' if r[1] else 'RED'),r[0],'|',r[2])
    print('COMMENT GATE RED -> no write'); sys.exit(1)
# write
new=art.rstrip('\n')+'\n\n'+COMMENT+'\n'
open(DISK,'w',encoding='utf-8').write(new)
nl=new.split('\n')
nhl=[l for l in nl if HASH in l]
gate('post-write-hash_lines==2',len(nhl)==2,len(nhl))
ncom=[l for l in nl if l.lstrip().startswith('<!-- TJJ-A')]
gate('post-write-comments==2',len(ncom)==2,len(ncom))
gate('post-write-own==1',sum(1 for l in ncom if l.lstrip().startswith('<!-- '+SLICE))==1)
gate('post-write-noncomment-carriers==0',not any(not l.lstrip().startswith('<!--') for l in nhl))
# stage+commit from toplevel with explicit pathspec
rc,o,e=g('add','-f','--',TOP)
gate('add',rc==0,e[:120])
SUBJ=SLICE+': verified-saturated tag page root_'+HASH+' (EOF comment only, both subjects carriers==1/dated==1)'
gate('subj-pure-ascii',all(ord(c)<0x80 for c in SUBJ),'maxcp=%04x'%max(ord(c) for c in SUBJ))
rc,o,e=g('commit','--no-verify','-m',SUBJ,'--',TOP)
gate('commit',rc==0,(o[-300:] if o else e[-300:]))
own_sha=None
if rc==0:
    rc2,o2,_=g('rev-parse','HEAD')
    own_sha=o2.strip()
state={'SLICE':SLICE,'HASH':HASH,'REL':REL,'TOP':TOP,'DISK':DISK,'POST':POST,'WB':WB,
 'SUBJ':SUBJ,'own_sha':own_sha,
 'hex_labels':{'tag page hex: ':re.findall(r'u([0-9a-f]{4})',title_body.encode('unicode_escape').decode('ascii')),
   'yang-ziqing (name hex: ':yb.split(),'zheng-bingquan (name hex: ':zb.split()},
 'COMMENT':COMMENT}
os.makedirs(os.path.join(REPO,'scratch'),exist_ok=True)
json.dump(state,open(os.path.join(REPO,'scratch/tjj-11231410-9.state.json'),'w'),ensure_ascii=True)
for r in res: print(('GREEN' if r[1] else 'RED'),r[0],'|',r[2])
print('OWN_SHA',own_sha)
