#!/usr/bin/env python3
"""Rank dangling wikilinks and emit Tier M / Tier 1 deepen cards.

Offline and stdlib-only. Walks content/ (not knowledge/web-archives).
Score = dangling-link count × corpus co-occurrence in works/ and articles.

Tier M: name is in ≥1 works/articles page, or linked from a non-hub
organization (M-institution chain), or linked from a non-hub source page
that carries a Taiwan/TA anchor.
Tier 1: linked from ≥1 non-hub M page and mentioned in ≥2 files, and not M.
Hub rule: a page with >50 distinct outbound wikilinks admits nobody alone.
Anything else is refused (Tier-2 firewall — never enqueued).

Default is --dry-run (prints tier counts and would-be cards, writes nothing).
--emit creates kanban cards and slice files. Compare dangling_dossier to the
288 baseline measured 2026-09-26.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

HUB = 50
BASELINE = 288
SLICE = 4
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")
TA_ANCHOR = re.compile(r"Taiwan|Taiwanese|台灣|台美")
TIER_RE = re.compile(r"^tier:\s*[\"']?([Mm12])[\"']?\s*$", re.M)

DOSSIER_SRC = ("people/", "organizations/")
CORPUS_SRC = ("works/", "articles/")


def norm_target(raw: str) -> str:
    t = raw.strip().strip("/")
    if t.endswith(".md"):
        t = t[:-3]
    if t.startswith("content/"):
        t = t[len("content/"):]
    return t


def resolves(target: str, slugs: set[str]) -> bool:
    if not target or target.startswith(("http://", "https://")):
        return True
    if target in slugs or f"{target}/index" in slugs:
        return True
    if "/" not in target:
        for kind in (
            "people", "organizations", "sources", "events", "topics", "works", "articles",
        ):
            if f"{kind}/{target}" in slugs:
                return True
    return False


def label_of(target: str, alias: str | None) -> str:
    if alias and len(alias.strip()) >= 2:
        return alias.strip()
    seg = target.rsplit("/", 1)[-1].replace("-", " ").strip()
    return seg


def classify(
    *,
    corpus_hits: int,
    nonhub_org_linkers: int,
    nonhub_m_linkers: int,
    source_anchor: bool,
    mention_files: int,
) -> str | None:
    if corpus_hits >= 1 or nonhub_org_linkers >= 1 or source_anchor:
        return "M"
    if nonhub_m_linkers >= 1 and mention_files >= 2:
        return "1"
    return None


def parse_tier(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return "M"
    mt = TIER_RE.search(m.group(1))
    return mt.group(1).upper() if mt else "M"


def walk_content(root: Path):
    import os
    slugs: set[str] = set()
    files: list[dict] = []
    for dirpath, _dirs, names in os.walk(root):
        for fn in names:
            if not fn.endswith(".md"):
                continue
            p = Path(dirpath, fn)
            rel = str(p.relative_to(root))
            slugs.add(rel[:-3])
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            links = []
            for m in LINK_RE.finditer(text):
                target = norm_target(m.group(1))
                if not target or target.startswith(("http://", "https://")):
                    continue
                links.append((target, label_of(target, m.group(2))))
            files.append({
                "rel": rel,
                "tier": parse_tier(text),
                "outbound": len({t for t, _ in links}),
                "org": rel.startswith("organizations/"),
                "source": rel.startswith("sources/"),
                "dossier": rel.startswith(DOSSIER_SRC),
                "corpus": rel.startswith(CORPUS_SRC),
                "ta": bool(rel.startswith("sources/") and TA_ANCHOR.search(text)),
                "links": links,
                "path": p,
            })
    return slugs, files


def build_candidates(slugs: set[str], files: list[dict]) -> dict[str, dict]:
    cand: dict[str, dict] = {}
    for f in files:
        hub = f["outbound"] > HUB
        # Tier-1 pages are not M pages. Hubs admit nobody alone.
        admits = f["tier"] == "M" and not hub
        is_m = f["tier"] == "M"
        for target, label in f["links"]:
            if resolves(target, slugs):
                continue
            c = cand.setdefault(target, {
                "target": target,
                "label": label,
                "refs": 0,
                "dossier_refs": 0,
                "linkers": set(),
                "nonhub_org": 0,
                "nonhub_m": 0,
                "source_anchor": False,
            })
            c["refs"] += 1
            if f["dossier"]:
                c["dossier_refs"] += 1
            if len(label) > len(c["label"]):
                c["label"] = label
            c["linkers"].add(f["rel"])
            if is_m and admits and f["org"]:
                c["nonhub_org"] += 1
            if is_m and admits:
                c["nonhub_m"] += 1
            if f["source"] and admits and f["ta"]:
                c["source_anchor"] = True
    return cand


def corpus_hits(files: list[dict], cand: dict[str, dict]) -> None:
    labels = {}
    for target, c in cand.items():
        lab = c["label"].strip()
        if len(lab) < 3:
            c["corpus"] = 0
            continue
        labels.setdefault(lab, []).append(target)
        c["corpus"] = 0
        c["corpus_files"] = set()
    if not labels:
        return
    ordered = sorted(labels, key=len, reverse=True)
    patterns = []
    step = 150
    for i in range(0, len(ordered), step):
        chunk = ordered[i:i + step]
        patterns.append((
            re.compile("|".join(re.escape(x) for x in chunk)),
            {lab: labels[lab] for lab in chunk},
        ))
    for f in files:
        if not f["corpus"]:
            continue
        try:
            text = f["path"].read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if len(text) > 1_500_000:
            text = text[:1_500_000]
        for pat, owners in patterns:
            seen = {m.group(0) for m in pat.finditer(text)}
            for lab in seen:
                for target in owners.get(lab, ()):
                    c = cand[target]
                    if f["rel"] not in c["corpus_files"]:
                        c["corpus_files"].add(f["rel"])
                        c["corpus"] += 1


def score_of(c: dict) -> int:
    return int(c["refs"]) * int(c.get("corpus", 0))


def would_be(cand: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    accepted = []
    refused = 0
    for c in cand.values():
        mentions = len(c["linkers"]) + int(c.get("corpus", 0))
        tier = classify(
            corpus_hits=int(c.get("corpus", 0)),
            nonhub_org_linkers=c["nonhub_org"],
            nonhub_m_linkers=c["nonhub_m"],
            source_anchor=c["source_anchor"],
            mention_files=mentions,
        )
        c["tier_class"] = tier
        c["mentions"] = mentions
        c["score"] = score_of(c)
        if tier is None:
            refused += 1
            continue
        accepted.append(c)
    accepted.sort(key=lambda c: (c["score"], c["refs"], c.get("corpus", 0)), reverse=True)
    return accepted, refused


def open_frontier(db: Path) -> tuple[set[str], set[str]]:
    titles, paths = set(), set()
    if not db.is_file():
        return titles, paths
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        rows = con.execute(
            "select title, body from tasks where status not in ('done','archived') "
            "and (title like 'FRONTIER%' or body like '%frontier-%')"
        ).fetchall()
        con.close()
    except sqlite3.Error:
        return titles, paths
    for title, body in rows:
        titles.add(title)
        for m in re.findall(r"frontier-\d+-\d+\.txt", body or ""):
            paths.add(m)
        for m in re.findall(r"(?:people|organizations)/[A-Za-z0-9][A-Za-z0-9._-]*", body or ""):
            paths.add(m)
    return titles, paths


def card_body(group: list[dict], slice_name: str, task_token: str) -> str:
    lines = [
        f"Frontier cards for {len(group)} dangling targets. Slice file: knowledge/operational/{slice_name}.",
        "Do NOT publish. Tier-2 firewall: these targets were classified M or 1.",
        "Per target, harvest only the baked facts below; list unused facts under ## Skipped.",
        "",
    ]
    for c in group:
        lines.append(f"### {c['label']} (`{c['target']}`) tier {c['tier_class']}")
        lines.append(
            f"- refs={c['refs']} dossier_refs={c['dossier_refs']} "
            f"corpus={c.get('corpus', 0)} score={c['score']}"
        )
        lines.append("#### Fact table")
        lines.append("- Corpus works/articles: see co-occurrence count above (builder is offline).")
        lines.append("- Dated archive lines: read at emit time; dry-run does not fetch.")
        lines.append("#### FETCH (worker runs; builder does not)")
        lines.append(f"- zh.wikipedia infobox for {c['label']}")
        lines.append(f"- Wikidata claims for {c['label']} (HOLD on conflict)")
        lines.append("## Online arms")
        for arm, q in (
            ("zh.wikipedia infobox+awards", c["label"]),
            ("Wikidata claims", c["label"]),
            ("official site / event page", c["label"] + " official"),
            ("ZH press (World Journal / 大紀元 / 台灣日報)", c["label"]),
        ):
            lines.append(
                f"- {arm}: search `{q}`. End absorb / HOLD / "
                f"miss (searched {q}, YYYY-MM-DD)."
            )
        lines.append("")
    lines.append(
        "LAST ACTION: hermes kanban complete "
        f"{task_token} --result 'frontier <tier counts>'"
    )
    return "\n".join(lines)


def emit_cards(accepted: list[dict], repo: Path, db: Path) -> int:
    titles, open_paths = open_frontier(db)
    stamp = subprocess.run(
        ["date", "+%m%d%H%M"], capture_output=True, text=True
    ).stdout.strip()
    made = 0
    groups = [accepted[i:i + SLICE] for i in range(0, len(accepted), SLICE)]
    out_dir = repo / "knowledge" / "operational"
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, group in enumerate(groups, 1):
        if any(c["target"] in open_paths for c in group):
            print("skip (open twin):", i)
            continue
        slice_name = f"frontier-{stamp}-{i}.txt"
        title = f"FRONTIER-{stamp}-{i}: {len(group)} dangling targets"
        if title in titles:
            print("skip (open title):", title)
            continue
        (out_dir / slice_name).write_text("\n".join(c["target"] for c in group) + "\n")
        proc = subprocess.run(
            ["hermes", "kanban", "create", title, "--assignee", "pinto",
             "--body", "pending", "--max-runtime", "2400"],
            capture_output=True, text=True,
        )
        m = re.search(r"t_[0-9a-f]+", proc.stdout or "")
        if not m:
            print("create failed:", title, proc.stderr[-200:] if proc.stderr else "")
            continue
        tid = m.group(0)
        body = card_body(group, slice_name, tid)
        con = sqlite3.connect(str(db))
        con.execute("update tasks set body=? where id=?", (body, tid))
        con.commit()
        con.close()
        subprocess.run(["hermes", "kanban", "promote", tid], capture_output=True)
        made += 1
        print("created", tid, slice_name)
    return made


def run(root: Path, *, emit: bool, repo: Path, db: Path) -> int:
    slugs, files = walk_content(root)
    cand = build_candidates(slugs, files)
    corpus_hits(files, cand)
    accepted, refused = would_be(cand)
    dossier_targets = {t for t, c in cand.items() if c["dossier_refs"]}
    n_m = sum(1 for c in accepted if c["tier_class"] == "M")
    n_1 = sum(1 for c in accepted if c["tier_class"] == "1")
    print(f"dangling_all: {len(cand)}")
    print(
        f"dangling_dossier: {len(dossier_targets)} "
        f"(baseline {BASELINE}, delta {len(dossier_targets) - BASELINE})"
    )
    print(f"tier M: {n_m}")
    print(f"tier 1: {n_1}")
    print(f"refused: {refused}")
    cards = (len(accepted) + SLICE - 1) // SLICE if accepted else 0
    print(f"would-be cards: {cards}")
    show = cards if cards <= 40 else 40
    for i in range(show):
        group = accepted[i * SLICE:(i + 1) * SLICE]
        names = ", ".join(f"{c['label']}[{c['tier_class']}]" for c in group)
        print(f"CARD {i + 1}: {names}")
    if cards > show:
        print(f"... {cards - show} more cards not listed")
    if not emit:
        print("mode=dry-run (no slice files, no kanban)")
        return 0
    made = emit_cards(accepted, repo, db)
    print(f"emitted: {made}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", default=str(Path.home() / "echo-system/content"))
    ap.add_argument("--repo", default=str(Path.home() / "echo-system"))
    ap.add_argument("--kanban-db", default=str(Path.home() / ".hermes/kanban.db"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--emit", action="store_true")
    args = ap.parse_args(argv)
    emit = bool(args.emit) and not args.dry_run
    return run(Path(args.content), emit=emit, repo=Path(args.repo), db=Path(args.kanban_db))


if __name__ == "__main__":
    sys.exit(main())
