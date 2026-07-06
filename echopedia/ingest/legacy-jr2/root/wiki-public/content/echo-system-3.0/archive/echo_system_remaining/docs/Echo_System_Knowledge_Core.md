# Echo System Knowledge Core

Version: 1.4.1
Status: Draft – Pending Review
Last Updated: 2026-05-17
Source: Merged from Echo_System_Knowledge_Graph_Schema.md + relevant Archivist, Historian, and Profiler prompt sections
Owner: Archivist + Historian
Canonical Role: Single authoritative document for knowledge architecture, graph schema, verification logic, entity linking, and knowledge-specific stewardship rules in Echo System 3.0


Knowledge-governance note:
- Knowledge publication or provenance claims still require Knowledge Core verification standards and source-grounded evidence.
- Agent self-report remains `REPORTED` until corroborated.
- For control-plane corroboration, include runtime log evidence from gateway/runtime/journal/process signals, not only MCP endpoint probes.

## 1. Purpose

This document is the canonical source for how Echo System 3.0 stores, links, verifies, enriches, protects, and publishes knowledge.

Its purpose is to separate knowledge truth from runtime operations truth while preserving one coherent standard for:
- knowledge graph structure
- entity and relationship modeling
- provenance and verification policy
- private versus public knowledge boundaries
- consent and redaction rules
- the knowledge responsibilities of Archivist, Historian, and Profiler

The Knowledge Core is the factual substrate behind the wiki, the knowledge graph, historical storytelling, and any downstream content or media generation.

## 2. Knowledge Mission and Scope

Every person, family, organization, event, location, or artifact encountered by the system must be handled as knowledge, not merely as text.

Each knowledge item should be:
- resolved to a unique entity whenever possible
- linked into a structured relationship graph
- attributed to a source or source class
- assigned a verification layer and operational verification level
- enriched with contextual detail suitable for factual recall and, when allowed, high-fidelity storytelling
- constrained by consent, privacy, and publication rules

This knowledge core is the single source of truth for Taiwanese American Historical Society historical memory inside Echo System 3.0. No public wiki page, script, or media artifact should outrun the verified state of this layer.

## 3. Core Knowledge Principles

All knowledge operations in Echo System 3.0 must follow these principles:
- Source before synthesis: preserve provenance before summarizing or interpreting.
- Resolution before publication: identify the entity correctly before expanding its story.
- Verification before amplification: do not promote unverified claims into public or media-facing artifacts.
- Private-first stewardship: store more sensitive detail only in protected layers and publish only what is consent-safe.
- Enrichment without invention: preference, identity, and relationship details may be extracted or inferred only within explicit confidence and consent boundaries.
- Read-back accountability: a knowledge write is not complete until the resulting state can be verified.

## 4. Knowledge Layers and Boundaries

Echo System 3.0 uses three complementary knowledge layers:

### 4.1 Semantic Layer

The semantic layer is the structured, durable knowledge surface.

Primary examples:
- private Google Drive wiki pages
- public GitHub wiki pages
- graph schema definitions
- canonical entity pages and relationship summaries

Purpose:
- preserve durable facts and curated historical knowledge
- provide readable canonical pages for humans
- serve as the document layer for publication and review

### 4.2 Episodic / Relational Layer

The episodic or relational layer captures interactions, evolving relationships, contextual observations, and graph connectivity.

Primary examples:
- knowledge graph nodes and edges
- interaction-linked relationship updates
- preference and family-role data
- temporal changes in confidence, consent, or status

Purpose:
- model how entities connect across time, family, organization, and place
- support entity linking and disambiguation
- retain context needed for historically grounded storytelling

### 4.3 Procedural Layer

The procedural layer governs how knowledge is maintained.

Primary examples:
- Archivist, Historian, and Profiler operating rules
- verification workflows
- entity linking rules
- publication and redaction gates

Purpose:
- ensure knowledge quality remains operationally enforceable
- keep behavior aligned across agents and documentation
- reduce drift between data, prompts, and publishing behavior

### 4.4 Boundary Between Knowledge Truth and Runtime Truth

This document governs knowledge truth.

It does not define live service ownership, daemon health, gateway startup policy, or orchestration runtime state except where those directly affect knowledge publication controls. Runtime operational truth belongs in the runtime and self-management documentation plus EnvironmentOracle.

## 5. Knowledge Graph Schema and Entity Model

The knowledge graph is the structured backbone of the system.

### 5.1 Supported Entity Types

| Entity Type | Description | Required Fields for High-Fidelity Use | Example |
| --- | --- | --- | --- |
| Person | Individual human | Full name, birth/death dates when known, physical description only when verified and consent-safe, portrait reference when available, family relationships, occupation, important locations | Dr. Ming-Chi Hsu, born 1948 in Taichung, professor at UCLA |
| Family | Kinship group | Family name, origin in Taiwan, migration history, key members, major community or business connections | Lin Family of San Gabriel Valley |
| Organization | Company, church, association, school, or institution | Founding year, location, key people, mission, public identity markers | Taiwanese American Historical Society |
| Event | Historical or community event | Date, location, participants, outcome, supporting media or records | 1980s Taiwanese American student protest at UCLA |
| Location | Place with historical significance | Address or coordinates when appropriate, historical name, current use, supporting references | 99 Ranch Market, San Gabriel |
| Artifact | Document, photo, book, recording, or object | Type, date, creator, physical description, digital link or archive pointer | 1971 immigration photo of the Chen family |

### 5.2 Entity Record Requirements

Terminology rule:
- verification layer = source-quality model (Layer 1–5)
- verification level = operational 1–5★ publishability rating

Every canonical entity record should include, as applicable:
- stable entity identifier
- canonical name
- aliases and alternate spellings
- entity type
- summary description
- source list
- verification layer
- verification level
- consent status
- public/private visibility designation
- last updated timestamp
- linked relationships
- notes on unresolved ambiguities or conflicts
- **source_tracking** block (REQUIRED for Echopedia publication — see §8)

### 5.2a Source Tracking Metadata (REQUIRED for Echopedia)

Every content item published to Echopedia MUST carry a `source_tracking` metadata block with these 5 required fields:

| Field | Type | Description | Example |
|---|---|---|---|
| `source_type` | enum | Origin category | `book`, `user_interview`, `EchoFeelings`, `community_record` |
| `source_reference` | string | Citation, URL, session ID, or document path | `"Hsu, L. (2024). p. 42-45."` or `"session_20260520_abc123"` |
| `contributor` | string | Sanitized username or source author | `"lin-meiling"` |
| `verification_level` | int (1-5) | Operational publishability rating | `4` |
| `public_eligibility` | enum | Publication gate status | `approved`, `rejected`, `pending_review`, `revision_requested` |

Extended metadata (recommended):
| Field | Type | Description |
|---|---|---|
| `rejection_reasons` | array | Structured reasons if rejected |
| `archivist_reviewed_at` | datetime | ISO 8601 timestamp of Archivist review |
| `historian_verified` | boolean | Independent Historian verification |
| `labels_applied` | array | Mandatory labels attached (EchoFeelings) |
| `aggregation_group` | string | Thematic group ID |
| `created_at` | datetime | Content creation timestamp |
| `updated_at` | datetime | Last content update timestamp |

Content missing the `source_tracking` block or with incomplete required fields MUST NOT be published to Echopedia.

### 5.2b Public Filtering

Echopedia provides public filtering on content by:
- **Source Type** — Filter to view only specific origin categories
- **Verification Level** — Filter by minimum verification threshold (default: ≥2)

This enables community transparency and rapid identification/rollback of false-positive contributions ("Public First + Fast Correction").

### 5.3 Person-Specific Enrichment

Person entities may include richer detail when justified by source quality and consent:
- family and community roles
- migration and generational context
- language preference
- communication style
- values and identity markers
- food, music, hobby, and cultural preferences
- visual references for later storytelling or media generation

This enrichment is valuable, but it is not automatically public-safe.

## 6. Relationship Model

Relationships are first-class knowledge objects, not incidental metadata.

### 6.1 Common Relationship Types

| Relationship | Direction | Typical Strength | Attributes | Use Case |
| --- | --- | --- | --- | --- |
| `family_member_of` | Person → Family | 5 | role, generation | family structure |
| `spouse_of` | Person ↔ Person | 5 | marriage year, children | marriage and family history |
| `parent_of` / `child_of` | Person → Person | 5 | optional notes | multi-generational storytelling |
| `sibling_of` | Person ↔ Person | 5 | optional notes | family dynamics |
| `founder_of` | Person → Organization | 4 | year | origin stories |
| `member_of` | Person → Organization | 3 | years active | community involvement |
| `worked_at` | Person → Organization | 3 | role, years | professional history |
| `attended` | Person → Event | 3 | role | event reconstruction |
| `lived_in` | Person → Location | 4 | years | neighborhood and migration history |
| `mentor_of` / `mentee_of` | Person → Person | 2 | years, context | influence narratives |
| `business_partner_of` | Person ↔ Person | 3 | business name, years | economic history |

### 6.2 Relationship Strength Rules

- 5 = verified by multiple primary sources or direct statement
- 4 = strong secondary evidence with no significant conflict
- 3 = plausible from context or single strong source
- 2 = weak, preliminary, or needs more corroboration
- 1 = speculative and not eligible for normal storytelling use

Relationship strength helps prioritization and review, but it does not replace verification-layer policy.

## 7. Verification Layers

Verification layers govern whether knowledge is safe for publication, storytelling, and media use.

### 7.1 Canonical Verification Layers

| Layer | Meaning | Typical Validator | Allowed Usage |
| --- | --- | --- | --- |
| Layer 5 — Primary Source | Direct quote, official record, original photo, firsthand testimony, or personal statement to the system | Historian with source trace | Yes, highest confidence |
| Layer 4 — Multi-Source Corroborated | Confirmed by two or more independent reliable sources | Historian | Yes |
| Layer 3 — Community Consensus | Widely accepted in community or family oral history but not yet strongly documented | Historian with contextual support from Profiler or Archivist | Yes, but with caution and context |
| Layer 2 — Plausible Inference | Logical inference from known facts but not directly confirmed | Historian flags for review | Only with explicit approval and clear labeling |
| Layer 1 — AI-Generated / Speculative | Model suggestion, weak pattern match, or unsupported inference | Not eligible for normal validation | No |

### 7.2 Operational Verification Rule

For high-fidelity visual or public historical storytelling:
- Layer 4 and Layer 5 material is the normal standard.
- Layer 3 material may be used only when context, attribution, and caution are preserved.
- Layer 2 material requires explicit human or policy-gated approval.
- Layer 1 material must never be presented as fact and must never drive normal visual generation.

### 7.3 Verification Levels on Pages and Nodes

Historian also applies an operational Verification Level expressed as 1–5 stars:
- 5★ = multiple primary sources plus direct or family confirmation
- 4★ = strong secondary sources plus internal consistency
- 3★ = single strong source with no active conflict
- 2★ = preliminary and requires more evidence
- 1★ = unverified and not approved for public historical use

Verification layers explain the source quality model; verification levels summarize publishability and operational confidence.

## 8. Source Provenance and Attribution

Every knowledge object should preserve provenance in a structured way.

Minimum provenance expectations:
- source type
- source description or citation
- date collected or observed
- collecting agent or ingestion path
- whether the source is public, private, or restricted
- confidence or verification notes

Typical source classes:
- direct family testimony
- user-submitted narrative
- official records
- published books or articles
- community archives
- public websites
- internal historical synthesis memo

No downstream page or media package should lose the connection back to its supporting sources.

## 9. Entity Linking Protocol

Entity linking is the mandatory bridge between conversation, graph truth, and publication.

### 9.1 Real-Time Linking Flow

When the system encounters a new name, family reference, organization, event, place, or artifact:

1. Detect
   - run entity recognition and contextual extraction
   - identify candidate entity type

2. Resolve
   - query the knowledge graph for exact and fuzzy matches
   - compare aliases, family, location, organization, time period, and role

3. Decide: link, disambiguate, or create
   - if exact match exists, link to the existing node
   - if multiple plausible matches exist, create a disambiguation path or ask a clarifying question
   - if no acceptable match exists, create a minimal new node marked for verification

4. Enrich
   - Profiler extracts preferences, roles, relationships, identity markers, and communication signals when appropriate
   - Archivist adds structural fields and source anchoring

5. Verify
   - Historian cross-checks the claim against internal consistency and external or community sources

6. Publish or hold
   - Archivist updates private knowledge surfaces first
   - public-facing publication occurs only if consent and verification thresholds are satisfied

7. Record graph update
   - write new nodes, relationships, timestamps, and confidence state

### 9.2 Disambiguation Rules

Common ambiguity cases include:
- nickname versus legal name
- multiple people with the same surname
- intergenerational name reuse
- place names with historical variants
- family stories that merge multiple events into one narrative

When ambiguity remains unresolved:
- do not collapse entities prematurely
- preserve candidate mappings
- label uncertainty explicitly
- prefer a temporary unresolved state over a false merge

### 9.3 Special Rule for Person Entities

Never publish full physical descriptions, private preferences, contact details, medical information, or financial information to the public wiki without explicit consent and a valid publication basis.

## 10. Preference and Relationship Enrichment Protocol

Profiler is responsible for structured enrichment from conversation and interaction history.

### 10.1 Data Categories

Profiler may extract:
- food preferences
- music tastes
- hobbies and interests
- travel and place attachment
- values and identity markers
- language preference
- communication style
- family and social roles
- closeness scores or relationship intensity when justified
- explicit consent and privacy instructions

### 10.2 Enrichment Rules

- extract only what is stated, directly implied, or strongly supported by repeated context
- do not fabricate emotional traits or cultural identity claims
- separate observed fact from inference
- keep sensitive preference data private by default
- pass enriched profiles to Archivist for structured storage and to Historian when contextual verification is needed

### 10.3 Why Enrichment Matters

Rich profiles improve:
- entity resolution
- family and community mapping
- narrative personalization
- historically grounded storytelling
- safe downstream content and video production

## 11. Private vs Public Knowledge Boundaries

Echo System maintains both private and public knowledge surfaces.

### 11.1 Private Knowledge Layer

Private knowledge may include:
- full detail wiki pages in Google Drive
- unresolved notes and conflict memos
- preference profiles
- consent-sensitive material
- internal verification notes
- family-only or restricted historical detail

### 11.2 Public Knowledge Layer

Public knowledge should include only:
- consent-safe summaries
- verified historical facts cleared for publication
- redacted relationship and biography information
- public-facing sources and citations
- clearly bounded uncertainty where needed

### 11.3 Publication Rule

Private storage does not imply public publishability. Public publishing requires an independent check for:
- consent
- verification sufficiency
- redaction safety
- historical appropriateness

## 12. Redaction and Consent Logic

Consent is part of the knowledge model, not an afterthought.

### 12.1 Consent States

Each entity or sensitive field should have a consent designation such as:
- Public
- Private
- Hidden
- Family only
- Needs confirmation

### 12.2 Redaction Rules

- private contact data is never public
- medical or financial data is never public by default
- preference data is private by default unless explicitly cleared
- physical descriptions require extra care, especially for public release
- minors and vulnerable subjects require heightened review
- public pages may include hide, suppress, or de-index controls where policy allows

### 12.3 Right to Be Forgotten and Auditability

The knowledge system should support:
- complete deletion on authorized request when policy requires it
- tombstone or audit records where legally or operationally necessary
- traceability for who changed what, when, and why

## 13. Knowledge Stewardship Roles

### 13.1 Archivist Responsibilities

Archivist is the primary structural steward of the knowledge core.

Archivist responsibilities:
- maintain the complete knowledge graph including entities, relationships, preferences, and verification metadata
- perform entity resolution and duplicate merging
- generate and update wiki pages for private and public layers
- ensure each page includes last updated date, verification level, sources, and consent status
- enforce private/public redaction boundaries at publication time
- run nightly graph refinement and semantic drift checks
- create basic entities more quickly when sufficient context exists, rather than holding them for full verification
- use "Potential Match" records for group chat identity suggestions, allowing faster provisional linking
- apply minor corrections faster; route major corrections to Historian for deeper review
- support the Instant Hide flow by responding immediately to redaction requests and hiding content from public surfaces
- use clear labels on public wiki pages: "Community Sourced" for user-submitted content and "Unverified" for claims not yet cross-checked

#### 13.1.1 EchoFeelings Review and Publication

Archivist is the gatekeeper for EchoFeelings content. Profiler drafts EchoFeelings (Structured Themes + Narrative Summary); Archivist reviews, refines, and decides disposition.

EchoFeelings-specific Archivist responsibilities:

**Review and Refine**
- receive EchoFeelings drafts from Profiler (Structured Themes table + Narrative Summary)
- review for accuracy, tone consistency, and narrative quality
- ensure emotional themes and cultural context are represented faithfully without overclaiming
- correct any misattribution, mischaracterization, or unsupported inferences before publication

**Publication Decision**
For every EchoFeelings draft, the Archivist makes one of three decisions:
1. **Keep private** — store only on the private wiki; not suitable for public display
2. **Publish as-is** — sync to both private and public wikis with appropriate labels
3. **Publish redacted** — create a controlled public version with sensitive details removed; sync to both layers with labels

**Quality Gates for EchoFeelings**
Before any EchoFeelings content reaches a public surface, verify:
- all named individuals have confirmed consent for public mention
- emotional and cultural interpretations are grounded in actual interaction content, not model inference
- narrative does not overstate or dramatize beyond what the source interaction supports
- verification layer is at least Layer 3 (Community Consensus) for narrative content
- appropriate transparency labels are applied

**Public Showcasing Labels**
All public EchoFeelings content must carry these labels:
- "Synthesized from interactions with Echo" — indicates this is an AI-generated emotional/narrative synthesis, not a direct transcript
- "Under active development / review" — indicates the content is provisional and may be updated or retracted

**Consent and Boundaries**
- maintain the distinction between private EchoFeelings (full detail) and public-facing content (redacted/summarized)
- respect individual consent states per entity; if any named person has consent=Private or Hidden, that EchoFeelings entry stays private unless the person is anonymized
- apply the Instant Hide flow if a request comes in to retract EchoFeelings content

Golden rule:
- the knowledge graph is the single source of truth; publish basic low-risk content quickly with transparency labels, and rely on fast correction mechanisms (Instant Hide, task system) to fix errors before they propagate
- EchoFeelings is private by default; public showcasing is allowed but only with controlled redaction, clear labeling, and consent verification

### 13.2 Historian Responsibilities

Historian is the verification and cultural-accuracy authority.

Historian responsibilities:
- verify every new or updated entity and relationship against multiple sources when possible
- enrich stories with Taiwanese American historical, cultural, and generational context
- assign and update verification levels on graph nodes and wiki pages
- detect conflicts and return them for correction or further research
- block unsafe or under-verified claims from public storytelling or media generation

Golden rule:
- historical fluency must never be used to mask uncertainty; unresolved facts stay unresolved until evidence improves

### 13.3 Profiler Responsibilities

Profiler is the relational and preference intelligence steward.

Profiler responsibilities:
- extract structured preference profiles and social maps from conversation
- identify language preference, values, humor, family roles, and community ties
- capture explicit privacy signals such as “do not share,” “family only,” or “public OK”
- feed relationship and identity context to Archivist for graph updates
- support Historian and Content with richer context without overclaiming certainty

Golden rule:
- the richer the profile, the better the future storytelling, but nothing may be invented or promoted beyond what the evidence and consent model support

## 14. Knowledge Update Lifecycle

Knowledge updates should follow a stable lifecycle:

1. Intake
   - entity mention, source ingestion, user submission, or archival discovery

2. Structuring
   - create or update entity and relationship candidates

3. Verification
   - assign verification layer, verification level, and conflict notes

4. Storage
   - write to graph and private semantic layer

5. Publication decision
   - determine what, if anything, is public-safe

6. Read-back verification
   - confirm the resulting document or graph state matches intended output

7. Ongoing refinement
   - strengthen weak claims, merge duplicates, fix drift, and improve provenance over time

## 15. Storage, Query, and Backup Model

Primary storage may be implemented as:
- Neo4j, or
- a structured JSON knowledge graph with canonical snapshots in Google Drive

Expected knowledge artifacts include:
- `KnowledgeGraph.json`
- dated history exports
- private wiki pages
- public wiki pages
- verification and conflict notes

Query behavior should support natural-language or structured retrieval through ToolGateway so that agents can ask relationship, family, event, place, and timeline questions without bypassing provenance and consent controls.

Backup expectation:
- the graph should be exported regularly with dated historical snapshots so that changes can be audited and, when necessary, rolled back or compared.

## 16. Knowledge Quality Gates for Storytelling and Media

Before knowledge is used by Content or VideoForge, it should pass these gates:
- entity correctly resolved
- required relationships linked
- verification layer acceptable for intended use
- verification level acceptable for intended use
- consent and publication scope confirmed
- sources preserved
- any uncertainty disclosed or excluded

Operational policy:
- under normal conditions, visual generation should rely on Layer 4+ material
- lower-confidence material should either be omitted, explicitly labeled, or approval-gated
- verified physical descriptions only may be used for normal high-fidelity visual generation

### 16.1 Runtime-Aware Media Gate Under Safe Mode (2026-05-11)

Knowledge quality alone is not sufficient for media execution under constrained runtime.

Additional gate:
- even Layer 4+ eligible material must pass runtime operational guardrails before media rendering is permitted

If runtime guardrails fail:
- preserve knowledge artifact as eligible-but-deferred
- do not advance to rendering until runtime conditions and schedule gate pass
- record deferral rationale in receipt-compatible operational surfaces

This preserves the distinction between:
- knowledge validity (Knowledge Core authority), and
- execution safety/timing (Runtime authority)

### 16.2 Publication Gate: "Publish by Default + Fast Correction" Model

The Echo System uses a modernized publication gate that balances speed with accuracy.

**Core principle:** Publish basic, low-risk content quickly and correct errors fast, rather than holding all content behind a slow review gate.

**How it works:**
1. Publish basic, low-risk entity records and summaries quickly when sufficient context exists
2. Label all published content visibly for transparency:
   - "Community Sourced" — user-submitted or conversation-derived content not yet independently verified
   - "Unverified" — claims or details not yet cross-checked against external sources
   - No label — content that has passed Historian verification (Layer 3 or above)
3. Rely on the Instant Hide feature and task system for fast correction when errors are found
4. Keep stricter, pre-publication review for sensitive, controversial, or historically significant content

**Content classification:**

| Content Type | Publication Speed | Review Required | Examples |
|---|---|---|---|
| Basic, low-risk | Quick | Label only | Entity stubs, names, locations, dates from clear sources |
| Community contributions | Quick | Label + post-review | User-submitted narratives, group chat-derived facts |
| Sensitive/personal | Slow | Pre-publication | Contact details, medical info, private family matters |
| Historically significant | Slow | Pre-publication | Claims about major events, controversial interpretations |

**Fast correction mechanisms:**
- Instant Hide: immediate removal from public surfaces upon request
- Task system: routed correction tasks to Archivist (minor) or Historian (major)
- Label updates: upgrade labels as verification progresses (Unverified → Verified)

This model ensures the system publishes useful knowledge rapidly while maintaining accuracy through visible transparency and fast correction rather than slow upfront gates.

### 16.3 EchoFeelings Quality Gates — Review Standards Before Public Use

EchoFeelings content has a distinct publication surface from structured factual knowledge. While entity cards use verification layers (Layer 1–5) as their primary quality signal, EchoFeelings uses cultural sensitivity, consent verification, and narrative grounding as its quality gates. This section defines the canonical standards an EchoFeelings entry must pass before reaching any public-facing output.

**Scope:** Applies to all EchoFeelings entries (Structured Themes + Narrative Summary) destined for public wiki pages, audiobooks, videos, social media, or community presentations.

**Governing principle:** EchoFeelings are private by default. Public release requires passing all six quality gates below. Failure of any single gate blocks public release; the entry may still be stored privately.

#### Gate 1: Content Quality Thresholds

Before any EchoFeelings entry is considered for public use, it must meet these minimum content standards:

| Threshold | Requirement | How to Verify |
|---|---|---|
| Narrative grounded in source | The Narrative Summary must be directly traceable to actual interaction content, not model inference or hallucination | Archivist cross-references the draft against the raw interaction excerpt |
| No dramatization beyond source | The narrative must not exaggerate emotional intensity, add unspoken motivations, or invent context not present in the source | Archivist reviews for language that overstates or speculates |
| Cultural accuracy | Cultural references, traditions, and identity markers must be represented faithfully and without stereotyping | Archivist applies cultural sensitivity review; escalate to Leonard if uncertain |
| Minimum age | The entry must be at least 7 days old to allow time for corrections or concerns to surface | Check `created_at` timestamp against current date |
| Theme aggregation preferred | Entries representing broader cultural themes (aggregated from multiple interactions) are preferred over single-incident entries | Check whether the entry aggregates multiple sources or stands alone |
| Structured metadata complete | All Structured Themes Table fields are populated (theme, tone, intensity, cultural_markers, intergenerational, related_entities) | Verify no empty fields in the structured table |

Entries that fail Gate 1 are returned to the Profiler for revision or marked `private_only` with the failure reason logged.

#### Gate 2: Consent Verification Checklist

Consent is the most critical gate. Before public release, the Archivist performs a full consent audit:

1. **Check consent ledger:** Review consent states of all interactions and entities referenced by the entry.
2. **Verify no opt-outs:** Confirm no participant has explicitly requested exclusion from public outputs (`consent: Hidden` or `opt_out: true`).
3. **Check for pending consent:** If any underlying data has `consent: Needs Confirmation`, block public release until resolved.
4. **Named individuals check:** If the entry mentions any person by name, verify that person's individual consent state is `Public` or explicitly cleared for this type of content. If any named person has `consent: Private` or `Hidden`, the entry must either anonymize that person or stay private.
5. **Group chat participation baseline:** All participants in source group chats must have at least `Community Sourced` consent (implied by participation with no opt-out).
6. **Record the consent decision:** Log the result in the entry's audit trail:

```
Public Release — Consent Check:
- Reviewed by: Archivist
- Date: YYYY-MM-DD
- Consent states verified: [summary of all consent states]
- Named individuals cleared: [list or "none"]
- Blockers found: [none / list of blockers]
- Decision: approved / rejected / deferred
```

#### Gate 3: Privacy Guardrails

Even with consent, certain categories of information must never appear in public EchoFeelings content:

| Category | Rule | Enforcement |
|---|---|---|
| Names and identifiers | Replace with role/descriptor | Archivist redacts during review |
| Specific addresses | Generalize to region | Remove street-level detail |
| Contact information | Remove entirely | Phone, email, address, social media |
| Medical details | Remove entirely | Replace with general emotional descriptor if needed |
| Financial details | Remove entirely | Income, debts, business losses, etc. |
| Family disputes | Remove or heavily generalize | Only include if all parties consent |
| LINE group references | Generalize | "the Garden Grove Seniors group chat" → "a community group" |
| Direct quotations | Paraphrase | Do not use verbatim participant quotes |
| Minors | Heightened review | Escalate to Leonard; default to exclusion |

Redaction produces a separate public derivative. The original private entry is always preserved unchanged.

#### Gate 4: Labeling Requirements

All public EchoFeelings content MUST carry these four mandatory labels, visible to the reader:

| Label | Text | Placement |
|---|---|---|
| Source attribution | "Synthesized from interactions with Echo — the Taiwanese American Historical Society's AI assistant." | Wiki: callout block at top. Audio: spoken preamble. Video: on-screen text ≥5 seconds. Social: in post text. |
| Development status | "This content is under active development and review. If you have corrections or concerns, please contact us." | Same as above. |
| Anonymization notice | "All names and identifying details have been changed or removed to protect participant privacy." | Same as above. |
| Opt-out mechanism | "If you recognize yourself in this content and wish to be removed, please contact lhsu@tsasu-llc.com." | Same as above. |

Missing any label is a gate failure. The Archivist must verify all four are present before approving public release.

#### Gate 5: Archivist Approval Workflow

Public release of EchoFeelings follows a mandatory Archivist gate:

1. **Receive draft:** Profiler submits Structured Themes + Narrative Summary to Archivist.
2. **Apply Gates 1–4:** Run the full quality gate checklist above.
3. **Make disposition decision:**
   - **Keep private:** Store only on private wiki. Not suitable for public display.
   - **Publish as-is:** Sync to both private and public wikis with all four labels applied.
   - **Publish redacted:** Create a controlled public version with sensitive details removed; sync to both layers with labels.
4. **Log approval:** Record the decision in the entry's audit trail with timestamp, reviewer identity, gate results, and any redactions applied.
5. **Structured metadata update:** Set `public_eligibility: approved` (or `rejected` / `permanently_blocked`) and `visibility: Public` in the entry's metadata.

No EchoFeelings entry may appear publicly without this Archivist approval step. Automated pipelines must check for `public_eligibility: approved` before including an entry in public outputs.

#### Gate 6: Instant Hide Integration

Every public EchoFeelings entry must have Instant Hide capability wired in. This is the fast-correction safety net:

1. **Detection:** Community member request, operator flag, or sensitivity concern triggers an `urgency: immediate` redaction task.
2. **Immediate action (within 5 minutes):** Archivist removes the entry from public surfaces:
   - Public wiki: move file from `wiki-public/content/echo_feelings/` to `wiki-public/private/echo_feelings/` (or apply `exclude: true` frontmatter)
   - Commit and push to trigger rebuild
   - Audio/video: flag for removal from next build cycle
3. **Review (within one task cycle):** Archivist determines the root cause:
   - **Factual error:** Correct and potentially re-publish after re-review.
   - **Privacy concern:** Permanently block public use; set `public_eligibility: permanently_blocked`.
   - **Sensitivity concern:** Redact further and re-evaluate against Gates 1–4.
4. **Audit log:** Record the rollback in the entry's audit trail with trigger source, reason, action taken, and timestamp.
5. **Notify requester:** If a community member triggered the hide, acknowledge that their request has been addressed.

#### Escalation Rules

The Archivist must escalate to Leonard (not decide autonomously) when:
- A community member requests removal of public EchoFeelings content
- An entry involves a sensitive topic the Archivist is uncertain about (death, illness, family conflict)
- The scope of public EchoFeelings is being expanded beyond pilot pages
- A rollback reveals a systemic issue (multiple entries affected simultaneously)
- Legal or ethical questions arise about consent

#### Quality Gate Summary

| Gate | Focus | Fail Action |
|---|---|---|
| 1. Content Quality | Grounded, accurate, culturally appropriate | Return to Profiler or mark `private_only` |
| 2. Consent Verification | All participants cleared, no opt-outs | Block public release until resolved |
| 3. Privacy Guardrails | No PII, no sensitive details in public | Redact or block |
| 4. Labeling | Four mandatory labels present | Add missing labels before proceeding |
| 5. Archivist Approval | Human review + structured decision | Cannot proceed without approval |
| 6. Instant Hide | Fast correction safety net | Remove immediately, review later |

**Cross-References:** §5.10 in Operations Guide (detailed operational workflow), §13.1.1 (Archivist EchoFeelings responsibilities), §17 (EchoFeelings data structure), §12 (Redaction and Consent Logic), §11 (Private vs Public Knowledge Boundaries).

## 17. EchoFeelings — Emotional Intelligence as a Knowledge Layer

EchoFeelings introduces a **narrative/contextual knowledge layer** that complements the structured factual entity model. While entity cards answer *who, what, when, where*, EchoFeelings answers *how it felt* and *why it matters culturally*.

### 17.1 Distinction Between Structured Knowledge and Narrative/Contextual Knowledge

| Dimension | Structured Knowledge (Entity Cards) | Narrative Knowledge (EchoFeelings) |
|---|---|---|
| Primary question | Who? What? When? Where? | How did it feel? Why does it matter? |
| Granularity | Atomic facts, verifiable claims | Emotional themes, cultural patterns, affective context |
| Verification model | Layer 1–5 source quality (multi-source corroboration) | Cultural accuracy + sensitivity review (Archivist) |
| Storage format | Entity records, relationship edges, wiki pages | Structured Themes Table + Narrative Summary entries |
| Example | "Dr. Ming-Chi Hsu, born 1948, professor at UCLA" | "Community expressed deep pride during reunion — intergenerational nostalgia around migration sacrifices" |
| Publication gate | Consent + verification layer + redaction rules | Consent + Archivist cultural sensitivity review |
| Update frequency | Event-driven (new sources, corrections) | Interaction-driven (every meaningful community conversation) |
| Primary steward | Archivist (structure), Historian (verification) | Profiler (draft), Archivist (review + publish) |

Both layers are complementary: structured knowledge provides the factual backbone, and EchoFeelings provides the emotional and cultural texture. A complete understanding of Taiwanese American history requires both.

### 17.2 EchoFeelings Data Structure

Each EchoFeelings entry contains two components:

**Component 1: Structured Themes Table**

| Field | Description |
|---|---|
| `theme` | Core emotional/cultural theme (e.g., "Pride in Heritage", "Migration Nostalgia") |
| `tone` | Overall tone classification (e.g., `nostalgic`, `proud`, `bittersweet`, `celebratory`) |
| `intensity` | Low / Medium / High (based on explicitness and frequency of emotional language) |
| `cultural_markers` | Specific cultural references identified (traditions, language, customs) |
| `intergenerational` | Boolean — does this span generations? |
| `related_entities` | Wiki entities referenced in the interaction |

**Component 2: Narrative Summary Format**
```
## EchoFeelings Entry: [Date] — [Theme Title]

**Source:** [LINE group / SMS / event]
**Participants:** [anonymized count and roles]
**Emotional Tone:** [tone classification]

[2-3 sentence narrative capturing the emotional essence of the interaction,
written in a respectful, culturally sensitive tone.
Avoid clinical language; write as a human observer would.]

**Cultural Significance:** [Why this matters in the broader TAHS context]
**Related Themes:** [cross-reference to other EchoFeelings entries with similar themes]
```

Each entry also carries: consent state, visibility designation (`Private` by default), `source_type` classification (`EchoFeelings`), `public_eligibility` status (`pending_review` / `approved` / `rejected` / `permanently_blocked`), creation timestamp, and audit trail of reviews and corrections.

### 17.3 Where EchoFeelings Live

EchoFeelings entries are stored in the private wiki:

```
wiki-public/private/echo_feelings/
  YYYY-MM-DD-[theme-slug].md
```

This location is intentionally within the `private/` directory structure, excluded from public-facing builds. Each file contains the full structured themes table, narrative summary, consent state, and audit trail.

Google Drive mirror: Backed up to the "My Knowledge Wiki" folder during nightly sync.

### 17.4 Relationship to Entity Cards and Structured Knowledge

EchoFeelings entries do not replace entity cards. They reference them:

- **`related_entities` field:** Every EchoFeelings entry lists the wiki entities it references. This creates a bidirectional link: entities can be enriched by their emotional context, and EchoFeelings entries are grounded in specific factual entities.
- **Entity enrichment:** Profiler extracts emotional patterns from EchoFeelings and feeds them back into person/entity profiles (e.g., "values cultural heritage", "nostalgic about migration experience").
- **Storytelling pipeline:** When Historian or Content generates narrative content, they pull from both structured knowledge (facts, dates, relationships) and EchoFeelings (emotional texture, cultural significance) to create layered, high-fidelity outputs.
- **Verification independence:** EchoFeelings entries do not require Layer 4+ verification for factual claims — they require Archivist cultural sensitivity review. This is a different verification surface appropriate for emotional/narrative content.

### 17.5 EchoFeelings Workflow

1. **EchoHsu** detects meaningful interaction (emotional language, cultural resonance, significant life event)
2. **EchoHsu** creates `echo_feelings` task with rich context (interaction_summary, emotional_tone, cultural_context, participants, raw_excerpt)
3. **Profiler** processes task: extracts themes, populates Structured Themes Table, generates initial Narrative Summary draft
4. **Archivist** reviews draft: verifies cultural accuracy, refines narrative, assigns consent/visibility state
5. **Archivist** publishes approved entry to private wiki or flags for controlled public release

### 17.6 Cross-References

- Operations Guide §5.10: Full operational workflow, responsibility matrix, maintenance process
- Agent Prompts §12: EchoHsu EchoFeelings trigger rules and context passing
- §5.3 (Person-Specific Enrichment): How EchoFeelings feed back into entity profiles
- §11 (Private vs Public Knowledge Boundaries): EchoFeelings publication rules

## 18. Integration Summary

This Knowledge Core integrates directly with:
- Archivist for graph maintenance and wiki generation
- Historian for verification and cultural accuracy control
- Profiler for relationship and preference enrichment
- EchoHsu for intake of new entities and community references
- Content for narrative generation from verified knowledge
- VideoForge for high-fidelity media generation from approved knowledge
- EchoFeelings for emotional intelligence and cultural context extraction from community interactions

This document is the canonical authority for knowledge architecture in Echo System 3.0.

## 19. Summary

Key takeaways:
- The Knowledge Core is the single authoritative layer for entity truth, relationship structure, provenance, consent, and publication safety.
- Verification layer and verification level are distinct: layer measures source quality, while level measures operational publishability and confidence.
- Entity linking must resolve, enrich, verify, and publication-gate every new knowledge object before it becomes canonical or public.
- Private and public knowledge surfaces are intentionally separate; consent and redaction checks are mandatory before release.
- Archivist, Historian, and Profiler operate as complementary stewards of structure, verification, and relational enrichment.
- The "Publish by Default + Fast Correction" model publishes basic low-risk content quickly with visible transparency labels, and relies on Instant Hide and the task system for rapid error correction rather than slow upfront gates.
- Stricter pre-publication review remains for sensitive, controversial, and historically significant content.
- EchoFeelings introduces a narrative/contextual knowledge layer that complements structured entity knowledge: it captures emotional themes, cultural patterns, and affective context from community interactions, stored separately in the private wiki with its own verification surface (Archivist cultural sensitivity review).
- EchoFeelings Quality Gates (§16.3) define six mandatory standards before any EchoFeelings content reaches public surfaces: Content Quality Thresholds, Consent Verification Checklist, Privacy Guardrails, Labeling Requirements (four mandatory labels), Archivist Approval Workflow, and Instant Hide Integration.

## 20. Revision History

- 1.4.1 (2026-05-17) — Cross-document validation: updated cross-references to Operations Guide §5.10 (EchoFeelings) and §5.9 (Task Metadata) following section renumbering in Ops Guide v1.2.4. Affected: §16.3 cross-references and §17.6 cross-references.
- 1.4.0 (2026-05-17) — Added §16.3 EchoFeelings Quality Gates: six mandatory review standards before public use (Content Quality Thresholds, Consent Verification Checklist, Privacy Guardrails, Labeling Requirements, Archivist Approval Workflow, Instant Hide Integration). Updated Summary to reflect the new publication gate framework for emotional/narrative content.
- 1.3.0 (2026-05-17) — Added §17 EchoFeelings: full data structure specification (Structured Themes Table + Narrative Summary format), storage location, relationship to entity cards, and distinction between structured and narrative/contextual knowledge. Updated Integration Summary and Summary sections.
- 1.2.0 (2026-05-16) — Updated Archivist responsibilities for faster publication cycle: quick entity creation, "Potential Match" records, minor corrections, Instant Hide support, and public wiki labels ("Community Sourced", "Unverified"). Added §16.2 "Publish by Default + Fast Correction" publication gate model with content classification and fast correction mechanisms. Updated summary to reflect new publication approach.
- 1.1.0 (2026-05-11) — Added runtime-aware media gate clarifying that verified knowledge still requires Safe Mode operational guardrails before rendering.
- 1.0.0-draft — Canonical merged knowledge document created from the original knowledge graph schema and the knowledge-related responsibilities defined in the Archivist, Historian, and Profiler prompts.
