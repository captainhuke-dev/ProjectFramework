# Operational Transition Record Template

Declarative evidence of one **operational state transition** on the execution aggregate. Operational state ordering belongs to the declared execution-state owner and its authoritative aggregate version; **timestamp order is audit evidence, not transition authority.**

```yaml
record_type: OPERATIONAL_TRANSITION
record_version: "1.0"
transition_id: "<unique operation ref>"
idempotency_key: "<retry identity>"
request_digest_profile_ref: "<semantic digest profile>"
request_semantic_digest: "<digest of intended semantic operation>"
aggregate_ref: "<execution aggregate>"
expected_version: "<version>"
expected_state: "<state>"
requested_state: "<state>"
observed_before:
  state: "<state observed before evaluation>"
  version: "<version observed before evaluation>"
causation_ref: "<cause>"
correlation_ref: "<correlation>"
authority_refs: ["<authority>"]
ownership_evidence_ref: "<ownership>"
state_binding_ref: "<binding when applicable>"
result: "ACCEPTED | DUPLICATE_ACCEPTED | VERSION_CONFLICT | STATE_CONFLICT | AUTHORITY_REJECTED | OWNERSHIP_REJECTED | PRECONDITION_REJECTED | INVALID_TRANSITION | IDEMPOTENCY_CONFLICT | UNKNOWN"
resulting_state: "<state after outcome, when known>"
resulting_version: "<version after outcome, when known>"
source_native_evidence_ref: "<source-native observation>"
observed_at: "<timestamp>"
```

Rules:

- **Exact duplicate recognition precedes generic CAS conflict handling:** first resolve whether the same idempotency operation was already durably accepted; an exact accepted duplicate returns `DUPLICATE_ACCEPTED`; the same idempotency key with a different semantic request fingerprint returns `IDEMPOTENCY_CONFLICT.` Only then evaluate expected version/state, authority/ownership/preconditions, atomic application, and observed outcome.
- A **timeout is not evidence of failure.** `UNKNOWN` requires authoritative reconciliation at the truth owner before unsafe retry.
- Timestamps never own order; the aggregate version does.
- This record is evidence of what the state owner observed/applied; it does **not** itself become the state authority.
- This file is evidence. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime CAS store, idempotency store, automatic transition engine, or state engine is implied by this record.
