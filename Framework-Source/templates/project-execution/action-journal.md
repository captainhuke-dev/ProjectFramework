# Action Journal Template

Declarative shape for fine-grained runtime Action/Effect observation. This is a runtime-domain contract starter, not an instruction to store an unbounded operational log inside Project Source.

```yaml
runtime_event:
  event_id: "<immutable unique event id within this execution>"
  execution_id: "<execution id>"
  event_sequence: "<strict contiguous monotonic sequence>"
  previous_event_id: "<immediately preceding event id, or NOT_APPLICABLE for first event>"
  event_type: "<bounded runtime event type>"
  event_payload_hash: "<canonical fingerprint of immutable event payload>"
  state_version_before: "<expected runtime state version before applying event>"
  state_version_after: "<resulting runtime state version after applying event>"
  observed_at: "<runtime-observed timestamp; telemetry, not ordering authority>"

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

- Runtime Journal ingestion is identity- and sequence-governed. `event_id` is immutable and unique within the Execution; `event_sequence` is contiguous/monotonic and is the ordering authority, while timestamps are telemetry only.
- Re-delivery of the same already-committed `event_id` with the same `event_payload_hash` is an idempotent duplicate observation: it MUST NOT append a second authoritative event, advance `state_version` again, or repeat an Action/Effect.
- Reuse of an already-committed `event_id` with a different `event_payload_hash`/immutable payload is `EVENT_IDENTITY_CONFLICT` and fails closed as `RECOVERY_BLOCKED` (or equivalent) until reconciled.
- Reuse of an existing `event_sequence` with a different `event_id`/payload is `EVENT_SEQUENCE_CONFLICT` and fails closed as `RECOVERY_BLOCKED` (or equivalent) until reconciled.
- An event whose `event_sequence` is greater than the next expected contiguous sequence is `EVENT_GAP`; it is quarantined/not authoritatively applied until missing predecessor continuity is proven. The runtime MUST NOT reorder authoritative history by timestamp or infer missing events.
- An event may transition runtime state only when `state_version_before` matches the current authoritative version and its identity/sequence/predecessor checks pass; stale or conflicting deliveries reload/reconcile rather than creating a second transition.
- `ACKNOWLEDGED ≠ APPLIED` unless the source-native protocol makes acknowledgement authoritative for the relevant result.
- `PERMIT_CONSUMED ≠ effect APPLIED`.
- Possible dispatch with unknown result enters reconciliation; blind retry is prohibited when duplicate effect cannot be ruled out.
- Compensation is a new governed Action/Effect, not history erasure.
- Raw secret values MUST NOT be persisted merely for observability.
- Executor/model processes cannot authoritatively rewrite runtime journal truth.
