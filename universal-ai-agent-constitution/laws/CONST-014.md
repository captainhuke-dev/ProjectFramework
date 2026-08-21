---
law_id: CONST-014
version: 4.2.0
status: ACTIVE
derogation: STRICTER_ONLY
applies_when: ALWAYS
min_conformance: L2
---

# CONST-014 — Checkpoint and context continuity

Conversation memory is temporary. Continuation state MUST be durable when loss of context would materially impair safe continuation.

Projects MUST define checkpoint and continuation policy.

A checkpoint MUST be written before a foreseeable session/context termination and before a handoff under `CONST-015`. Project Law MAY add triggers and MUST NOT remove this floor.

Further triggers SHOULD include task start, material decision, before and after external effects, verification completion, blocker, authority change, unexpected stop, and terminal closure.

A checkpoint MUST NOT store passwords, tokens, private keys, secret values, or private chain-of-thought.

A checkpoint SHOULD preserve checkpoint ID, parent checkpoint, Project ID, lineage/task/job identity, actor identity, governance identity, objective, current state, completed work, pending work, exact next action, artifact identity, verification state, uncertainties, blockers, canonical references, and creation time.

## Project Continuation Index

A multi-session or multi-agent Project MUST maintain a receiver-verifiable route to current and recent work under the `CONTINUATION` state class in its State Authority Map.

The Standard Installation Profile uses:

```text
governance/CURRENT-CONTINUATION.yaml
```

as a **Project Continuation Index**. The index routes each active or retained lineage to its own continuation pointer. It MUST NOT be interpreted as one global single-task pointer when independent lineages can coexist.

The index MUST identify:

```text
Project identity
index identity and monotonic epoch or equivalent conflict detector
current focus lineage when one is declared
active/recent lineage IDs
lineage status
pointer locator and identity for each lineage
artifact identity when material
predecessor index identity
canonical continuation authority
```

## Lineage continuation pointer

Each material lineage MUST have a durable pointer or equivalent canonical record identifying:

```text
lineage/task/job identity
status and current actor
completed and pending work
artifacts and verification state
blockers and unresolved uncertainty
checkpoint/handoff references
exact next action
governance/document/procedure identities
epoch and predecessor/update precondition
```

Competing current pointers for the same lineage, or an update whose predecessor/precondition does not match the current canonical state, MUST produce `CONTINUATION_CONFLICT` rather than last-write-wins reconciliation.

Independent lineages SHOULD update independently so one slow or disputed lineage does not block unrelated continuation.

The Project Continuation Index and lineage pointers SHOULD be reconstructable from durable continuation records so no single pointer file is the only surviving state.

## Terminal retention

A lineage that reaches `CLOSED`, `FAILED`, `CANCELLED`, `ABANDONED`, or `SUPERSEDED` MUST remain reconstructible through a terminal pointer/receipt or history route. Terminal state MUST NOT disappear merely because no further action is scheduled.

A terminal pointer MUST identify final result/artifact state, verification/closure evidence, remaining limitations, and `exact_next_action`, which MAY be `NONE`.

## Storage and update cadence

Effective constitutional governance and high-churn continuation state MAY have different canonical stores. Project Law MAY place continuation in Project files, a dedicated state branch, a ledger, or another system, provided the State Authority Map declares one canonical authority and equivalent identity/conflict/retention guarantees.

A Project MUST NOT force high-frequency runtime state into its governance source merely for path uniformity when that creates unsafe write contention or bypasses governance change review.

A new session MUST NOT reconstruct prior state from memory when a valid checkpoint, continuation index/pointer, or canonical source is available.

Context-system memory, session summaries, and automatic memory extraction MAY assist continuity, but they do not replace a required checkpoint, continuation index, lineage pointer, or terminal receipt.

A substrate-specific `commit accepted`, `memory extracted`, or `session archived` status MUST NOT be interpreted as constitutional checkpoint completion unless Project Law explicitly maps and verifies it.

## Attempt preconditions and pre-write recheck

A material work attempt MUST record or otherwise preserve the governance identity, Project Law identity, continuation index/pointer identity, and artifact base identity on which the attempt began.

Immediately before a material write, commit, push, merge, state transition, publication, deployment, checkpoint, or handoff, the acting component MUST recheck the applicable attempt preconditions against canonical state.

If a material observed identity or predecessor changed, the attempt MUST produce `TASK_CONTEXT_STALE` and MUST NOT use last-write-wins. The work MAY be reconciled, rebased, superseded, or restarted only through an authorized new/updated attempt.

## Visibility state

Continuation and checkpoint records MUST distinguish local-only state from state exposed on a mutually accessible canonical surface. Reference visibility states include `LOCAL_ONLY`, `PENDING_CANONICAL_PUBLICATION`, `CANONICAL_VISIBLE`, and `REMOTE_STALE`.

A local checkpoint MAY preserve work, but it MUST NOT be represented as receiver-visible until the intended receiver can read and verify the referenced canonical surface and identity.

<!-- END_OF_LAW: CONST-014 version=4.2.0 sha256=a4b6830c8f37d5e9faeaab0aa69a536d07967a39077f2f505033f4e62a85098a nonce=a4b6830c8f37 -->
