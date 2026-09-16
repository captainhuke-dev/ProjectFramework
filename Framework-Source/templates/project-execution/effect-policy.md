# Effect Policy Template

Declarative consequence-boundary policy for Material Effects. Effect policy narrows/mediates execution; it never grants AUTH.

```yaml
effect_policy:
  policy_version: "1.0"
  effect_class: "<bounded material effect class>"
  effect_surfaces:
    - surface: "<MCP | SHELL | NETWORK | GIT_SSH | CLOUD | FILESYSTEM | CONTAINER_SOCKET | DATABASE | SDK | CHILD_PROCESS | OTHER>"
      control: "MEDIATED_BY_EFFECT_GATEWAY | EXPLICITLY_PROHIBITED | CONFINED"
      basis: "<enforcement basis>"
  credential_boundary:
    raw_mutation_credential_in_executor: false
    broker_or_gateway_ref: "<ref or NOT_APPLICABLE>"
  target_precondition:
    support: "SUPPORTED | UNSUPPORTED"
    mechanism: "<SHA | ETAG | RESOURCE_VERSION | ROW_VERSION | OBJECT_HASH | CAS | OTHER | NOT_APPLICABLE>"
    mismatch_result: "PRECONDITION_CONFLICT"
    unsupported_recovery: "<reconciliation/fail-closed strategy when unsupported>"
  idempotency: "IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN"
  reconciliation: "NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK | NATIVE_READBACK | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE"
  reversibility: "REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN"
  permit:
    required: true
    max_uses: 1
    transferable: false
    binds: [execution_id, attempt_id, action_id, action_hash, target_ref, tool_ref, runtime_generation, fence_epoch, task_contract_fingerprint, execution_envelope_fingerprint]
  cancellation:
    new_dispatch_after_cancel: FORBIDDEN
    in_flight_result: RECONCILE_SOURCE_NATIVE
  compensation:
    treated_as_new_effect: true
  ambiguous_without_reconciliation: "MANUAL_RESOLUTION_REQUIRED"
```

Conformance rules:

- Every governed Material Effect path is mediated or prohibited/confined.
- Policy text alone is not effect-surface closure.
- A supported target precondition mismatch yields `PRECONDITION_CONFLICT`; it is never silently dispatched against a materially different target.
- `Effect Permit ≠ AUTH`; `Gateway eligibility ≠ AUTH`; `Tool availability ≠ eligibility`.
- Permit mint/consume is atomic/CAS-equivalent and stale generation/fence or replay/transfer is rejected.
- One Permit maps to one independently reconcilable Material Effect unless a verified source-native atomic transaction makes a compound operation one reconcilable unit.
- Arbitrary external exactly-once execution is not claimed.
- Unreconcilable ambiguous non-idempotent/unknown effect is blocked/manual-resolution, not automatically retried.
- Compensation is a separately governed effect; `Compensation ≠ rollback`.
