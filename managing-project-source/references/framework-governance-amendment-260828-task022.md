---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.5.0"
project_source_framework_version: "1.6.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-28"
compatibility: "BACKWARD_COMPATIBLE_FEDERATED_PROJECT_GRAPH_GOVERNANCE"
---

# Framework 1.6.0 Amendment — Federated Project Graph + OpenViking Relation Governance

Framework `1.6.0` preserves `1.5.0` unless refined here. Project Source Schema stays `1.0.0`; release format stays `3`. This release standardizes one new conditional semantic slot (`92 Project Graph`) and one Stable-ID family (`REL-*`) while narrowing generic extension space to `93–99`.

## 1. Standard conditional `92 Project Graph`

The extended namespace is now:

```text
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92 Project Graph                  CONDITIONAL / STANDARD IN 1.6.0+
93–99 Project-specific / Governance Extension
```

`18–19` remain RESERVED. `92` is created only when Project-level relation truth is applicable; no empty graph document is required for an unrelated Project.

`92 Project Graph` is the canonical home of current `REL-*` Project-relation assertions. It does not replace or duplicate canonical payloads owned elsewhere: `DEP-*` stays in `91`, `DEC-*` in `04`, `REQ-*` in `05`, `ISS-* / DRIFT-* / CONFLICT-*` in `08`, and identity/lineage remains governed by existing root/change semantics.

## 2. Project identity and `REL-*`

Relation endpoints use immutable `project_uuid` as authoritative Project identity. Project names, repository URLs, workspace paths, MCP workspace IDs, and external index IDs are labels/routing evidence only.

Each current `REL-*` records at least source Project UUID, target Project UUID, relation type, direction, assertion state, related Stable-ID/evidence pointers when material, and review/verification context.

Core relation vocabulary is exactly:

```text
PARENT_OF
CHILD_OF
PEER_OF
DEPENDS_ON
SUPPORTS
RELATED_TO
```

Project/domain-specific extensions use a namespaced token `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>` and must not redefine a core relation.

Current assertion state is exactly:

```text
ASSERTED
CORROBORATED
CONFLICTED
RETIRED
```

`ASSERTED` is authoritative only for the owning Project's assertion. `CORROBORATED` requires verified compatible authoritative assertions with matching endpoint UUIDs; it is not central approval. `CONFLICTED` surfaces irreconcilable authoritative assertions. `RETIRED` preserves prior relation history while removing it from current topology.

Reciprocal compatibility includes `PARENT_OF ↔ CHILD_OF`, `CHILD_OF ↔ PARENT_OF`, `PEER_OF ↔ PEER_OF`, and `RELATED_TO ↔ RELATED_TO`. A derived inverse edge may exist for traversal but never becomes another Project's assertion automatically.

## 3. Late binding and semantic nesting

A Project may begin with no graph document and bind relations later. Creating, retiring, or reclassifying a relation does not reconstruct the Project or change `project_uuid`.

`PARENT_OF` / `CHILD_OF` is semantic Project topology, not a filesystem/repository requirement:

```text
Project Relation
≠ Repository Location Binding
≠ Local Workspace Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
```

Relation changes never silently rewrite those independent roles.

## 4. Merge, absorption, and split

Existing Project identity/lineage rules remain authoritative. Absorption, true merge, carve-out, and true split preserve their existing UUID semantics. Relations are reassessed for the surviving/new Projects; graph edges are not bulk-cloned merely because predecessor topology existed. Material transformations use existing `MIG-*` governance and preserve history.

## 5. AI-ControlTower / OpenViking derived-index contract

Cross-Project indexing/orchestration belongs at AI-ControlTower scope. OpenViking is a **derived, rebuildable** knowledge/index layer, not a Project authority.

Projects expose enough non-secret identity/relation metadata and durable source pointers for indexing. AI-ControlTower/OpenViking may discover, normalize, correlate reciprocal assertions, query/traverse, incrementally update, detect stale/orphan/conflicting derived state, and fully rebuild the index.

OpenViking MUST NOT overwrite Project Source, infer Project authority from recency/ranking/similarity/confidence, synthesize authoritative reciprocal assertions, or become required to reconstruct a Project's current relation truth. If the derived index is lost, current graph state must be rebuildable from authoritative Project Sources.

## 6. Drift/conflict behavior

Reuse existing families. A stale/orphan derived edge may be tracked with existing `DRIFT-*` when material. Contradictory authoritative Project assertions use `CONFLICTED` on the affected `REL-*` and existing `CONFLICT-*` when managed resolution is required. Do not create parallel graph-specific drift/conflict families. Timestamp/ranking/confidence never auto-resolves authoritative disagreement.

## 7. Brownfield custom slot `92`

Framework `1.5.0` allowed custom use of `92–99`, so upgrade must check slot `92` occupancy. An active custom `92` is never overwritten. Use existing `MIG-*` flow to preserve document identity/history/references, relocate only with governed approval to a free `93–99` or another semantically correct slot, then activate standard `92` only after collision resolution.

Existing initialized Projects remain locally pinned and do not auto-upgrade.

## 8. Non-goals

This amendment defines governance/documentation only. It adds no OpenViking runtime/deployment, graph database requirement, Graphify integration, crawler, watcher, webhook, scheduler, sync daemon, background agent, MCP graph tool, validator/CLI, automatic Project discovery/promotion, or automatic conflict resolution.
