#!/usr/bin/env python3
"""Autonomy catalog + daily ledger. Called from vault-morning-brief (no cron).

Stdout silent on success unless --print-auto.
Never writes wiki pages. Never enables B/C/D.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date, datetime
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
INTEL = REPO / "knowledge" / "operational" / "intelligence"
LEDGER_PATH = INTEL / "autonomy-ledger.json"
CATALOG_PATH = INTEL / "autonomy-catalog.json"
JOBS_PATH = Path("/home/leedt/.hermes/profiles/pinto/cron/jobs.json")
STANDARDS_PATH = REPO / "echopedia" / "standards.json"
QUEUE_PATH = REPO / "echopedia" / "content-analysis-queue.json"
JANITOR_LOG_DIR = REPO / "knowledge" / "operational" / "janitor-log"
ENRICH_PATH = REPO / "knowledge" / "operational" / "content-analysis" / "enrichment-decisions.jsonl"
DRAIN_BRIEF = REPO / "echopedia" / "drain-brief.md"
JANITOR_BRIEF = REPO / "echopedia" / "janitor-brief.md"

WATCHDOG_OK_ERROR = {"vllm-thermal-scaler", "unified-watchdog", "kanban-sync"}
ESCALATE_FAIL = {
    "echopedia-ci-heal",
    "echopedia-docs-sync",
    "vault-morning-brief",
    "echopedia-digest",
}


def build_ledger(
    *,
    jobs: dict,
    janitor_run: dict,
    queue: dict,
    standards: dict,
    enrichment_today: list | None = None,
    kanban_blocked: list | None = None,
    hold_count: int = 0,
) -> dict:
    mentions = list(janitor_run.get("healed_mentions") or [])
    related = list(janitor_run.get("healed_related") or [])
    lines: list[str] = []
    nodes: dict = {}

    if mentions:
        lines.append(f"✅ AUTO first-mention {len(mentions)} page(s)")
    nodes["janitor.first_mention"] = {"n": len(mentions), "enabled": True}

    if related:
        lines.append(f"✅ AUTO related-pages {len(related)}")
    nodes["janitor.related"] = {"n": len(related)}

    scanned = int(queue.get("total_pages_scanned") or 0)
    queued = int(queue.get("auto_queued") or 0)
    supp = int(queue.get("suppressed_findings") or 0)
    if scanned or queued or supp == 0:
        lines.append(f"✅ AUTO analyzer scanned {scanned} queued {queued} suppressed {supp}")
    nodes["analyzer"] = {"scanned": scanned, "queued": queued, "suppressed": supp}

    wrote = [e for e in (enrichment_today or []) if e.get("wrote")]
    if wrote:
        lines.append(f"🟡 QUEUE enrichment wrote {len(wrote)} page(s) — review identity")
    nodes["enrichment_writes"] = {"n": len(wrote), "enabled": False}

    if hold_count:
        lines.append(f"🟡 QUEUE janitor HOLD leftover {hold_count}")
    nodes["janitor.hold"] = {"n": hold_count}

    blocked = kanban_blocked or []
    if blocked:
        lines.append(f"🟡 QUEUE kanban blocked {len(blocked)}")
    nodes["kanban.blocked"] = {"n": len(blocked)}
    nodes["kanban.auto_go"] = {"enabled": False}
    nodes["kanban.retry_timeout"] = {"enabled": False}

    jan = standards.get("janitor") or {}
    nodes["standards"] = {
        "version": standards.get("version"),
        "auto_apply_agent": bool(jan.get("auto_apply_agent")),
        "first_mention_apply": bool((jan.get("first_mention_apply") or {}).get("enabled")),
    }

    cron_fail: list[str] = []
    for j in jobs.get("jobs") or []:
        if not j.get("enabled"):
            continue
        name = j.get("name") or j.get("id") or "?"
        st = j.get("last_status")
        if j.get("last_delivery_error"):
            cron_fail.append(name)
            continue
        if st in ("ok", None, ""):
            continue
        if name in WATCHDOG_OK_ERROR and not j.get("last_delivery_error"):
            continue
        if name in ESCALATE_FAIL or st == "error":
            if name not in WATCHDOG_OK_ERROR:
                cron_fail.append(name)
    if cron_fail:
        lines.append("🔴 NEED YOU cron fail: " + ", ".join(cron_fail[:4]))
    nodes["cron.fail"] = cron_fail

    if not lines:
        lines.append("✅ AUTO overnight ok (0 writes)")
    return {
        "date": date.today().isoformat(),
        "standards_version": standards.get("version"),
        "auto_apply_agent": bool(jan.get("auto_apply_agent")),
        "nodes": nodes,
        "telegram_auto_lines": lines[:8],
        "cron_fail_names": cron_fail,
    }


def build_catalog(standards: dict | None = None, jobs: dict | None = None) -> dict:
    std = standards or {}
    jan = std.get("janitor") or {}
    fm = bool((jan.get("first_mention_apply") or {}).get("enabled"))
    job_list = (jobs or {}).get("jobs") or []
    nodes = [
        {
            "id": "cron.crons",
            "enabled": bool(job_list),
            "human": False,
            "ssot": "pinto cron/jobs.json",
            "count": len(job_list),
        },
        {
            "id": "janitor.first_mention",
            "enabled": fm,
            "human": False,
            "ssot": "standards.janitor.first_mention_apply",
        },
        {
            "id": "janitor.related",
            "enabled": bool(jan.get("auto_apply_programmable", True)),
            "human": False,
            "ssot": "standards.janitor.auto_apply_programmable",
        },
        {
            "id": "janitor.hold",
            "enabled": True,
            "human": True,
            "ssot": "drain-brief / janitor-brief NO_SAFE_ACT",
        },
        {
            "id": "ci_heal",
            "enabled": True,
            "human": False,
            "ssot": "standards.autonomy.l3_auto_push_on_green",
        },
        {
            "id": "analyzer",
            "enabled": True,
            "human": False,
            "ssot": "echopedia-content-analysis-queue.json",
        },
        {
            "id": "generate_cards",
            "enabled": True,
            "human": False,
            "ssot": "knowledge/operational/generated/ + review-gate-brief",
        },
        {
            "id": "enrichment_writes",
            "enabled": False,
            "human": True,
            "ssot": "auto_apply_agent false",
        },
        {
            "id": "watchdogs",
            "enabled": True,
            "human": False,
            "ssot": "cron jobs.json",
        },
        {
            "id": "kanban.blocked",
            "enabled": True,
            "human": True,
            "ssot": "hermes kanban list --status blocked",
        },
        {
            "id": "standards",
            "enabled": True,
            "human": False,
            "ssot": "echopedia/standards.json",
        },
        # B/C/D autonomy flags — never enabled by this plan
        {
            "id": "kanban.auto_go",
            "enabled": False,
            "human": True,
            "ssot": "WHERE L4+ / plan less-hitl",
        },
        {
            "id": "kanban.retry_timeout",
            "enabled": False,
            "human": True,
            "ssot": "WHERE L4+",
        },
        {
            "id": "enrichment.page_write",
            "enabled": False,
            "human": True,
            "ssot": "auto_apply_agent false",
        },
    ]
    return {"updated": datetime.now().isoformat(timespec="seconds"), "nodes": nodes}

def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def load_latest_janitor_run(path: Path) -> dict:
    if not path.is_file():
        return {}
    last = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "run_at" in rec and "page" not in rec:
            last = rec
    return last


def load_enrichment_today(path: Path, today: str | None = None) -> list:
    today = today or date.today().isoformat()
    out = []
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = str(rec.get("timestamp") or "")
        if ts.startswith(today):
            out.append(rec)
    return out


def load_hold_count(*briefs: Path) -> int:
    n = 0
    for p in briefs:
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        n += len(re.findall(r"NO_SAFE_ACT", text))
    return n


def load_kanban_blocked() -> list:
    try:
        r = subprocess.run(
            ["hermes", "kanban", "list", "--status", "blocked"],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return []
    if r.returncode != 0:
        return []
    return [ln for ln in (r.stdout or "").splitlines() if ln.strip().startswith("⊘")]


def collect_live() -> tuple[dict, dict]:
    jobs = load_json(JOBS_PATH, {"jobs": []})
    today = date.today().isoformat()
    janitor_run = load_latest_janitor_run(JANITOR_LOG_DIR / f"{today}.jsonl")
    queue = load_json(QUEUE_PATH, {})
    standards = load_json(STANDARDS_PATH, {})
    enrichment = load_enrichment_today(ENRICH_PATH, today)
    blocked = load_kanban_blocked()
    hold = load_hold_count(DRAIN_BRIEF, JANITOR_BRIEF)
    ledger = build_ledger(
        jobs=jobs,
        janitor_run=janitor_run,
        queue=queue,
        standards=standards,
        enrichment_today=enrichment,
        kanban_blocked=blocked,
        hold_count=hold,
    )
    catalog = build_catalog(standards, jobs)
    # attach cron nodes from jobs
    catalog["cron_jobs"] = [
        {
            "name": j.get("name"),
            "enabled": j.get("enabled"),
            "no_agent": j.get("no_agent"),
            "last_status": j.get("last_status"),
            "last_run_at": j.get("last_run_at"),
        }
        for j in jobs.get("jobs") or []
    ]
    return ledger, catalog


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--print-auto", action="store_true")
    args = ap.parse_args(argv)
    ledger, catalog = collect_live()
    INTEL.mkdir(parents=True, exist_ok=True)
    LEDGER_PATH.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")
    if args.print_auto:
        print("\n".join(ledger["telegram_auto_lines"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
