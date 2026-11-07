# Quarantine manifest — stray `people/*.md.md` fragments

**Date:** 2026-11-06 · **Card:** t_9b4417c5 (parent inventory t_6f917b24)
**Source vault:** `~/echo-system/content` · **Files:** 11 · **Mode:** `cp -p` (mtime preserved), then deleted from vault

## Why archived before deleting
`git ls-files 'people/*.md.md'` is **empty** — all 11 were UNTRACKED. Untracked means deletion has
no git safety net, so bytes were archived first. Nothing else was preserved: content is duplicated
verbatim in each canonical page (retention gate below, re-run immediately before each delete).

## Shared fingerprint (all 11)
5 lines · 392–451 B · unique md5 each · mtime `2026-10-08 00:25:43` (single batch write) ·
no frontmatter · no H1 · `<!-- TJJ-A10060800-7 … -->` + blank + `## Related Pages` + blank +
`- [[people/albert-s-lai|Dr. Albert S. Lai]]` in all 11 (writer constant, not curation).

## Emitter (identified with direct evidence, see card t_9b4417c5)
`~/.hermes/scripts/echopedia-queue-drain.py` — the `NO_RELATED_PAGES` branch appends that literal
stub, and its queue carried `<slug>.md.md` paths. `knowledge/operational/janitor-log/2026-10-08-drain.jsonl`
lists all 12 writes by name with `acts: ["add Related Pages stub", "WROTE"]`.

## Retention gate result
Each stray's line-1 audit tag was confirmed present in its canonical (`grep -cF` == 1) immediately
before deletion. 11/11 PASS, 0 aborted. No audit receipt was lost.

## md5 (11)
00d27ed24d5a816ed6fb7a30ffe43003  dr-tong-y-chen.md.md
0bae46ad5b63495499e2189f3dcbacc7  yang-xin.md.md
11edfc8f47f2ffda3251fd6c48a4fb3e  paul-chen.md.md
245aed05a54bb454cf58a22e77ea9bd1  peter-chen.md.md
30355c6199b193af1c699e40dec2119d  dr-long-song-simon-lin.md.md
5f3cdc7a2ec93975e439eb09c2c188ca  dr-lisa-su.md.md
7a64330a486c07ba52f6a6555d28c61c  david-yang.md.md
81ab2bc78db4f80669b4a8d6b9d8ce41  chun-chieh-chiu.md.md
b5d2addefaf6c64d4eca36f5680eb5a6  lisa-su.md.md
e9bfde078b839d4c9b1d6a8a6364aa1a  dr-yeongchi-wu.md.md
ed0ae0fc0d6dbe01a5fd88eb042e0e29  ing-hui-lai.md.md

## Restore
```bash
# put any file back into the vault
cp -p /home/leedt/echo-system/echopedia/quarantine/stray-md-md-2026-11-06/<slug>.md.md ~/echo-system/content/people/<slug>.md.md
```
