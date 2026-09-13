# ProjectFramework Structured Core + Generated Governance Roadmap

Date: `2026-09-13` (Asia/Bangkok)
Document type: `PLANNING_PROPOSAL / FUTURE_ARCHITECTURE_ROADMAP`
Task allocation: `NOT_ALLOCATED`
Stable-ID allocation: `NOT_ALLOCATED`
Implementation state: `NOT_STARTED`
Recommended sequencing: `ONLY_AFTER_TRANSACTION_MODE_IS_IMPLEMENTED_AND_MEASURED`

## 1. Purpose

Define a future ProjectFramework architecture in which the smallest possible structured canonical core owns machine-relevant Project truth and Markdown governance documents become deterministic generated projections where appropriate.

The objective is to preserve ProjectFramework auditability, human readability, authority boundaries, history, Stable IDs, evidence, and reconstructability while eliminating large classes of manual synchronization work across Index, Current State, Handoff, registries, Manifest, and repeated metadata propagation.

This roadmap is **Option 3**. It is intentionally more invasive than Transaction Mode and SHOULD NOT be the immediate fix for current governance latency.

## 2. Why This Exists

The current Project Source model uses human-readable Markdown documents as both:

1. canonical semantic records; and
2. manually synchronized projections/indexes/registries/manifests over those records.

This provides transparency but creates a structural cost: one semantic change can require coordinated edits across many documents that contain partially duplicated current state.

Typical synchronization surfaces include:

```text
00 Framework
01 Index
03 Current State
09 Handoff
10 Change Log
11 Actor Registry
12 Authorization Registry
13 Evidence Registry
14 Manifest
15 Action Registry
16 Migration Registry
40 Technical Design
60 Deployment Plan
91 Project Management Control
```

Not every surface is independently authoritative. Several are indexes, registries, current-state projections, or reconstruction aids. When those are updated manually, ProjectFramework can behave like a database whose indexes/materialized views are maintained by hand.

Structured Core + Generated Governance proposes separating **canonical semantic records** from **generated projections**.

## 3. Relationship to Existing Upstream Work

This roadmap MUST build on, and not bypass:

- existing Stable-ID and semantic-slot ownership rules;
- Project Source reconstructability;
- state-bound evidence and authority semantics;
- TASK-051 Feature Delivery Fast Path;
- TASK-052 Project Upgrade One-Session Fast Path;
- the Transaction Mode optimization roadmap;
- Git-native immutable history and completion-commit semantics;
- Root Governance / Project Location Binding boundaries;
- Brownfield no-auto-adopt;
- existing Markdown as a first-class human review/audit format.

Option 3 is not a substitute for optimizing the current workflow first. Transaction Mode should provide baseline friction metrics that prove where generation would produce material value.

## 4. Design Goals

The architecture MUST:

- reduce manual synchronization across projection documents;
- preserve human-readable Markdown review surfaces;
- preserve Git diff/review/audit quality;
- preserve Stable IDs and non-recycling;
- preserve authority and Risk semantics;
- preserve historical documents and migrations;
- make generated outputs reproducible from canonical structured truth;
- make drift between canonical records and projections detectable deterministically;
- keep generated projections non-authoritative unless explicitly designated otherwise;
- support partial adoption rather than requiring all Projects to migrate at once;
- provide a safe Brownfield migration route;
- keep secret values outside canonical Project Source;
- avoid introducing a mandatory always-on database/service/runtime;
- work with ordinary Git repositories and local tools;
- remain reviewable without proprietary infrastructure; and
- allow ProjectFramework to continue functioning in documentation-only environments.

## 5. Non-Goals

This roadmap does NOT propose:

- replacing Git with a database;
- replacing all Markdown with YAML/JSON;
- making generated files impossible for Humans to inspect;
- hiding authority decisions in opaque machine state;
- introducing a central multi-Project database as the new Project authority;
- auto-mutating consuming Projects;
- storing actual secrets in structured Project files;
- eliminating historical archive files;
- making runtime services mandatory for validation;
- changing Project UUID semantics;
- changing Stable-ID ownership without a separately governed migration;
- eliminating `FRAMEWORK-001`; or
- converting every Project-specific narrative/architecture document into generated text.

## 6. Architectural Principle

The core principle is:

> **Canonical semantics should be authored once; derived views should be generated.**

The architecture distinguishes three artifact classes:

```text
A. Canonical Structured Core
B. Canonical Human Semantic Documents
C. Generated Governance Projections
```

### 6.1 Canonical Structured Core

Structured records optimized for deterministic machine processing and synchronization.

Potential files:

```text
Project-Source/core/project.yaml
Project-Source/core/framework.yaml
Project-Source/core/state.yaml
Project-Source/core/authority.yaml
Project-Source/core/actions.yaml
Project-Source/core/evidence.yaml
Project-Source/core/migrations.yaml
Project-Source/core/deployment.yaml
Project-Source/core/relations.yaml          # only when slot 92 applies
```

This exact file layout is a design candidate, not an approved schema.

### 6.2 Canonical Human Semantic Documents

Human-authored documents remain canonical where narrative reasoning is itself the governed truth.

Examples likely to remain authored Markdown:

```text
04 Decision Log / Decision Detail
05 Requirements / Requirement Detail
06 Architecture
07 Implementation Plan
08 Open Issues / Conflict details
40 Technical Design
60 Deployment Plan narrative sections where needed
91 outcome/management narratives where not normalized into structured records
```

The system MUST NOT generate decisions or requirements that a Human/authorized Agent did not actually make.

### 6.3 Generated Governance Projections

Documents whose primary role is routing, indexing, summarized current state, registry projection, or inventory should be strong candidates for deterministic generation.

Likely candidates:

```text
01 Project Source Index
03 Current State projection
09 Handoff routing summary
10 Change Log registry view
11 Actor Registry
12 Authorization Registry
13 Evidence Registry
14 Project Source Manifest
15 Action Registry
16 Migration Registry
91 selected Project Management Control summaries
```

Whether each slot becomes fully generated, partially generated, or remains canonical must be decided explicitly during design.

## 7. Authority Model

Generated projections MUST NOT create new authority.

Recommended rule:

```text
canonical structured record / canonical semantic document
        ↓ deterministic projection
rendered Markdown
```

Authority flows from the canonical source record, never from the generated rendering merely because it is newer.

Generated files MUST carry machine-visible provenance such as:

```yaml
generated: true
generator_contract_version: "..."
generated_from:
  - path: "..."
    git_blob: "..."
generated_at: "..."
```

Exact metadata requires design review.

## 8. Candidate Structured Core Domains

### 8.1 Project identity

`project.yaml` candidate fields:

```yaml
project_uuid:
project_id:
product_version:
repository:
project_source_root:
```

Project identity remains governed and immutable where current rules say so.

### 8.2 Framework consumption

`framework.yaml` candidate fields:

```yaml
framework_version:
schema_version:
release_format_version:
source_repository:
source_ref:
resolved_commit:
resolved_tree:
migration_id:
```

Root semantic narrative remains in `FRAMEWORK-001`; structured values support deterministic routing/generation.

### 8.3 Current state

`state.yaml` SHOULD contain normalized state assertions rather than free-form replacement prose.

Each state assertion may need:

```text
subject
state/value
epistemic status
freshness class
source/evidence reference
updated boundary
```

This can reduce repeated copying of the same current-state statement into Index, Handoff, PMCTRL, and registry files.

### 8.4 Authority

`authority.yaml` could represent current AUTH state and scope in a normalized way while detailed authority documents remain durable evidence/history.

It MUST preserve:

- exact grantor/grantee;
- scope;
- risk/action boundaries;
- state-bound consumption conditions;
- no authority transfer unless explicit;
- expiry/consumption/revocation state.

### 8.5 Actions and envelopes

`actions.yaml` could normalize active/terminal action/envelope state and links to detailed canonical records.

It MUST NOT replace task-specific narrative/evidence when material.

### 8.6 Evidence

`evidence.yaml` should index evidence identity/status/binding; large evidence payloads remain in their native files.

### 8.7 Deployment

`deployment.yaml` could normalize slot-60 facts such as applicability, roles, source-to-runtime mapping, and verified/unverified runtime locators while preserving narrative Deployment Plan where required.

## 9. Stable IDs

Stable IDs remain canonical ProjectFramework concepts.

Option 3 SHOULD NOT replace IDs such as:

```text
DEC-*
REQ-*
CHG-*
INST-*
AUTH-*
EVD-*
ACT-*
ENV-*
MIG-*
OUT-*
REL-*
```

Instead, structured core records SHOULD index them deterministically and enforce uniqueness.

Potential advantage:

```text
one canonical ID registry/index
→ deterministic uniqueness validation
→ generated slot registries
```

This removes repeated whole-repository string scanning as the normal allocation mechanism.

## 10. ID Allocation Service Without a Runtime Service

A deterministic local allocator can exist as a script/library invoked inside the repository without becoming an always-on service.

Example contract:

```text
read canonical ID registry
→ verify exact base/tree
→ reserve bounded IDs in transaction state
→ materialize canonical records
→ commit
→ reservation becomes consumed
```

The allocator itself is not authority. It only prevents collision.

Transaction Mode should be implemented first so this allocator can reuse its reservation semantics.

## 11. Generated Markdown Contract

Every generated projection MUST satisfy:

1. deterministic output for the same canonical inputs and generator version;
2. stable ordering;
3. normalized line endings/encoding;
4. no volatile timestamp where it would destroy reproducible diffs unless the timestamp is semantically required;
5. explicit generated-file marker;
6. provenance to canonical inputs;
7. `--check` mode that fails on drift without writing;
8. generation mode that updates only affected projections where possible;
9. no hidden network access;
10. no secret-value inclusion.

## 12. Generator Architecture

Recommended initial architecture:

```text
repository files
    ↓
parser + schema validation
    ↓
canonical in-memory Project model
    ↓
projection renderers
    ├─ Index renderer
    ├─ Current State renderer
    ├─ Handoff renderer
    ├─ Registry renderers
    └─ Manifest renderer
    ↓
Markdown/YAML files
```

Implementation language is not decided by this roadmap.

The generator SHOULD be:

- deterministic;
- local;
- stateless across runs except ordinary files;
- testable with fixtures/golden files;
- able to run in read-only validation mode;
- able to explain drift in machine-readable and human-readable form.

## 13. Manifest as Generated Projection

Slot 14 is the strongest early candidate for full generation.

The generator SHOULD derive the Manifest from exact Git candidate state and canonical routing, rather than requiring manual Markdown construction.

The Manifest pipeline SHOULD:

```text
resolve exact candidate/index
→ enumerate current reconstructable snapshot
→ compute exact Git blob IDs after filters
→ validate active-primary routing
→ render deterministic Manifest
→ self-exclude its own final blob where necessary
→ verify regeneration is stable
```

This directly eliminates a high-friction and error-prone manual synchronization surface.

## 14. Index as Generated Projection

Slot 01 is another strong candidate.

Inputs:

```text
active semantic slots
active primary document metadata
canonical Project identity
applicability map
```

Output:

```text
exact active primary table
routing notes
applicability status
```

The Index SHOULD NOT duplicate semantic narrative that belongs in canonical records.

## 15. Registry Generation

Registries for Change, Actor, Authorization, Evidence, Action, and Migration can potentially be generated from detail records plus normalized structured state.

A major design decision is whether registry lifecycle status is:

- canonical in each detail record;
- canonical in structured state; or
- split, with immutable detail + structured current projection.

The chosen model MUST prevent two authoritative locations for the same lifecycle field.

## 16. Current State and Handoff

These are more complex because they contain useful human synthesis.

Recommended hybrid model:

### Current State

- generated normalized current assertions;
- optional clearly delimited human narrative section;
- machine validation ensures narrative cannot silently contradict generated state without a surfaced conflict.

### Handoff

- generated Required Read/current routing/current active work;
- optional Human/Agent handoff notes;
- volatile execution state SHOULD remain outside canonical Handoff when reconstructable from Git/task state.

## 17. Narrative vs Structured Ownership Rule

Before migration, every field/concept MUST have exactly one canonical owner.

Example ownership table:

| Concept | Proposed owner |
|---|---|
| Project UUID | structured core |
| Framework pin | structured core + Root semantic contract, with one designated canonical value owner |
| Decision rationale | Decision Markdown |
| Requirement statement | Requirements Markdown |
| Active AUTH lifecycle | structured authority core |
| AUTH detailed approval basis | detail Markdown |
| Active action state | structured actions core |
| Evidence payload | evidence/detail file |
| Evidence current index | structured evidence core |
| Index routing | generated |
| Manifest | generated |

No migration may proceed while ownership remains ambiguous.

## 18. History Model

Generated projections SHOULD NOT create archival explosion on every regeneration.

Possible model:

- canonical structured records and human semantic documents carry durable history through Git and explicit detail records;
- generated projection files are updated in place per commit;
- Git history itself preserves prior rendered projections;
- Project Source `archive/` remains for historical canonical revisions where Framework semantics require explicit archive identity, but not every regenerated view requires a separately named revision file.

This would be a major semantic change and requires explicit compatibility analysis before adoption.

Alternative conservative model:

- generated projections continue receiving revisions/archive files exactly as today;
- generator automates the rotations.

Recommended first migration: **conservative generated rotations**, then evaluate whether named projection archives can be simplified in a later major version.

## 19. Compatibility and Versioning

Option 3 likely warrants a major Framework compatibility classification unless the structured core is introduced as optional/advisory first.

Possible staged adoption:

```text
Stage 0 — generators validate current Markdown-only Projects
Stage 1 — generated Manifest only
Stage 2 — generated Index + registries
Stage 3 — optional structured core mirrors existing Markdown authority
Stage 4 — structured core becomes canonical for explicitly selected domains
Stage 5 — broader generated governance
```

Do not switch canonical ownership in the same release that first introduces a mirror unless migration proof is unusually strong.

## 20. Brownfield Migration

Existing Projects MUST NOT auto-convert.

A migration Preview MUST include:

- source Framework/Schema/version;
- exact current Project Source reconstruction;
- proposed structured records;
- field-by-field ownership mapping;
- generated projection comparison against existing documents;
- all semantic mismatches/conflicts;
- archive/history strategy;
- rollback route;
- tool availability;
- verification plan.

Migration SHOULD first run in shadow mode:

```text
existing Markdown remains canonical
→ generator builds structured mirror/projections
→ compare
→ resolve discrepancies
→ explicit promotion approval
```

## 21. Shadow Mode

Shadow mode is strongly recommended.

In shadow mode:

- current ProjectFramework remains canonical;
- structured core is generated/inferred as a candidate mirror;
- generated projections are compared with current active documents;
- no authority shifts;
- drift metrics are collected;
- migration blockers are surfaced.

Only after repeated exact/accepted equivalence should canonical ownership move.

## 22. Security and Trust

Structured files MUST NOT contain actual secret values.

Generators MUST:

- operate on authorized local Project data only;
- preserve disclosure classifications;
- avoid network calls by default;
- never send Project Source content to external AI merely to generate projections;
- produce deterministic logs/evidence sufficient for review without leaking protected data.

## 23. Validation and Testing Strategy

The future implementation requires strong test coverage:

### Schema tests

- required fields;
- enum vocabulary;
- Stable-ID uniqueness;
- referential integrity;
- lifecycle transitions;
- canonical-owner uniqueness.

### Golden projection tests

- identical input → identical output;
- stable ordering;
- expected Markdown projection;
- no volatile unrelated diff.

### Round-trip tests

Where supported:

```text
canonical input → projection → parse projection → equivalent semantics
```

The generated Markdown need not be a lossless serialization of all structured data, but all projected semantics must be reproducible.

### Brownfield fixture tests

Use representative existing Projects with:

- long archive history;
- active Goal/AUTH chains;
- slot 60 applicable/not applicable;
- optional Project Execution/Knowledge/Graph surfaces;
- concurrent local worktrees;
- stale branches;
- historical revision gaps.

## 24. Failure and Recovery

Generation MUST be atomic at candidate level.

Recommended flow:

```text
read canonical sources
→ validate
→ render into temporary transaction output
→ compare/check
→ replace affected generated projections as one bounded mutation
→ verify
```

On failure before replacement: no Project Source mutation.

On interrupted replacement: transaction recovery must identify exact affected generated files and regenerate from canonical inputs instead of guessing partial state.

## 25. Performance / Friction Objectives

Option 3 is justified only if it materially improves measured friction after Transaction Mode.

Candidate objectives:

- 70%+ reduction in manual projection edits per normal governance transaction;
- zero manual Manifest hash construction;
- zero manual Index routing synchronization in generated-mode Projects;
- zero whole-repository Stable-ID collision scans during normal reserved allocation;
- no more than one generator invocation per final candidate in normal flow;
- regenerated unrelated projections produce zero diff;
- Project Source reconstruction/check time is materially lower than current manual multi-file inspection.

Exact targets should be calibrated from Transaction Mode metrics.

## 26. Required Upstream Components

A future implementation program would likely require:

```text
Framework-Source/schemas/            # optional candidate
Framework-Source/generator/          # implementation or reference tooling
Framework-Source/templates/core/     # structured starter templates
Framework-Source/tests/fixtures/     # Project fixtures
Framework-Source/tests/golden/       # deterministic projection outputs
Framework-Source/references/...      # normative ownership/generation contract
```

These paths are illustrative, not approved.

## 27. Phased Roadmap

### Phase A — Domain Ownership Design

- inventory every duplicated field across Project Source;
- classify each as canonical semantic truth vs projection;
- produce canonical owner matrix;
- reject ambiguous ownership.

### Phase B — Manifest Generator Pilot

- implement read-only/check mode first;
- generate Manifest from Git/index/routing;
- compare against current manual Manifest across fixtures;
- add deterministic golden tests;
- make generation optional.

### Phase C — Index and Registry Pilot

- generate Index;
- generate one low-risk registry such as Migration or Actor Registry;
- prove history/revision behavior;
- measure friction reduction.

### Phase D — Structured Mirror

- define structured schemas;
- derive mirrors from current canonical Markdown;
- run shadow mode across representative Projects;
- resolve semantic gaps.

### Phase E — Selective Canonical Promotion

- choose domains where structured ownership is clearly superior;
- create explicit migration contract;
- promote only those domains;
- retain Markdown projections for Human use.

### Phase F — Broader Generated Governance

- extend generation only when measured benefit exceeds complexity;
- revisit named archive/revision strategy for generated projections;
- preserve rollback to Markdown-only mode until migration maturity is proven.

## 28. Decision Gates

Before moving from Option 2 to Option 3, require evidence that:

- Transaction Mode is implemented;
- friction metrics have been collected across real workflows;
- the remaining dominant cost is manual projection synchronization rather than approval or high-risk safety gates;
- generator tooling can run reliably in target environments;
- Brownfield migration can be demonstrated safely;
- the ProjectFramework maintenance burden of tooling is acceptable.

If these are not proven, remain on optimized Markdown Transaction Mode.

## 29. Acceptance Criteria for an Initial Option 3 Pilot

An initial pilot is successful when:

- current Markdown authority remains intact;
- Manifest is generated deterministically in shadow/optional mode;
- generator `--check` detects drift without writes;
- generated Manifest matches exact Git blob identity rules;
- unrelated candidate content does not change;
- rollback is simply removal/disablement of generated mode;
- no secret or external-data leakage occurs;
- fixtures prove Windows/local Git behavior relevant to existing Projects;
- measured manual synchronization effort falls materially; and
- no new ambiguity is introduced over canonical ownership.

## 30. Recommended Sequencing

The recommended upstream sequence is:

```text
TASK-051 Risk-Tiered Feature Delivery Fast Path
→ TASK-052 Project Upgrade One-Session Fast Path
→ Transaction Mode Optimization Roadmap implementation
→ collect Governance Friction Budget evidence
→ Manifest generator pilot
→ structured mirror/shadow mode
→ selective Structured Core canonicalization only if evidence supports it
```

Option 3 should be treated as an evidence-driven architectural evolution, not as an urgent replacement for the current Project Source model.

## 31. Recommendation

Adopt Option 2 first.

Do not commit ProjectFramework to Option 3 implementation until Transaction Mode proves which synchronization surfaces remain expensive. The lowest-risk high-value Option 3 pilot is **generated Manifest**, followed by **generated Index**, because these surfaces are highly mechanical and provide clear deterministic acceptance criteria.
