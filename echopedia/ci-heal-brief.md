## CI heal — 2026-07-15
- Started: 2026-07-15T21:47:33-07:00
- dry_run=0 l2_drift=True l2_drain=True l3_push=True

- OPS_WARN: standards v5 not yet seen by janitor (seen=4) — next 4am run will resweep
- OPS_WARN: legacy script still present (prefer echopedia-publish.sh): echopedia_publish_loop.py
- OPS_WARN: legacy script still present (prefer echopedia-publish.sh): echopedia_publish_staging.sh
- OPS_SUMMARY: fail=0 warn=3
- OPS_STATUS: WARN
- DRIFT_SUMMARY: stale=0 missing_html=0
- DRIFT_STATUS: OK
- broken_wikilink_hits≈14 (max_green=0)
- SMOKE_SUMMARY: ok=3 fail=0
- SMOKE_STATUS: OK
- **green=1**
- committed heal
- PUBLISH_STATUS: OK
- **L3 pushed** `96a5f2f`

### Actions
- CI: ops-check WARN
- CI: drift OK
- CI: smoke OK
- CI: committed heal
- CI: L3 pushed 96a5f2f
