#!/usr/bin/env python3
"""taiwandaily-domain-build.py — absorb-card builder for taiwandaily.net.

Enumeration is NOT this script's job and NOT a worker's job. The no_agent
fetcher `scripts/taiwandaily-month-fetch.py YYYYMM` walks the WordPress date
archive https://www.taiwandaily.net/date/YYYY/MM/page/N/ (direct curl, 10
in-month posts per page, parse per `td-module-` block) and writes
knowledge/web-archives/tdm-YYYYMM.json. Agent crawl cards were retired
2026-10-18: a month is ~1,300-1,600 posts, one fetch per tool call dies at
`Iteration budget exhausted (30/30)`, and the fragment left behind reads as a
finished month. Do not re-add a crawl card class; do not raise agent.max_turns.

One card kind:
  TAIWANDAILY-ABSORB-YYYYMM  SLICE card (v2, 2026-10-19 churn fix): the
                             builder runs taiwandaily-slice-prep.py (no LLM)
                             to pre-select + hanzi identity pre-filter, and
                             the card carries an explicit URL list of
                             TD_DOMAIN_BATCH (default 8) articles. The worker
                             only judges; per-article decisions go through
                             taiwandaily-absorb-ledger.py (fsync); month
                             closure is graded by ledger-coverage +
                             swarm-churn-sweep.py, never by worker self-report.
                             Minted only when grade() says the month is complete.
                             `--remint` archives v1 whole-month cards (title
                             -v1 suffix) so slice cards can be minted.

State: knowledge/research/taiwandaily-domain-state.json
Idempotent: skips months already carded. Newest-first.

Env: TD_DOMAIN_MAXCARDS ready cards per run (default 10)
     TD_DOMAIN_FLOOR  oldest month to seed (default 202101)
     TD_DOMAIN_BATCH  articles per slice card (TD-FIX-20261117 t_41245b8f:
                      default DERIVED from mint_gate.MAX_ITEMS — see td_batch();
                      SSOT S4 anti-ratchet rule before making it adaptive)
"""
import json, os, re, sqlite3, subprocess, sys, time
from pathlib import Path

# SWARM-GUARD-1 (t_0cb42501): fail-closed backlog gate + SWARM-GUARD-2
# (t_4c357f44): ALL mints route through mint_gate.pre_mint_gate via
# mint_gate.mint_via. Imported at module scope — the prior run moved it into
# main() while make_card (defined outside main) still called gated_once,
# which made every run die NameError before minting anything (live repro
# 2026-11-15 13:55).
sys.path.insert(0, str(Path.home() / '.hermes' / 'scripts'))
from mint_guard import gated_once, budget_args  # noqa: E402
from mint_gate import mint_via, MAX_ITEMS  # noqa: E402  SWARM-GUARD-2
# TD-FIX-20261117 (t_41245b8f) item 3: the mint_gate slicing authority is
# MAX_ITEMS — a numbered list longer than it gets re-chunked into gate [i/n]
# titles (the silent-drop shape). The effective batch is DERIVED from this
# import — never a copied integer — and mint_gate._td_item_cap_floor()
# self-checks the TAIWANDAILY-ABSORB registry item_cap against it so a
# future batch raise re-aligns the registry instead of silently re-slicing.

def td_batch():
    """Articles per slice card: TD_DOMAIN_BATCH env, default = MAX_ITEMS - 1
    (one step of headroom for the numbered GATE step in the body, so the
    whole card passes the gate as shape B instead of being re-sliced)."""
    default = MAX_ITEMS - 1
    n = int(os.environ.get('TD_DOMAIN_BATCH', str(default)))
    if n > MAX_ITEMS:
        print(f"TD_DOMAIN_BATCH={n} exceeds mint_gate.MAX_ITEMS={MAX_ITEMS} "
              f"— clamped (registry/gate is the single authority)")
        n = MAX_ITEMS
    # Registry must cover the effective batch; below-cap registry is the TD
    # 8>6 mismatch class — fail loud here instead of at every GATE|ITEMCAP.
    from mint_gate import _td_item_cap_floor
    _td_item_cap_floor(n)
    return n

REPO = Path.home() / 'echo-system'
STATE = REPO / 'knowledge/research/taiwandaily-domain-state.json'
DB = Path.home() / '.hermes/kanban.db'
MAXCARDS = int(os.environ.get('TD_DOMAIN_MAXCARDS', '10'))
FLOOR = int(os.environ.get('TD_DOMAIN_FLOOR', '202101'))

def load_state():
    if STATE.exists():
        s = json.load(open(STATE))
        # months_newest_first() yields ints; the state file stores strings.
        # An un-normalized `ym not in crawled` int/str compare is never true,
        # which silently disabled the entire absorb phase — zero
        # TAIWANDAILY-ABSORB cards were ever minted despite crawled=28.
        return {'crawled': [str(x) for x in s.get('crawled', [])],
                'carded': [str(x) for x in s.get('carded', [])]}
    return {'crawled': [], 'carded': []}

def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    json.dump(s, open(STATE, 'w'), indent=1)

def months_newest_first():
    """Last 12 calendar months from TODAY (Grok F8: was hardcoded 2026,10 —
    November would never have entered the loop)."""
    import datetime
    out = []
    y, m = datetime.date.today().year, datetime.date.today().month
    while y * 100 + m >= FLOOR:
        out.append(y * 100 + m)
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return out

def absorb_body(ym, batch_items, batch, slice_n=1):
    """Slice card: the worker judges THIS list only. Selection + identity
    pre-filter already ran outside the 30-turn budget (slice-prep). Closure is
    graded by ledger-coverage via swarm-churn-sweep.py, never by worker
    self-report (SSOT ~/knowledge/swarm-churn/SSOT.md)."""
    lines = []
    for i, it in enumerate(batch_items, 1):
        cands = ', '.join(it['candidates']) or '(none — create page only if Tier-M/1 floor met)'
        lines.append(f"{i}. `{it['url']}`\n   file: `{it['file']}`\n   title: {it['title']}\n"
                     f"   names: {', '.join(it['names']) or '-'}\n   candidate pages: {cands}\n"
                     f"   prep-tag: {it['tag']}")
    listing = '\n'.join(lines)
    return f"""# TAIWANDAILY-ABSORB-{ym} (slice of {batch}, slice #{slice_n})

Slice absorption of {len(batch_items)} PRE-SELECTED articles from
`knowledge/web-archives/tdm-{ym}.json`. You judge; you do not enumerate.

## THE SLICE — this is your complete work list
{listing}

- GATE — run this FIRST and believe its exit code, not the manifest:
   `python3 ~/echo-system/scripts/taiwandaily-month-fetch.py {ym} --verify`
   If it prints REFETCH (non-zero exit), close the card with
   `manifest-incomplete` and stop — never absorb a fragment.
   Do NOT read the manifest's `complete` flag as the manifest gate: verify()
   exists precisely because that flag has been true while 102 files were
   upstream error payloads. grade() recomputes from disk.

- Read the ledger first — already-decided urls are DONE, skip them:
  `cat ~/echo-system/knowledge/web-archives/tdm-{ym}-absorb-ledger.jsonl`

- For EACH numbered article below, in order:
   a. Read the article file (front-matter title + body).
   b. Judge person-relevance (台美人物 / named person with biographical or
      event content). Pure wire news, ads, listings, photo albums -> skipped.
   c. Identity gate: candidate pages above are HYPOTHESES (prep-tag tells you
      how confident). HIT = hanzi appears in a people-page title or
      unambiguous bio. Collisions -> HOLD (never merge). Uncertain between
      absorb and HOLD -> HOLD.
   d. Absorb: dated record line (date + fact + [美洲台灣日報](URL) + (reported)
      where hedged) appended to the From-the-record table of the HIT page.
      New persons meeting Tier-M/1 floors get layered pages (template:
      ~/.hermes/profiles/pinto/skills/echopedia-draft-article/templates/layered-person-page.md).
   e. IMMEDIATELY after the page write, record the decision (fsync'd, this is
      your only durable progress — if you die, the next run resumes from here):
      `python3 ~/echo-system/scripts/taiwandaily-absorb-ledger.py {ym} --url URL --decision absorbed|skipped|hold [--page content/people/x.md] [--note why]`

- When EVERY article above has a ledger line: update the source hub
  `content/sources/taiwandaily-net.md` entity index line for {ym}, then
  commit explicit paths only (touched pages + the ledger file), message
  `taiwandaily-domain: absorb {ym} slice (N pages touched)`.

- Close the card with a one-line result: `slice-complete N=<decided this run>`.
   The MONTH is not yours to close — coverage is graded by
   `taiwandaily-slice-prep.py ledger-coverage {ym}`; if uncovered remains, the
   BUILDER mints the next slice card (slices are never reopened). Budget nearly exhausted ->
   commit what is ledger'd and close anyway; never end without ledger lines
   for what you already wrote.

Contract: judgment work only. HOLD is cheap, wrong merges are not.
"""

def prep_batches(ym, batch):
    """Run the deterministic slicer (no LLM). Returns (batches, stats) or
    (None, error)."""
    import subprocess as sp
    r = sp.run([sys.executable, str(REPO / 'scripts/taiwandaily-slice-prep.py'),
                'prep', str(ym), '--batch', str(batch)],
               capture_output=True, text=True, timeout=600)
    try:
        d = json.loads(r.stdout)
    except Exception:
        return None, (r.stdout or r.stderr)[:200]
    if 'error' in d:
        return None, d['error']
    return d.get('batches') or [], d.get('stats')

def card_exists(title_prefix):
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    try:
        # '-v1' = remint-archived whole-month cards: they must NOT block the
        # slice-class mint (probe 2026-10-19: LIKE 'PREFIX%' matched the
        # renamed -v1 rows and the mint loop silently minted 0 cards).
        n = con.execute("select count(*) from tasks where title like ? "
                        "and title not like '%-v1'",
                        (title_prefix + '%',)).fetchone()[0]
    except sqlite3.OperationalError:
        n = 0
    con.close()
    return n > 0

def active_slice(ym):
    """(has_active, next_slice_n): active = non-archived, non-done slice card.
    A month whose LATEST slice closed with a manifest-incomplete GATE is also
    'active' (do-not-mint): the fetcher must re-verify the month first, else
    the builder mints s2 -> GATE -> s3 -> GATE churn (probe 2026-10-20:
    202512 GATE-closed while its s1 ledger held 8 lines).

    TD-FIX-20261117 (t_41245b8f) item 2: the gate re-slices an over-cap body
    and appends ' [i/n]' to the title, so a row can exist as
    '...-s22 [1/3]'. Strip that chunk suffix BEFORE the -sN match (shared
    mint_gate.strip_gate_chunk_suffix — one parse shape, not two regexes) —
    otherwise a bracketed title never matches -s\\d+, the month sticks at
    next_n=1, and it re-mints slice 1 forever."""
    sys.path.insert(0, str(Path.home() / '.hermes' / 'scripts'))
    from mint_gate import strip_gate_chunk_suffix  # noqa: E402  TD-FIX item 2
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    # TD-FIX-20261117b (t_41245b8f): the docstring promised 'non-archived,
    # non-done' but the query never excluded status='archived' — archived
    # chunk rows both froze the month (archived != done -> active) and pushed
    # next_n past unworked slices (frozen 202407/202411/202501/202510 class).
    rows = con.execute("select id, title, status from tasks where title like ? "
                       "and title not like '%-v1' and status != 'archived'",
                       (f'TAIWANDAILY-ABSORB-{ym}%',)).fetchall()
    gate = False
    if rows:
        ids = [r[0] for r in rows]
        last = con.execute(
            "select task_id, coalesce(payload,'') from task_events where kind='completed' "
            f"and task_id in ({','.join('?'*len(ids))}) "
            "group by task_id having max(id) order by max(id) desc limit 1", ids).fetchone()
        gate = bool(last) and 'manifest-incomplete' in last[1].lower()
    con.close()
    ns = [0]
    active = gate
    for tid, title, status in rows:
        m = re.search(r'-s(\d+)$', strip_gate_chunk_suffix(title))
        ns.append(int(m.group(1)) if m else 1)
        if status != 'done':
            active = True
    return active, max(ns) + 1

def make_card(title, body, max_runtime='5400'):
    """Create-time caps are LOOSE on purpose (SSOT S1): the clock must never
    be the killer — the iteration budget is the real envelope, and it is
    respected by design (slice fits budget_max - reserve). Bumping caps after
    create is NOT a thing (kanban_parser: --max-runtime is create-only).
    --goal-max-turns on a non-goal card = per-card iteration budget
    (pinto-local session_kanban maps it to agent.max_turns; profile default
    30). SWARM-GUARD-3 (t_418565a8): the budget is NO LONGER a literal here —
    both goal_max_turns and max_retries resolve from the ONE registry
    (mint_guard.budget_args -> mint-class-registry.json TAIWANDAILY-ABSORB),
    fail closed. The old 45/3 hardcode was one of three drifting sources."""
    # SWARM-GUARD-2 (t_4c357f44): route the mint through mint_gate.mint_via —
    # backlog gate (FAIL CLOSED) + pre_mint_gate body gate + budget_class
    # resolution in ONE call. body rides with create ('--body'), not a
    # create-then-sqlite-update: a death between the two no longer leaves a
    # 'pending'-body card dispatched to a worker (no partial insert).
    # Idempotency key covers the whole slice title (title carries the month +
    # slice number = the chunk identity).
    # TD-FIX-20261117 (t_41245b8f): the window starts BEFORE the mint call;
    # nothing below may take >2 s between start_ts and the minted_sink
    # read-back, so made can never credit a row created before this run.
    start_ts = int(time.time())
    made_ids = []  # minted_sink: only exact-title rows read back IN-WINDOW
    # TD-FIX-20261117b (t_41245b8f): outcome_sink tells per chunk whether it
    # was 'created' (in-window row), 'deduped' (exact-title row already
    # covered) or 'failed' (true silent drop). mint-via-no-row must print for
    # FAILED chunks only — a dedupe is coverage, not a drop.
    chunk_outcomes = []
    made = mint_via(title, body, assignee='pinto',
                    backlog_source='taiwandaily-domain-build',
                    budget_class='TAIWANDAILY-ABSORB',
                    minted_sink=made_ids,
                    outcome_sink=chunk_outcomes)
    if not made:
        print('mint-via-blocked', title)
        return None
    # SWARM-GUARD-2 (codeeater fix 2026-11-15): mint_via ALREADY minted every
    # returned chunk (own idempotency keys, item cap, registry budget). The
    # old code checked only made[0] and refused non-'pass' — which reported
    # 'card not minted' AFTER the gate had minted slice chunks, breaking the
    # month state machine.
    # TD-FIX-20261117 (t_41245b8f) items 1+4: the old per-chunk `select id
    # from tasks where title=?` had NO window and NO status guard, so a
    # pre-window done row was re-credited (the 11-17 made=1 lie = done@02:01
    # t_6c458746, created before the run). mint_via now prints MINT|OK /
    # MINT|FAIL per chunk from its own in-window read-back; the ids here are
    # only those that passed it (minted_sink). A no-row chunk logs
    # mint-via-no-row and is NOT counted.
    for action, t, b in made:
        if action == 'reject':
            print('mint-via-routed', action, t, '— reslice at the source; card not minted')
    ids = made_ids
    if not ids:
        # TD-FIX-20261117b (t_41245b8f): only TRUE drops print the
        # mint-via-no-row close-gate line. If every chunk was already covered
        # by an exact-title row (MINT|DEDUP in mint_gate), the slice is
        # covered, not dropped — log mint-via-dedup and skip without carding.
        dropped = [t for (t, kind, _rid) in chunk_outcomes if kind == 'failed']
        if not dropped:
            print('mint-via-dedup', title, flush=True)
            return None
        for _t in dropped:
            print('mint-via-no-row', _t)
        return None
    return ids if len(ids) > 1 else ids[0]

def month_complete(ym: str) -> bool:
    """Trust the fetcher's grade, not file existence. A worker that died at
    30 turns left partial manifests behind and file existence cannot see that."""
    ym = str(ym)  # months_newest_first() yields ints; grade() slices ym[:4]
    dest = REPO / f'knowledge/web-archives/tdm-{ym}.json'
    if not dest.exists():
        return False
    try:
        d = json.loads(dest.read_text())
    except Exception:
        return False
    results = d.get('results') or []
    if not results:
        return False
    try:
        import importlib.util
        sp = importlib.util.spec_from_file_location(
            'tdm_fetch', str(REPO / 'scripts' / 'taiwandaily-month-fetch.py'))
        mod = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(mod)
        grade = mod.grade
    except Exception:
        return False
    done, _cov = grade(ym, d.get('listed') or len(results), results)
    return done


def main():
    remint = '--remint' in sys.argv
    # TD-FIX-20261117 (t_41245b8f) item 3: was a hardcoded '8' exceeding
    # mint_gate.MAX_ITEMS — the gate then re-chunked every body into [i/3]
    # titles (the silent-drop shape). td_batch() derives from the gate
    # authority and self-checks the registry item_cap.
    batch = td_batch()
    # SWARM-GUARD-1 (t_0cb42501): the backlog gate is held inside make_card
    # (mint_guard.gated_once) per create, fail closed. The shared mint lock
    # serializes enumerate->decide->mint against sibling minters; the
    # month-level active_slice()/card_exists() dedupe is unchanged, so a
    # skip re-checks truth on the next pass and never loses work.
    sys.path.insert(0, str(Path.home() / '.hermes' / 'scripts'))
    from mint_guard import gated_once, budget_args
    if remint:
        # v1 whole-month cards cannot close by construction. Archive them out
        # of card_exists' path (title gains -v1; archived cards never dispatch)
        # so the slice-class card can be minted. Ledger, if any, is kept —
        # it is the resumable truth.
        con = sqlite3.connect(str(DB), timeout=30)
        # v1 signature = whole-month card (max_runtime 2400, no slice header).
        # NEVER archive a v2 slice card (Grok F5: a second --remint used to
        # archive the freshly minted slice class).
        rows = con.execute("select id, title from tasks where title like "
                           "'TAIWANDAILY-ABSORB-%' and title not like '%-v1' "
                           "and max_runtime_seconds=2400 "
                           "and body not like '%(slice of%'").fetchall()
        for tid, title in rows:
            # rename+commit FIRST, then archive: a death between the two
            # leaves a ready orphan with a -v1 title (never dispatched,
            # never blocks card_exists) — the safe side of the window
            # (Grok F5: archive-first left archived cards still blocking
            # the mint when the title commit was lost).
            con.execute("update tasks set title=? where id=?", (title + '-v1', tid))
            con.commit()
            r = subprocess.run(['hermes', 'kanban', 'archive', tid],
                               capture_output=True, text=True, timeout=300,
                               stdin=subprocess.DEVNULL)
            if r.returncode != 0:
                print('archive-failed (renamed orphan is safe)', tid, (r.stderr or r.stdout)[:100])
            print('remint-archived', tid, title, flush=True)
        con.close()
    state = load_state()
    carded = set(state['carded'])
    crawled = set(state['crawled'])
    made = 0
    skipped = 0
    # absorb cards for crawled months without one
    for ym in months_newest_first():
        if made >= MAXCARDS:
            break
        ym = str(ym)
        if ym not in crawled:
            continue
        # Dedupe on the DB, never on state['carded']. Active slice -> skip;
        # all slices done -> mint the next slice (continuation, Grok F1).
        active, next_n = active_slice(ym)
        if active:
            continue
        a = f'TAIWANDAILY-ABSORB-{ym}-s{next_n}'
        batches, stats = prep_batches(ym, batch)
        if batches is None:
            print('prep-failed', ym, stats)
            skipped += 1
            continue
        n_undecided = stats.get('undecided') if isinstance(stats, dict) else '?'
        if not batches:
            # nothing undecided. NEVER mark carded on a zero-settled manifest —
            # 'no data' is not 'covered' (status-vocabulary drift hid 27 months
            # this way, probe 2026-10-20). Only a real, covered month closes.
            n_settled = stats.get('settled', -1) if isinstance(stats, dict) else -1
            if n_settled == 0:
                print('NO_DATA', ym, stats)
                continue
            print('covered-or-empty', ym, stats)
            carded.add(ym)
            continue
        # TD-FIX-20261117 (t_41245b8f) item 5 (close gate): audit lines —
        # 'minted slice:' carries the exact baker title; a probe proves an
        # exact-title row created in-window for EVERY such line and
        # made == the in-window shape-B count. Print, don't trust, the ids.
        t = make_card(a, absorb_body(ym, batches[0], batch, next_n))
        if t:
            carded.add(ym)
            made += 1
            print('minted slice:', a, 'ids=', t, flush=True)
            print('absorb', ym, t, f'undecided={n_undecided}')
    # crawl state sweep. NOT budget-gated: this loop mints no cards, and an
    # earlier `made >= MAXCARDS: break` here meant that whenever the absorb
    # backlog filled the budget the sweep never ran at all — leaving complete
    # months (202411, 202601) unmarked in `crawled` forever.
    for ym in months_newest_first():
        ym = str(ym)  # state stores strings; months_newest_first() yields ints
        c = f'TAIWANDAILY-CRAWL-{ym}'
        # A missing or partial manifest is taiwandaily-month-fetch.py, not an
        # agent card. Agent crawl cards die at 30 turns and leave fragments.
        if month_complete(ym):
            # Grade first, unconditionally. A legacy TAIWANDAILY-CRAWL card
            # left `done` by a QA-close must not mask a month that is now
            # complete — skipping on card existence before grading stranded
            # 202411/202601: complete manifests, never marked crawled, so the
            # absorb loop above never minted a card for them.
            crawled.add(ym)
        if card_exists(c):
            continue
    state['carded'] = sorted(carded)
    state['crawled'] = sorted(crawled)
    save_state(state)
    if made:
        print(f'made={made} carded={len(carded)} crawled={len(crawled)} crawl_skipped={skipped}')

if __name__ == '__main__':
    main()
