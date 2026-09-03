---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.13.0"
project_source_framework_version: "1.14.0"
project_source_schema_version: "1.0.0"
approval_basis: "OUT-008_USER_GOAL_2026-09-03"
compatibility: "BACKWARD_COMPATIBLE_FEDERATED_CHANGE_INTELLIGENCE_SUITE"
---

# Framework 1.14.0 Amendment — Federated Change Intelligence Suite

Framework `1.14.0` preserves Framework `1.13.0` unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`; the Registered Command set remains unchanged. This cumulative suite is dependency-ordered `TASK-036 + TASK-030 → TASK-029 → TASK-031`.

At this foundation checkpoint, TASK-036 Project Change/Event History Feed and TASK-030 Cross-Project Relation Reconciliation are normative from this amendment. TASK-029 and TASK-031 remain dependency-gated and non-normative until their focused implementation checkpoints are completed.

## 1. TASK-036 Project Change/Event History Feed

Framework 1.14.0 defines an optional root-level derived surface:

```text
<Project-Root>/Project-Change-Feed/
├── README.md
└── feed.md
```

Maintained starter sources live under `Framework-Source/templates/project-change-feed/`. `Project-Change-Feed/` is optional and applicability-driven. Its absence does not invalidate a Project when no incremental consumer has adopted it.

The feed is **derived, non-authoritative, bounded, rebuildable, and disposable**. It is outside `Project-Source/00–99`, outside Root Governance, and outside canonical Project history authority.

Exact separation:

```text
Project-Change-Feed ≠ Project Source
Project-Change-Feed ≠ 10 Change Log
Project-Change-Feed ≠ Git/source-native history
Project-Change-Feed ≠ Evidence
Project-Change-Feed ≠ Project Knowledge
Project-Change-Feed ≠ OpenViking authority
```

Loss, corruption, staleness, or absence of the feed never makes current Project truth unreconstructable when the authoritative/source-native sources remain available.

## 2. Projection metadata and maintenance state

The derived feed MAY carry compact projection metadata such as:

```yaml
feed_projection_id: "<UUID_OR_STABLE_OPAQUE_DERIVED_ID>"
project_uuid: "<PROJECT_UUID>"
projection_state: "CURRENT | STALE | REBUILD_REQUIRED | UNAVAILABLE"
source_checkpoint:
  repository_ref: "<COMMIT_OR_UNKNOWN_OR_NOT_APPLICABLE>"
  project_source_manifest_ref: "<ACTIVE_14_POINTER_OR_UNKNOWN>"
  change_log_ref: "<ACTIVE_10_POINTER_OR_UNKNOWN>"
generated_at: "<ISO8601_OR_UNKNOWN>"
retention_policy: "<BOUNDED_POLICY_DESCRIPTION>"
```

Exact projection-state vocabulary is:

```text
CURRENT | STALE | REBUILD_REQUIRED | UNAVAILABLE
```

These values are derived-surface maintenance labels only. They are not Project lifecycle, health, Risk, Evidence, or authority states.

`feed_projection_id` is derived-layer identity only and MUST NOT become a Project Source Stable ID, authorization object, evidence identity, or cross-Project authority token.

## 3. Feed entry contract

`feed.md` is a bounded chronological projection. Each material entry records enough routing/provenance to reconstruct why it exists without copying whole canonical objects:

```text
Sequence within current projection generation
Source checkpoint / source-native ordering pointer
Change kind
Subject refs
Authoritative/source refs
Concise changed-state summary
Observed/materialized time when known
```

Exact change-kind vocabulary:

```text
STABLE_ID_CHANGE
DOCUMENT_CHANGE
RELATION_CHANGE
LIFECYCLE_CHANGE
EVIDENCE_CHANGE
RELEASE_PUBLICATION_CHANGE
OTHER_MATERIAL_CHANGE
```

`Sequence` is projection-local ordering only. A feed entry is not `EVD-*`, not a canonical event, not an impact classification, and not an authorization. Framework 1.14.0 creates no `EVENT-*`, `FEED-*`, `CHANGE-EVENT-*`, or other Project Source Stable-ID family for this feature.

The feed records material changes, not every read/tool call. It MUST NOT become a raw MCP transcript, private-reasoning store, unbounded diff log, watcher journal, or execution telemetry stream.

## 4. Incremental since/source checkpoint semantics

Consumers may ask for changes **since** a previously observed source checkpoint. A source checkpoint is a routing/evidence bundle, not authority. It may include as applicable:

```text
repository/source-native ref
+ active Project Source Manifest pointer
+ active Change Log pointer
+ projection generation/context
```

Ordering uses source-native ordering when material. Git ancestry/order and Project Source revision/current-routing evidence outrank wall-clock timestamp guessing. Equal, missing, or contradictory timestamps do not decide authoritative order by themselves.

If the requested checkpoint is older than the retained feed window, either rebuild the requested delta from authoritative/source-native history or return explicit `UNKNOWN / VERIFICATION_REQUIRED` for the unavailable portion. Never silently return only the retained tail as if it were complete.

## 5. Retention, corruption, and rebuild

Retention MUST be bounded but Framework 1.14.0 does not mandate one universal count/time window. A Project MAY choose a retention policy appropriate to its scale. Trimming derived feed entries never deletes or supersedes authoritative history.

Known corruption, broken checkpoint continuity, or unsafe projection reuse moves the projection to `REBUILD_REQUIRED`; do not repair Project Source to match the feed. Rebuild from authoritative/source-native inputs such as current/history Project Source, `10 Change Log`, Git/source-native history, current relation history, durable evidence pointers, and release/publication evidence when material.

Project Knowledge and AI-ControlTower/OpenViking may assist discovery, but cannot become feed authority. Chat memory, retrieval rank, similarity, central confidence, or a stale feed backup cannot substitute for authoritative reconstruction inputs.

## 6. Adoption and migration

GREENFIELD feed creation is optional and requires applicability/approval. Framework installation or upgrade does not synthesize feed content merely because the target supports TASK-036.

Brownfield Direct-to-Latest upgrade preserves existing Project truth and does not auto-create `Project-Change-Feed/`. An existing Project may adopt it separately when an incremental consumer materially benefits. Adoption creates a derived projection only; it grants no new Project authority or runtime capability.

## 7. Runtime and authority boundary

This contract creates no watcher, crawler, webhook, daemon, scheduler, background agent, event bus, queue, CDC mechanism, file monitor, Git hook, or feed-maintenance runtime. Actual automation requires a separate explicit implementation scope and applicable authority.

The feed grants no mutation, push/publication, cross-Project access, disclosure, Decision, Risk acceptance, or notification authority.

## 8. TASK-030 Cross-Project Relation Reconciliation

Relation reconciliation is a governance workflow over existing `92 Project Graph` / `REL-*`; it creates no new relation family and grants no cross-Project write authority.

Canonical workflow:

```text
identify local REL-* candidate
→ discover counterpart Project by immutable project_uuid
→ resolve counterpart authoritative 92 / REL-* when available
→ verify endpoint UUIDs + current source pointers + evidence freshness
→ evaluate compatibility under existing relation semantics
→ classify local assertion disposition using ASSERTED | CORROBORATED | CONFLICTED | RETIRED
→ persist local change only with applicable local authority
→ never synthesize/write the counterpart Project's assertion
```

Discovery may use AI-ControlTower/OpenViking, Project Graph indexes, Project Knowledge, repositories, or configured connectors as routing assistance only. Material reconciliation claims require authoritative Project-local evidence. Counterpart discoverability, central index visibility, repository proximity, or name similarity never establishes relation authority.

## 9. Reciprocal compatibility

Framework 1.14.0 preserves TASK-022 exactly. Guaranteed reciprocal-compatible core pairs are only:

```text
A PARENT_OF B  ↔ B CHILD_OF A
A CHILD_OF B   ↔ B PARENT_OF A
A PEER_OF B    ↔ B PEER_OF A
A RELATED_TO B ↔ B RELATED_TO A
```

`DEPENDS_ON` and `SUPPORTS` remain directional. Framework 1.14.0 defines no universal `DEPENDS_ON ↔ SUPPORTS` inverse. A derived inverse/index traversal edge never becomes reciprocal authoritative evidence automatically. Namespaced relation types require their owning Project/domain semantics; central similarity/ranking cannot infer reciprocal compatibility.

## 10. CORROBORATED evidence gate

A local `REL-*` may move to `CORROBORATED` only when evidence resolves at least:

```text
local Project UUID + current local REL-* pointer
counterpart Project UUID + current counterpart REL-* pointer
matching endpoint UUIDs
compatible relation type/direction under governed semantics
authoritative/current source references for both assertions
freshness/review evidence sufficient for the claim
```

Derived inverse edges, OpenViking normalization, search rank, similarity, central confidence, repository proximity, naming similarity, or timestamp recency alone are insufficient.

Temporary counterpart unavailability never auto-retires a valid local assertion. If corroboration cannot be freshly revalidated, preserve current local truth and report `VERIFICATION_REQUIRED` for the corroboration-sensitive claim rather than fabricating freshness or silently rewriting assertion state.

## 11. Conflict, drift, migration, and authority

Incompatible authoritative assertions preserve both Projects' truth and use `CONFLICTED` plus existing `CONFLICT-*` when managed resolution is material. Do not choose by recency, ranking, confidence, central index, or which Project is easier to mutate.

Stale/orphan derived state may use existing `DRIFT-*`. Migration/lineage/slot changes reuse `MIG-*`. Reconciliation creates no graph-specific conflict/drift/migration family.

A counterpart that is unavailable, inaccessible, unbound, stale, or unresolved produces explicit `VERIFICATION_REQUIRED` for corroboration-sensitive claims while preserving what is still known locally.

Reconciliation may mutate only the owning Project's canonical `REL-*` under applicable local authority. It MUST NOT write, create, retire, corroborate, or repair another Project's `REL-*` on that Project's behalf merely because the counterpart was discovered or inspected.

## 12. Suite dependency boundary

TASK-036 and TASK-030 focused completion are the two foundation gates. TASK-029 may activate only after both are complete; TASK-031 remains downstream of TASK-029/TASK-030. This amendment does not pre-implement TASK-029 or TASK-031.

Existing TASK-022 Project Graph, TASK-025 Project Knowledge, TASK-026 disclosure, TASK-028 Project Audit, TASK-032 remediation, TASK-042 response-close, and TASK-043 strict-command contracts remain unchanged.
