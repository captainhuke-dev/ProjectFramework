# Action Journal Template

Declarative shape for fine-grained runtime Action/Effect observation. This is a runtime-domain contract starter, not an instruction to store an unbounded operational log inside Project Source.

```yaml
action_effect:
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  action_id: "<durable action id>"
  action_hash: "<canonical action fingerprint>"
  action_state: "PROPOSED | PREPARED | PERMITTED | DISPATCH_INTENT_RECORDED | DISPATCHED | ACKNOWLEDGED | RECONCILING | APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED"
  permit_ref: "<Effect Permit ref or NOT_APPLICABLE>"
  target_ref: "<exact target>"
  target_precondition_ref: "<precondition or explicit unsupported classification>"
  effect_semantics:
    idempotency: "IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN"
    reconciliation: "NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK | NATIVE_READBACK | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE"
    reversibility: "REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN"
  source_native_evidence_refs:
    - "<evidence ref>"
  cancellation_ref: "<ref or NOT_APPLICABLE>"
  compensation_action_ref: "<ref or NOT_APPLICABLE>"
  durable_argument_representation: "REFERENCE_ONLY | REDACTED | HASH_ONLY | CLASSIFIED_METADATA"
```

Rules:

- `ACKNOWLEDGED ≠ APPLIED` unless the source-native protocol makes acknowledgement authoritative for the relevant result.
- `PERMIT_CONSUMED ≠ effect APPLIED`.
- Possible dispatch with unknown result enters reconciliation; blind retry is prohibited when duplicate effect cannot be ruled out.
- Compensation is a new governed Action/Effect, not history erasure.
- Raw secret values MUST NOT be persisted merely for observability.
- Executor/model processes cannot authoritatively rewrite runtime journal truth.
