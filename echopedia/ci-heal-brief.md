## CI heal — 2026-07-18
- Started: 2026-07-18T23:56:46-07:00
- dry_run=1 l2_drift=True l2_drain=True l3_push=True

- OPS_WARN: standards v6 not yet seen by janitor (seen=5) — next 4am run will resweep
- OPS_WARN: legacy script still present (prefer echopedia-publish.sh): echopedia_publish_loop.py
- OPS_WARN: legacy script still present (prefer echopedia-publish.sh): echopedia_publish_staging.sh
- OPS_SUMMARY: fail=0 warn=3
- OPS_STATUS: WARN
- would queue-drain
- DRIFT_SUMMARY: stale=0 missing_html=0
- DRIFT_STATUS: OK
- would: site-design-heal
- broken_wikilink_hits≈18 (max_green=0)
- SMOKE_SUMMARY: ok=4 fail=0
- SMOKE_STATUS: OK
- **green=1**
- would push (L3 green)

### Actions
- CI: ops-check WARN
- CI: would drain queue (dry-run)
- CI: drift OK
- CI: would site-design-heal (dry-run)
- CI: smoke OK
- CI: would commit heal (dry-run)
- CI: would push gh-pages (dry-run green)
