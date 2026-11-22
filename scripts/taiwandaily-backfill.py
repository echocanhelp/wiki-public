#!/usr/bin/env python3
"""taiwandaily-backfill.py — deterministic vault backfill for taiwandaily.net (Gate A).

WEBSITE_INGEST Gate A for taiwandaily.net (owner `go echopedia website
taiwandaily.net`, 2026-11-18). The full-domain lane (taiwandaily-domain-build.py)
only ever loops the LAST 12 months (months_newest_first with FLOOR), so months
older than that can only enter the vault through this script: it walks
TD_BACKFILL_FLOOR (default 202101) .. last completed month, skips months whose
manifest already grades complete, and runs the SAME fetcher
(taiwandaily-month-fetch.py) — never an agent crawl card (agent crawl cards are
retired; a dead 30-turn crawl leaves a fragment that reads as a finished month).

State: shares knowledge/research/taiwandaily-domain-state.json 'crawled'.
Idempotent: a partial month is re-entered every run (the fetcher resumes per
article file and the manifest truncation veto protects good manifests).

Guards:
  - TOU freeze (15:45..21:00 America/Los_Angeles, swarm-pause-resume skill):
    exits 0 printing SKIP_FREEZE inside the window so a mis-timed cron burns
    nothing.
  - Per-run cap TD_BACKFILL_MAX (default 2 months/run) keeps one cron tick
    bounded (~1300-1600 posts/month).

no_agent cron: nightly 21:50 is the wired slot (post-thaw, pre-continuity).
"""
from __future__ import annotations

import datetime
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path.home() / "echo-system"
FETCHER = REPO / "scripts" / "taiwandaily-month-fetch.py"
STATE = REPO / "knowledge" / "research" / "taiwandaily-domain-state.json"
LOGDIR = Path.home() / ".hermes/profiles/pinto/logs"
PIDFILE = LOGDIR / "taiwandaily-backfill.pid"
FLOOR = int(os.environ.get("TD_BACKFILL_FLOOR", "202101"))
MAXM = int(os.environ.get("TD_BACKFILL_MAX", "1"))
# stale-pid guard: a dead host reboot (nightly 03:00) must not wedge the lane
PID_STALE_S = int(os.environ.get("TD_BACKFILL_PID_STALE", "18000"))


def already_running() -> bool:
    if not PIDFILE.exists():
        return False
    try:
        age = time.time() - PIDFILE.stat().st_mtime
        pid = int(PIDFILE.read_text().strip().split()[0])
        os.kill(pid, 0)
        if age < PID_STALE_S:
            return True
        print(f"STALE_PID {pid} age={int(age)}s — relaunching", flush=True)
    except (ProcessLookupError, ValueError, OSError):
        pass
    return False


def launch_detached(months: list[str]) -> int:
    """Run the months in a detached child; return after liveness proof.

    WHY detached: the hermes no_agent cron kills 'script' runs at 3600 s and
    an id-scan month legitimately needs ~1 h (18k-id probe range). The cron
    tick must LAUNCH and PROVE, not carry the fetch (learned 2026-11-18:
    ede526edf8b2 timed out at 3600 s with zero files). The fetcher's
    id-scan resume cache makes a killed run resumable, not lost.
    """
    LOGDIR.mkdir(parents=True, exist_ok=True)
    log = open(LOGDIR / "taiwandaily-backfill.log", "ab", buffering=0)
    env = dict(os.environ, TD_BACKFILL_MAX=str(len(months)),
               TD_BACKFILL_NO_LAUNCH="1")
    p = subprocess.Popen([sys.executable, os.path.abspath(__file__)] + months,
                         stdout=log, stderr=log, start_new_session=True,
                         env=env, cwd=str(REPO))
    PIDFILE.write_text(f"{p.pid} {' '.join(months)}\n")
    time.sleep(3)
    try:
        os.kill(p.pid, 0)
        print(f"LAUNCHED pid={p.pid} months={months} "
              f"log={LOGDIR / 'taiwandaily-backfill.log'}", flush=True)
        return 0
    except ProcessLookupError:
        print(f"LAUNCH_DEAD pid={p.pid} months={months} — see log", flush=True)
        return 1


def in_freeze() -> bool:
    """TOU freeze 15:45-21:00 America/Los_Angeles (no heavy network in it)."""
    try:
        from zoneinfo import ZoneInfo
        now = datetime.datetime.now(ZoneInfo("America/Los_Angeles"))
    except Exception:
        return False  # no tz data: don't block the pipeline on it
    hm = now.hour * 60 + now.minute
    return 15 * 60 + 45 <= hm < 21 * 60


def month_complete(ym: str) -> bool:
    """Same grade-first rule as taiwandaily-domain-build.month_complete."""
    dest = REPO / f"knowledge/web-archives/tdm-{ym}.json"
    if not dest.exists():
        return False
    try:
        d = json.loads(dest.read_text())
    except Exception:
        return False
    results = d.get("results") or []
    if not results:
        return False
    sp = importlib.util.spec_from_file_location(
        "tdm_fetch", str(FETCHER))
    if sp is None or sp.loader is None:
        return False
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    done, _cov = mod.grade(ym, d.get("listed") or len(results), results)
    return done


def months_to_do() -> list[str]:
    out = []
    y, m = datetime.date.today().year, datetime.date.today().month
    # last COMPLETED month: the current month is the lane's own job
    m -= 1
    if m == 0:
        y, m = y - 1, 12
    while y * 100 + m >= FLOOR:
        ym = str(y * 100 + m)
        if not month_complete(ym):
            out.append(ym)
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return out


def load_state() -> dict:
    if STATE.exists():
        s = json.load(open(STATE))
        return {"crawled": [str(x) for x in s.get("crawled", [])],
                "carded": [str(x) for x in s.get("carded", [])]}
    return {"crawled": [], "carded": []}


def save_state(s: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    json.dump(s, open(STATE, "w"), indent=1)


def run_worker(months: list[str]) -> int:
    rc_any = 0
    state = load_state()
    crawled = set(state["crawled"])
    for ym in months:
        print(f"FETCH {ym}", flush=True)
        r = subprocess.run([sys.executable, str(FETCHER), ym], timeout=5400)
        if r.returncode != 0:
            rc_any = 1
        if month_complete(ym):
            crawled.add(ym)
            print(f"MARKED {ym}", flush=True)
    state["crawled"] = sorted(crawled)
    save_state(state)
    print(f"BACKFILL_RUN done={months} crawled={len(crawled)} "
          f"remaining={len(months_to_do())}", flush=True)
    return rc_any


def main(argv: list[str]) -> int:
    months = [a for a in argv if re.fullmatch(r"\d{6}", a)]
    if months:  # detached worker mode (launched by launch_detached)
        try:
            return run_worker(months)
        finally:
            PIDFILE.unlink(missing_ok=True)
    if in_freeze():
        print("SKIP_FREEZE taiwandaily-backfill (TOU 15:45-21:00 PT)", flush=True)
        return 0
    todo = months_to_do()
    if not todo:
        print("BACKFILL_COMPLETE floor=%d" % FLOOR, flush=True)
        return 0
    if already_running():
        print("RUNNING — skip this tick", flush=True)
        return 0
    # oldest-first: the historical record first, newest gap last
    todo = sorted(todo)[:MAXM]
    return launch_detached(todo)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
