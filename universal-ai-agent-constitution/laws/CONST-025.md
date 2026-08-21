---
law_id: CONST-025
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: ALWAYS
min_conformance: L1
---

# CONST-025 — Substantiation of claims

Governance and status claims that control work MUST be backed by an inspectable contract.

```text
No governance claim token is self-substantiating.
```

## Governance claim token

A governance claim token is a bounded status value used to authorize, block, advance, accept, publish, deploy, close, or otherwise control governed work. Ordinary factual prose remains governed by `CONST-005` and `CONST-006`; it does not become a claim token merely because it contains a claim.

Each Project MUST maintain a Claim Contract Registry for the governance tokens it uses.

Each claim contract MUST define:

```yaml
token:
meaning:
issuer_scope:
substantiating_artifact:
validation_method:
admissible_evidence_classes: []
freshness_or_expiry:
safe_fallback:
controls: []
```

## Substantiation and fallback

Whenever an agent emits a governance claim token, it MUST provide or reference the substantiating artifact required by the registered contract.

A token without its required artifact is unsubstantiated and MUST resolve to the contract's `safe_fallback`. The fallback MUST NOT be inferred as the logical opposite unless the contract explicitly defines that semantics.

An unregistered token MUST NOT authorize, advance, accept, publish, deploy, close, or unblock work. Its default interpretation is `STATUS_UNKNOWN` until a valid contract is registered.

Where a mandatory check must run whether or not it finds a problem, the contract MUST require an unconditional check receipt. Silence is not evidence that the check passed.

## Capability boundary

An agent MUST NOT omit a required artifact merely because it considers the artifact impractical, unnecessary, or disproportionate.

If the artifact is outside the attempt's proven/operating capability established before work, the agent MUST emit the registered `NOT_VERIFIABLE` or equivalent safe fallback and MUST NOT emit the positive token.

## Computed values

A hash, digest, checksum, or count MUST come from an executed tool or source system capable of producing it. An agent without that capability MUST emit `NOT_VERIFIABLE` rather than fabricate the value.

## Standard installation claim contracts

A Project claiming the Standard Installation Profile MUST register contracts for at least:

```text
INSTALLATION_VALIDATED
EFFECTIVE
GOVERNANCE_BOOT_CONFLICT
GOVERNANCE_DRIFT
PROJECT_DOCUMENTS_UNRESOLVED
PROCEDURE_MATERIALIZATION_REQUIRED
CONTINUATION_CONFLICT
BOOTSTRAP_CONVERGENCE_FAILED
```

`INSTALLATION_VALIDATED` MUST require inspectable static validation and configured-agent convergence evidence appropriate to the Project profile. Its safe fallback MUST NOT be a positive installation state.

`EFFECTIVE` MUST require a competent Project authority reference and MUST be separate from installation validation.

If the installation report, Project front door, adoption identity, State Authority Map, Project Document Registry, Capability Pack, Procedure Registry, or Continuation Index changes materially, Project Law MUST define whether prior installation/convergence evidence becomes stale and requires revalidation.

## Additional installation and publication claim contracts

A Project using Auto-Boot, multi-Agent continuation, or the Standard Installation Profile MUST register claim contracts, with non-positive safe fallbacks, for at least:

```text
PROJECT_BINDING_MATCH
AUTO_BOOT_VALID
TASK_CONTEXT_CURRENT
CANONICAL_SURFACE_VISIBLE
PLATFORM_ADAPTER_INVOKED
BASE_FRESHNESS_MATCH
ATOMIC_PUBLICATION_VERIFIED
```

`PROJECT_BINDING_MATCH` MUST require comparison of Project ID, root/boundary, repository identity, canonical ref policy, and front door.

`TASK_CONTEXT_CURRENT` MUST require a pre-write comparison of the attempt's expected and observed material identities. Its unsupported fallback MUST be `TASK_CONTEXT_UNKNOWN`, not permission to write.

`CANONICAL_SURFACE_VISIBLE` MUST require receiver-side access/readback evidence. Its absence MUST NOT be inferred as visibility.

`PLATFORM_ADAPTER_INVOKED` MUST require behavioral invocation evidence; file presence is insufficient.

`BASE_FRESHNESS_MATCH` and `ATOMIC_PUBLICATION_VERIFIED` MUST require publication-time base/ref rechecks and remote readback of the exact final tree. Their safe fallback MUST block the affected publication claim.

<!-- END_OF_LAW: CONST-025 version=4.2.0 sha256=444fb426bea20715447bd6af1ae961649d27854d49dec20482ec1bdb40082ce5 nonce=444fb426bea2 -->
