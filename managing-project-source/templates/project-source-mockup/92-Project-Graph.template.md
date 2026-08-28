---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<PROJECT_GRAPH_DOCUMENT_ID>"
document_type: "PROJECT_GRAPH"
semantic_slot: "92"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.6.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 92 — Project Graph

**Applicability:** CONDITIONAL / STANDARD IN Framework `1.6.0+`. Create only when current Project relation truth is materially applicable. Do not create an empty `92` for completeness.

`92` is the canonical home of current `REL-*` Project-relation assertions owned by this Project. Relation endpoints use immutable `project_uuid`; another Project's authoritative relation record is never written here on its behalf.

## Relation Registry

### REL-<NNN> — <RELATION_TITLE>
- **Source Project UUID:** <THIS_PROJECT_UUID>
- **Target Project UUID:** <TARGET_PROJECT_UUID>
- **Relation Type:** <PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO | X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>>
- **Direction:** <DIRECTED | UNDIRECTED>
- **Assertion State:** <ASSERTED | CORROBORATED | CONFLICTED | RETIRED>
- **Related Stable IDs:** <DEP-* / DEC-* / REQ-* / EVD-* / OTHER_REFS_OR_NONE>
- **Evidence / Source Pointers:** <DURABLE_POINTERS_OR_UNKNOWN>
- **Last Verified / Reviewed:** <ISO8601_OR_UNKNOWN>
- **Notes:** <MATERIAL_NOTES_OR_NONE>

Core relation vocabulary is exactly `PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO`. Extension types must be namespaced as `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>` and must not redefine core meanings.

`DEPENDS_ON` in `REL-*` is graph linkage only. Canonical dependency-management payload remains `DEP-*` in `91`. Likewise, `DEC-*`, `REQ-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, identity, and lineage remain in their existing canonical homes.

## Reciprocal Evidence / Corroboration

`CORROBORATED` requires verified compatible authoritative assertions with matching endpoint UUIDs. Compatible core pairs include:

```text
A PARENT_OF B  ↔ B CHILD_OF A
A CHILD_OF B   ↔ B PARENT_OF A
A PEER_OF B    ↔ B PEER_OF A
A RELATED_TO B ↔ B RELATED_TO A
```

`DEPENDS_ON` and `SUPPORTS` are directional and do not require an inverse record unless the other Project independently asserts compatible truth. A derived inverse edge from an external index is not reciprocal Project evidence and never becomes another Project's assertion.

## External Derived Index Status / Pointers

```text
Owner Scope: AI_CONTROLTOWER
Authority: DERIVED_ONLY
Index Product / Runtime: <OPTIONAL_NON_AUTHORITATIVE_LABEL_OR_UNKNOWN>
Projection Freshness: <CURRENT | STALE | UNKNOWN | NOT_APPLICABLE>
Last Projection Evidence: <EVD_OR_POINTER_OR_UNKNOWN>
```

OpenViking or another indexing engine is derived and `REBUILDABLE` from authoritative Project Sources. Runtime endpoints, credentials, access tokens, secret-bearing URLs, database passwords, or comparable secrets do not belong in this document.

## Conflict / Drift Pointers

Use existing families when material:

```text
CONFLICT-* → contradictory authoritative Project assertions requiring managed resolution
DRIFT-*    → stale/orphan/misaligned derived projection that should align with Project Source
MIG-*      → Brownfield slot-92 collision or governed relation migration
```

Timestamp, ranking, similarity, or confidence score never auto-resolves authoritative Project conflict.

## Rebuild / Re-index Notes

The cross-Project derived graph may be discarded and rebuilt from current authoritative Project Sources. Rebuild may normalize inverse/symmetric traversal views, correlate reciprocal assertions, and surface stale/orphan/conflicting state, but it must not overwrite Project Source or synthesize authoritative reciprocal assertions.

## Authority Separation

```text
Project Relation
≠ Repository Location Binding
≠ File Storage Binding
≠ Local Workspace Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
≠ AUTH / Risk approval
```

`PARENT_OF` / `CHILD_OF` is semantic Project topology only. It does not require nested folders/repositories/workspaces and does not silently rewrite location, implementation, integration, runtime, or authority state.
