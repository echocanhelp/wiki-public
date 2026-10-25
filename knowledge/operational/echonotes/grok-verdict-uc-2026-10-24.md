Reconciliation: wrong as specified, right as a split. Do not go back to full manual confirm. Filed at /home/leedt/echo-system/knowledge/operational/echonotes/grok-verdict-uc-2026-10-24.md.

VERDICT

UC-1 confirm-with-changes — upload-later stands; LINE drops, partial files, and pre-picks-as-facts are unspecified failure paths.
UC-2 confirm-with-changes — claimed/confirmed ladder stands; independent argmax plus centroid-on-every-tap does not.
UC-3 rework — keep automatic publish, replace this green gate; it false-greens living pages and will not fire on the phone path you will actually use.
UC-4 confirm-with-changes — review UI stands; it is not the daily path, and it has no retract.
UC-5 confirm-with-changes — LINE to kanban to brief stands; LINE-only first, no auto-edit.
UC-6 confirm-with-changes — deterministic sections stand; full public transcript and reciprocal bridge writes do not.

TOP IMPROVEMENTS

1. UC-3 auto_publish / green gate. Split the two wants. The meeting page may auto-stage for the next ci-heal (00:25, live cron 25 0 * * *) only for an owner-uid upload with explicit consent=public. Person-page writes do not ride that gate. A LINE drop or a missing consent stays private, so household-ON cannot mean any family file goes live. Green means redaction trigger count = 0 on the raw text (post-redaction "clean" is a false-green), decisions omitted unless they have a verbatim span, no person name outside the purity-confirmed set, and Speaker N allowed. Requiring every speaker to be named makes auto_publish a dead switch: 0.55 is CAM++'s clean-speech same-speaker floor in voiceprints.py, not a measured phone false-accept rate, and guests never clear it. Drop the >=1 wikilink rule. Pre-picks are priors, not links. Taigi or code-switch with no dictionary coverage is not green. A green ledger row still unpublished after 00:25 is NEED YOU — ci-heal failed on 2026-10-15.

2. UC-2 assignment. Match clusters to profiles 1:1. A second cluster that also clears 0.55/0.15 against the same profile stays Speaker N. Two clusters become one slug only through an explicit merge, and only when their mutual cosine says same voice. No auto-merge on phone audio until that number is measured on the existing 16 meetings. A claimed tap labels this meeting only and must not update the centroid. Persisting every assignment into voice_identities is how one bad tap poisons the household, which is exactly the population where voices collide. A second-meeting confirm must be a different audio fingerprint, not a re-encode. Intro cues stay suggestions. Their absence is the normal case, not a failed job.

3. UC-1 consent subject. The auto_publish subject is the owner uid, not tenant hsu-family. Another household uploader, an allow-listed contributor, an uploader who is not an attendee, or pre-picks outside the tenant all force a private draft and one owner push. Tenant comes from the token, not the form. The API treats missing consent as private even if your own card preselects public, so the happy path needs no extra tap. Store the attestation. It is a record, not proof, and it does not let a forwarded Zoom clear the gate.

4. UC-1 preflight. No job, no GPU lock, and no :8888 call until the complete file's sha256 exists. A 90% chunk expiry is a non-event. LINE oversize is a reject with a PWA instruction, not a resumable upload. A recorder that died mid-meeting is status=partial: no vault write, no centroid update. Preflight is deterministic and runs first: decode, container duration vs decoded duration, abrupt cut, speech vs silence. Failed quality skips the LLM call. Phone compression is not the Teams audio the silence gate was tuned on, and a garbage meeting must not occupy the one shared slot.

5. UC-3 / UC-6 related-page payload and transcript. Append-only is the right shape and the wrong default payload. Auto-write one "present at" bullet for a purity-confirmed speaker on a public meeting. Never a quote, never a fact, and never anything from a private meeting onto a Tier1 page. The public meeting page is a grounded summary, spanned decisions, talk time, and cited excerpts. The full transcript and the LAN-archive sentence that mint_echopedia.py writes today stay Tier2. A semantic contradiction HOLDs the bullet. Cap the managed section. Hold-stubs stay in sqlite, because tier1-sweep will commit anything left in content/people.

6. UC-6 bridge links. Do not reciprocal-write both pages at publish. Co-mention is not presence, and a mis-hear of "invite X" must not land on X. Store the pairs, list them on the meeting page labeled mention vs presence, and let the janitor suggest rather than append. The cap that matters is the corpus cap — max_pairs_per_target=3 existed because popular targets explode across meetings — plus a page-level cap and a hub denylist. Per-meeting <=3 still floods a hub page in a month.

7. UC-4 retract and triage. v1 needs unstage-before-push, tombstone-after-push, and centroid rollback, or the first false green is permanent on GitHub Pages, including git history. The daily surface is the 08:30 brief: one strip, typed items, cap 5, owner-uid postback, free Reply, no summary body in the push. The dashboard is only for what one tap cannot resolve.

8. Pipeline batching and the ground-truth loop (UC-2 / N0). The GPU job writes sqlite only. A no_agent pass before 00:25 does green-eval, staging, presence bullets, and bridge rows. ci-heal remains the only pusher. Corrections (split, merge, reject) are stored as constraints, not averaged into the centroid, and if those two profiles are both expected next time, neither is auto-named. learn_ground_truth.py does not do this. Overflow on the single-flight lock waits — owner, then household, then external — with a postback, not a push. There is no second :8888 call to update related pages.

CHECKLIST

1. Recommendation: owner-uid + explicit public + the non-vacuous gate. Not tenant-wide ON, not full manual. Why: tenant-wide ON publishes other people's uploads, and the spec's gate either false-greens or never fires on phone audio.
2. Recommendation: append-only yes; the automatic payload is a presence bullet only. Why: quotes and facts on a living page are the reputational failure, and a write-conflict check does not catch a contradiction.
3. Recommendation: yes, plus claimed does not update the centroid, and assignment is 1:1. Why: one tap plus independent argmax is how two people become one slug and the error becomes permanent.
4. Recommendation: LINE-only first; rate-limit reports; never auto-edit; PWA waits for auth. Why: readers are not on the contributor allow-list, and a LINE complaint is not a P8 source.
5. Recommendation: no publish-time reciprocal writes; corpus and page caps, not per-meeting <=3 alone. Why: the janitor explosion was across meetings, and co-mention is not presence.
6. Recommendation: confirm upload-later; require complete-file preflight. Why: the primary path fails at partial files and garbage audio, not at the missing in-app recorder.

MISSING UCs

1. Retract / bad-publish recovery. Unstage, tombstone, centroid rollback, and a visible miss when ci-heal does not push a green row. GitHub Pages does not forget.
2. Forwarded or third-party recording. The uploader is not the only data subject. A Zoom of a meeting they were not in, non-consenting attendees, or health talk the dictionary only partly catches, needs a forced-private path no green gate can override.
3. Reprocess, and the oral-history misroute. sha256 idempotency blocks "I fixed the speakers, run it again," and a trimmed re-encode looks like a new meeting that can false-confirm a voice and double-append bullets. A long 2-person recording is an EE oral history: route it to the EE OA, do not mint a meeting page or touch person pages.
