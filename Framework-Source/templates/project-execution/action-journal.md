# Action / Effect Journal Template

Declarative conceptual shape for one independently reconcilable Action/Material Effect. This is not an instruction to store an unbounded runtime log in Project Source; the authoritative fine-grained stream belongs to the runtime domain.

```yaml
record_type: ACTION_EFFECT
record_version: "1.0"
execution_id: "<execution id>"
attempt_id: "<attempt id>"
action_id: "<durable action id>"
action_hash: "<canonical action fingerprint>"
state: "<PROPOSED | PREPARED | PERMITTED | DISPATCH_INTENT_RECORDED | DISPATCHED | ACKNOWLEDGED | RECONCILING | APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED>"

permit_ref: "<Effect Permit ref or NOT_APPLICABLE>"

target:
  target_ref: "<exact target>"
  precondition_ref: "<source-native precondition or EXPLICITLY_UNSUPPORTED>"

effect_semantics:
  idempotency: "<IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN>"
  reconciliation: "<NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE>"
  reversibility: "<REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN>"

source_native_result:
  evidence_refs:
    - "<evidence ref>"
  observed_result: "<APPLIED | NOT_APPLIED | AMBIGUOUS | UNKNOWN>"

cancellation:
  requested: "<true | false>"
  observed_at: "<time or NOT_APPLICABLE>"

compensation:
  action_ref: "<separate compensation action or NOT_APPLICABLE>"
  result: "<NOT_APPLICABLE | APPLIED | FAILED | PARTIALLY_COMPENSATED | AMBIGUOUS>"

secret_safe_representation:
  policy: "<REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata>"
```

Rules:

- `ACKNOWLEDGED ≠ resulting-state proof`.
- `PERMIT_CONSUMED ≠ effect APPLIED`.
- Possibly dispatched actions reconcile before retry/fallback.
- `NON_IDEMPOTENT|UNKNOWN + reconciliation NONE + AMBIGUOUS` requires manual/blocking resolution; no automatic retry.
- Cancellation prevents new governed dispatch but does not erase already-caused external facts.
- Compensation is a distinct governed Material Effect, not history erasure.
- Raw secret values are not persisted merely for observability.