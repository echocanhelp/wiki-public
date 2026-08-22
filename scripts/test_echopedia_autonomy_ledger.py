#!/usr/bin/env python3
"""Planted tests for the autonomy ledger + catalog builder (daily track).

Covers Tasks 1-3 of the autonomy daily-track plan:
  - Task 1: ledger schema requires date, nodes, <=8 telegram_auto_lines
  - Task 2: build_ledger() from fixtures (no live FS yet)
  - Task 3: build_catalog() full node map; B/C/D disabled
  - Task 4: file loaders parse real overnight artifacts
"""
import importlib.util
import sys
import unittest
from pathlib import Path

MOD_PATH = Path("/home/leedt/echo-system/scripts/echopedia-autonomy-collect.py")
spec = importlib.util.spec_from_file_location("echopedia_autonomy_collect", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules["echopedia_autonomy_collect"] = mod
spec.loader.exec_module(mod)


def _standards(v=10, auto_apply=False, fm_enabled=True):
    return {
        "version": v,
        "janitor": {
            "auto_apply_agent": auto_apply,
            "first_mention_apply": {"enabled": fm_enabled},
        },
    }


def _jobs(*names_status):
    """names_status: list of (name, enabled, last_status)"""
    return {
        "jobs": [
            {"name": n, "enabled": e, "last_status": s}
            for (n, e, s) in names_status
        ]
    }


def _queue(scanned=1658, queued=52, suppressed=0):
    return {
        "total_pages_scanned": scanned,
        "auto_queued": queued,
        "suppressed_findings": suppressed,
    }


class LedgerSchemaTests(unittest.TestCase):
    """Task 1 — locking the JSON contract before the collector exists."""

    def test_ledger_requires_date_and_nodes(self):
        raw = mod.build_ledger(
            jobs={"jobs": []},
            janitor_run={"healed_mentions": ["a.md"], "healed_related": []},
            queue=_queue(),
            standards=_standards(),
        )
        self.assertTrue(raw["date"])
        self.assertIn("nodes", raw)
        self.assertIsInstance(raw["telegram_auto_lines"], list)
        self.assertLessEqual(len(raw["telegram_auto_lines"]), 8)


class LedgerFromFixturesTests(unittest.TestCase):
    """Task 2 — pure function: inputs in, ledger out."""

    def test_first_mention_count_becomes_auto_line(self):
        ledger = mod.build_ledger(
            jobs=_jobs(("echopedia-janitor", True, "ok")),
            janitor_run={"healed_mentions": ["a.md", "b.md"], "healed_related": []},
            queue=_queue(),
            standards=_standards(),
            enrichment_today=[],
            kanban_blocked=[],
        )
        text = "\n".join(ledger["telegram_auto_lines"])
        self.assertIn("first-mention", text.lower())
        self.assertIn("2", text)
        self.assertIn("suppressed 0", text.lower()) or self.assertIn(
            "queued 52", text.lower()
        )
        self.assertLessEqual(len(ledger["telegram_auto_lines"]), 8)

    def test_enrichment_write_becomes_queue_not_auto(self):
        ledger = mod.build_ledger(
            jobs=_jobs(),
            janitor_run={"healed_mentions": [], "healed_related": []},
            queue=_queue(suppressed=1),
            standards=_standards(),
            enrichment_today=[{"page": "x", "wrote": True}],
            kanban_blocked=[],
        )
        text = "\n".join(ledger["telegram_auto_lines"])
        self.assertIn("enrichment", text.lower())

    def test_kanban_blocked_becomes_queue_line(self):
        ledger = mod.build_ledger(
            jobs=_jobs(),
            janitor_run={"healed_mentions": [], "healed_related": []},
            queue=_queue(),
            standards=_standards(),
            enrichment_today=[],
            kanban_blocked=[{"title": "needs creds"}],
        )
        text = "\n".join(ledger["telegram_auto_lines"])
        self.assertIn("kanban", text.lower())

    def test_no_lines_falls_back(self):
        ledger = mod.build_ledger(
            jobs=_jobs(),
            janitor_run={"healed_mentions": [], "healed_related": []},
            queue=_queue(),
            standards=_standards(),
            enrichment_today=[],
            kanban_blocked=[],
        )
        self.assertTrue(ledger["telegram_auto_lines"])
        self.assertLessEqual(len(ledger["telegram_auto_lines"]), 8)

    def test_cron_fail_tracked(self):
        ledger = mod.build_ledger(
            jobs=_jobs(("ci-heal", True, "error")),
            janitor_run={"healed_mentions": [], "healed_related": []},
            queue=_queue(),
            standards=_standards(),
            enrichment_today=[],
            kanban_blocked=[],
        )
        self.assertIn("ci-heal", ledger["cron_fail_names"])

    def test_auto_apply_agent_flag(self):
        ledger = mod.build_ledger(
            jobs=_jobs(),
            janitor_run={"healed_mentions": [], "healed_related": []},
            queue=_queue(),
            standards=_standards(auto_apply=True),
            enrichment_today=[],
            kanban_blocked=[],
        )
        self.assertTrue(ledger["auto_apply_agent"])
        ledger2 = mod.build_ledger(
            jobs=_jobs(),
            janitor_run={"healed_mentions": [], "healed_related": []},
            queue=_queue(),
            standards=_standards(auto_apply=False),
            enrichment_today=[],
            kanban_blocked=[],
        )
        self.assertFalse(ledger2["auto_apply_agent"])


class CatalogFromFixtureTests(unittest.TestCase):
    """Task 3 — build_catalog() returns the full closed-list node map."""

    def test_catalog_includes_first_mention_and_disabled_b(self):
        cat = mod.build_catalog(
            standards=_standards(),
            jobs=_jobs(
                ("echopedia-janitor", True, "ok"),
                ("vault-morning-brief", True, "ok"),
            ),
        )
        ids = {n["id"] for n in cat["nodes"]}
        self.assertIn("janitor.first_mention", ids)
        b = next(n for n in cat["nodes"] if n["id"] == "kanban.auto_go")
        self.assertFalse(b["enabled"])

    def test_catalog_all_closed_list_ids_present(self):
        cat = mod.build_catalog(
            standards=_standards(),
            jobs=_jobs(),
        )
        ids = {n["id"] for n in cat["nodes"]}
        expected = {
            "cron.crons",
            "janitor.first_mention",
            "janitor.related",
            "janitor.hold",
            "ci_heal",
            "analyzer",
            "generate_cards",
            "enrichment_writes",
            "watchdogs",
            "kanban.blocked",
            "standards",
            "kanban.auto_go",
            "kanban.retry_timeout",
            "enrichment.page_write",
        }
        self.assertTrue(expected.issubset(ids), f"missing {expected - ids}")

    def test_bcd_flags_disabled(self):
        cat = mod.build_catalog(
            standards=_standards(),
            jobs=_jobs(),
        )
        by_id = {n["id"]: n for n in cat["nodes"]}
        for flag in ("kanban.auto_go", "kanban.retry_timeout", "enrichment.page_write"):
            self.assertFalse(by_id[flag]["enabled"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
