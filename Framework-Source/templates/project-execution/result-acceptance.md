# Result Acceptance Template

Declarative **state-bound derived evaluation** of whether a Task Record observation may be promoted toward governed verification. `Task Record observation ≠ Result Acceptance.` Result Acceptance is not a new canonical truth owner; it consumes the applicable canonical/source-native truths.

```yaml
record_type: RESULT_ACCEPTANCE
record_version: "1.0"
acceptance_ref: "<immutable evaluation instance>"
task_ref: "TASK-xxx"
execution_ref: "<attempt>"
task_record_ref: "<observation>"
state_binding_ref: "<binding>"
evaluated_against:
  task_lifecycle_ref: "<Task Source observation>"
  authority_evaluation_ref: "<fresh AUTH evaluation>"
  ownership_evidence_ref: "<fresh ownership evidence>"
  r4_context_ref: "<fresh applicable current truth>"
  operational_aggregate_ref: "<aggregate>"
  aggregate_version: "<version>"
disposition: "ELIGIBLE | STALE_OWNERSHIP | TASK_NOT_ACTIVE | AUTHORITY_INVALID | STATE_BINDING_INVALIDATED | DUPLICATE | STATE_CONFLICT | RESULT_IDENTITY_INCOMPLETE | PRECONDITION_FAILED | UNKNOWN"
evidence_refs: ["<evidence>"]
evaluated_at: "<timestamp>"
```

Rules:

- Disposition is **exactly** the ten values above. Observed execution success is not result eligibility; observed failure may still be a valid governed result for verification/recovery.
- **Historical acceptance evaluations are immutable.** Current promotability uses the exact latest applicable state-bound evaluation for the current decision boundary; no global newest-timestamp rule is implied.
- A stale ownership result remains historical evidence but **cannot be promoted.** Cancellation, authority invalidity, incomplete result identity, or unresolved material truth similarly block promotable verification.
- Promotable verification starts only from a current applicable `ELIGIBLE` acceptance.
- This file is a derived evaluation. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No automatic acceptance engine or runtime is implied by this record.
