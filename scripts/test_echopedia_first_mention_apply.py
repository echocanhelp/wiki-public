#!/usr/bin/env python3
"""Planted tests for fail-closed first-mention apply (Slice A)."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MOD_PATH = Path("/home/leedt/echo-system/scripts/echopedia-first-mention-apply.py")
spec = importlib.util.spec_from_file_location("echopedia_first_mention_apply", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules["echopedia_first_mention_apply"] = mod
spec.loader.exec_module(mod)


def _page(root: Path, rel: str, body: str, *, title=None, typ=None, redirect_to=None):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = ["---", f'title: "{title or path.stem}"']
    if typ:
        fm.append(f"type: {typ}")
    if redirect_to:
        fm.append("verification_status: redirect")
        fm.append(f"redirect_to: {redirect_to}")
    fm.append("---")
    path.write_text("\n".join(fm) + "\n" + body + "\n", encoding="utf-8")
    return path


class FirstMentionApplyTests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        self.lex = {
            "cai-yingwen": "tsai-ing-wen",
            "lai-qingde": "lai-ching-te",
            "hou-youyi": "hou-yu-ih",
            "xie-changting": "frank-hsieh",
            "cai-jinrong": "gene-tsai",
        }

    def tearDown(self):
        self.td.cleanup()

    def test_resolve_redirect_to_canonical_not_old_slug(self):
        _page(self.root, "people/cai-yingwen.md", "Moved", title="Redirect", typ="person", redirect_to="tsai-ing-wen")
        _page(self.root, "people/tsai-ing-wen.md", "President.", title="Tsai Ing-wen (蔡英文)", typ="person")
        dest, reason = mod.resolve_dest("people/cai-yingwen", self.root, self.lex)
        self.assertEqual(dest, "people/tsai-ing-wen", reason)
        self.assertNotIn("cai-yingwen", dest)

    def test_reject_seminary_typed_person(self):
        _page(
            self.root,
            "people/san-francisco-theological-seminary.md",
            "A school.",
            title="San Francisco Theological Seminary",
            typ="person",
        )
        dest, reason = mod.resolve_dest(
            "people/san-francisco-theological-seminary", self.root, self.lex
        )
        self.assertIsNone(dest)
        self.assertEqual(reason, "hold_type")

    def test_prefer_org_over_source_same_stem(self):
        _page(self.root, "organizations/irvine-taiwanese-presbyterian-church.md", "Church.", typ="organization")
        _page(self.root, "sources/irvine-taiwanese-presbyterian-church.md", "History doc.", typ="source")
        page = "She served at Irvine Taiwanese Presbyterian Church in 2020."
        dest, reason = mod.choose_dest(
            "sources/irvine-taiwanese-presbyterian-church",
            page,
            self.root,
            self.lex,
        )
        self.assertEqual(dest, "organizations/irvine-taiwanese-presbyterian-church", reason)

    def test_skip_source_when_org_already_linked(self):
        _page(self.root, "organizations/irvine-taiwanese-presbyterian-church.md", "Church.", typ="organization")
        _page(self.root, "sources/irvine-taiwanese-presbyterian-church.md", "Doc.", typ="source")
        page = "Pastor at [[organizations/irvine-taiwanese-presbyterian-church|ITPC]]."
        dest, reason = mod.choose_dest(
            "sources/irvine-taiwanese-presbyterian-church",
            page,
            self.root,
            self.lex,
        )
        self.assertIsNone(dest)
        self.assertEqual(reason, "org_already_linked")

    def test_wrap_first_plain_mention_only(self):
        text = "Chen Meihui served ITPC. Later Chen Meihui left."
        new, n = mod.wrap_first_mention(
            text, r"Chen Meihui", "people/chen-meihui"
        )
        self.assertEqual(n, 1)
        self.assertIn("[[people/chen-meihui|Chen Meihui]] served ITPC.", new)
        self.assertIn("Later Chen Meihui left.", new)
        self.assertEqual(new.count("[[people/chen-meihui"), 1)

    def test_does_not_wrap_inside_existing_wikilink_or_md_link(self):
        text = "See [[people/chen-meihui|Chen Meihui]] and [Chen Meihui](https://ex.com)."
        new, n = mod.wrap_first_mention(text, r"Chen Meihui", "people/chen-meihui")
        self.assertEqual(n, 0)
        self.assertEqual(new, text)

    def test_does_not_treat_sparse_as_apply(self):
        lines = ["LINK_BODY_SPARSE: people/x.md (body_wikis=0 related=7)"]
        acts = mod.targets_from_hygiene(lines)
        self.assertEqual(acts, [])

    def test_apply_writes_canonical_and_skips_frontmatter(self):
        _page(self.root, "people/tsai-ing-wen.md", "Bio.", title="Tsai Ing-wen (蔡英文)", typ="person")
        src = _page(
            self.root,
            "organizations/taiwanjustice-net.md",
            "Coverage of 蔡英文 in 2020.",
            title="taiwanjustice",
            typ="organization",
        )
        r = mod.apply_page(
            src,
            ["LINK_UNLINKED_ENTITY: organizations/taiwanjustice-net.md → people/cai-yingwen"],
            content_root=self.root,
            lexicon=self.lex,
            dry_run=False,
        )
        self.assertEqual(r["wrote"], True, r)
        out = src.read_text(encoding="utf-8")
        self.assertIn("[[people/tsai-ing-wen|蔡英文]]", out)
        self.assertNotIn("cai-yingwen", out)
        self.assertTrue(out.startswith("---"))


if __name__ == "__main__":
    unittest.main()
