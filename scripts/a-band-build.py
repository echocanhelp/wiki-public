#!/usr/bin/env python3
"""a-band-build.py — deepen emitter: A-class taiwandaily articles whose cited
person pages do not yet carry the citation. Owner GO 2026-11-19 (mint-wave
deepen automation): deterministic detection (this file, no LLM), minting via
mint_gate.mint_via, closure graded by the absorb ledger — never worker report.

A-BAND unit (all conditions, deterministic):
  - month has an absorb ledger (the lane has JUDGED that month),
  - unit has an archived vault file >= MIN_BODY bytes,
  - slice-prep identity pre-filter yields candidate person pages with tag
    'hit' (1-3 candidates; 'collision' stays with the TD slice lane, which is
    built for judgment-heavy batches),
  - LIVE close-predicate: no page under content/ cites the article (bare id
    or URL) — the page exists but does not yet carry the record line.

Card = one bounded batch (mint_gate.MAX_ITEMS - 1, derived never copied),
numbered items = articles only (TD-FIX-20261117b template rule; protocol is
bullets). Close gate: every numbered article has a ledger line
(taiwandaily-absorb-ledger.py), verified live by the worker.

no_agent cron: daily 22:05 (behind generate-cards 22:40? no — it FEEDS the
queue, so it sits after the emitter cluster and before dispatch starvation).
Idempotent: open A-BAND cards on the same month are never re-minted; ledger'd
articles drop out on the next run.
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".hermes" / "scripts"))
from mint_gate import mint_via, MAX_ITEMS, strip_gate_chunk_suffix  # noqa: E402
import sqlite3  # noqa: E402

REPO = Path.home() / "echo-system"
ARCH = REPO / "knowledge" / "web-archives"
CONTENT = REPO / "content"
DB = Path.home() / ".hermes" / "kanban.db"
MIN_BODY = int(os.environ.get("ABAND_MIN_BODY", "1500"))
BATCH = int(os.environ.get("ABAND_BATCH", str(MAX_ITEMS - 1)))
MAXCARDS = int(os.environ.get("ABAND_MAXCARDS", "10"))
PREP = REPO / "scripts" / "taiwandaily-slice-prep.py"

SKIP_FREEZE = os.environ.get("ABAND_IGNORE_FREEZE", "") != "1"


def in_freeze() -> bool:
    if not SKIP_FREEZE:
        return False
    try:
        from zoneinfo import ZoneInfo
        now = datetime.now(ZoneInfo("America/Los_Angeles"))
    except Exception:
        return False
    hm = now.hour * 60 + now.minute
    return 15 * 60 + 45 <= hm < 21 * 60


def cited_ids() -> set[str]:
    """Ids already cited anywhere under content/ (bare 4-7 digit token)."""
    r = subprocess.run(
        ["grep", "-rhoE", r"taiwandaily\.net/[^\"' )]+/([0-9]{4,7})/",
         str(CONTENT)],
        capture_output=True, text=True, timeout=600)
    ids = set(re.findall(r"/([0-9]{4,7})/", r.stdout or ""))
    return ids


def open_months() -> set[str]:
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    rows = con.execute(
        "select title from tasks where title like 'A-BAND-%' "
        "and status not in ('done','archived')").fetchall()
    con.close()
    out = set()
    for (t,) in rows:
        m = re.match(r"A-BAND-(\d{6})-", strip_gate_chunk_suffix(t))
        if m:
            out.add(m.group(1))
    return out


def body_for(ym: str, items: list[dict], stamp: str, n: int) -> str:
    lines = []
    for i, it in enumerate(items, 1):
        cands = ", ".join(it["candidates"])
        lines.append(f"{i}. `{it['url']}`\n   file: `{it['file']}`\n"
                     f"   title: {it['title']}\n   candidate pages: {cands}")
    listing = "\n".join(lines)
    return f"""# A-BAND-{ym}-{stamp}-{n} (deepen, {len(items)} article(s))

A-class taiwandaily articles with identity-matched person pages that do not
yet cite the article. You judge and record; you do not enumerate.

## THE LIST — this is your complete work list
{listing}

- Read the ledger first — already-decided urls are DONE, skip them:
  `cat ~/echo-system/knowledge/web-archives/tdm-{ym}-absorb-ledger.jsonl`
- For EACH numbered article, in order:
  - Read the article file (front-matter title + body).
  - Identity gate vs each candidate page: HIT = hanzi appears in the page
    `title`/`name_zh` or unambiguous bio. Collision/uncertain -> HOLD, never merge.
  - On HIT append one dated From-the-record line (date + fact +
    [美洲台灣日報](URL) + (reported) where hedged) to that page.
  - IMMEDIATELY record the decision (durable progress):
    `python3 ~/echo-system/scripts/taiwandaily-absorb-ledger.py {ym} --url URL --decision absorbed|skipped|hold [--page content/people/x.md] [--note why]`
- Close only when EVERY numbered article has a ledger line; close with
  `a-band-complete N=<decided this run>`. An honest GAPS line is success.

Contract: judgment work only. HOLD is cheap, wrong merges are not.
"""


def main() -> int:
    if in_freeze():
        print("SKIP_FREEZE a-band-build", flush=True)
        return 0
    if BATCH > MAX_ITEMS:
        print(f"ABAND_BATCH={BATCH} clamped to {MAX_ITEMS}", flush=True)
    months = sorted(
        p.name[len("tdm-"):-len("-absorb-ledger.jsonl")]
        for p in ARCH.glob("tdm-*-absorb-ledger.jsonl"))
    busy = open_months()
    cited = cited_ids()
    stamp = datetime.now(timezone.utc).strftime("%m%d")
    minted = 0
    for ym in months:
        if minted >= MAXCARDS:
            break
        if ym in busy:
            continue
        r = subprocess.run([sys.executable, str(PREP), "prep", ym,
                            "--batch", str(BATCH)],
                           capture_output=True, text=True, timeout=600)
        try:
            d = json.loads(r.stdout)
        except Exception:
            print("prep-fail", ym, (r.stderr or r.stdout)[:120], flush=True)
            continue
        keep: list[dict] = []
        for b in d.get("batches") or []:
            for it in b:
                if it.get("tag") != "hit":
                    continue
                m = re.search(r"/(\d+)/?$", it["url"].rstrip("/") + "/")
                if not m or m.group(1) in cited:
                    continue
                f = Path(it["file"])
                try:
                    if f.stat().st_size < MIN_BODY:
                        continue
                except OSError:
                    continue
                keep.append(it)
        if not keep:
            continue
        batch = keep[:BATCH]
        title = f"A-BAND-{ym}-{stamp}-1"
        made = mint_via(title, body_for(ym, batch, stamp, 1),
                        assignee="pinto",
                        backlog_source=f"a-band-build:{ym}",
                        budget_class="A-BAND")
        if made:
            minted += 1
            print("minted slice:", title, "articles=", len(batch), flush=True)
    print(f"A_BAND_RUN minted={minted} months_judged={len(months)} "
          f"busy={sorted(busy)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
