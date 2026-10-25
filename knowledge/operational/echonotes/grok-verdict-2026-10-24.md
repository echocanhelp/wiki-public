VERDICT: ship-with-changes. The reuse boundary is right (MeetNotes engine, owner GO, no second wiki, static site stays read-only, LINE webhook stays ack-only). Do not build it in this phase order. N1–N4 as written will publish person-attributed speech before the identity rule can actually be enforced, and they treat LINE video plus a global vault search as if they were a safe public intake. Freeze an N0 worker and change the gates below before GO.

1. HIGH-VALUE EFFICIENCIES & IMPROVEMENTS

1. Insert N0 before N1: a single background worker, not a fatter mint script. jobs needs an idempotency key (LINE messageId or media sha256), attempt count, tenant, stage timestamps, and a single-flight GPU lock. Today's webapp.py runs run_pipeline inside the HTTP request; LINE retries and a phone upload will double-burn Breeze/pyannote/CAM++ on the same 4 slots :8888 uses for chat. Cap concurrency at 1. Refuse a second job with the same key. Dead-letter after 2 failures with a terminal state. Original media and 16 kHz wavs need a retention rule now (derived wav kept, source video deleted after successful decode, per-tenant disk quota). A 1-hour 16 kHz mono wav is ~115 MB; this plan has no ceiling.

2. Resequence identity ahead of any person wikilink. N1 may generalize mint and add provenance, but it must emit voiceprint labels only (Leonard, Speaker 3), never [[people/...]]. Person links wait until N2 status=confirmed. mint_echopedia.py currently open(path,"w") overwrites content/topics/<slug>.md. That violates HOLD-on-conflict. Mint must refuse an existing slug unless the ledger records an explicit amend. Publish from a LINE postback must stage into the vault and let ci-heal be the only pusher. A webhook git push races the nightly pusher.

3. The voiceprint rule in the plan does not match the failure mode in voiceprints.py. match() is one cosine on the mean embedding of a diarization cluster, threshold 0.45 and margin 0.10, tuned so Phoenix vs BoardMember would not collapse. Diarization merge still attributes the other person's words to the winner, and a confirmed flag does not detect that. Publishable attribution needs a stricter bar than enrollment match: score ≥0.55, margin ≥0.15, minimum voiced seconds, and low intra-cluster variance (or a per-utterance reject). status=confirmed requires a second meeting or an explicit owner confirm, not one tap on the unauthenticated /meeting/{id}/learn form. Role profiles (BoardMember, AuditBoss) must not map to a person slug. Match stays inside the tenant. Anything else stays Speaker N in both the LAN report and Tier1.

4. Do not trust the LLM to obey the identity rule. N3's one :8888 pass must not be the source of quotes, timeline rows, or "X said". Those already have deterministic nightlies. Feed them utterance rows. The model does summary, decisions, conflicts, hints only. Every people_deepen or conflict claim is dropped unless code finds the cited span verbatim in the transcript. LLM action-item owners are not speakers and must not be published as such. Cap the transcript, not just the dossier. extract.py today sends the full transcript, max_tokens 1500, timeout 120s. A long meeting plus 4 dossiers repeats the EE pack blow-up on the transcript side. Deterministic pre-extract (name hits, decision cues, timestamp windows) then one capped call.

5. LINE is the control plane, not the recording pipe. User-sent LINE video/audio will not carry a real community meeting (client compression, content-API size, webhook must return 200 before download). N4 exit "send video in LINE → published page" will pass on a 30-second clip and fail in production. Intake is an adapter branch before the agent and before mention-gating: verify signature, dedupe messageId, enqueue, one free Reply with job id. Do not spend a Grok turn. Do not push queued → transcribed → drafted. Reply token TTL is ~60s; each later push burns the metered quota (free tier is on the order of a few hundred pushes a month). Later status is a postback tap (fresh free Reply) or one terminal push. Draft and publish-confirm go to the uploader DM plus the owner, never the group. Postback data is a job id only. Publish postback checks owner uid, not "whoever tapped".

6. Kill the community tier on the public site. GitHub Pages has no auth. Real states are private vault/LAN, or public content/ after owner GO. A "community" Quartz page is world-readable. N6 CTAs may be line.me/R/oaMessage/@970tzxdg/?… with a slug in the prefilled text. No token, no LAN host, no :8130 URL in committed markdown. Related-meeting injection reads only consent_tier=public and published_at set. Prefill without an allow-list (open question 1) invites strangers into tenant hsu-family. N6 ships after the allow-list, not before N7.

7. PWA auth is not a query-string token on today's app. :8130 has no auth. /ingest, /learn, and /speakers/{id}/delete are voiceprint poisoning and profile deletion if the phone path is reachable off-LAN. Every route, including /meeting/{id}/audio, requires a scoped, expiring, revocable credential. Token-in-URL leaks via LINE screenshots, history, and Referer. iOS MediaRecorder will not survive a real meeting (tab suspend, codec quirks). N5 v1 is file upload plus the same job API, record-in-browser later. Native stays deferred. Do not put LAN replay links into published pages; public readers cannot open them, and the path leaks machine layout. Tier1 cites meeting_id plus mm:ss only.

8. Tenant-scope retrieval before any non-household job. echopedia-first-answer / bm25 are vault-global. A TAHS transcript will hit household person pages, the dossier pack will pull private Tier2 into :8888, and the summary can carry it into content/. Public-tenant linking searches only public pages plus that tenant's holds. Health redaction is an English substring list (heart, surgery, hospital). zh/taigi meetings will not match it, and the LLM summary can paraphrase past the line filter. Extend the list (心臟, 手術, 醫院, 藥物, and the household's actual terms) and run it on summary, decisions, and deepens, not only utterance lines. Substring "hospital"/"doctor" will also over-redact. Prefer token or CJK-aware match.

2. RISKS THE PLAN UNDERSTATES

1. False attribution will come from cluster-mean matching and diarization merge, then from the model writing "X said" off a name mention while the voice is still Speaker N. "Confirmed voiceprints only" does not stop either path. A wrong quote under an elder's name is the reputational failure, and N2's exit (link the existing 6 names) encourages mapping role profiles to pages.

2. Private material reaches the public site through global search, dossier context, English-only redaction, and any community-tier page. There is no second check that the minted markdown contains no U-id, no filesystem wav path, and no Tier2-only fact.

3. LINE-primary intake duplicates work and goes silent. Webhook retries without messageId dedupe enqueue two GPU jobs. Progress pushes die on 429. Mention-gating drops a group 筆記 if this is implemented as an agent skill instead of an adapter branch. The user sees a job id and then nothing.

4. Phone and LINE audio will not behave like the 16 Teams/PipeWire meetings. The silence gate (mean_abs ≥150 and 2% of samples above 500) was tuned on those wavs. Compressed m4a can pass the gate and still be unusable, or fail it and be dropped with no owner-visible reason. No CER/speaker-error/false-accept number exists, so N4 can "succeed" on garbage.

3. METRICS

N0 worker
- Duplicate LINE messageId or identical sha256 creates exactly one jobs row.
- Two uploads while a job is running: second stays queued; GPU process count for Breeze/pyannote stays 1; :8888 chat still answers.
- Failed ffmpeg/STT/:8888 leaves status=dead after 2 attempts, wav preserved, no content/ write.
- Disk: source video removed after decode; wav bytes per tenant visible and capped.

N1 mint (no person links)
- Re-mint of the Kanola meeting is idempotent: second run does not change the file hash unless an amend is ledgered.
- Output contains zero [[people/]] links and zero hardcoded kanola-deck / hsu-family tags.
- Every published utterance still has mm:ss. Health fixture with 心臟/手術/hospital is redacted in transcript and in the LLM summary.
- Existing slug on disk causes a non-zero exit and no write.

N2 identity
- On a held-out slice of the 16 meetings, confirmed-match false accepts = 0 at the publish threshold (report FAR/FRR, not just "6 voices linked").
- A cluster with high internal variance or margin <0.15 stays Speaker N even if the best name is confirmed.
- BoardMember and AuditBoss have status=rejected for person_slug. A single /learn does not flip status to confirmed.
- Cross-tenant: a hsu-family profile is not a candidate when tenant=tahs.

N3 grounded extract
- 100% of people_deepen and page_conflicts in the pilot meeting have a verbatim transcript span; claims without a span are absent, not drafted.
- The :8888 request body stays under the cap (transcript window + ≤4 public dossiers, <14k chars of dossier, one call). Measure tokens, do not assume.
- Quotes and timeline rows written for the nightlies equal deterministic utterance extracts, not model paraphrases.
- A known contradiction with an existing page produces a HOLD record and does not edit the page.

N4 LINE
- Webhook returns 200 before media download. Heavy work is not in the handler. No Grok call on the intake path.
- One meeting costs ≤1 free Reply on ingest plus ≤1 push or 1 postback-delivered terminal card. No three progress pushes.
- Group upload: group receives no transcript and no draft. Owner uid is required for the publish postback; a non-owner tap does not write content/.
- A >N-minute or oversize LINE media is rejected with a PWA/file instruction, not silently truncated. N is measured, not hoped (start by rejecting anything the content API cannot fetch intact).

N5 PWA
- Unauthenticated GET /meeting/{id}/audio, POST /learn, and POST /speakers/{id}/delete return 401, including from the LAN if the token is missing.
- Same API sequence as N4 (POST /jobs, poll, owner publish) completes from a phone browser on a file upload, without calling run_pipeline inside the request.
- Expired or other-tenant token cannot read meeting list or audio. Revocation works on the next request.
- No committed Quartz page contains a :8130 host, a token, or a wav filesystem path.

N6–N7 (only after the above)
- Public CTA URL contains the slug and the OA id, and no credential. Hitting it from a non-allow-listed account creates no job.
- Injected "related meetings" block lists only rows with consent_tier=public and a publish ledger time. Private meetings on the same person page: count 0 in the built HTML.
- The non-household tenant publishes one meeting whose person links are all confirmed, whose redaction fixture passes, and whose git push is performed by ci-heal only.
