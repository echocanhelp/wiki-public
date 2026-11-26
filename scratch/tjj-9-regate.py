# post-commit regate ~45s later, read from own sha + disk
import subprocess, os, json, re, sys, time
REPO=os.path.expanduser('~/echo-system')
st=json.load(open(os.path.join(REPO,'scratch/tjj-11231410-9.state.json')))
SLICE=st['SLICE']; HASH=st['HASH']; TOP=st['TOP']; DISK=st['DISK']
POST=st['POST']; WB=st['WB']; SUBJ=st['SUBJ']; own=st['own_sha']
res=[]
def gate(name,ok,detail=""):
    res.append((name,bool(ok),str(detail)))
def g(*a):
    r=subprocess.run(['git']+list(a),cwd=REPO,capture_output=True,text=True)
    return r.returncode,r.stdout,r.stderr
rc,o,_=g('cat-file','-t',own); gate('own-is-commit',rc==0 and o.strip()=='commit',o.strip())
# sufficient ownership check: own commit blob count of own marker line == 1
rc,blob,_=g('show',own+':'+TOP)
marker='<!-- '+SLICE
gate('own-blob-exists',rc==0)
ownlines=[l for l in blob.split('\n') if l.lstrip().startswith(marker)]
gate('own-comment-in-own-blob==1',len(ownlines)==1,len(ownlines))
owncom=ownlines[0] if ownlines else ''
gate('own-comment-ascii',all(ord(c)<0x80 for c in owncom),'maxcp=%04x'%(max(ord(c) for c in owncom) if owncom else 0))
gate('own-comment-shape',owncom.startswith(marker) and owncom.endswith('-->'))
gate('own-blob-equals-disk',blob==open(DISK,encoding='utf-8').read())
# hex spans vs persisted labels (unified regex)
for lab,toks in st['hex_labels'].items():
    m=re.search(re.escape(lab.rstrip())+r' ?\(?([0-9a-f]{4}(?: [0-9a-f]{4})*)',owncom)
    got=m.group(1).split() if m else None
    gate('hexspan-'+lab.rstrip(),got==toks,(got[:3],toks[:3]))
# disk gates
dl=open(DISK,encoding='utf-8').read().split('\n')
hl=[l for l in dl if HASH in l]
gate('disk-hash_lines==2',len(hl)==2,len(hl))
com=[l for l in dl if l.lstrip().startswith('<!-- TJJ-A')]
gate('disk-comments==2',len(com)==2,len(com))
gate('disk-noncomment-carriers==0',not any(not l.lstrip().startswith('<!--') for l in hl))
fences=[i for i,l in enumerate(dl) if l.strip()=='---']
gate('fm-no-comment',fences[0]==0 and not any(l.lstrip().startswith('<!--') for l in dl[:fences[1]]),fences[:2])
# people pages still saturated
for s in ['yang-ziqing','zheng-bingquan']:
    pl=open(os.path.join(REPO,'content/people/%s.md'%s),encoding='utf-8').read().split('\n')
    nonidx=[l for l in pl if HASH in l and not l.lstrip().startswith('<!--') and not l.lstrip('0123456789. ').startswith('[[')]
    dated=[l for l in nonidx if l.startswith('- '+POST+' ')]
    gate(s+'-carriers==1',len(nonidx)==1,len(nonidx))
    gate(s+'-dated==1',len(dated)==1,len(dated))
# subject pages' own fact-line cps via hex(ord) on disk (no typed CJK)
# subject page wikilink present
# diff stats vs parent
rc,ns,_=g('diff','--numstat',own+'^',own,'--',TOP)
lines=[l for l in ns.split('\n') if l.strip() and '\t' in l]
gate('numstat-single',len(lines)==1,lines)
if lines:
    p=lines[0].split('\t'); gate('dels==0',p[1]=='0',p[1]); print('adds',p[0])
rc,rw,_=g('diff','--raw',own+'^',own,'--',TOP)
gate('create-mode-A',rw.strip().startswith(':000000 100644'),rw.strip()[:80])
# commit subject: equality + ascii, codepoints via hex(ord)
rc,ls,_=g('log','-1','--pretty=%s',own)
gate('subject-equals-built',ls.strip()==SUBJ,repr(ls.strip()[:60]))
gate('subject-ascii',all(ord(c)<0x80 for c in ls.strip()),'maxcp=%04x'%max(ord(c) for c in ls.strip()))
# ownership hints
rc,pk,_=g('log','--all','--pretty=%h','-S',marker,'--',TOP)
print('pickaxe',pk.split())
for r in res: print(('GREEN' if r[1] else 'RED'),r[0],'|',r[2])
print('REGATE',sum(1 for r in res if r[1]),'/',len(res))
