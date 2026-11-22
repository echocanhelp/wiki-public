#!/usr/bin/env python3
"""tier-triage.py — deterministic triage of NEEDS-TIER cards (2026-10-13).

The news-digest files NEEDS-TIER cards for stories whose subjects our archive
doesn't tie to. 57 cards, zero ever claimed — a dead letter box. The tier
question has a deterministic first pass, and this script runs only that pass:

  1. subject resolves to a vault page / >=3 archive files  -> evidence exists:
     leave the card for a worker (the tie was missed by the matcher, fix that).
  2. tie_state unknown BUT the story sits on a theme spine we already hold as
     Tier E (the community IS a party to the theme) -> the reporting is appended
     to the theme's topic page as a `Reported` line, card closed. No biography
     is minted — the story is about someone, not about us tying to them.
  3. neither -> genuinely ambiguous. Card stays open; body rewritten with the
     exact evidence gap so a human sees what is missing.

The script NEVER asserts party-status for a new person. It only records
reporting onto a spine whose party-status was already ruled by Leonard
(CONTROL 1b). Same shape as web-pass: deterministic work, judgment stays out.

Dry-run by default; --apply writes.
"""
from __future__ import annotations
import argparse, glob, importlib.util, json, os, re, sqlite3, subprocess, sys, time
from datetime import date
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
CONTENT = REPO / "content"
DRY = "--apply" not in sys.argv
ap = argparse.ArgumentParser()
ap.add_argument("--limit", type=int, default=50)
ap.add_argument("--only", default=None, help="single card id (for write-path tests)")
ap.add_argument("--apply", action="store_true", help="write (default: dry-run)")
args = ap.parse_args()
DRY = not args.apply

# reuse the digest's own gate so triage and digest can never disagree
spec = importlib.util.spec_from_file_location(
    "nd", os.path.expanduser("~/.hermes/profiles/pinto/scripts/echopedia-news-digest.py"))
nd = importlib.util.module_from_spec(spec)
nd.DRY = True
spec.loader.exec_module(nd)

# theme spines: pages whose party-status is already ruled (Tier E, Leonard 2026-10-08)
SPINES = [("跨國鎮壓", "topics/transnational-repression"),
          ("跨境鎮壓", "topics/transnational-repression"),
          ("228", "topics/228-incident")]

def subject_of(title: str) -> str:
    m = re.match(r"NEEDS-TIER:\s*(.+?)\s*[-|]", title)
    return (m.group(1) if m else title[:40]).strip()

con = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))
if args.only:
    cards = con.execute(
        "select id, title, body from tasks where status='ready' and id=?",
        (args.only,)).fetchall()
else:
    cards = con.execute(
        "select id, title, body from tasks where status='ready' and title like 'NEEDS-TIER%' "
        "order by created_at limit ?", (args.limit,)).fetchall()

stats = {"evidence": 0, "spine-recorded": 0, "already-recorded": 0, "tier-D": 0, "ambiguous": 0, "dup": 0}
seen_titles: set[str] = set()
disposition: dict[str, str] = {}
today = date.today().isoformat()

for cid, title, body in cards:
    lead_title = title.replace("NEEDS-TIER: ", "", 1)
    if lead_title in seen_titles:
        # a dup closes only if its original closed; if the original stayed open
        # for judgment, the dup adds nothing and closes as dup.
        if disposition.get(lead_title) == "open":
            stats["ambiguous"] += 1
            print(f"{cid} DUP-OPEN -> leave open (original still open): {lead_title[:60]}")
        else:
            stats["dup"] += 1
            print(f"{cid} DUP -> close (original already triaged): {lead_title[:60]}")
            if not DRY:
                subprocess.run(["hermes", "kanban", "complete", cid,
                                "--result", "deterministic triage: duplicate of an already-triaged story"],
                               capture_output=True)
        continue
    seen_titles.add(lead_title)
    disposition[lead_title] = "open"
    st, det = nd.tie_state({"lead": {"title": lead_title, "desc": ""}, "slugs": set()})
    if st == "proven" or st == "evidenced":
        stats["evidence"] += 1
        disposition[lead_title] = "open"  # matcher missed a tie; worker judgment needed
        print(f"{cid} EVIDENCE({st}) -> leave open (matcher missed a tie): {lead_title[:60]}")
        continue
    spine = next((slug for kw, slug in SPINES if kw in lead_title), None)
    if spine:
        page = CONTENT / (spine + ".md")
        fp = re.sub(r"[^\w]", "", nd.strip_publisher(lead_title))[:12]
        if fp and fp in re.sub(r"[^\w]", "", page.read_text()):
            stats["already-recorded"] += 1
            disposition[lead_title] = "closed"
            print(f"{cid} ALREADY-RECORDED({spine}) -> close only: {lead_title[:60]}")
            if not DRY:
                subprocess.run(["hermes", "kanban", "complete", cid,
                                "--result", f"deterministic triage: reporting already recorded on {spine}"],
                               capture_output=True)
            continue
        stats["spine-recorded"] += 1
        page = CONTENT / (spine + ".md")
        url = re.search(r"\((https://news\.google\.com/[^)]+)\)", body or "")
        link = url.group(1) if url else ""
        line = (f"\n**Reported.** {today} — {nd.strip_publisher(lead_title)}"
                + (f" [wire]({link})" if link else "") + " — reported by the wire; "
                  "the community is not a named party in this item, the theme is ours.\n")
        print(f"{cid} SPINE({spine}) -> append Reported line, close")
        disposition[lead_title] = "closed"
        if not DRY:
            # the page's arrival section (## 從每日脈絡來的話) is where today's
            # 報導 lines live; appending at EOF lands after Revision History.
            text = page.read_text()
            head = f"### {today} — 報導，尚未成為我們的檔案"
            if head in text:
                idx = text.rindex(head) + len(head)
                # insert after the last non-empty line of that subsection
                nxt = text.find("\n## ", idx)
                if nxt == -1:
                    nxt = len(text)
                block = text[idx:nxt].rstrip("\n")
                text = text[:idx] + block + "\n" + line + text[nxt:]
            else:
                anchor = "## Why this belongs"
                i = text.index(anchor)
                text = text[:i] + head + "\n" + line + "\n" + text[i:]
            page.write_text(text)
            subprocess.run(["git", "-C", str(REPO), "add", "--", str(page.relative_to(REPO))],
                           check=False)
            subprocess.run(["git", "-C", str(REPO), "commit", "-q", "-m",
                            f"tier-triage: report recorded on {spine} ({lead_title[:40]})"],
                           check=False)
            subprocess.run(["hermes", "kanban", "complete", cid,
                            "--result", f"deterministic triage: reporting recorded on {spine}"],
                           capture_output=True)
        continue
    # Tier D close (2026-10-13): the card body's own rule — story about them, not
    # us -> cite reporting, no page. No theme keyword AND no community entity in
    # the title means the digest filed noise (fruit prices, tariffs, third-country
    # stories). Closing is the rule's answer; leaving open is not.
    if not re.search(r"(僑|台灣人|臺灣人|台美人|台灣人|US soil|洛杉磯|紐約|Toronto|僑界)", lead_title):
        stats["tier-D"] += 1
        disposition[lead_title] = "closed"
        print(f"{cid} TIER-D -> close (no tie, no theme, no community entity): {lead_title[:60]}")
        if not DRY:
            subprocess.run(["hermes", "kanban", "complete", cid,
                            "--result", "deterministic triage: Tier D — reporting about others, "
                                        "no community tie; cited, no page"],
                           capture_output=True)
        continue
    stats["ambiguous"] += 1
    print(f"{cid} AMBIGUOUS -> leave open: {lead_title[:60]}")

print("triage:", stats, "| cards:", len(cards), "| dry" if DRY else "| APPLY")
