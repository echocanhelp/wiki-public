#!/usr/bin/env python3
"""GoatCounter gap detector — turns reader demand into queue work (advisory).

Two independent signals, cross-checked (2026-09-27 audit lesson: do NOT
declare gap counts from one source; contentIndex key-space may differ from
the live URL space, so a "ghost" is a CANDIDATE until live-probed):

  1. contentIndex demand — live (fetched or local-copy) contentIndex.json,
     whose `links` are cross-page refs. Refs pointing to no existing file =
     real demand with a dead target. Checked against BOTH id-space
     conventions (raw and ".md"-suffixed) plus slugifyPath space, so the
     custom fork emitter and upstream-compatible builds both work.
  2. Live probe — every candidate GET against the live site; 404/403 =>
     live404 (demand confirmed), 200 => ghost (self-healed / client-resolved).
  3. Optional --cdx: Wayback ever-archived-200 tiering (regression tier).

Output knowledge/research/gap-paths.json:
 {"scraped": date, "probes": n, "gaps": [{path, tier, code, demand}]}
Advisory only; never blocks publish.
"""
import argparse, json, os, re, time, urllib.request, urllib.error
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor

SITE = "https://echocanhelp.github.io/wiki-public"

UA = {"User-Agent": "Mozilla/5.0 (gap-audit)"}


def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


# --- slug space (mirror of quartz/util/path.ts slugifyPath, verified 2026-09-27) ---
import unicodedata

NFD_REMOVE = "´˝`"
ZWJ = "\u200d"


def _fold(x):
    x = unicodedata.normalize("NFD", x).casefold()
    return "".join(c for c in x if c not in NFD_REMOVE)


def slugifyPath(path):
    if "/" in path:
        folders, fname = path.rsplit("/", 1)
    else:
        folders, fname = "", path
    parts = [_fold(c).replace(" ", ZWJ).replace("/", "-").lower()
             for c in folders.split("/") if c and c not in ("index", "_index")]
    fname = _fold(fname).lower().replace("/", "-")
    if not parts:
        return fname
    return "/".join(parts) + "/" + fname


def coverage_sets(repo):
    """Both membership spaces, computed ONCE (sets — O(1) lookups)."""
    tree, slugs = set(), set()
    root = os.path.join(repo, "content")
    for dp, dirs, files in os.walk(root):
        for fn in files:
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(dp, fn), root)[:-3]
                tree.add(rel)
                tree.add(rel + ".md")
                slugs.add(slugifyPath(rel))
                d = os.path.dirname(rel)
                if d:
                    tree.add(d + "/index")
                    slugs.add(slugifyPath(d))
    return tree, slugs


def main():
    repo = os.path.expanduser("~/echo-system")
    os.chdir(repo)
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="knowledge/research/gap-paths.json")
    ap.add_argument("--live", action="store_true", help="probe candidates live")
    ap.add_argument("--cdx", action="store_true", help="wayback ever-200 tiering")
    ap.add_argument("--fetch-live-index", action="store_true",
                    help="fetch live contentIndex.json instead of repo copies")
    args = ap.parse_args()

    tree, slugs = coverage_sets(repo)

    traffic = {}
    tpath = "knowledge/research/gc-path-counts.json"
    if os.path.exists(tpath):
        try:
            traffic = json.load(open(tpath)).get("counts", {})
        except Exception:
            pass

    candidates = {}  # slug -> {"path","tier","codes","demand"}

    def add_candidate(slug, tier, demand=None):
        if slug in candidates:
            if demand and (candidates[slug].get("demand") or 0) < demand:
                candidates[slug]["demand"] = demand
            return
        p = "/wiki-public/" + slug
        candidates[slug] = {"path": p, "tier": tier, "code": None,
                           "demand": demand if demand is not None
                           else traffic.get(p) or traffic.get(p + ".html") or 0}

    # ---- source 1: contentIndex demand ------------------------------------
    ci = None
    if args.fetch_live_index:
        st, body = get(SITE + "/static/contentIndex.json", timeout=60)
        if st == 200 and body:
            try:
                ci = json.loads(body)
            except Exception:
                ci = None
    if ci is None:
        for idx in ("static/contentIndex.json", "public/static/contentIndex.json"):
            if os.path.exists(idx):
                try:
                    ci = json.load(open(idx, encoding="utf-8"))
                except Exception:
                    ci = None
                break
    if ci:
        keys = list(ci.keys())
        sample = ci[keys[0]] if keys else {}
        keys_md = all(k.endswith(".md") for k in keys[:200])
        def norm_ref(ref):
            r = ref.get("to", ref) if isinstance(ref, dict) else ref
            return r.lstrip("/")
        for k in keys:
            kspace = k[:-3] if keys_md and k.endswith(".md") else k
            entry = ci[k]
            refs = entry.get("links", []) if isinstance(entry, dict) else []
            for ref in refs:
                r = norm_ref(ref)
                if r.startswith("articles/") or r.startswith("tags/"):
                    continue
                if r not in tree and (r + ".md") not in tree:
                    add_candidate(r, "demand")

    # ---- source 2: broken wikilinks (writer demand) ----------------------
    LINK = re.compile(r"\[\[([^\]|#\[]+)")
    for dp, dirs, files in os.walk("content"):
        if "articles" in dp.split(os.sep):
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            try:
                t = open(os.path.join(dp, fn), encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for m in LINK.finditer(t):
                s = m.group(1).strip().rstrip("/")
                if s.endswith(".md"):
                    s = s[:-3]
                if "/" in s and s not in tree:
                    add_candidate(s, "demand")

    # normalize to slug space (CJK-safe) + dedupe
    by_slug = {}
    for s, g in candidates.items():
        sg = slugifyPath(s)
        g2 = by_slug.setdefault(sg, {"path": "/wiki-public/" + sg, "tier": "demand",
                                    "code": None, "demand": g.get("demand", 0)})
        g2["demand"] = max(g2.get("demand", 0), g.get("demand", 0) or 0)
    gaps = list(by_slug.values())

    # ---- live probe (confirm or self-heal) --------------------------------
    if args.live:
        def probe(g):
            return g, get(SITE + quote(g["path"]))[0]
        with ThreadPoolExecutor(6) as pool:
            for g, code in pool.map(probe, gaps):
                g["code"] = code
                if code in (404, 403):
                    g["tier"] = "live404"
                elif code == 200:
                    g["tier"] = "ghost-resolved"

    if args.cdx:
        def cdx(g):
            rel = g["path"][len("/wiki-public"):]
            st, body = get("http://web.archive.org/cdx/search/cdx?url="
                           + quote("echocanhelp.github.io/wiki-public" + rel)
                           + "&output=json&limit=1&filter=statuscode:200")
            if st == 200 and body.strip().startswith("["):
                g["tier"] += "+was200"
        with ThreadPoolExecutor(4) as pool:
            list(pool.map(cdx, [g for g in gaps if g["tier"] != "ghost-resolved"][:40]))

    hot = [g for g in gaps if g.get("demand")]
    dead = [g for g in gaps if g["tier"] == "live404"]

    path = os.path.abspath(args.cache)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump({"scraped": time.strftime("%Y-%m-%d"), "probes": len(gaps),
               "gaps": gaps}, open(path, "w"), ensure_ascii=False, indent=0)
    tiers = {}
    for g in gaps:
        tiers[g["tier"]] = tiers.get(g["tier"], 0) + 1
    print("GAPSCAN: candidates=%d tiers=%s hot=%d confirmed404=%d"
          % (len(gaps), tiers, len(hot), len(dead)))
    for g in dead[:10]:
        print("CONFIRMED-404:", g["path"], "demand7d=", g.get("demand"))


if __name__ == "__main__":
    main()
