# TASK-022 Project Graph + OpenViking Relation Governance — Design

Date: `2026-08-28` (Asia/Bangkok)
Task: `TASK-022`
Design state: `USER_APPROVED_DESIGN / SPEC_APPROVED`
Approval basis: user approved Sections 1–4 and then gave continuous approval to proceed through completion on `2026-08-28`.

## 1. Problem

Projects may start independently and only later become related, nested, merged, split, or reorganized. ProjectFramework needs a relation model that allows late binding without requiring destructive Project reconstruction and without transferring Project authority to a central graph/index service.

The design must preserve four existing Framework invariants:

1. Each Project's local Project Source Markdown remains authoritative for that Project's current governance truth.
2. `project_uuid` remains the immutable authoritative Project identity; names, paths, repositories, MCP workspace IDs, and external index IDs are not substitutes.
3. Existing canonical homes remain canonical: dependency management stays in `91`, decisions in `04`, requirements in `05`, issues/drift/conflicts in `08`, identity/lineage in existing root/change semantics.
4. Correct relation/index location does not grant Authority, Risk approval, implementation authority, runtime authority, or binding authority.

## 2. Chosen architecture: Federated Project Graph

The approved architecture is **Federated Graph**:

```text
Project-local Project Source / 92 Project Graph = authoritative relation assertions
AI-ControlTower = owner of cross-Project indexing/orchestration
OpenViking = derived, rebuildable cross-Project knowledge/index layer
```

OpenViking MUST NOT become the canonical owner of Project relation truth. A complete loss of OpenViking's derived graph must be recoverable by rebuilding from authoritative Project sources plus their durable source pointers.

A Project may participate in the federated graph without knowing every reciprocal relation at creation time. A central service may correlate, normalize, traverse, rank, cache, and detect inconsistencies, but it cannot silently promote derived inference into Project truth.

## 3. Namespace and document ownership

Framework standardizes:

```text
90 General / Special Governance Extension
91 Project Management Control             CONDITIONAL
92 Project Graph                          CONDITIONAL
93–99 Project-specific / Governance Extension
```

`18–19` remain RESERVED.

`92 Project Graph` is materialized only when Project-level relation truth is applicable. A Project with no current relation requirement does not create an empty `92` merely for completeness.

### 3.1 Canonical home of `92`

`92 Project Graph` owns current `REL-*` records and only the graph-specific metadata required to interpret those records:

- source Project identity;
- target Project identity;
- relation type and direction;
- assertion/corroboration lifecycle;
- evidence/source pointers;
- links to canonical Stable IDs that own richer semantics elsewhere;
- current conflict or retirement state.

`92` MUST NOT duplicate the authoritative payload of `DEP-*`, `DEC-*`, `REQ-*`, `RISK-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, or identity/lineage records.

## 4. Project identity and node identity

Every relation endpoint is identified primarily by `project_uuid`.

```text
project_uuid = immutable authoritative node identity
project_id   = stable human-readable label
project_name = mutable display label
```

Repository URL, local workspace path, display name, OpenViking node ID, and MCP workspace ID MAY be routing/index metadata but MUST NOT replace `project_uuid` as Project identity.

Rename, repository move, workspace relocation, or OpenViking re-indexing does not by itself change `project_uuid` or invalidate a relation whose endpoint identity is otherwise unchanged.

## 5. `REL-*` record model

Each Project Graph relation is a current materialized record with a Stable ID in the `REL-*` family.

Minimum fields:

```text
Relation ID: REL-*
Source Project UUID
Target Project UUID
Relation Type
Direction
Assertion State
Related Stable IDs
Evidence / Source Pointers
Last Verified / Reviewed
Notes when material
```

The source Project for a `REL-*` record is the Project whose `92` document owns that record. A Project MUST NOT write another Project's authoritative `REL-*` record directly.

### 5.1 Core relation vocabulary

Initial Framework vocabulary is intentionally small:

```text
PARENT_OF
CHILD_OF
PEER_OF
DEPENDS_ON
SUPPORTS
RELATED_TO
```

Semantics:

- `PARENT_OF` / `CHILD_OF` are inverse directed relations.
- `PEER_OF` and `RELATED_TO` are symmetric.
- `DEPENDS_ON` and `SUPPORTS` are directed.
- `DEPENDS_ON` is graph linkage only; the authoritative dependency object remains `DEP-*` in `91` when dependency-management semantics are material.

Project-specific relation types are allowed only through an explicitly namespaced extension token, not unrestricted free text. The standard syntax is:

```text
X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>
```

A namespaced extension MUST define its meaning in the owning Project's active governance/technical source and MUST NOT redefine a core relation token.

### 5.2 Assertion states

Current `REL-*` assertion state is exactly:

```text
ASSERTED
CORROBORATED
CONFLICTED
RETIRED
```

- `ASSERTED` — the owning Project declares the relation; no compatible reciprocal Project assertion has yet been verified.
- `CORROBORATED` — a compatible relation in the other Project has been verified using matching endpoint UUIDs and compatible relation semantics.
- `CONFLICTED` — authoritative Project assertions cannot be reconciled without changing at least one Project's current truth.
- `RETIRED` — the relation is no longer current, but its historical existence is preserved through normal revision/change history.

`CORROBORATED` does not mean a central service approved the relation. It means independently authoritative Project assertions support the same relation.

### 5.3 Reciprocal compatibility

OpenViking/AI-ControlTower may classify corroboration only from compatible authoritative assertions:

```text
A PARENT_OF B  ↔ B CHILD_OF A
A CHILD_OF B   ↔ B PARENT_OF A
A PEER_OF B    ↔ B PEER_OF A
A RELATED_TO B ↔ B RELATED_TO A
```

Directed relations such as `DEPENDS_ON` and `SUPPORTS` do not require an inverse record unless the other Project independently records a meaningful compatible relation.

A derived inverse edge MAY exist in the OpenViking index for traversal but MUST be labeled derived and MUST NOT be written back as if the other Project had asserted it.

## 6. Late binding and lifecycle

A Project does not need a graph placeholder at bootstrap. `92` becomes applicable when current relation truth becomes material.

Example lifecycle:

```text
Project A created independently
Project B created independently
later: A discovers B is its parent
→ materialize 92 in A if absent
→ create REL-* in A as ASSERTED
→ optionally verify a compatible B relation later
→ mark A relation CORROBORATED only after reciprocal evidence is verified
```

Adding or changing a relation does not reconstruct the Project or change `project_uuid`.

When a current relation changes materially, preserve history instead of rewriting the old record to pretend the prior state never existed:

```text
old REL-* → RETIRED
new REL-* → ASSERTED / CORROBORATED as supported
```

## 7. Project nesting is semantic, not filesystem topology

`PARENT_OF` / `CHILD_OF` expresses semantic Project relationship. It does not require nested folders, nested repositories, matching local paths, or a common runtime.

Therefore:

```text
Project Relation ≠ Repository Location Binding
Project Relation ≠ Local Workspace Binding
Project Relation ≠ current branch/worktree
Project Relation ≠ Canonical Integration Target
Project Relation ≠ Canonical Implementation Source
Project Relation ≠ Runtime Location
```

A relation change MUST NOT silently rewrite any location/binding role.

## 8. Merge, absorption, and split

Existing Project identity semantics remain authoritative.

### 8.1 Absorption

The primary Project keeps its UUID; the absorbed Project keeps its UUID historically and ends according to existing lifecycle semantics. Relations owned by the absorbed Project are not copied blindly into the survivor. Each relation is assessed for whether an equivalent relation is still true for the surviving Project.

### 8.2 True merge

A true merge creates a new Project UUID and preserves predecessor lineage. The new Project creates its own current relation set through governed migration/assessment. OpenViking may index lineage edges derived from authoritative identity/change records; it cannot invent lineage from graph topology.

### 8.3 Split / carve-out

A carve-out preserves the original Project UUID and gives the carved-out Project a new UUID. A true split ends the predecessor lifecycle and creates new descendant UUIDs. Descendant relation sets are assessed; they are not cloned wholesale.

Material merge/split relation transformation uses existing `MIG-*` migration semantics and preserves history.

## 9. OpenViking / AI-ControlTower integration contract

AI-ControlTower owns cross-Project indexing/orchestration. OpenViking is the derived index/knowledge engine used by that scope.

A Project exposes/publishes enough non-secret metadata to support indexing:

- `project_uuid`;
- relevant human-readable identity labels;
- current active `REL-*` payloads;
- durable source pointers needed to verify the assertion;
- related Stable-ID pointers when graph edges summarize semantics owned elsewhere.

AI-ControlTower/OpenViking may:

- discover and read governed relation records;
- normalize core/inverse/symmetric relation views;
- correlate reciprocal assertions;
- maintain traversal/search indexes;
- surface stale, orphaned, or conflicting derived state;
- incrementally update affected nodes/edges;
- perform a full rebuild/re-index.

It MUST NOT:

- overwrite Project Source because an index disagrees;
- infer Project authority from recency, ranking, similarity, or central confidence score;
- create authoritative reciprocal Project assertions automatically;
- make OpenViking availability a prerequisite for reconstructing current Project truth.

## 10. Rebuild / re-index semantics

The derived cross-Project graph is explicitly **REBUILDABLE**.

Full rebuild contract:

```text
discard or invalidate derived graph generation
→ discover governed Project sources
→ read current Project identity + active 92/REL-* records
→ resolve endpoint UUIDs and durable source pointers
→ normalize derived inverse/symmetric views
→ correlate compatible reciprocal assertions
→ surface conflicts/orphans/stale pointers
→ publish a new derived index generation
```

Normal operation MAY use incremental updates. Full rebuild is supported when topology changes materially, merge/split occurs, relation vocabulary changes, index corruption is suspected, or bounded incremental correctness cannot be established.

OpenViking-specific scheduling, watcher, webhook, crawler, MCP, daemon, storage, and deployment mechanisms are out of scope for TASK-022 and belong to a later AI-ControlTower implementation task.

## 11. Drift, conflict, and failure handling

Reuse existing Framework families. No new graph-specific issue/drift family is introduced.

- Project Source newer than OpenViking derived projection → derived index is stale; use existing `DRIFT-*` when material Project truth requires tracking the mismatch.
- Project A/B authoritative assertions contradict → relevant `REL-*` becomes `CONFLICTED`; use existing `CONFLICT-*` in `08` when the conflict is material and requires managed resolution.
- OpenViking contains an edge with no current authoritative source → orphan/stale derived edge; remove or rebuild the derived projection, recording `DRIFT-*`/evidence when material.
- Index unavailable or corrupt → Project Source remains reconstructable and authoritative; cross-Project query capability may degrade but local Project governance truth does not.

Timestamp, search ranking, or confidence score MUST NOT resolve an authoritative Project-to-Project conflict automatically.

## 12. Root/project surfaces

### 12.1 `00 Project Source Framework`

Add a bounded Project Graph applicability/integration block. It records whether standard Project Graph semantics are applicable and that external indexing is derived-only at AI-ControlTower scope. It does not store OpenViking credentials or make a runtime endpoint authoritative.

Allowed applicability vocabulary:

```text
APPLICABLE
NOT_APPLICABLE
VERIFICATION_REQUIRED
```

### 12.2 `01 Project Source Index`

Lists `92 Project Graph` only when active/materialized. No empty conditional file is required.

### 12.3 `03 Current State`

May summarize relation health/counts and external derived-index freshness, with pointers to `92`/evidence. It is not a duplicate relation registry.

### 12.4 `08 Open Issues`

Retains canonical ownership of material `ISS-*`, `DRIFT-*`, and `CONFLICT-*` arising from relation/index mismatch.

### 12.5 `10 Change Log`

May record material relation additions/retirements, merge/split topology changes, mass reclassification, and full re-index events as history. It is not current graph truth.

### 12.6 `13 Evidence Registry`

May register reciprocal relation evidence, verified Project UUID evidence, migration evidence, source pointers, and derived index-generation evidence.

### 12.7 `14 Project Source Manifest`

An active `92` required for current relation truth is part of the Current Reconstructable Snapshot/CURRENT export. A fresh agent must reconstruct Project relation truth without querying OpenViking.

### 12.8 `16 Migration Registry`

Owns Brownfield adoption and relation migration work through `MIG-*` when material.

## 13. Brownfield slot-92 collision migration

Framework 1.5.0 permits Project-specific use of `92–99`, so a Brownfield Project may already occupy slot `92`.

Upgrade MUST fail closed against overwrite:

```text
detect active custom 92
→ open/route MIG-* assessment
→ preserve custom document identity, history, references, and current semantics
→ propose relocation to a free 93–99 slot or another semantically correct slot
→ obtain the approval required by existing migration/root-governance rules
→ relocate/promote through governed migration
→ activate standard 92 only after collision resolution
```

No initialized Project auto-upgrades and no custom `92` is silently renamed or overwritten.

## 14. Templates and distribution surfaces

TASK-022 implementation is expected to affect these surfaces where applicable:

- `managing-project-source/FRAMEWORK-RELEASE.yaml`;
- a new Framework amendment for TASK-022;
- `managing-project-source/references/core-governance-rules.md`;
- `managing-project-source/SKILL.md`;
- `README.md`;
- `managing-project-source/MIGRATION-NOTES.md`;
- `managing-project-source/templates/00-project-source-framework.md`;
- `managing-project-source/templates/core-document-skeletons.md`;
- `managing-project-source/templates/project-source-mockup/README.md`;
- new `managing-project-source/templates/project-source-mockup/92-Project-Graph.template.md`;
- affected mockup/index/manifest guidance where needed;
- `managing-project-source/tests/pressure-scenarios.md`;
- platform launchers only if a bootstrap-critical invariant cannot be reliably reached through the normal Required Read chain without launcher text.

Launcher changes are not required merely to advertise Project Graph; character-budget pressure and shared-marker byte identity remain binding.

## 15. Release classification

TASK-022 is a backward-compatible **Framework minor semantic expansion** because it:

- standardizes a new conditional slot `92`;
- introduces `REL-*` as a standard Stable-ID family;
- narrows generic extension space from `92–99` to `93–99`;
- adds Brownfield migration semantics for pre-existing custom slot `92`.

Target release is **Framework `1.6.0` / Schema `1.0.0` / release format `3`** unless implementation reveals a genuine schema break. The approved design does not require a Schema major/minor change because existing document metadata/lifecycle machinery can represent the new conditional slot and Stable-ID family.

## 16. Verification strategy

Implementation verification is proportional but must cover at least:

1. release identity consistency across descriptor/README/SKILL/templates;
2. `92` namespace standardization and `93–99` extension-space consistency;
3. `REL-*` canonical-home and non-duplication rules;
4. exact assertion states `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`;
5. core relation vocabulary and reciprocal compatibility;
6. `project_uuid` endpoint identity and relation/location separation;
7. late-binding without mandatory empty `92`;
8. Brownfield custom-92 collision fail-closed migration;
9. OpenViking derived-only/rebuildable authority boundary;
10. merge/split relation assessment without blind cloning;
11. reuse of existing `DRIFT-*` / `CONFLICT-*` / `MIG-*` families;
12. mockup/template support for `92`;
13. reserved `18–19` unchanged;
14. launcher ceiling/shared-marker invariants if launchers are touched;
15. `git diff --check` and Markdown/YAML-only scope;
16. one final `RELEASE_FULL` on the unchanged Framework 1.6.0 candidate before completion claim.

## 17. Non-goals

TASK-022 does not authorize implementation of:

- OpenViking runtime/deployment;
- graph database selection or provisioning;
- Graphify or another graph product integration;
- sync daemon, watcher, crawler, webhook, scheduler, background agent, MCP graph tool, or reconciliation service;
- automatic Project discovery/promotion;
- automatic conflict resolution;
- source-code/runtime changes outside ProjectFramework documentation/governance scope.

Those are separate AI-ControlTower/implementation decisions after this Framework contract exists.

## 18. Acceptance criteria

The design is complete when implementation can make the following statements true without ambiguity:

- a Project can start unrelated and bind relations later;
- relation topology can change without changing Project identity;
- Project nesting is semantic and independent of filesystem/repository topology;
- each Project remains authoritative for its own `REL-*` assertions;
- compatible reciprocal assertions can be corroborated without a central authority takeover;
- OpenViking is derived and fully rebuildable from authoritative Project sources;
- current relation truth remains reconstructable without OpenViking;
- merge/split/absorption preserve existing identity/lineage semantics and reassess relations;
- Brownfield custom slot `92` is never overwritten;
- no specific graph product is required by the Framework contract.
