# Audiobook Voice Capture Workflow (Echopedia)

Use this when a user wants chapter/page audio narration hosted on the wiki.

## Why this exists
Phone-call capture is convenient but commonly too compressed/noisy for audiobook-grade cloning. This workflow preserves consent integrity and audio quality while keeping wiki deployment predictable.

## Minimal sequence
1. Build a consent/recording kit page in wiki content.
2. Link kit from target chapter/book page.
3. Collect explicit written + spoken consent.
4. Collect clean sample audio (preferred WAV, mono, 16k/24k+, quiet room).
5. Generate pilot (60–90s), QA, then full chapter.
6. Publish audio and add metadata to page.
7. Run broken-link scan and deploy.

## Consent bundle checklist
- Written consent scope (work/chapter, usage, duration, revocation)
- Spoken consent line recorded verbatim
- Attribution preference (display name)
- Privacy/publication limits

## Recording checklist
- Quiet room, no speakerphone
- Consistent mic distance
- 10–30 min varied speaking styles
- Include pronunciation-critical proper nouns (Taiwanese names/places)

## Twilio usage guidance
Recommended use:
- outreach
- scheduling
- consent confirmation

Not recommended as primary voice-model corpus:
- phone-call narrowband recordings
- noisy mobile conditions

## Publication metadata checklist (on chapter page)
- Narrator/voice attribution
- Consent status + date
- Audio version + date
- Source confidence note
- Link to consent/recording kit page

## QA gate before full release
- Name pronunciation accuracy
- Natural pacing
- No clipping/noise artifacts
- Stakeholder approval of pilot clip
