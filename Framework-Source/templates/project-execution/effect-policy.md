# Effect Policy Template

Declarative consequence-boundary policy for Material Effects. Effect policy narrows/mediates execution; it never grants AUTH.

```yaml
effect_policy:
  policy_version: "1.0"
  effect_class: "<bounded material effect class>"
  effect_surface_closure:
    inventory_state: "COMPLETE | INCOMPLETE | UNKNOWN"
    expected_surface_classes:
      - "<MCP | SHELL | NETWORK | GIT_SSH | CLOUD | FILESYSTEM | CONTAINER_SOCKET | DATABASE | SDK | CHILD_PROCESS | OTHER>"
    all_governed_routes_accounted_for: "<true | false>"
    closure_state: "PROVEN | NOT_PROVEN | NOT_APPLICABLE"
    closure_evidence_refs:
      - "<independently reviewable confinement/mediation evidence ref, or NOT_APPLICABLE: <reason>>"
  effect_surfaces:
    - surface: "<MCP | SHELL | NETWORK | GIT_SSH | CLOUD | FILESYSTEM | CONTAINER_SOCKET | DATABASE | SDK | CHILD_PROCESS | OTHER>"
      route_ref: "<bounded route/tool/process/network/credential path>"
      control: "MEDIATED_BY_EFFECT_GATEWAY | EXPLICITLY_PROHIBITED | CONFINED"
      enforcement_basis: "<enforcement mechanism/boundary>"
      evidence_ref: "<source-native or reviewable evidence ref>"
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
    binds: [execution_id, attempt_id, action_id, action_hash, target_ref, tool_ref, runtime_generation, fence_epoch, task_contract_fingerprint, execution_envelope_fingerprint, authority_ref, r4_context_ref]
    freshness:
      issued_at: "<runtime-authoritative timestamp>"
      expires_at: "<short validity boundary>"
      expired_permit_result: REJECT
  cancellation:
    new_dispatch_after_cancel: FORBIDDEN
    in_flight_result: RECONCILE_SOURCE_NATIVE
  compensation:
    treated_as_new_effect: true
  ambiguous_without_reconciliation: "MANUAL_RESOLUTION_REQUIRED"
```

Conformance rules:

- Every governed Material Effect path is mediated or prohibited/confined.
- `effect_surface_closure.closure_state: PROVEN` is valid only when `inventory_state: COMPLETE`, `all_governed_routes_accounted_for: true`, every expected applicable effect-surface class is represented, every governed route is mapped to `MEDIATED_BY_EFFECT_GATEWAY | EXPLICITLY_PROHIBITED | CONFINED`, and independently reviewable closure evidence exists for those controls. Missing/unknown surface coverage or evidence forces `NOT_PROVEN` for autonomous Material-Effect eligibility.
- Policy text, a self-declared `PROVEN` value, or executor attestation alone is not effect-surface closure.
- A supported target precondition mismatch yields `PRECONDITION_CONFLICT`; it is never silently dispatched against a materially different target.
- `Effect Permit ≠ AUTH`; `Gateway eligibility ≠ AUTH`; `Tool availability ≠ eligibility`.
- Every Gateway-mediated Permit is bound to current `authority_ref` and `r4_context_ref`, is minted with runtime-authoritative `issued_at` plus short-lived `expires_at`, and is rejected after expiry; stale AUTH/R4 cannot be preserved merely because an earlier Permit existed.
- Permit mint/consume is atomic/CAS-equivalent and stale generation/fence or replay/transfer is rejected.
- One Permit maps to one independently reconcilable Material Effect unless a verified source-native atomic transaction makes a compound operation one reconcilable unit.
- Arbitrary external exactly-once execution is not claimed.
- Unreconcilable ambiguous non-idempotent/unknown effect is blocked/manual-resolution, not automatically retried.
- Compensation is a separately governed effect; `Compensation ≠ rollback`.
