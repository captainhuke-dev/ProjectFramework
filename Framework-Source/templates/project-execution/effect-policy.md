# Effect Policy / Effect Permit Template

Declarative **Material-Effect mediation** contract: which effect classes are mediated, their semantics, and the single-use permit shape that gates their dispatch. The permit is never `AUTH-*.`

```yaml
record_type: EFFECT_POLICY
record_version: "1.0"
policy_ref: "<contract-local reference>"
effect_class: "<declared effect class>"
mediation: "MEDIATED_BY_EFFECT_GATEWAY | EXPLICITLY_PROHIBITED | CONFINED"
idempotency_class: "IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN"
reversibility_class: "REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN"
reconciliation_class: "NATIVE_READBACK | IDEMPOTENCY_KEY | COMPARE_AND_SET | EXTERNAL_CONFIRMATION | HUMAN_VERIFICATION | NONE"
target_precondition_support: "SUPPORTED | NOT_SUPPORTED | UNKNOWN"
credential_placement: "AT_OR_BELOW_GATEWAY | DECLARED_ALTERNATIVE"
```

```yaml
record_type: EFFECT_PERMIT
record_version: "1.0"
permit_id: "<unique id>"
execution_id: "<execution id>"
attempt_id: "<attempt id>"
action_id: "<action id>"
action_hash: "<canonical action fingerprint>"
target_ref: "<exact governed target>"
tool_ref: "<eligible effect tool>"
runtime_generation: "<control generation>"
fence_epoch: "<epoch within generation>"
ownership_epoch: "<Wave A V2 ownership epoch>"
task_contract_fingerprint: "<fingerprint>"
execution_envelope_fingerprint: "<fingerprint>"
authority_ref: "<AUTH-* or explicit authority ref>"
r4_context_ref: "<fresh current truth ref>"
target_precondition_ref: "<precondition>"
issued_at: "<runtime-authoritative time>"
expires_at: "<short validity boundary>"
max_uses: 1
```

Rules:

- For a mediated effect class the governed path is: `executor proposal → fresh authority/current-truth/precondition evaluation → Effect Permit → Gateway dispatch → source-native reconciliation.` A direct uncontrolled mutation path for a mediated class is **non-conforming.**
- The permit is **short-lived, single-use, non-transferable**, and bound to execution/attempt/action identity, exact target/tool/effect digest, applicable ownership epoch, and runtime control generation. `Effect Permit != AUTH-*.`
- `PERMIT_ACTIVE → PERMIT_CONSUMED` is atomic/compare-and-set equivalent. Reuse, transfer, action/target mismatch, stale generation, stale fence, or expiry produces **rejection**, not fallback inference.
- `PERMIT_CONSUMED` proves dispatch-eligibility consumption only; it does not prove the external effect was applied.
- One permit corresponds to one **independently reconcilable Material Effect** unless a verified source-native atomic transaction justifies grouping. Composite intent is normally decomposed.
- Effects are classified by idempotency and reversibility; no arbitrary exactly-once claims. After a possibly-dispatched effect with unknown result: `UNKNOWN → reconcile at source-native truth owner → APPLIED | NOT_APPLIED | PARTIAL | STILL_UNKNOWN.` Unsafe blind retry is prohibited.
- Raw mutation credentials SHOULD reside at or below the Gateway boundary; every effect-capable surface for a mediated class is `MEDIATED_BY_EFFECT_GATEWAY` or `EXPLICITLY_PROHIBITED / CONFINED.`
- This file is policy/permit evidence. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No Effect Gateway service, permit store, credential broker, or dispatch engine is implied by this record.
