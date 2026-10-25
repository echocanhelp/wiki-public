Round 3 is additive only. Publish-first, unlabeled-speaker shipping, related-page auto-update, the publisher identity gate, partial banners, and the EN|中 plan stay as decided. Nothing below adds a service, a native app, or a second :8888 call. Filed at /home/leedt/echo-system/knowledge/operational/echonotes/grok-verdict-r3-2026-10-24.md.

Checked against live code, not the spec sheet: stt.py accepts initial_prompt and never uses it; auto mode always runs Breeze-26 and invents 30-second Taigi spans; voiceprints.match already refuses thin margins (the Phoenix/BoardMember note); mint_echopedia.py still prints LLM action-item owners, the full transcript, and a LAN replay sentence.

Build these, in order

1. Meeting-keyed upsert. S. Reuses the meeting_id citation you already require. Re-publish replaces that meeting's machine block on the meeting page and on related pages. Append-only still means do not touch human prose. Without this, publish-first plus the verification re-publish queue doubles quotes and presence lines. Measure: machine bullets per meeting_id stay 1 after two publishes.

2. Retract on the ready push. S. Reuses the one terminal push, the linked LINE uid, and retract (unstage / tombstone / centroid rollback). That push already owed to the credited publisher includes the public URL and one 收回 postback, accepted only from that uid or the owner uid. No second push. Measure: minutes from publish to tombstone, not "next 08:30."

3. Thin-margin A/B clip. S. Reuses voiceprints.match, the kept 16k wav, and that same push. When the matcher refuses on margin, the push carries two ~6s cuts and postbacks A / B / neither. Names stay Speaker N until the tap. A tap is a claimed label for this meeting only and does not move the centroid. Measure: household collisions closed in one tap; wrong names published on thin-margin pairs stay 0.

4. Cross-meeting voice family. M. Reuses CAM++ embeddings already in sqlite and the re-publish queue. An unconfirmed cluster that matches a prior meeting's Speaker N gets a family id. One confirm re-publishes every meeting in the family. Family membership is a constraint row, not a centroid update and not a person slug. Measure: confirms per distinct voice, not per meeting.

5. Collapse banner. S. Reuses diarize.py, align.py's unknown bucket, the partial-banner path, and conflict HOLD. If attendee priors are 4 or more and diarization returns 1 speaker, or a large share of time is unknown, the meeting still publishes, with that banner, and person-page presence bullets HOLD. Measure: presence bullets on collapsed jobs = 0.

6. Citation fitness. S. Reuses the lang flag and avg_logprob already on utterance rows, plus HOLD. Person-page quote writes HOLD when a Taigi block's text does not fit the zh-timed run, or when logprob is under a fixed floor. The meeting page still shows the text, labeled with the real window. Taigi is a ~30s block, not word time. No second STT pass. Measure: person-page quotes whose cited span does not contain the quote = 0.

7. Fail-closed marker audit. S. Reuses the site-design audit. Every line in the meeting-records section must carry the machine-added marker and meeting_id+mm:ss, or the page is NEED YOU and is not treated as clean. Labeling is the safety policy; this is what makes a missing label visible. Measure: unlabeled machine lines in built HTML = 0, or a brief row.

8. Brief ordered by reads. S. Reuses GoatCounter gc-path-counts.json (already the MT backfill priority) and the morning brief cap of 5. Unread Speaker N meetings wait. Measure: share of brief slots whose path had at least one hit.

9. Action items are claims, not owners. S. Reuses the action items from the one :8888 call, the ready-push postback, the identity link, and Hermes kanban. Stop publishing the LLM owner field (mint writes it today). A 我來 tap opens a kanban card for the tapper's linked person. Measure: published action rows with a person-name owner = 0.

10. 我的筆記. S. Reuses the adapter keyword branch, the jobs table, and the publish ledger. One free Reply, no push: that uid's last 3 jobs, with status and public URL or private-draft. Measure: repeat uploads per linked publisher within 14 days.

Do not build yet

1. Name hotwords through initial_prompt. The hook is sitting unused in stt.py, so it looks free. Breeze will speak prompted names into quiet or garbled spans, and publish-first will cite them. Fold known-attendee aliases only at link time. Leave the transcript verbatim. Do not prompt the decoder with the vault.

2. Live captions, or a group transcript while the bot is in the call. That holds the one GPU lock for the whole meeting, starves the shared :8888 slots, and a group push breaks the Reply/push budget. Upload-later is the product.

3. A second :8888 cleanup pass, or auto-minted person pages for repeated unknown names. Hints already feed janitor and NEED YOU. A cleanup pass or a new biography is how a mis-hear becomes a permanent page. Same sink: a new diarization model, a vector DB, native recording, reciprocal bridge writes.

Cheapest enhancement with the biggest trust impact

Retract on the ready push (item 2). One postback on a message you already send. Publish-first puts a wrong page on GitHub Pages at T+0, and the credited publisher is the only person watching then. The brief is hours later. That button is the difference between a bad page that lives for minutes and one that lives overnight. No new message, no model call, no service.
