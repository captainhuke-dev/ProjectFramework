---
law_id: CONST-015
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: MULTI_AGENT
min_conformance: L2
---

# CONST-015 — Agent-to-agent state transfer

A handoff is a verified state transfer, not a conversation transfer.

A chat message alone is not a valid state-transfer artifact when governed continuation requires verifiable state.

The sending agent MUST identify Project/task/lineage identity, state-class authorities used, current continuation index and lineage pointer, current state, completed and incomplete work, Project-document and procedure identities when material, artifact identity, verification state, unresolved uncertainty, exact next action, and applicable checkpoint/canonical references.

The receiving agent MUST NOT assume shared memory, conversation, workspace, filesystem, branch, repository state, runtime, authority, history, context service, namespace, Project documents, procedure registry, or hidden context.

The receiver MUST verify the State Authority Map, applicable Project documents, Project Capability Pack/Procedure Registry, Current Continuation Index, lineage pointer, required artifact identity, and current state before accepting the transfer.

A sending agent's claim of completion does not establish completion for the receiver. A transfer completes on the receiving side with a receiver receipt.

Authority does not travel with state.

## State Authority Map

A Project in which more than one component or agent can hold Project state MUST define one canonical authority for each material state class. Different state classes MAY have different canonical authorities.

Reference state classes include:

```text
GOVERNANCE
SOURCE_ARTIFACTS
RUNTIME_JOBS
EVIDENCE
CONTINUATION
EXTERNAL_EFFECTS
DERIVED_CONTEXT
```

A replica, cache, semantic index, context database, local workspace, feature branch, or summary MUST declare itself derived for the relevant class unless Project Law explicitly makes it canonical and provides equivalent identity and consistency guarantees.

Two canonical authorities declared for the same state class, or two competing continuation pointers for one lineage, produce `STATE_AUTHORITY_CONFLICT` and MUST stop the affected continuation.

## Cross-agent bootstrap convergence

When a Project expects two or more agents, sessions, models, CLIs, or runtimes to collaborate, installation and material handoff MUST establish that their entrypoints resolve the same intended operating context.

At minimum, convergence comparison SHOULD include:

```text
Project identity and boundary
pinned Constitution identity
Project Law identity
State Authority Map identity
Project Document Registry identity
Project Capability Pack / Procedure Registry identity
Continuation Index and applicable lineage pointer identity
current task/artifact identity when one is in scope
```

The Standard Installation Profile requires all wrappers to route through one effective Project front door and to preserve a byte-identical shared boot contract between designated markers.

Matching path names, product names, branch labels, or service URLs alone do not prove convergence. The resolved identities and access scope must be compared.

If intended collaborators resolve different identities, cannot access a required canonical source, or disagree on the applicable lineage/artifact:

```text
BOOTSTRAP_CONVERGENCE_FAILED
```

MUST be surfaced and the affected shared work MUST NOT continue as though the agents share state.

## Local and canonical governance

A local workspace or feature branch MAY contain a pending governance proposal. It MUST NOT be treated as effective governance merely because the local agent can read it.

If local and canonical governance differ unexpectedly, the agent MUST identify whether the difference is an authorized governance-change task. Otherwise it MUST report `GOVERNANCE_DRIFT` and stop affected governed work rather than choosing silently.

## Review independence

Review types are distinct:

```text
SELF_REVIEW
INDEPENDENT_DECISION_DERIVATION
INDEPENDENT_ARTIFACT_VERIFICATION
```

For `INDEPENDENT_DECISION_DERIVATION`, the reviewer MUST form and record an initial evaluation from criteria, original inputs, and the target artifact without first receiving the author's verdict or supporting rationale.

For `INDEPENDENT_ARTIFACT_VERIFICATION`, the reviewer MAY inspect implementation rationale, but MUST independently verify the exact target artifact against governing criteria and MUST NOT rely on the author's claim of correctness.

Different agent IDs, models, sessions, or instances alone do not establish independence. A review by the author is `SELF_REVIEW` and MUST NOT be represented as independent verification.

Project/Risk Law determines which independent review type is mandatory.

A handoff MAY be indexed or summarized through a context substrate, but the receiver MUST resolve the canonical handoff/checkpoint/artifact rather than accept recalled summary as state transfer.

## Receiver-visible canonical surface

Cross-Agent continuity MUST use a canonical surface that the intended receiver can actually access through its supported access channel. A URL, path, branch label, prompt, or sender assertion alone does not prove access.

Before accepting a handoff, the receiver MUST produce or reference an access/readback receipt for the canonical front door, continuation, and material artifact identities. If the receiver cannot access or verify them, `CANONICAL_SURFACE_NOT_VISIBLE` or the registered equivalent MUST be emitted and the handoff MUST remain unaccepted.

Local uncommitted/unpublished state MUST be reported as `LOCAL_ONLY` or `PENDING_CANONICAL_PUBLICATION`; it MUST NOT be described as shared Current Truth.

<!-- END_OF_LAW: CONST-015 version=4.2.0 sha256=59d6cfeb4e1b47fdbd5b5ed4b7f8b6941c3014a741f838c49bd3ccdfe17d68e2 nonce=59d6cfeb4e1b -->
