#!/usr/bin/env python3
"""zh-link-precision-log.py — precision log for the work-entity-linker ZH
name-matching class (the gate for P3 deterministic pre-verify, seal item open3).

Measures the REAL matcher: imports scripts/work-entity-linker.py (registry +
zh_lookup are built at import; main loop is __main__-guarded) and replays its
ZH pass — `for zh, e in zh_lookup: if zh in hay` over the same haystack
(head 6000 + ## Article body 60000) — on a seeded random sample of pages.

Output (append-only, checked into knowledge/operational/):
  knowledge/operational/zh-link-precision/<date>.jsonl   one row per ZH hit
  knowledge/operational/zh-link-precision/latest.json    run summary

Each row carries everything a reviewer needs WITHOUT re-running: page, entity,
zh string, matched context (±30 chars), zh length, honorific-suffix flag,
already-in-Subjects flag. Verdicts are added later by --verdicts (review pass)
so the raw matcher output is never rewritten by hand.

Usage:
  python3 zh-link-precision-log.py --sample 400 --seed 20261030
  python3 zh-link-precision-log.py --verdicts verdicts.json   (merge review)
"""
from __future__ import annotations
import argparse, glob, importlib.util, json, os, random, re, sys
from datetime import date
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
OUT = REPO / "knowledge/operational/zh-link-precision"

ap = argparse.ArgumentParser()
ap.add_argument("--sample", type=int, default=400)
ap.add_argument("--seed", type=int, default=20261030)
ap.add_argument("--verdicts", default="", help="json file: {row_id: correct|wrong|uncertain}")
args = ap.parse_args()

if args.verdicts:
    # merge pass: attach reviewer verdicts to today's rows, write summary
    vmap = json.load(open(args.verdicts, encoding="utf-8"))
    rows = [json.loads(l) for l in OUT.joinpath(f"{date.today().isoformat()}.jsonl").read_text().splitlines() if l.strip()]
    counts = {"correct": 0, "wrong": 0, "uncertain": 0, "unreviewed": 0}
    for r in rows:
        v = vmap.get(r["id"])
        r["verdict"] = v if v in counts else "unreviewed"
        counts[r["verdict"]] += 1
    OUT.joinpath(f"{date.today().isoformat()}.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    reviewed = counts["correct"] + counts["wrong"]
    precision = round(counts["correct"] / reviewed, 4) if reviewed else None
    summary = {"date": date.today().isoformat(), "rows": len(rows), **counts,
               "precision_reviewed_only": precision,
               "note": "precision = correct/(correct+wrong); uncertain excluded pending owner ruling"}
    OUT.joinpath("latest.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    sys.exit(0)

# --- import the real matcher (registry build runs; main loop is __main__-guarded) ---
spec = importlib.util.spec_from_file_location("work_entity_linker", REPO / "scripts/work-entity-linker.py")
assert spec and spec.loader
wel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wel)
# SUBJ_RE lives inside the linker's __main__-guarded block; prefer its copy,
# fall back to the identical pattern so the logger never crashes on drift.
SUBJ_RE = getattr(wel, "SUBJ_RE", None) or re.compile(r"(## Subjects\n)(.*?)(\n## |\Z)", re.S)

files = sorted(glob.glob(str(wel.CONTENT / "works/**/*.md"), recursive=True)
               + glob.glob(str(wel.CONTENT / "articles/**/*.md"), recursive=True))
rng = random.Random(args.seed)
sample = rng.sample(files, min(args.sample, len(files)))

OUT.mkdir(parents=True, exist_ok=True)
out_path = OUT / f"{date.today().isoformat()}.jsonl"
n_rows = 0
seen_ids = set()
if out_path.is_file():  # idempotent re-runs: keep existing rows, skip duplicate ids
    for l in out_path.read_text(encoding="utf-8").splitlines():
        try:
            seen_ids.add(json.loads(l)["id"])
        except Exception:
            pass

with out_path.open("a", encoding="utf-8") as fh:
    for f in sample:
        rel = os.path.relpath(f, REPO)
        t = open(f, encoding="utf-8", errors="ignore").read()
        head = t[:6000]
        body_start = t.find("## Article")
        body = t[body_start: body_start + 60000] if body_start >= 0 else ""
        hay = head + "\n" + body
        sm = SUBJ_RE.search(t)
        subj_sec = sm.group(2) if sm else ""
        subj_span = (sm.start(2), sm.end(2)) if sm else None
        for zh, e in wel.zh_lookup.items():
            pos = hay.find(zh)
            if pos < 0:
                continue
            rid = f"{rel}::{e['path']}::{zh}"
            if rid in seen_ids:
                continue
            # already-linked check must cover BOTH wikilink shapes: quartz links
            # omit .md (Grok 2026-10-30: .md-only test undercounted self-hits)
            slug = e["path"]
            linked = (slug in subj_sec) or (slug.removesuffix(".md") in subj_sec) or \
                     (e["slug"] in subj_sec)
            # stratum: prefer a PROSE occurrence outside the Subjects section for
            # the logged context; self-hits only ever see the matcher's own output
            ctx_pos, stratum = pos, "third_party_prose"
            in_title = pos < 200 and zh in t[:200]
            if subj_span and subj_span[0] <= pos < subj_span[1]:
                stratum = "subjects_rematch"
                nxt = -1
                from_pos = 0
                while True:
                    q = hay.find(zh, from_pos)
                    if q < 0:
                        break
                    if not (subj_span[0] <= q < subj_span[1]):
                        nxt = q
                        break
                    from_pos = q + 1
                if nxt >= 0:
                    ctx_pos = nxt
                else:
                    ctx_pos = pos
            elif in_title:
                stratum = "title_self"
            ctx = hay[max(0, ctx_pos - 30): ctx_pos + len(zh) + 30].replace("\n", " ")
            fh.write(json.dumps({
                "id": rid, "date": date.today().isoformat(), "seed": args.seed,
                "page": rel, "entity": e["path"], "slug": e["slug"], "zh": zh,
                "zh_len": len(zh), "honorific": bool(re.search(r"(先生|女士|醫師|博士|牧師|教授)$", zh)),
                "already_in_subjects": linked,
                "stratum": stratum,
                "context": ctx,
            }, ensure_ascii=False) + "\n")
            seen_ids.add(rid)
            n_rows += 1

summary = {"date": date.today().isoformat(), "seed": args.seed, "pages_sampled": len(sample),
           "zh_lookup_size": len(wel.zh_lookup), "registry_size": len(wel.registry),
           "ambiguous_zh_skipped": len(wel.ambiguous_zh),
           "new_rows": n_rows, "total_rows": len(seen_ids), "file": str(out_path)}
OUT.joinpath("latest.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False))
