#!/usr/bin/env python3
"""taiwandaily-units.py — deterministic units.jsonl builder for taiwandaily.net.

Gate A (WEBSITE_INGEST, owner `go echopedia website taiwandaily.net`
2026-11-18). taiwandaily.net is a WordPress news corpus ingested as
**directory-corpus** (planner ruling 2026-11-18, WEBSITE_INGEST §2S carve-out
class): the vault bar is mandatory, the wiki bar is hub-catalog only — NO
per-unit work pages (a news site is not a magazine; /works/ would be 85k
chrome pages). The source hub is the front door.

Every article that has a manifest result with an archived file becomes one
unit line in knowledge/research/taiwandaily-net/units.jsonl:
  value_band A  = judged `absorbed` in tdm-<ym>-absorb-ledger.jsonl (the
                  台美人物 record lines already on wiki pages)
  value_band B  = everything else with a vault body
  capture "vault" when the archive file exists with >= 400 bytes
Deterministic: no LLM, no invention. Rerun any time; output is a full rebuild
from manifests + ledgers, so it can ride a weekly cron beside the fetcher.

Sources read: knowledge/web-archives/tdm-<ym>.json (all months present),
tdm-<ym>-absorb-ledger.jsonl. Never writes anything but units.jsonl.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path.home() / "echo-system"
ARCH = REPO / "knowledge" / "web-archives"
OUT = REPO / "knowledge" / "research" / "taiwandaily-net" / "units.jsonl"
SID = "taiwandaily-net"
MIN_VAULT_BYTES = 400

FM_TITLE = re.compile(r'^title:\s*"(.*?)"\s*$', re.M)
FM_PUB = re.compile(r"^published:\s*(\d{4}-\d{2}-\d{2})", re.M)
FM_URL = re.compile(r"^source_url:\s*(\S+)\s*$", re.M)


def fm_read(path: Path) -> tuple[str | None, str | None, str | None]:
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    except OSError:
        return None, None, None
    t = FM_TITLE.search(head)
    p = FM_PUB.search(head)
    u = FM_URL.search(head)
    return (t.group(1) if t else None,
            p.group(1) if p else None,
            u.group(1) if u else None)


def ledger_decisions(ym: str) -> dict[str, str]:
    led = ARCH / f"tdm-{ym}-absorb-ledger.jsonl"
    out: dict[str, str] = {}
    if not led.is_file():
        return out
    for line in led.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        url = str(d.get("url") or "").rstrip("/")
        if url:
            # last write wins
            out[url] = str(d.get("decision") or "")
    return out


def main() -> int:
    manifests = sorted(ARCH.glob("tdm-2*.json"))
    manifests = [m for m in manifests
                 if re.fullmatch(r"tdm-\d{6}\.json", m.name)]
    if not manifests:
        print("NO_MANIFESTS", file=sys.stderr)
        return 1
    units: dict[str, dict] = {}  # unit_id -> row (dedupe across months)
    n_absorbed = 0
    # url per id (from any month manifest's results)
    url_by_id: dict[str, str] = {}
    for mf in manifests:
        try:
            dd0 = json.loads(mf.read_text())
        except Exception:
            print(f"SKIP {mf.name} (unreadable)", flush=True)
            continue
        for r0 in dd0.get("results") or []:
            u0 = str(r0.get("url") or "").rstrip("/")
            if not u0:
                continue
            m0 = re.search(r"/(\d+)/?$", u0 + "/")
            if m0 and m0.group(1) not in url_by_id:
                url_by_id[m0.group(1)] = u0 + "/"
    # absorbed ids (band A) from every ledger, keyed by url
    absorbed_urls: set[str] = set()
    for led in ARCH.glob("tdm-2*-absorb-ledger.jsonl"):
        for line in led.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                dd = json.loads(line)
            except json.JSONDecodeError:
                continue
            if str(dd.get("decision") or "") == "absorbed" and dd.get("url"):
                absorbed_urls.add(str(dd["url"]).rstrip("/"))
    # UNITS ARE THE VAULT: one line per archived article file >= MIN bytes.
    # Weak months' legacy /date/ listings polluted old manifests with
    # never-archived rows; enumerating from disk keeps units == vault truth
    # (Gate C then verifies what actually exists; month closure is graded by
    # taiwandaily-month-fetch.py --verify, not by this file). 2026-11-18.
    for fpath in ARCH.glob("taiwandaily-net-*-*.md"):
        m = re.fullmatch(r"taiwandaily-net-(\d+)-(\d+)\.md", fpath.name)
        if not m or m.group(1) != m.group(2):
            continue
        try:
            size = fpath.stat().st_size
        except OSError:
            continue
        if size < MIN_VAULT_BYTES:
            continue
        uid = m.group(1)
        title, published, fm_url = fm_read(fpath)
        url = (fm_url or url_by_id.get(uid) or "").rstrip("/")
        if not url:
            continue
        url = url + "/"
        band = "A" if url.rstrip("/") in absorbed_urls else "B"
        if band == "A":
            n_absorbed += 1
        row = {
            "class": "directory-corpus",
            "source_id": SID,
            "unit_id": uid,
            "url": url,
            "title": title or "",
            "date": published or "",
            "license": "all-rights",
            "absorb": "vault-index",
            "value_band": band,
            "capture": "vault",
        }
        prev = units.get(uid)
        if prev is None or (not prev.get("title") and row.get("title")):
            units[uid] = row
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        for uid in sorted(units, key=lambda x: int(x) if x.isdigit() else 0):
            fh.write(json.dumps(units[uid], ensure_ascii=False) + "\n")
    tmp.replace(OUT)
    print(f"UNITS wrote={len(units)} absorbed_A={n_absorbed} "
          f"vaulted={sum(1 for u in units.values() if 'capture' in u)} "
          f"months={len(manifests)} out={OUT}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
