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
ap.add_argument("--stamp-saturated", action="store_true",
                help="stamp articles whose registry scan found nothing new "
                     "(>=2 subject links already present) so the TJJ re-check "
                     "lane stops re-minting verification-theater cards")
# Importable by zh-link-precision-log.py: registry build runs at import, the
# main loop runs only as a script (argv parsed only then, so an import never
# eats the caller's argv).
args = ap.parse_args([] if __name__ != "__main__" else None)

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

# ---------- news-boilerplate gate (FALSE-PERSON class, Leonard ruling 2026-10-21) ----------
# 嚴厲譴責 ("sternly condemn") was minted as people/嚴厲譴責.md and injected as a `## Subjects`
# bullet into 70 taiwanjustice-net articles. It passed every old gate: name_zh is 4 hanzi so
# zh_variants accepted it, and it is left-clean in 60% of its 193 archive occurrences, so the
# left-clean ratio bar that catches place-name fragments (金山 vs 舊金山) never fires. What
# separates it from a name is not its shape or its hit rate but its CLASS: Chinese press
# boilerplate verbs and stance phrases, which recur verbatim across thousands of articles
# precisely BECAUSE they are formulaic. A phrase gate must therefore be a whitelist of known
# boilerplate, not a heuristic over frequency.
BOILERPLATE_ZH = {
    # condemn / protest / regret stance verbs
    "嚴厲譴責", "强烈谴责", "強烈譴責", "予以譴責", "譴責", "深表遺憾", "深表遗憾", "表示遺憾",
    "表示遗憾", "强烈不满", "強烈不滿", "表示抗議", "表示抗议", "嚴正交涉", "严正交涉",
    "堅決反對", "坚决反对", "强烈抗议", "強烈抗議", "令人髮指", "令人发指",
    # official-response verbs that headline as the subject
    "正告", "駁斥", "驳斥", "批駁", "批驳", "痛批", "狠批", "怒批", "敦促", "呼籲", "呼吁",
    "關切", "关切", "嚴重關切", "严重关切", "回應", "声讨", "聲討",
}
# A hanzi run that ENDS in one of these is a verb/stance phrase glued to a name, not a name.
BOILERPLATE_SUFFIX = (
    "譴責", "谴责", "遺憾", "遗憾", "不滿", "不满", "抗議", "抗议", "交涉", "反對", "反对",
    "關切", "关切", "敦促", "呼籲", "呼吁", "駁斥", "驳斥", "批駁", "批驳", "痛批", "狠批",
    "怒批", "聲討", "声讨", "髮指", "发指", "正告", "慰问", "慰問", "祝賀", "祝贺",
)
# Honorific / role suffixes that DO name a person (the old 2-char exemption, widened).
NAME_SUFFIX = ("先生", "女士", "醫師", "博士", "牧師", "教授", "长老", "長老", "主任",
               "主席", "校長", "局長", "部長", "院長", "董事長", "師")

# 嚴-ADVERB CLASS (t_ba1b68b7, 2026-11-10) — same class, same reason as in
# ~/.hermes/scripts/echopedia-news-digest.py, where the measurements live. 嚴 is both a 百家姓
# surname and the adverb "strictly", so 嚴防 / 嚴查 / 嚴禁 / 嚴重 are surname-anchored verb
# phrases that the shape+frequency gates pass: 嚴防中 (from 「嚴防中共對台跨國鎮壓」) reached
# archive_presence True at left-clean ratio 0.868 against LEFT_CLEAN_RATIO_MIN 0.10, and this
# linker then injected it into every article that mentioned the token. A whitelist of whole
# stance phrases (BOILERPLATE_ZH above) cannot see it — 嚴防中共對台跨國鎮壓 contains no known
# phrase — so the class is killed by its HEAD, which no real given name begins with.
# HEAD RULE, NOT CONTAINS: a contains-rule on 嚴正 would match people/dr-jheng-yan.md
# (name_zh: 嚴正博士, TAH Who's Who) and silently de-index a real person.
# SCOPE: 14 stems from the card body + 嚴厲 / 嚴重 (the two most frequent members, 780 / 4,963
# corpus occurrences, omitted from the card's list). Excluded by measurement, not by oversight:
# the adjective/noun class 嚴峻 / 嚴肅 / 嚴守 / 嚴控 / 嚴刑 — none had an observed mint.
# REMOVED 2026-11-11: 嚴正. The comment above always claimed it excluded; the tuple
# contradicted the comment — the head rule on 嚴正 misclassifies 嚴正博士 as boilerplate and
# fixture L241 demands False. Comment was right, tuple was wrong.
# ADDED 2026-11-11 (fixture-as-contract, news_match_fixture L212 demands 嚴令打詐 True):
# 嚴令. The earlier zero-mint exclusion is retired — the fixture is the contract. Recall probe
# run the same day over content/ front matter: no name_zh begins with 嚴令, so no real person
# is de-indexed (the 嚴正博士 lesson applied before shipping).
# Mirror of YADVERB_STEMS in echopedia-news-digest.py; change both together.
YADVERB_STEMS = ("嚴防", "嚴查", "嚴禁", "嚴抓", "嚴辦", "嚴治", "嚴打", "嚴管", "嚴懲",
                 "嚴密", "嚴格", "嚴詞", "嚴加", "嚴厲", "嚴重", "嚴令")


def is_yadverb_stem(tok: str) -> bool:
    """True if a hanzi run BEGINS with a 嚴-adverb verb. Head rule, never a substring match."""
    if not tok:
        return False
    return any(tok.startswith(s) for s in YADVERB_STEMS)


def is_boilerplate_zh(tok: str) -> bool:
    """True if a hanzi run is news boilerplate rather than a person name.

    Four checks, all cheap and all deterministic:
      1. exact whitelist hit (嚴厲譴責 itself), or a run that BEGINS with a 嚴-adverb verb
         (嚴防中, 嚴查, 嚴重影響) — see YADVERB_STEMS;
      2. the run ENDS in a stance verb — 予以嚴厲譴責, 外交部譴責 — a Chinese person name never
         ends in 譴責/遺憾/抗議/關切;
      3. the run CONTAINS a whitelist phrase without a name suffix — catches a boilerplate verb
         glued to a name fragment (陸委會嚴厲譴責) while 東門巴克禮紀念教會-style org names survive
         because they carry a real name stem and no boilerplate phrase.
      4. the run is a strict PREFIX of a whitelist phrase (嚴厲譴責 -> 嚴厲譴 -> 嚴厲), which a
         person name never is.
    """
    if not tok:
        return False
    if tok in BOILERPLATE_ZH:
        return True
    if is_yadverb_stem(tok):
        return True
    if tok.endswith(BOILERPLATE_SUFFIX):
        return True
    if any(p in tok for p in BOILERPLATE_ZH) and not tok.endswith(NAME_SUFFIX):
        return True
    # prefix chain: surname_candidates also yields truncated chains (嚴厲譴責 -> 嚴厲譴 -> 嚴厲),
    # and a person name is never a strict prefix of a known boilerplate phrase
    if any(p.startswith(tok) for p in BOILERPLATE_ZH):
        return True
    return False


def zh_variants(name: str) -> list[str]:
    m = re.search(r"[\u4e00-\u9fff]{2,}", name or "")
    if not m:
        return []
    zh = m.group(0)
    if len(zh) < 3 and not re.search(r"(先生|女士|醫師|博士|牧師|教授)$", zh):
        return []  # 2-char names too ambiguous unless suffixed
    if is_boilerplate_zh(zh):
        return []  # news boilerplate verb, never a person (see FALSE-PERSON gate above)
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

if __name__ == "__main__":
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
      elif args.stamp_saturated and not fresh:
          # nothing new from the registry scan. If the page already carries >=2
          # subject links and no stamp, write the deterministic stamp now so the
          # TJJ feeder cools it instead of minting a 7-minute worker re-check.
          subj_n = 0
          if "## Subjects" in t:
              subj_n = len(re.findall(r"\n- \[\[(?:people|organizations)/",
                                      t[t.find("## Subjects"):]))
          if subj_n >= 2 and not re.search(r"verified.?saturat", t[:12000], re.I):
              stamp = (f"\nverified-saturation: {__import__('datetime').date.today().isoformat()}"
                       " (work-entity-linker: registry scan found no new entity links; "
                       f"{subj_n} subject links already present)\n")
              m = re.match(r"\A(---\n.*?\n---\n)", t, re.S)
              if m:
                  t2 = t[: m.end(1)] + stamp + t[m.end(1):]
              else:
                  t2 = stamp.lstrip("\n") + "\n" + t
              stats["stamped"] = stats.get("stamped", 0) + 1
              if args.apply:
                  open(f, "w", encoding="utf-8").write(t2)
  print("pages", stats["pages"], "| cards-linked", stats["links"] if "links" in stats else stats["linked"],
        "| subject-links", stats["scanned"], "| skipped(done)", stats["skipped_done"],
        "| stamped-saturated", stats.get("stamped", 0),
        "| registry", len(registry), "| ambiguous-zh-skipped", len(ambiguous_zh),
        "| APPLY" if args.apply else "(dry)")
