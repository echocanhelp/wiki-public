"""Dangling-link classifier: corpus and org links admit, hubs do not."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path("/home/leedt/echo-system/scripts/frontier-build.py")


def load():
    spec = importlib.util.spec_from_file_location("frontier_build", ROOT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


class FrontierBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load()

    def test_classify_rules(self):
        mod = self.mod
        self.assertEqual(mod.classify(
            corpus_hits=1, nonhub_org_linkers=0, nonhub_m_linkers=0,
            source_anchor=False, mention_files=1,
        ), "M")
        self.assertEqual(mod.classify(
            corpus_hits=0, nonhub_org_linkers=1, nonhub_m_linkers=1,
            source_anchor=False, mention_files=1,
        ), "M")
        self.assertEqual(mod.classify(
            corpus_hits=0, nonhub_org_linkers=0, nonhub_m_linkers=1,
            source_anchor=False, mention_files=2,
        ), "1")
        self.assertIsNone(mod.classify(
            corpus_hits=0, nonhub_org_linkers=0, nonhub_m_linkers=0,
            source_anchor=False, mention_files=4,
        ))

    def test_dry_run_on_a_tiny_corpus(self):
        mod = self.mod
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            content = tmp / "content"
            _write(content / "people" / "real.md", "---\ntitle: Real\ntype: person\n---\n# Real\n")
            _write(
                content / "organizations" / "small-org.md",
                "---\ntitle: Small\ntype: organization\ntier: M\n---\n"
                "# Small\n\nSee [[people/corpus-person|Corpus Person]] and [[people/real|Real]].\n",
            )
            _write(
                content / "articles" / "story.md",
                "---\ntitle: Story\n---\n\nCorpus Person spoke in 1998.\n",
            )
            _write(
                content / "people" / "a.md",
                "---\ntitle: A\ntype: person\ntier: M\n---\n\n[[people/twice-named|Twice Named]]\n",
            )
            _write(
                content / "people" / "b.md",
                "---\ntitle: B\ntype: person\ntier: M\n---\n\n[[people/twice-named|Twice Named]] again.\n",
            )
            for i in range(50):
                _write(content / "people" / f"pad-{i}.md", "---\ntitle: Pad\ntype: person\n---\n# Pad\n")
            hub_links = "\n".join(f"[[people/pad-{i}|Pad {i}]]" for i in range(50))
            hub_links += "\n[[people/hub-only|Hub Only]]\n"
            _write(
                content / "organizations" / "hub.md",
                "---\ntitle: Hub\ntype: organization\ntier: M\n---\n" + hub_links,
            )
            before = {p.relative_to(content) for p in content.rglob("*")}
            buf = StringIO()
            with redirect_stdout(buf):
                rc = mod.run(content, emit=False, repo=tmp, db=tmp / "no.db")
            out = buf.getvalue()
            self.assertEqual(rc, 0, out)
            self.assertIn("Corpus Person[M]", out)
            self.assertIn("Twice Named[1]", out)
            self.assertNotIn("Hub Only", out)
            self.assertIn("mode=dry-run", out)
            after = {p.relative_to(content) for p in content.rglob("*")}
            self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
