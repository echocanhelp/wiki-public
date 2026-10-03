"""Tier floors: known expansion pages pass; a 900-byte tier-M stub fails."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path("/home/leedt/echo-system")
SCRIPT = ROOT / "scripts" / "substance-lint.py"

PASS_PAGES = [
    "organizations/stc-management.md",
    "organizations/stc-rowland-legacy.md",
    "organizations/yes-plaza.md",
    "people/john-hsu.md",
    "organizations/ai-education-foundation.md",
    "organizations/rowland-heights-chinese-association.md",
    "people/pan-yi-ling.md",
    "organizations/american-chinese-dance-association.md",
    "organizations/forus-foundation.md",
]


def load():
    spec = importlib.util.spec_from_file_location("substance_lint", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TierFloors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lint = load()

    def test_expansion_pages_pass(self):
        root = ROOT / "content"
        for rel in PASS_PAGES:
            text = (root / rel).read_text(encoding="utf-8")
            bad = [ln for ln in self.lint.lint_text(rel, text) if self.lint.is_violation(ln)]
            self.assertEqual(bad, [], rel)

    def test_900_byte_tier_m_is_flagged(self):
        page = (
            "---\n"
            "title: Thin M\n"
            "type: person\n"
            "tier: M\n"
            "---\n"
            "# Thin M\n\n"
            "## Identity Snapshot\n"
            "- Era: Contemporary\n"
            "- Geography: Nowhere\n"
            "- Core roles: example\n\n"
            "## Record\n"
            "A short community mention with no dated source and no quote.\n\n"
            "## Related Pages\n"
            "- [[people/john-hsu|John Hsu]]\n"
        )
        filler = " Nothing sourced is recorded here."
        while len(page.encode()) + len(filler.encode()) <= 900:
            page += filler
        self.assertLessEqual(len(page.encode()), 900)
        bad = [ln for ln in self.lint.lint_text("people/thin.md", page) if self.lint.is_violation(ln)]
        self.assertTrue(any(ln.startswith("FLOOR:") for ln in bad), bad)

    def test_tier2_requires_publish_false(self):
        page = (
            "---\n"
            "title: Far\n"
            "type: person\n"
            "tier: 2\n"
            "---\n"
            "# Far\n\n"
            "A context line only.\n"
        )
        bad = self.lint.lint_text("people/far.md", page)
        self.assertTrue(any(ln.startswith("TIER2_PUBLISH:") for ln in bad))
        ok = page.replace("tier: 2\n", "tier: 2\npublish: false\n")
        self.assertFalse(any(self.lint.is_violation(ln) for ln in self.lint.lint_text("people/far.md", ok)))

    def test_online_arms_floor(self):
        def page(arms: str) -> str:
            return (
                "---\n"
                "title: Armed\n"
                "type: organization\n"
                "tier: M\n"
                "---\n"
                "# Armed\n\n"
                "## Record\n"
                "- Founded 1999 per the board minutes, [[people/john-hsu|John Hsu]] attended.\n"
                "- Second gala in 2001, documented in the World Journal.\n"
                "- Third fact $10,000 raised in 2004 according to the LA Times.\n\n"
                "## Online arms\n"
                f"{arms}\n"
            )

        thin = page("- zh.wikipedia: miss (searched Armed Org, 2026-10-02)\n")
        bad = [ln for ln in self.lint.lint_text("organizations/armed.md", thin) if self.lint.is_violation(ln)]
        self.assertTrue(any(ln.startswith("ONLINE_ARMS_UNACCOUNTED:") for ln in bad), bad)

        full = page(
            "- zh.wikipedia: miss (searched Armed Org, 2026-10-02)\n"
            "- wikidata: HOLD no distinct item\n"
            "- official site: miss (searched Armed Org official, 2026-10-02)\n"
            "- World Journal: absorb the 2001 gala line\n"
        )
        bad = [ln for ln in self.lint.lint_text("organizations/armed.md", full) if self.lint.is_violation(ln)]
        self.assertEqual(bad, [])

    def test_publish_gate_holds_on_a_legacy_shaped_corpus(self):
        lint = self.lint
        with tempfile.TemporaryDirectory() as tmp:
            people = Path(tmp) / "content" / "people"
            people.mkdir(parents=True)
            stub = (
                "---\n"
                "title: Nobody\n"
                "type: person\n"
                "---\n"
                "# Nobody\n\n"
                "A name with no sourced fact.\n"
            )
            for i in range(60):
                (people / f"p{i}.md").write_text(stub)
            rows = []
            for p in sorted(people.glob("*.md")):
                rel = f"people/{p.name}"
                rows.append((rel, lint.lint_text(rel, p.read_text())))
            exclude, summary = lint.gate_decision(rows, enforce=False)
            self.assertIn("enforced=HOLD", summary)
            self.assertEqual(exclude, [])
            exclude2, summary2 = lint.gate_decision(rows, enforce=True)
            self.assertIn("enforced=yes", summary2)
            self.assertEqual(len(exclude2), 60)


if __name__ == "__main__":
    unittest.main()
