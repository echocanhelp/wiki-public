# Echo System Documentation Simplification — Full Implementation Checklist

Status: Draft for review
Owner: Orchestrator
Execution Owner: Archivist for documentation integrity workstreams
Dependency Anchor: `Echo_System_Master_Index.md`

## 0. Objective

Reduce the fragmented documentation layer to exactly 6 living canonical documents plus 1 automated maintenance layer, while preserving auditability, path stability during migration, and Layer 4 verification for all documentation changes.

## 1. Target Canonical Structure

Create and maintain exactly these 6 living core files:
- `Echo_System_Master_Index.md`
- `Echo_System_Vision_Architecture.md`
- `Echo_System_Knowledge_Core.md`
- `Echo_System_Runtime_and_Self_Management.md`
- `Echo_System_Agent_Prompts.md`
- `Echo_System_Operations_Guide.md`

Supporting rule:
- all other documentation becomes either deprecated, historical, exported, or receipt-backed support material
- no other file may function as a parallel canonical source of truth

## 2. Governance Rules

### 2.1 Single source of truth
- enforce `Echo_System_Master_Index.md` as the first-stop document for all documentation queries
- allow agents to use `EnvironmentOracle.documentation_state` as the machine-readable equivalent
- prohibit agents from treating legacy docs as authoritative
- have ToolGateway enforce this routing policy when documentation lookups are requested

### 2.2 Ownership
- Archivist owns Documentation Integrity
- Orchestrator approves structural changes
- Historian verifies factual/cultural/public-safety truth but does not own canonical system docs
- ToolGateway enforces documentation access policy

### 2.3 Authority precedence
1. live runtime/config truth
2. EnvironmentOracle documented state
3. Master Index
4. other canonical docs
5. legacy docs with deprecation banners
6. dated exports/history

## 3. Canonical Registry Implementation

Create a documentation registry tracked in both:
- `Echo_System_Master_Index.md`
- `EnvironmentOracle.documentation_state`

For each of the 6 canonical docs, record:
- doc_id
- path
- title
- owner
- version
- status
- last_updated
- sha256
- source_inputs
- included_in_backup
- runtime_alignment_status

## 4. Daily Documentation Sync & Validation Stage

### 4.1 Stage definition
Add new daily stage:
- stage name: `docsync`
- owner profile: `archivist`
- time: 5:15 AM PT
- execution mode: parallel with `historian`
- upstream dependencies: `sentinel`, `healer`, `evolver`, `orchestrator`

### 4.2 Why parallel
- `historian` and `docsync` both depend on upstream operational truth
- neither depends on the other
- parallel execution prevents avoidable downstream schedule drift
- `content`, `videoforge`, and `echohsu` keep their existing timing unless later optimization is required

### 4.3 Daily loop target order
- 3:00 AM PT — Sentinel
- 3:30 AM PT — Healer
- 4:30 AM PT — Evolver
- 5:00 AM PT — Orchestrator
- 5:15 AM PT — Historian
- 5:15 AM PT — DocSync
- 5:30 AM PT — Archivist knowledge sync
- 6:00 AM PT — Content
- 6:30 AM PT — VideoForge
- 7:00 AM PT — EchoHsu


### 5.1 Stage definition
Before each automated self-improvement cycle:
- verify MCP route availability and external service reachability
- record execution status in `EnvironmentOracle.documentation_state`
- do not silently skip scheduled runs
- escalate persistent external-service failures to Evolver and Orchestrator review

## 6. Receipt-Based Documentation Integrity Architecture

Implement the same planner -> JSON -> deterministic executor -> receipt flow already used elsewhere.

### 6.1 Sidecar plan file
Create:
- `runtime/stage_outputs/YYYY-MM-DD/docsync.plan.json`

Required fields:
- observed_runtime_facts
- observed_documentation_state
- detected_drift
- files_to_update
- master_index_updates
- deprecations_to_apply
- version_bumps
- blocked_items
- required_orchestrator_approval

### 6.2 Receipt file
Create:
- `runtime/stage_outputs/YYYY-MM-DD/docsync.receipt.json`

Required fields:
- schema_version
- stage
- timestamp
- success
- blocked
- actions_attempted
- files_written
- sha256_before_after
- verification
- drift_summary
- warnings
- errors

Create:

Required fields:
- schema_version
- stage
- timestamp
- availability_check
- execution_decision
- input_artifact
- external_handle
- verification
- parsed_recommendations
- downstream_evolver_handoff
- warnings
- errors

## 7. Drift Detection Inputs

Documentation sync should compare canonical docs against:

1. live Hermes root/profile configs
- `/root/.hermes/config.yaml`
- `/root/.hermes/profiles/*/config.yaml`

2. live runtime/loop truth
- `/root/echo_system/runtime/echo_autonomous_loop.py`
- latest stage receipts
- current cron inventory

3. EnvironmentOracle truth
- `/root/echo_system/environment/EnvironmentOracle.json`

4. canonical doc set
- the 6 core files only

Interpretation rule:
- runtime/config truth overrides prose
- receipts override narrative claims about side effects

## 8. Auto-Allowed vs Approval-Gated Updates

### 8.1 Auto-allowed
- timestamp refreshes
- version/hash refreshes in Master Index
- deprecation banner insertion
- deprecation-reference counters
- link repair
- alignment of already-approved facts proven by runtime evidence
- backup manifest refreshes

### 8.2 Approval-gated
- architecture claims
- agent role/ownership changes
- new/removed agents
- major prompt semantics
- loop order changes
- changes to the canonical 6-file set
- modifications that reclassify public/private knowledge boundaries

Rule:
- approval-gated changes must be proposed by Archivist or Evolver and approved by Orchestrator before deterministic writeback

## 9. EnvironmentOracle Extension

Add `documentation_state` to `EnvironmentOracle.json`.

Required fields:
- canonical_docs_version
- canonical_docs[]
- deprecated_docs[]
- last_docsync_at
- last_docsync_receipt
- last_drift_count
- last_drift_summary
- docsync_status
- documentation_policy_version

For each deprecated doc track:
- path
- replacement_docs
- deprecation_start
- consecutive_zero_reference_runs
- eligible_for_legacy_move
- moved_to_legacy_at

## 10. Explicit Deprecation Policy

Hard rule:
- keep legacy files in place with deprecation banners first
- after 14 consecutive successful docsync runs with zero references to a legacy file, it may be moved to `docs/legacy/`
- until then, keep it path-stable and read-only

Migration evidence required:
- deprecation banner present
- reference counter history preserved
- move recorded in receipt
- Master Index updated
- EnvironmentOracle updated

## 11. Transition Strategy with Minimal Disruption

### Phase 1 — Create canonical docs first
Create the 6 canonical files without deleting old ones.

### Phase 2 — Populate by merge mapping
Merge from current files as follows:

`Echo_System_Vision_Architecture.md`
- `Echo_System_3.0_Project_Brief.md`
- `Echo_System_Multi_Platform_Deployment.md`
- `Hermes_Echo_System_3.0_Master_Initialization_Prompt.md` (high-level sections only)

`Echo_System_Knowledge_Core.md`
- `Echo_System_Knowledge_Graph_Schema.md`
- Archivist/Historian/Profiler-relevant knowledge sections from prompt docs

`Echo_System_Runtime_and_Self_Management.md`
- `Echo_System_Self_Management_Layer_Prompts.md`
- `Echo_System_Autonomous_Loop_Executor_Receipt_Architecture.md`
- `Echo_System_Morning_Briefing_Protocol.md`

`Echo_System_Agent_Prompts.md`
- all 12 agent prompts from the current split prompt files

`Echo_System_Operations_Guide.md`
- `Hermes_Knowledge_Transfer_Guide.md`
- practical deployment, maintenance, extension, recovery notes

### Phase 3 — Deprecate in place
- prepend banners to superseded files
- declare canonical replacement(s)
- mark as read-only
- stop manual edits to legacy docs

### Phase 4 — Switch automation to canonical-only
Update:
- doc backup scripts
- docsync logic
- references from prompts/ops docs
- any maintenance jobs that still sweep all markdown indiscriminately

### Phase 5 — Move eligible legacy docs
- after 14 clean zero-reference runs
- move to `docs/legacy/`
- preserve receipts and history

## 12. Backup and Export Redesign

### 12.1 Canonical docs bundle
Include only:
- `Echo_System_Master_Index.md`
- `Echo_System_Vision_Architecture.md`
- `Echo_System_Knowledge_Core.md`
- `Echo_System_Runtime_and_Self_Management.md`
- `Echo_System_Agent_Prompts.md`
- `Echo_System_Operations_Guide.md`

### 12.2 Control-plane truth bundle
Include:
- `EnvironmentOracle.json`
- `EnvironmentOracle.md`
- `SystemPulse.json`
- `SystemPulse.md`
- `runtime/echo_autonomous_loop.py`
- latest `docsync.receipt.json`
- latest deployment-reality audit
- current cron inventory snapshot
- canonical doc manifest / hash table

### 12.3 Current script changes required
Current daily sync script:
- `/root/.hermes/scripts/echo_system_docs_sync.py`

Required redesign:
- replace recursive markdown sweep with explicit allowlist for canonical bundle
- add second bundle for control-plane truth artifacts
- exclude deprecated docs and dated exports from canonical backup
- include receipts only in control-plane truth bundle

## 13. ToolGateway Enforcement Plan

ToolGateway should enforce:
- documentation lookup requests are resolved through Master Index or `EnvironmentOracle.documentation_state`
- legacy file reads are redirected to canonical replacement guidance unless explicitly requested for historical reasons
- any write attempt to a deprecated file is blocked unless the operation is a deprecation banner insertion or historical archiving action approved by Orchestrator

## 14. Verification Checklist

A documentation change is not complete until all checks pass:
- target file written successfully
- content read back matches plan
- sha256 refreshed in registry
- Master Index updated if canonical state changed
- EnvironmentOracle updated if documentation state changed
- receipt written successfully
- deprecated mapping still valid
- backup allowlists still correct

- availability check executed
- execution or failure reason recorded
- MCP response archived if run
- Evolver handoff recorded

## 15. Recommended Implementation Order

1. create `Echo_System_Master_Index.md`
2. create skeletons for the other 5 canonical docs
3. define canonical doc registry fields
4. extend `EnvironmentOracle.documentation_state`
5. add `docsync` stage to runtime at 5:15 AM PT in parallel with Historian
6. define `docsync.plan.json` and `docsync.receipt.json`
8. implement MCP availability and execution guardrail
9. redesign backup scripts into canonical bundle + control-plane bundle
10. add deprecation banners to legacy docs
11. test one full simulated cycle
12. run 14-day observation window for legacy-reference counters
13. move eligible legacy files to `docs/legacy/`

## 16. Immediate Deliverables for This Migration Wave

- Master Index draft
- implementation checklist draft
- skeleton versions of all 6 canonical docs
- merge-source map
- docsync executor design
- backup allowlist redesign plan

## 17. Definition of Success

This migration is successful when:
- exactly 6 living canonical docs remain authoritative
- all legacy files are either deprecated or archived
- Master Index is the enforced first-stop authority
- daily docsync runs automatically with receipts
- backup bundles reflect canonical truth rather than duplication
- no agent needs to consult fragmented legacy docs to understand system state

## Change Log

