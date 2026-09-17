#!/usr/bin/env python3
"""work-entity-linker.py — deterministically link works pages to people/org
pages from the page's own body text (title, byline, Article section). Pure CPU,
no LLM. Resumable via jsonl state. Dry-run by default; --apply writes.

Links are appended to the "## Subjects" section (append-only; body text is
never rewritten, so re-runs are safe and idempotent).
"""
from __future__ import annotations
import argparse, glob, json, os, re, sys, unicodedata
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
CONTENT = REPO / "content"
STATE = REPO / "knowledge/operational/work-linker-state.jsonl"
SUBJ_PENDING = "(named subjects pending absorb)"

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
ap.add_argument("--limit", type=int, default=0)
ap.add_argument("--min-hits", type=int, default=1)
args = ap.parse_args()

# ---------- registry from person/org frontmatter ----------
def fm_field(text: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*\"?([^\"\n]+)\"?\s*$", text, re.M)
    return m.group(1).strip() if m else ""

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()

def en_variants(name: str) -> list[str]:
    """Matching variants for an English display name."""
    name = norm(name)
    if not name:
        return []
    out = {name}
    # strip leading honorifics for matching
    stripped = re.sub(r"^(Dr|Prof|Rev|Pastor|Mr|Mrs|Ms)\.?\s+", "", name, flags=re.I)
    if stripped:
        out.add(stripped)
        out.add(stripped.replace(".", ". "))  # normalize 'Y.Wu' style spacing below
    # spaced-initials variant: 'Henry Y. Wu' -> also match 'Henry Wu'
    parts = stripped.split()
    if len(parts) >= 3:
        noinit = " ".join(p for p in parts if not re.fullmatch(r"[A-Z]\.?", p))
        if len(noinit.split()) >= 2:
            out.add(noinit)
    cands = []
    for v in out:
        v = re.sub(r"\s+", " ", v.replace(".", " ").strip())
        # allow flexible space/period between tokens
        toks = [re.escape(t) for t in v.split() if t]
        if len(toks) < 2:
            continue
        cands.append(re.compile(r"(?<![\w.-])" + r"[\s.]*\.?\s+".join(toks) + r"(?![\w-])"))
    return cands

def zh_variants(name: str) -> list[str]:
    m = re.search(r"[\u4e00-\u9fff]{2,}", name or "")
    if not m:
        return []
    zh = m.group(0)
    if len(zh) < 3 and not re.search(r"(先生|女士|醫師|博士|牧師|教授)$", zh):
        return []  # 2-char names too ambiguous unless suffixed
    return [zh]

registry: dict[str, dict] = {}  # canonical name -> {path, en_re, zh}
ambiguous_zh: set[str] = set()
amb_seen: dict[str, set] = {}
for pat in ("people/*.md", "organizations/*.md"):
    for f in glob.glob(str(CONTENT / pat)):
        t = open(f, encoding="utf-8", errors="ignore").read(3000)
        rel = os.path.relpath(f, CONTENT)
        en = fm_field(t, "name_en") or re.sub(r"\s*\([^)]*\)\s*", "", fm_field(t, "title"))
        zh = fm_field(t, "name_zh")
        slug = rel.rsplit("/", 1)[-1][:-3]
        key = norm(en)
        if not key:
            continue
        if zh:
            amb_seen.setdefault(zh, set()).add(rel)
        registry.setdefault(key, {"path": rel, "en": en_variants(en), "zh": [], "slug": slug})
        if zh:
            registry[key]["zh"] = zh_variants(zh)
for zh, paths in amb_seen.items():
    if len(paths) > 1:
        ambiguous_zh.add(zh)

# prebuilt indices: cheap substring prefilter gates the regex work (12k pages
# x 2.4k entities is otherwise CPU-suicidal)
en_prefilter: dict[str, set[str]] = {}
zh_lookup: dict[str, dict] = {}   # unambiguous zh string -> registry entry
for k, e in registry.items():
    try:
        en_src = fm_field(open(CONTENT / e["path"], encoding="utf-8", errors="ignore").read(1500), "name_en") or k
    except OSError:
        en_src = k
    en_prefilter[k] = {t.upper() for t in re.findall(r"[A-Za-z]{4,}", en_src)}
    for zh in e["zh"]:
        if zh not in ambiguous_zh:
            zh_lookup.setdefault(zh, e)

done = set()
if STATE.is_file():
    for line in STATE.read_text().splitlines():
        try:
            done.add(json.loads(line)["file"])
        except Exception:
            pass

files = sorted(
    glob.glob(str(CONTENT / "works/**/*.md"), recursive=True)
    + glob.glob(str(CONTENT / "articles/**/*.md"), recursive=True))
if args.limit:
    files = files[: args.limit]

SUBJ_RE = re.compile(r"(## Subjects\n)(.*?)(\n## |\Z)", re.S)
stats = {"scanned": 0, "linked": 0, "pages": 0, "skipped_done": 0}
for f in files:
    rel = os.path.relpath(f, REPO)
    if rel in done:
        stats["skipped_done"] += 1
        continue
    stats["pages"] += 1
    t = open(f, encoding="utf-8", errors="ignore").read()
    head = t[:6000]
    body_start = t.find("## Article")
    body = t[body_start: body_start + 60000] if body_start >= 0 else ""
    hay = head + "\n" + body
    hay_up = hay.upper()
    hits: list[tuple[str, dict]] = []
    seen_paths: set[str] = set()
    for key, e in registry.items():
        toks = en_prefilter.get(key) or set()
        if not toks or not any(tk in hay_up for tk in toks):
            continue
        for rx in e["en"]:
            if rx.search(hay):
                hits.append((key, e)); seen_paths.add(e["path"]); break
    for zh, e in zh_lookup.items():
        if zh in hay and e["path"] not in seen_paths:
            hits.append((zh, e)); seen_paths.add(e["path"])
    # idempotence: don't re-add subjects already present in the Subjects section
    sm = SUBJ_RE.search(t)
    subj_sec = sm.group(2) if sm else ""
    fresh = [(k, e) for k, e in hits if e["path"] not in subj_sec]
    if len(hits) >= args.min_hits and fresh:
        lines = "".join(
            f"- [[{e['path']}|{norm(k)}]] — mentioned in this record\n" for k, e in fresh[:12]
        )
        if sm:
            if SUBJ_PENDING in subj_sec:
                new_subj = lines + f"- {SUBJ_PENDING}\n"
            else:
                new_subj = subj_sec.rstrip("\n") + "\n" + lines
            t2 = t[: sm.start(2)] + new_subj + t[sm.end(2):]
        else:
            t2 = t.rstrip("\n") + "\n\n## Subjects\n" + lines + "\n"
        stats["linked"] += 1
        stats["scanned"] += len(fresh)
        if args.apply:
            open(f, "w", encoding="utf-8").write(t2)
            with STATE.open("a") as fh:
                fh.write(json.dumps({"file": rel, "n": len(fresh)}) + "\n")
print("pages", stats["pages"], "| cards-linked", stats["links"] if "links" in stats else stats["linked"],
      "| subject-links", stats["scanned"], "| skipped(done)", stats["skipped_done"],
      "| registry", len(registry), "| ambiguous-zh-skipped", len(ambiguous_zh),
      "| APPLY" if args.apply else "(dry)")
