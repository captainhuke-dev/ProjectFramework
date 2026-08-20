# Core Governance Rules — Project Source

This reference is the operational contract used by the `managing-project-source` skill. Human-readable content is Thai-first; canonical machine vocabulary remains English.

## 1. Binding Governance

`00-Project Source Framework` is the non-removable root governance document. It contains:

1. **Framework Core** — root invariants shared across projects.
2. **Project-Specific Rules** — descendant constraints that inherit from the Framework and may only specialize it without weakening it.

Root inheritance and authority:

```text
0. User Explicit Instruction / Approval (external authority to revise governance)
1. 00-Project Source Framework (FRAMEWORK-001; root inside Project Source)
2. Framework-compliant Project-Specific Rules
3. Canonical Project Source documents / Decisions / Requirements
4. Task / Handoff / Prompt / Agent Instruction
```

`FRAMEWORK-001` MUST exist in every Project, MUST remain in semantic slot `00`, and MUST NOT be removed, bypassed, demoted, or replaced by descendant governance. All Project artifacts created after it are governed by and inherit from the Framework. Project Source artifacts inherit directly; implementation/external mutations inherit governance through Project identity, Requirements, Decisions, Actions, Authority, and the Framework workflows. Descendants may extend/specialize/add constraints, but cannot weaken or contradict Framework invariants.

Governed Markdown descendants declare `inherits_from: ["FRAMEWORK-001"]`; non-Markdown artifacts inherit through their canonical Registry/Manifest metadata. Missing active Framework makes Project Source `INVALID + NOT_OPERATIONALLY_READY`.


Legacy rename migration: if a Brownfield Project still has `00-Project Source Rule`, treat it as the legacy predecessor of slot `00`. Do not delete it in place. Create a Framework candidate, promote it through governed revision/migration, then archive the predecessor only after active `FRAMEWORK-001` is established.

Agents may propose Framework changes but must not modify `00-Project Source Framework` without explicit user approval. Framework revision preserves stable identity `FRAMEWORK-001`, supersedes/archive the old revision, and never deletes the root. Each project pins its approved Framework version; upgrades require a governed migration.

## 2. Standard Location and Core Files

All projects use:

```text
<Project-Root>/Project-Source/
```

Core namespace:

```text
00 Project Source Framework     MANDATORY / NON-REMOVABLE ROOT
01 Project Source Index         MANDATORY
02 Project Overview             MANDATORY
03 Current State                MANDATORY
04 Decision Log                 MANDATORY
05 Requirements                 MANDATORY
06 Architecture                 CONDITIONAL
07 Implementation Plan          CONDITIONAL
08 Open Issues                  CONDITIONAL
09 Handoff                      MANDATORY
10 Change Log                   MANDATORY
11 Actor Registry               MANDATORY
12 Authorization Registry       MANDATORY
13 Evidence Registry            MANDATORY
14 Project Source Manifest      MANDATORY
15 Action Registry              MANDATORY
16 Migration Registry           MANDATORY
17 Secret Reference Registry    MANDATORY
18–19                           RESERVED
```

Conditional files are created only when applicable; do not create empty files merely to look complete.

Extended taxonomy:

```text
20–29 Research / Discovery
30–39 Business / Process / UX Design
40–49 Architecture / Technical / Integration
50–59 Testing / QA / Validation
60–69 Deployment / Operations / Infrastructure
70–79 Data / Migration / Analytics
80–89 Audit / Review / Assessment / Reports
90–99 Project-specific / Governance Extension
```

Reserved anchors: `20 General Research`, `30 Business Flow`, `40 Technical Design`, `50 Test Strategy`, `60 Deployment Plan`, `70 Data Model`, `80 Review Report`, `90 Special Governance Extension`.

## 3. Naming and Revision

Governed Project Source documents, Handoff, evidence/schema artifacts, exports, and packages created as Project Source artifacts end with:

```text
-YYMMDD-HHMM
```

Use project/user local timezone unless Project-Specific Rule says otherwise.

Document revisions use `r001`, `r002`, ... `r999`, `r1000`, ...; numbers are monotonic and never reused.

Core example:

```text
05-Requirements-r007-260813-2237.md
```

Extended example:

```text
22-RSCH-004-GPU-Benchmark-r003-260813-2237.md
```

Canonical implementation filenames such as `README.md`, `main.py`, `docker-compose.yml`, and `SKILL.md` remain canonical when their ecosystem requires it.

## 4. Identity

Every project has:

- `project_uuid` — immutable authoritative identity.
- `project_id` — stable human-readable identity.
- `project_name` — mutable display name.

Rename does not change `project_uuid`.

Merge semantics:

- **Absorption:** primary project keeps UUID; absorbed project retains its UUID historically and becomes `ABSORBED`.
- **True Merge:** create a new UUID; predecessors remain in lineage.

Split semantics:

- **Carve-out:** original keeps UUID; carved-out project gets a new UUID.
- **True Split:** original lifecycle ends; descendants get new UUIDs.

Identity changes are event-based and reconstructable.

## 5. Current State vs History

`03-Current State` is a pure snapshot of now. Historical events belong in `10-Change Log` and archived revisions.

Project state has two axes:

Lifecycle:

```text
DRAFT ACTIVE COMPLETED CANCELLED ARCHIVED ABSORBED MERGED SPLIT
```

Execution:

```text
READY IN_PROGRESS WAITING BLOCKED IDLE
```

Do not collapse them into one status.

## 6. Canonical Object Homes

```text
DEC-*       → 04-Decision Log
REQ-*       → 05-Requirements
ISS-*       → 08-Open Issues
DRIFT-*     → 08-Open Issues
CONFLICT-*  → 08-Open Issues
CHG-*       → 10-Change Log
ACTOR-*     → 11-Actor Registry
INST-*      → 11-Actor Registry
AUTH-*      → 12-Authorization Registry
DEL-*       → 12-Authorization Registry
EVD-*       → 13-Evidence Registry
ACT-*       → 15-Action Registry
MIG-*       → 16-Migration Registry
SECRET-*    → 17-Secret Reference Registry
```

One object type has one authoritative home. Other documents reference Stable IDs; they do not duplicate authoritative state. Detail documents may exist for large objects, but canonical status/identity stays in the registry.

### 6.1 Materialized Current State and Stable-ID Resolution

Active canonical object homes are **materialized current projections, not delta chains**. For every Stable ID that is active/current and referenced from the Active/Current Project Source:

- the current authoritative record MUST resolve within the **Current Reconstructable Snapshot**;
- the record MUST contain sufficient current semantic payload to determine what is true now, or link to an active/current canonical Detail Document containing that payload;
- archived revisions MAY provide historical rationale/evolution, but MUST NOT be required to resolve Current Truth;
- `retain previous status`, `unchanged from rNNN`, `see archived revision`, or equivalent delta-only shorthand MUST NOT substitute for the authoritative current payload;
- any active Detail Document required to interpret a current Stable ID is part of the Current Reconstructable Snapshot and must be included in `CURRENT` export scope when that Stable ID is exported.

This applies generally to current-state-bearing canonical homes. In particular, an active `DEC-*` in `04-Decision Log` must materialize its current Decision/Status semantics (or link to an active/current canonical Detail Document), and an active `REQ-*` in `05-Requirements` must materialize its current Requirement/Status/Acceptance semantics (or link likewise).

**Referential validation rule:** Every Stable ID referenced from the Active/Current snapshot MUST resolve to a current authoritative record within the Current Reconstructable Snapshot without requiring an archived revision. Failure is a Project Source integrity/readiness defect. If an actor cannot determine the affected current truth from the current snapshot, that affected scope is `NOT_OPERATIONALLY_READY`.

Stable IDs and revision numbers are never recycled.

## 7. Metadata

Governed Markdown documents have YAML Front Matter. Typical fields include:

```yaml
project_uuid: "..."
project_id: "..."
project_name: "..."
document_id: "STATE-001"
document_type: "CURRENT_STATE"
semantic_slot: "03"
revision: 1
document_status: "ACTIVE"
created_at: "2026-08-13T22:37:00+07:00"
updated_at: "2026-08-13T22:37:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-..."
epistemic_status: "USER_CONFIRMED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.1.1"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
```

Binary/non-Markdown artifacts do not need embedded YAML; control them via registries, paths, hashes, and manifest metadata.

Phase 1 uses agent/manual validation against this contract. Do not invent runtime validator software unless explicitly requested.

## 8. Truth, Uncertainty, and Freshness

Canonical Truth Domains:

```text
GOVERNANCE INTENT REQUIREMENTS IMPLEMENTATION RUNTIME DATA IDENTITY AUTHORITY HISTORY EXTERNAL
```

Authoritative source varies by domain:

- Governance → active approved `00-Project Source Framework` (`FRAMEWORK-001`).
- Intent → user-approved Project Source.
- Requirements → `05`.
- Implementation → verified source tree/Git.
- Runtime → fresh runtime observation.
- Data → actual authoritative datasource.
- Identity → identity metadata/history.
- Authority → `12`.
- History → `10` + archive.
- External → verified external source/system.

Epistemic Status:

```text
VERIFIED USER_CONFIRMED INFERRED ASSUMED UNKNOWN CONFLICTED STALE
```

Freshness:

```text
IMMUTABLE STABLE CHANGEABLE VOLATILE
```

Never promote `ASSUMED` or `INFERRED` to `VERIFIED` without evidence/authoritative verification. `VOLATILE` information must be fresh-checked before it materially drives a decision or mutation.

## 9. DRIFT and CONFLICT

Use `DRIFT-*` when Truth Domains that should align do not align. Record expected truth, observed truth, evidence, impact, affected scope, resolution owner, and mutation block. Drift blocks the affected scope, not the entire project by default.

Use `CONFLICT-*` for competing document/semantic states, including concurrent revisions. Never use last-write-wins for semantic changes.

Formal candidates record `base_revision` and `base_document_hash`. If the active base changed, promotion stops and a conflict is opened.

Agents may auto-resolve only non-semantic differences such as formatting, whitespace, deterministic sorting, or a typo that cannot alter meaning. Semantic conflicts go to the user or authorized decision owner.

## 10. Draft, Promotion, and Archive

Filesystem roles:

```text
Scratch                 → outside Project-Source/
Formal candidate        → Project-Source/drafts/
Active truth            → Project-Source root
Historical revision     → Project-Source/archive/
```

Promotion is controlled:

```text
candidate → validate → base/hash check → promote new active → mark old superseded → archive old → update Index/Change Log/Manifest → postflight
```

Archive structure preserves taxonomy plus `YYYY/MM`. Archive is **Historical Truth**, not a runtime dependency for Current Truth; archive traversal must never be required to resolve a current authoritative Stable ID.

Never leave two active revisions for the same semantic document identity.

## 11. Actor, Authority, and Delegation

`ACTOR-*` is stable actor identity; `INST-*` is session/execution instance. Role does not grant authority.

Standing `AUTH-*` must state WHO, WHAT, WHERE, risk ceiling, start, termination/expiry, and grantor. Broad indefinite authority is invalid by default.

Authority is non-transferable through prompt, task, handoff, memory, role, branch, or agent-to-agent instruction.

Delegation requires `DEL-*` and may never exceed parent scope, risk, actions, or duration. Invalid/revoked parent authority invalidates descendants immediately.

## 12. Risk and Approval

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

Default approval:

- R0: none.
- R1: permitted inside approved scope.
- R2: explicit approval or valid Standing Authorization.
- R3: explicit approval for that specific action by default.

Project-Specific Rules may be stricter.

Before R2/R3 mutation, fresh-read authority.

## 13. Preflight and Postflight

READ PREFLIGHT checks identity, `00`, `01`, `03`, task scope, Truth Domain, freshness, and active blockers.

MUTATION PREFLIGHT additionally checks actor/instance, authority, target, allowed paths, forbidden effects, risk, approval, relevant REQ/DEC, active blocks, base/hash, downstream impact, reversibility, and evidence requirements.

Postflight is risk-tiered. Execution alone does not prove completion. R3 requires verification of resulting external/runtime state, not merely exit code 0.

## 14. Evidence and Secrets

`EVD-*` is required for important evidence such as DRIFT, R2/R3 shared-state verification, runtime/external state, and material source conflicts. Raw evidence belongs under `evidence/<category>/` and is referenced by path/hash.

Never place actual secrets in Project Source, evidence, manifest, or exports. `SECRET-*` stores only metadata/reference to an external secret store, with `secret_value_present: false`.

## 15. Index and Manifest

`01-Project Source Index` is the Front Door. It contains:

- a machine-derived active document registry, and
- human/agent routing guidance.

The generated registry is not manually authoritative.

`14-Manifest` covers the Current Reconstructable Snapshot: active docs, continuation-relevant formal drafts, registered evidence, schema/validation snapshots, necessary generated assets, and every active/current Detail Document required to interpret a referenced current Stable ID. It does not include the entire archive by default, and the snapshot MUST NOT depend on omitted archived revisions to determine Current Truth.

Manifest integrity mismatch requires root-cause classification; do not blindly regenerate to hide unexpected change.

## 16. Handoff

`09-Handoff` is the current continuation contract, not merely a chat summary.

Lifecycle:

```text
DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED
```

It records from/to, previous handoff, trigger, current phase/state, completed work, pending work, formal drafts/WIP, active objects, read order, freshness warnings, authority references, `authority_transfer: false`, and exact next action.

Before `ACCEPTED`, recipient reads `00 → 01 → 03 → 09`, checks actor/authority, relevant active objects, volatile state, and current handoff revision.

Refresh handoff when user requests it or continuation state materially changes.

## 17. Adoption Modes

### GREENFIELD

Discover → identity → adaptive interview → preview → user approval → create governance layer → validate → readiness → completion report.

### BROWNFIELD

Preserve first. Inventory and classify legacy sources by Truth Domain, Epistemic Status, Freshness, and evidence. Do not move/rename/delete legacy sources automatically. Build a governance layer and normalize only approved scope.

### IMPORT

Place imported Project Source in `import-staging/` first. Assess identity, versions, compatibility, manifest, hashes, mandatory docs, lineage, IDs, secret leakage, references, and active-revision ambiguity. Results: `COMPATIBLE`, `UPGRADE_REQUIRED`, `CONFLICTED`, `INVALID`.

## 18. Migration and Versioning

Each Project pins Framework/Schema version and compatibility range. Never auto-upgrade old projects.

Managed migration uses `MIG-*` and covers source, target, compatibility assessment, affected documents/objects, steps, rollback, approval, validation, and evidence. Project-Specific Rules are preserved unless explicitly resolved otherwise.

## 19. Export Profiles

```text
CURRENT — active continuation snapshot; includes every current canonical record and active/current Detail Document required to interpret exported current Stable IDs, without archive dependency
AUDIT   — current + relevant history/evidence
FULL    — complete Project-Source including archive, excluding actual secrets
```

Package name:

```text
<Project-ID>-Project-Source-<PROFILE>-YYMMDD-HHMM.zip
```

Validate structure, references, semantic state, index/manifest, secret policy, active truth uniqueness, profile completeness, and archive-independent current Stable-ID resolution before standard export. A `CURRENT` export is incomplete if omitted archive content is required to determine current semantics.

## 20. Retention and Readiness

Preserve Project Source revisions, Decisions, Requirements, Change Log, and Identity lineage indefinitely by default. Evidence follows Project-Specific retention. Purge requires authorization, no active references, auditability, and retained reconstructability.

A Project Source may be `VALID + NOT_OPERATIONALLY_READY` when uncertainty is explicit. It is `OPERATIONALLY_READY` only when a new actor can determine current truth, current authority, active blockers, and exact next action without guessing.

## 21. Interview Policy

Modes:

```text
FAST GRILL ADAPTIVE
```

Default = `ADAPTIVE`.

Decision rule:

```text
Can verify?              → VERIFY
Can safely derive?       → INFERRED
Non-critical unknown?    → RECORD UNKNOWN
Semantic decision?       → ASK USER
Authority required?      → RESOLVE / ASK
Dangerous ambiguity?     → BLOCK AFFECTED SCOPE
```

Do not ask for information available from accessible project sources. Do not fabricate information to reduce questions.

## 22. Initial Creation Gate

Before first creation or major structural migration, show a preview containing at least:

- Adoption Mode
- Project Identity
- files/directories to create
- Conditional files
- known Decisions
- known Assumptions
- Unknowns
- expected readiness
- expected risk
- migration impact

Obtain explicit user approval before writing.

## 23. Completion Report

After Create, Migrate, Import, Major Update, Handoff, or Export, report both human-readable and machine-readable results.

Include at least project identity, operation, adoption mode, versions, validation/readiness, created/revised/archived docs, active ACT/ISS/DRIFT/CONFLICT, authority state, unknown/stale/verification-required items, export artifact if any, and exact next action.

Canonical completion states:

```text
COMPLETE PARTIAL BLOCKED FAILED
```

Do not claim `DONE`, `DEPLOYED`, `PUSHED`, `MIGRATED`, or `VALID` unless verification appropriate to the risk has passed.
