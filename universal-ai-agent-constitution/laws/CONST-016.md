---
law_id: CONST-016
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: ALWAYS
min_conformance: L2
---

# CONST-016 — Artifact identity and synchronization

A statement such as "the file was updated", "the workflow was uploaded", or "the artifact exists" is not sufficient identity.

Governed artifacts MUST use an identity appropriate to their source system.

Abstract artifact identity:

```yaml
artifact_identity:
  locator:
  version:
  integrity:
  observed_at:
  observed_by:
```

`integrity` MAY be `NOT_VERIFIABLE` when the source system provides no reliable integrity primitive and no authorized capability can compute one.

A version label alone is not artifact identity. A mutable branch, mutable URL, logical context URI, semantic-search result, memory key, vector-store object ID, path name, or tool connection name alone is not immutable identity.

Governed dependencies and extensions MUST be pinned to an immutable, verifiable identity when Project Law or the adoption contract requires immutability.

## Installed constitutional identity

A Project MUST NOT use a mutable upstream branch as its effective constitutional identity. A standard installation MUST preserve an exact local/vendored release identity and the observed upstream source identity used during installation.

The upstream installation entrypoint MAY be mutable for discovery, but it MUST resolve an exact release/commit/content identity before installation evidence or adoption is issued.

## Governance and workspace identity

The Project's effective governance source MUST identify its canonical repository/store, ref/revision policy, bootstrap path, and observed identity appropriate to the system.

A local workspace, worktree, feature branch, or uncommitted change set is a distinct artifact/state identity. An agent MUST NOT claim that local and canonical governance/artifacts match without comparing the identities required by Project Law.

Local state MUST NOT be assumed to be shared state. Upload does not equal publication. Publication does not equal receiver verification.

The State Authority Map, Project Document Registry, Project Capability Pack, Current Continuation Index and lineage pointers, claim contracts, checkpoints, handoffs, results, installation validation, and context bindings are governed artifacts and MUST carry appropriate identity.

When a context substrate points to a governed canonical artifact, the Project SHOULD preserve both the logical context locator and the canonical source identity so retrieval and verification remain separate operations.

Matching filenames, URLs, or labels with different bytes or revisions MUST produce conflict/unknown rather than equivalence.

## Task-context and publication identity

A material attempt's identity MUST include its verified Project binding, governance/Project Law identities, continuation predecessor/epoch, and artifact base identity. Reusing an earlier verification after any of these identities changes is prohibited unless a registered freshness contract explicitly proves the change is non-material to the action.

A release publication MUST identify the verified base commit or equivalent, the expected old effective ref identity, the exact final tree/artifact identities, and the validation evidence. Immediately before moving an effective ref, the publisher MUST recheck both base freshness and expected-old-ref identity.

If the base or expected old ref differs from the validated precondition, publication MUST stop with `BASE_FRESHNESS_MISMATCH`, `BASE_FRESHNESS_UNKNOWN`, or an equivalent lease failure. A force update MUST NOT silently overwrite an unexpected concurrent update.

<!-- END_OF_LAW: CONST-016 version=4.2.0 sha256=4d3d4fe77389ff2cc18fc497052dec77b891e37928b6e43df19ea880aecad677 nonce=4d3d4fe77389 -->
