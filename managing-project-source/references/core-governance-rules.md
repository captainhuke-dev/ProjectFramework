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

`FRAMEWORK-001` MUST exist in every Project, MUST remain in semantic slot `00`, and MUST NOT be removed, bypassed, demoted, or replaced by descendant governance. All Project artifacts created after it are governed by and inherit from the Framework. Project Source artifacts inherit directly; implementation/external mutations inherit governance through Project identity, Requirements, Decisions, Actions, Authority, and Framework workflows. Descendants may extend/specialize/add constraints, but cannot weaken or contradict Framework invariants.

Governed Markdown descendants declare `inherits_from: ["FRAMEWORK-001"]`; non-Markdown artifacts inherit through their canonical Registry/Manifest metadata. Missing active Framework makes Project Source `INVALID + NOT_OPERATIONALLY_READY`.

Legacy rename migration: if a Brownfield Project still has `00-Project Source Rule`, treat it as the legacy predecessor of slot `00`. Do not delete it in place. Create a Framework candidate, promote it through governed revision/migration, then archive the predecessor only after active `FRAMEWORK-001` is established.

Agents may propose Framework changes but must not modify `00-Project Source Framework` without explicit user approval. Framework revision preserves stable identity `FRAMEWORK-001`, supersedes/archive the old revision, and never deletes the root. Each Project pins its approved Framework version; upgrades require governed migration.

## 2. Standard Location and Semantic Namespace

All Projects use:

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

Framework `1.2.0` standardizes these extended anchors:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension unless governed otherwise later
```

`40`, `60`, and `91` do not join the mandatory `00–17` bootstrap set. They are materialized only when applicable.

Framework distribution artifacts exist outside the Project Source semantic namespace:

```text
managing-project-source/FRAMEWORK-RELEASE.yaml
managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md
managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
```

`FRAMEWORK-RELEASE.yaml` is distribution metadata, not Root Governance or a semantic slot. Platform instruction files are bootstrap/continuation launchers. Their shared governance contract MUST remain byte-identical and MUST NOT replace, weaken, bypass, or override active local `FRAMEWORK-001`.

### 2.1 Concept-First Framework Boundary

ProjectFramework is a **conceptual Project governance and planning framework first**. It defines governance semantics, namespace, technical/installation blueprints, management controls, integrity expectations, bootstrap, authority, migration, handoff, readiness, pressure scenarios, mockups, and examples.

A technical or integrity requirement does not implicitly authorize executable implementation. Unless the user explicitly requests a separate implementation scope, do not create application code, Dockerfile, Compose/Kubernetes/Helm runtime artifacts, installer scripts, validator, CLI, CI/CD, migration engine, scheduler, background automation, dashboard, or runtime enforcement merely because a rule can be checked or implemented mechanically.

A real Project's current Project Source may document concrete verified commands, paths, ports, configuration keys, or operating procedures when those are actual Project truth. ProjectFramework itself does not invent executable commands for nonexistent software.

## 3. Naming and Revision

Governed Project Source documents, Handoff, evidence/schema artifacts, exports, and packages created as Project Source artifacts end with:

```text
-YYMMDD-HHMM
```

Use Project/user local timezone unless Project-Specific Rules say otherwise. Document revisions use monotonic `r001`, `r002`, ... and never reuse a revision number.

Examples:

```text
05-Requirements-r007-260813-2237.md
40-Technical Design-r002-260820-1145.md
91-Project Management Control-r003-260820-1145.md
```

Canonical implementation filenames such as `README.md`, `main.py`, `docker-compose.yml`, and `SKILL.md` remain canonical when their ecosystem requires it.

## 4. Identity

Every Project has:

- `project_uuid` — immutable authoritative identity.
- `project_id` — stable human-readable identity.
- `project_name` — mutable display name.

Rename does not change `project_uuid`.

Merge semantics:

- **Absorption:** primary Project keeps UUID; absorbed Project retains its UUID historically and becomes `ABSORBED`.
- **True Merge:** create a new UUID; predecessors remain in lineage.

Split semantics:

- **Carve-out:** original keeps UUID; carved-out Project gets a new UUID.
- **True Split:** original lifecycle ends; descendants get new UUIDs.

Identity changes are event-based and reconstructable.

## 5. Current State vs History

`03-Current State` is a pure snapshot of now. Historical events belong in `10-Change Log` and archived revisions.

Project state has two axes:

```text
Lifecycle: DRAFT ACTIVE COMPLETED CANCELLED ARCHIVED ABSORBED MERGED SPLIT
Execution: READY IN_PROGRESS WAITING BLOCKED IDLE
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
RISK-*      → 91-Project Management Control
ASM-*       → 91-Project Management Control
MS-*        → 91-Project Management Control
OUT-*       → 91-Project Management Control
DEP-*       → 91-Project Management Control
CR-*        → 91-Project Management Control
GATE-*      → 91-Project Management Control
```

One object type has one authoritative home. Other documents reference Stable IDs; they do not duplicate authoritative state. Detail documents may exist for large objects, but canonical status/identity stays in the canonical home.

### 6.1 Materialized Current State and Stable-ID Resolution

Active canonical object homes are **materialized current projections, not delta chains**. For every Stable ID that is active/current and referenced from Active/Current Project Source:

- current authoritative record MUST resolve within the **Current Reconstructable Snapshot**;
- record MUST contain sufficient current semantic payload to determine what is true now, or link to an active/current canonical Detail Document containing that payload;
- archived revisions MAY explain historical rationale/evolution, but MUST NOT be required to resolve Current Truth;
- `retain previous status`, `unchanged from rNNN`, `see archived revision`, or equivalent delta-only shorthand MUST NOT substitute for authoritative current payload;
- any active Detail Document required to interpret a current Stable ID is part of Current Reconstructable Snapshot and must be included in `CURRENT` export scope when needed.

This applies to `DEC-*`, `REQ-*`, and Framework `1.2.0` management-control objects in `91` equally. Failure to resolve a referenced current Stable ID without archive traversal is an integrity/readiness defect for the affected scope.

Stable IDs and revision numbers are never recycled.

### 6.2 Risk, Assumption, Milestone, Outcome, Dependency, Change, Gate

#### Risk vs Issue

`RISK-*` is a material uncertain future event/condition. `ISS-*` is a materialized/current problem. Risk materialization preserves `RISK-*` and links the resulting `ISS-*`; do not delete or rewrite the Risk into an Issue.

Risk statuses may include:

```text
IDENTIFIED OPEN MITIGATING MONITORING ACCEPTED MATERIALIZED CLOSED SUPERSEDED
```

`ACCEPTED` means remaining exposure is intentionally accepted. Material acceptance records the relevant decision/authority and review trigger where continued monitoring is needed.

Minimum Risk semantics include Risk Statement, Probability, Impact, Trigger/Early Warning, Mitigation, Contingency, Owner, Review Trigger/Review By, Status, related Stable IDs/evidence, and Materialized Issue when applicable.

#### Assumption

`ASM-*` is a proposition currently relied upon without sufficient verification to treat it as established truth.

```text
UNVERIFIED → VALIDATED / INVALIDATED / SUPERSEDED
```

Invalidation triggers impact assessment. Depending on affected truth, this may require `DRIFT-*`, `CR-*`, re-planning, Decision revalidation, Requirement revision, Risk update, or Issue creation. A validated assumption becomes verified truth only when an appropriate authoritative source/evidence supports promotion.

#### Action vs Milestone vs Outcome

```text
ACT-* = work/action
MS-*  = significant checkpoint/state
OUT-* = intended result/benefit/effect

ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED
```

Milestone and Outcome must be evaluated independently against their own criteria/evidence.

#### Dependency

`DEP-*` may represent `PERSON / TEAM / APPROVAL / DECISION / VENDOR / SYSTEM / API / DATA / CONTRACT / PROJECT / INFRASTRUCTURE / OTHER`.

`AVAILABLE` means the dependency is currently obtainable; `SATISFIED` means the governed dependency requirement has been fulfilled. A dependency failure may trigger a Risk, Issue, Change Request, or Health degradation based on impact.

#### Change Request vs Change Log

```text
CR-*  = proposed/material change + impact assessment + decision path
CHG-* = historical record of applied/observed change
```

A Change Request considers affected scope, Requirements, Decisions, Architecture, Tech Stack, source structure, configuration, installation/deployment modes, data/migration, security/authority, Milestones/Outcomes, Risks, Dependencies, schedule/effort, operations, and handoff when applicable. Approval authorizes only the governed scope; it does not grant unrelated implementation authority.

#### Review / Phase Gate

`GATE-*` is a governed checkpoint with Purpose, Affected Scope, Entry Criteria, Pass Criteria, Required Evidence, Review Owner, Required Authority, Status, Findings, Exceptions/Waiver, Next Action, and Reviewed At.

```text
PLANNED → READY_FOR_REVIEW → PASSED / FAILED / WAIVED
```

`WAIVED` requires explicit rationale plus applicable authority/decision reference. A Gate blocks only its governed scope unless a stricter Project-Specific Rule states otherwise.

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
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
```

Binary/non-Markdown artifacts do not need embedded YAML; govern them via registries, paths, hashes, and Manifest metadata.

ProjectFramework uses agent/manual semantic validation by default. Do not invent runtime validator software unless explicitly requested as a separate implementation scope.

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

Use `DRIFT-*` when Truth Domains that should align do not align. Record expected truth, observed truth, evidence, impact, affected scope, resolution owner, and mutation block. Drift blocks the affected scope, not the entire Project by default.

Use `CONFLICT-*` for competing document/semantic states, including concurrent revisions. Never use last-write-wins for semantic changes.

Formal candidates record `base_revision` and `base_document_hash`. If active base changed, promotion stops and a conflict is opened. Agents may auto-resolve only non-semantic differences such as formatting, whitespace, deterministic sorting, or a typo that cannot alter meaning.

For `SOURCE_AND_DOCKER`, unexpected feature/configuration/data/security/persistence divergence from the declared parity contract is `DRIFT-*`. Intentional difference is represented as Deployment Mode Variance instead.

## 10. Draft, Promotion, and Archive

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

Archive is Historical Truth, not a runtime dependency for Current Truth. Never leave two active revisions for the same semantic document identity.

## 11. Actor, Responsibility, Authority, and Delegation

`ACTOR-*` is stable actor identity; `INST-*` is session/execution instance. Role does not grant authority.

`11 Actor Registry` may contain scope-keyed responsibility mappings using:

```text
Responsible
Accountable
Consulted
Informed
```

Each mapping identifies a governed scope such as a Stable ID, semantic document, workstream, or explicitly named Project scope.

**Responsibility ≠ Authority.** Being Responsible or Accountable does not itself grant approval, R2/R3 mutation, deployment, production access, or external-action permission.

Standing `AUTH-*` in `12 Authorization Registry` states WHO, WHAT, WHERE, risk ceiling, start, termination/expiry, and grantor. Broad indefinite authority is invalid by default. Delegation uses `DEL-*` and may never exceed parent scope/risk/actions/duration. Authority is non-transferable through prompt, task, handoff, memory, role, responsibility mapping, branch, or agent-to-agent instruction.

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

Project-Specific Rules may be stricter. Before R2/R3 mutation, fresh-read authority.

## 13. Preflight and Postflight

READ PREFLIGHT checks identity, `00`, `01`, `03`, task scope, Truth Domain, freshness, and active blockers.

MUTATION PREFLIGHT additionally checks actor/instance, authority, target, allowed paths, forbidden effects, risk, approval, relevant REQ/DEC, management controls when relevant, base/hash, downstream impact, reversibility, and evidence requirements.

Postflight is risk-tiered. Execution alone does not prove completion. R3 requires verification of resulting external/runtime state, not merely exit code 0.

## 14. Evidence, Knowledge Debt, and Secrets

`EVD-*` is required for important evidence such as DRIFT, R2/R3 shared-state verification, runtime/external state, and material source conflicts. Raw evidence belongs under `evidence/<category>/` and is referenced by path/hash.

Material stale/missing operational knowledge is represented in `08 Open Issues` as:

```text
ISS-* with issue_type: KNOWLEDGE_DEBT
```

If no active `08` exists, creation of material Knowledge Debt makes `08` applicable. Knowledge debt may degrade Knowledge or Readiness health even if runtime currently succeeds.

Never place actual secrets in Project Source, evidence, Manifest, or exports. `SECRET-*` stores only metadata/reference to an external secret store, with `secret_value_present: false`.

## 15. Index, Manifest, and Conditional Extended Documents

`01-Project Source Index` is the Front Door. It contains a derived active document registry plus human/agent routing guidance. The generated registry is not manually authoritative.

When active, route:

```text
40 → Tech Stack / technical design / source/config/runtime blueprint
60 → installation / deployment / operations blueprint
91 → RISK / ASM / MS / OUT / DEP / CR / GATE
```

`14-Manifest` covers the Current Reconstructable Snapshot: active docs, continuation-relevant formal drafts, registered evidence, validation assets, necessary generated assets, and every active/current Detail Document required to interpret referenced current Stable IDs. If active `40`, `60`, or `91` is required to interpret current truth, it belongs in the Manifest and `CURRENT` export scope.

When Framework Source Provenance is tracked, `14` preserves the same observed state as active `00`. Missing optional exact Git provenance is not itself a Manifest defect; fabricated provenance is prohibited.

Manifest integrity mismatch requires root-cause classification; do not blindly regenerate to hide unexpected change.

## 16. Handoff

`09-Handoff` is the current continuation contract, not merely a chat summary.

```text
DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED
```

It records from/to, previous handoff, trigger, current phase/state, completed work, pending work, formal drafts/WIP, active objects, read order, freshness warnings, authority references, `authority_transfer: false`, and exact next action.

When applicable, surface continuation-critical `RISK-*`, invalid/unverified `ASM-*`, blocking `DEP-*`, upcoming/recent `MS-*`, Outcomes awaiting measurement, open/approved `CR-*`, upcoming/failed `GATE-*`, Technical/Deployment health warnings, Source/Docker variance, and Knowledge Debt.

Before `ACCEPTED`, recipient reads `00 → 01 → 03 → 09`, checks actor/authority, relevant active objects, volatile state, and current handoff revision.

### 16.1 Externalized Working Memory and Chat Lifecycle

**Externalized Working Memory** is the minimum durable continuation state maintained outside Chat in source-native Project storage. Chat remains a temporary interaction/execution surface; connector/MCP use does not make Chat persistent Project memory.

Canonical terms:

- **Material Project Work** — any connector-derived result or change needed for reliable continuation, governance, decision-making, or execution.
- **Transient MCP Activity** — reads, searches, comparisons, or intermediate connector detail that is discarded or not needed for later continuation.
- **Logical Checkpoint** — the coherent point after related connector activity where the current usable result can be persisted once without per-tool-call logging.
- **PERSISTED** — required durable continuation state has been successfully written to its source-native owner or approved continuation cache.
- **PERSISTENCE_PENDING** — required durable continuation state has not been successfully written; continuation safety must not be claimed.
- **CONTINUE_CURRENT_CHAT** / **START_NEW_CHAT** — the only Chat lifecycle recommendation vocabulary.

Binding behavior:

1. Material Project Work MUST be persisted at a Logical Checkpoint; Transient MCP Activity has no persistence requirement by default.
2. GitHub-backed Material Project Work persists to the repository artifact or canonical Project Source semantic home that owns the state.
3. Google Drive Material Project Work updates the existing designated Project progress `.md` when one exists. If none exists and durable continuation state is required, use one stable `PROJECT-PROGRESS.md` as a continuation cache, not as a new authoritative source.
4. Cross-system GitHub/Drive state uses references/pointers. Do not create a third duplicate source of truth.
5. Do not persist raw MCP/tool payloads, long search-result dumps, full diffs, repetitive intermediate state, or private intermediate reasoning merely for audit convenience. Include such detail only when explicitly requested or necessary for approval or ambiguity resolution.
6. `09-Handoff` remains a continuation contract, not an MCP transcript or execution log.
7. If required persistence fails, classify the state as `PERSISTENCE_PENDING`, disclose what remains unpersisted, and default to `CONTINUE_CURRENT_CHAT`.
8. `START_NEW_CHAT` is continuation-safe only after the durable state outside Chat includes current state, blocker/pending state, Exact Next Action, and Required Read location.
9. A new chat/session MUST be able to continue from persisted current state and Required Read pointers without the old chat transcript as a prerequisite.
10. A successful connector call alone is not a Logical Checkpoint and MUST NOT trigger one progress write per tool call.
11. Existing initialized Projects remain governed by their local pinned Framework and never auto-upgrade merely because upstream ProjectFramework changes.

## 17. Adoption Modes and Bootstrap

### GREENFIELD

If environment is a ChatGPT Project or Claude Project, begin with the matching canonical platform Project instruction artifact. If no valid local Project Source exists, bootstrap from canonical repository `main` using:

```text
README.md
→ FRAMEWORK-RELEASE.yaml
→ SKILL.md
→ latest amendment
→ Core Governance
→ Framework template
→ skeletons
→ mockup
```

Then Discover → identity → adaptive interview → Preview → user approval → create governance layer → validate → readiness → completion report.

Create mandatory `00–05` and `09–17`; evaluate conditional `06–08`, `40`, `60`, and `91` by applicability. Keep `18–19` reserved. Do not create empty conditional files merely to look complete.

Exact Git tag/SHA provenance is optional assurance. If observed, record accurately; if unavailable, do not fabricate it and do not block otherwise valid bootstrap solely for that reason. If canonical Framework source itself is inaccessible, stop affected governance mutation instead of reconstructing Framework rules from memory.

### BROWNFIELD

Preserve first. Inventory and classify legacy sources by Truth Domain, Epistemic Status, Freshness, and evidence. Do not move/rename/delete legacy sources automatically. Build governance layer and normalize only approved scope.

### IMPORT

Place imported Project Source in `import-staging/` first. Assess identity, versions, compatibility, Manifest, hashes, mandatory docs, lineage, IDs, secret leakage, references, and active-revision ambiguity. Results: `COMPATIBLE`, `UPGRADE_REQUIRED`, `CONFLICTED`, `INVALID`.

## 18. Migration and Versioning

Each Project pins Framework/Schema version and compatibility range. Never auto-upgrade old Projects.

Managed migration uses `MIG-*` and covers source, target, compatibility assessment, affected documents/objects, steps, rollback, approval, validation, and evidence. Project-Specific Rules are preserved unless explicitly resolved otherwise.

### 18.1 Framework 1.2.0 Slot-91 Migration Safety

Framework releases before `1.2.0` allowed `90–99` as Project-specific/Governance Extension space. A Brownfield Project may already use slot `91` for a custom document.

Migration MUST NOT overwrite it. Required flow:

```text
detect occupied 91
→ open MIG-* compatibility assessment
→ preserve custom document identity/history/references
→ propose suitable free 92–99 or other semantically correct location
→ obtain explicit approval
→ migrate/promote/archive through governed flow
→ only then activate standard 91 if applicable
```

Existing Projects that do not migrate remain unaffected.

### 18.2 No Automatic Free-Text Promotion

Existing prose mentioning risks, assumptions, dates, dependencies, scope changes, outcomes, or gates MUST NOT be automatically reinterpreted as new `RISK-*`, `ASM-*`, `MS-*`, `OUT-*`, `DEP-*`, `CR-*`, or `GATE-*` identities.

Promotion requires enough current semantics, status, ownership, and epistemic/evidence state to avoid fabrication. If identity/current truth cannot be established, preserve prose as historical/current context with explicit uncertainty rather than inventing a Stable ID.

### 18.3 Framework Operational Use and Optional Release Assurance

Treat Framework state as independent dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

A Framework MAY be operationally usable while exact Git provenance is `UNKNOWN/UNVERIFIED` or repository hardening is absent. These optional assurance states MUST NOT become blockers unless Project-Specific Rules explicitly require them.

When exact source provenance is actually observed, a Project may record:

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "<OBSERVED_REF_OR_MAIN>"
  release_tag: "<OPTIONAL_OBSERVED_TAG_OR_NONE>"
  resolved_commit_sha: "<OPTIONAL_OBSERVED_SHA_OR_UNKNOWN>"
  framework_version: "1.2.0"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
  provenance_status: "<VERIFIED | PARTIAL | UNVERIFIED>"
```

Exact tag/SHA values come only from actual observation; never predict, fabricate, or retroactively backfill them.

## 19. Project Health and Review Cadence

Project Health is a **derived current assessment** in `03 Current State`, not a replacement for canonical records.

Standard dimensions:

```text
Scope
Progress / Schedule
Risk
Quality / Validation
Dependencies
Authority
Knowledge
Readiness
Technical / Deployment when applicable
```

States:

```text
GREEN AMBER RED UNKNOWN
```

Omit a non-applicable optional dimension rather than marking it `GREEN`. Each applicable dimension records/resolves:

```text
State
Reason
Supporting Stable IDs / Evidence
Owner
Last Reviewed
Next Review / Trigger when applicable
```

Framework defines no opaque automatic weighted health score. A Project-specific aggregate label may exist only if derivation/limitations are explicit and it does not replace dimensional view.

Review Cadence supports:

```text
TIME_BASED
EVENT_BASED
```

It may govern Current State Review, Risk Review, Assumption Review, Milestone/Outcome Review, Decision Revalidation, Technical Design Review, Deployment Readiness Review, and Handoff Refresh. ProjectFramework defines semantics only and does not create a scheduler/reminder runtime.

## 20. Decision Revalidation

`DEC-*` remains canonical in `04 Decision Log`. Current Decisions may record:

```text
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
```

Recommended statuses:

```text
NOT_DUE REVIEW_DUE REVALIDATED SUPERSEDED
```

Typical triggers include invalidated `ASM-*`, materially changed `DEP-*`, Requirement change, Tech Stack change, deployment-mode change, material approved `CR-*`, regulation/vendor-contract change, review date, or runtime evidence contradicting Decision basis.

A previously approved Decision is not assumed valid forever when its stated basis no longer holds.

## 21. Technical Design and Deployment Blueprint

### 21.1 `06 Architecture` vs `40 Technical Design`

`06 Architecture` remains the conditional major architecture view: major systems/components/interfaces, boundaries, data flow, constraints, and key architecture Decisions.

`40 Technical Design` is the deeper implementation-facing **blueprint** when meaningful software/technical detail exists. It deepens/references `06`; it must not fork the same authoritative payload.

A material Tech Stack entry records:

```text
Technology
Role / Responsibility
Version or Supported Range
Required / Optional
Why Used / Decision Reference
Used By Component(s)
Operational Dependency
Lifecycle / Support Constraint when material
Replacement Boundary when material
Epistemic / Verification State
```

`40` may also document Component Responsibility, Inputs/Outputs, Interfaces, Dependencies, Data/Storage interaction, Security/Authority boundaries, Runtime boundaries, source-structure responsibilities, Configuration Contract, and Runtime Requirements.

Configuration semantics are independent from packaging mode and may include Application Settings, Environment-specific Settings, External Service Endpoints, Persistence Settings, Feature/Capability Settings, and Secret References. Actual secret values remain forbidden.

### 21.2 Deployment Support Model

A software Project declares one of:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

For `SOURCE_AND_DOCKER`, Source and Docker share one declared contract for:

```text
core application semantics
configuration meaning
required external dependencies
data compatibility
security assumptions
supported capability set
persistence semantics
upgrade compatibility
```

Packaging/runtime mechanics may differ. Intentional differences use **Deployment Mode Variance** with Affected Capability, Source Behavior, Docker Behavior, Reason, Impact, related Stable IDs, Owner, and Acceptance/Resolution State. Unexpected mismatch is `DRIFT-*`.

### 21.3 `07 Implementation Plan` vs `60 Deployment Plan`

`07 Implementation Plan` answers what work/actions are planned, sequence, dependencies, risks, verification, and rollback/reversibility.

`60 Deployment Plan` answers how the resulting system is installed, configured, started, stopped, verified, diagnosed, upgraded, rolled back, backed up/restored, cleaned up, and troubleshot in each supported deployment mode.

When applicable, `60` addresses:

```text
Prerequisites
Supported OS / Platform / Architecture
Source or Artifact Acquisition
Required Runtime / Container Runtime
External Services
Required Permissions
Configuration Inputs
Secret Requirements / SECRET-* references
Data / Storage Initialization
Installation / Initialization Procedure
Start / Stop Procedure
Verification / Health Check
Logs / Diagnostics
Upgrade
Rollback
Backup / Restore
Uninstall / Cleanup
Troubleshooting
Known Limitations / Deployment Mode Variance
```

Installation is not operationally ready merely because an install/start command returns success. Verification may include service availability, dependency reachability, storage initialization/persistence, configuration loading, secret resolution without exposure, health/runtime signal, core flow usability, running version identity, and Source/Docker parity when applicable.

## 22. Framework Integrity Contract

Current Framework distribution integrity means at minimum:

- current Framework/Schema declarations are internally consistent;
- `00–17` meanings remain intact;
- `06–08` remain conditional;
- `18–19` remain reserved;
- `40`, `60`, and `91` remain conditional/applicability-driven;
- `91` is standard Project Management Control in `1.2.0+` and `92–99` remain extension space unless governed otherwise;
- canonical object homes remain consistent across Framework, Core Governance, skeletons, mockup, platform launchers, and examples;
- ChatGPT and Claude shared governance contracts remain byte-identical;
- current Stable IDs resolve without archive dependency;
- existing Projects do not silently auto-upgrade;
- actual secrets remain forbidden;
- technical planning does not silently expand into implementation artifacts;
- missing facts, authority, source, provenance, or management-object identity are never fabricated.

These are semantic requirements and may be reviewed manually or by an Agent. They do not require executable enforcement tooling.

## 23. Export Profiles

```text
CURRENT — active continuation snapshot; includes current canonical records and required active/current Detail Documents without archive dependency
AUDIT   — current + relevant history/evidence
FULL    — complete Project-Source including archive, excluding actual secrets
```

Package name:

```text
<Project-ID>-Project-Source-<PROFILE>-YYMMDD-HHMM.zip
```

If active `40`, `60`, or `91` is needed to interpret current truth, it belongs in `CURRENT`. A `CURRENT` export is incomplete if omitted archive content is required to determine current semantics.

## 24. Retention and Readiness

Preserve Project Source revisions, Decisions, Requirements, Change Log, management-control history, and Identity lineage indefinitely by default. Evidence follows Project-Specific retention. Purge requires authorization, no active references, auditability, and retained reconstructability.

A Project Source may be `VALID + NOT_OPERATIONALLY_READY` when uncertainty is explicit. It is `OPERATIONALLY_READY` only when a new actor can determine current truth, current authority, active blockers, and exact next action without guessing.

Optional immutable-tag/SHA provenance or repository protection does not change readiness automatically unless Project-Specific Rules make it a requirement.

## 25. Interview Policy

Modes:

```text
FAST GRILL ADAPTIVE
```

Default = `ADAPTIVE`.

```text
Can verify?              → VERIFY
Can safely derive?       → INFERRED
Non-critical unknown?    → RECORD UNKNOWN
Semantic decision?       → ASK USER
Authority required?      → RESOLVE / ASK
Dangerous ambiguity?     → BLOCK AFFECTED SCOPE
```

Do not ask for information available from accessible Project sources. Do not fabricate information to reduce questions.

## 26. Initial Creation / Structural Migration Gate

Before first creation or major structural migration, show a preview containing at least Adoption Mode, Project Identity, files/directories to create, conditional files, known Decisions, known Assumptions, Unknowns, expected readiness, expected risk, and migration impact. Obtain explicit user approval before writing.

## 27. Completion Report

After Create, Migrate, Import, Major Update, Handoff, or Export, report human-readable and machine-readable results. Include Project identity, operation, adoption mode, versions, validation/readiness, created/revised/archived docs, active ACT/ISS/DRIFT/CONFLICT and relevant management controls, authority state, unknown/stale/verification-required items, export artifact if any, and exact next action.

Canonical completion states:

```text
COMPLETE PARTIAL BLOCKED FAILED
```

Do not claim `DONE`, `DEPLOYED`, `PUSHED`, `MIGRATED`, or `VALID` unless verification appropriate to the risk has passed.
