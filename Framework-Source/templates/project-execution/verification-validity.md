# Verification Validity Evaluation Template

Declarative **current proof-usability evaluation** of a historical Verification Record. Historical Verification Records are immutable; validity answers whether the historical proof can currently be used, and is **not** a rewrite of the old result.

```yaml
record_type: VERIFICATION_VALIDITY_EVALUATION
record_version: "1.0"
validity_ref: "<immutable evaluation instance>"
verification_record_ref: "<historical verification>"
evaluated_against:
  state_binding_ref: "<applicable state>"
  result_acceptance_ref: "<current applicable acceptance>"
  current_truth_ref: "<current truth>"
  dependency_state_refs: ["<dependencies>"]
  target_state_refs: ["<targets when applicable>"]
state: "CURRENT | STALE | INVALIDATED | UNKNOWN"
reason_refs: ["<reason/evidence>"]
invalidated_by: "<cause or NOT_APPLICABLE>"
evaluated_at: "<timestamp>"
```

Rules:

- State is **exactly** `CURRENT | STALE | INVALIDATED | UNKNOWN.`
  - `CURRENT`: proof remains usable for its exact applicable scope.
  - `STALE`: freshness is insufficient; incompatibility is not yet proven.
  - `INVALIDATED`: a known material incompatibility/invalidation condition exists.
  - `UNKNOWN`: current applicability cannot be established.
- A historical `PASS` is **not rewritten to `FAIL`** merely because validity changes. The Verification Record result remains exactly `PASS | FAIL | UNKNOWN` and is never overloaded with freshness states.
- Selective invalidation is allowed only when the affected scope can be bounded safely; **unknown material impact fails closed.**
- Task lifecycle eligibility and AUTH are still independent gates. Task cancellation or later AUTH revocation does not automatically rewrite technical verification truth; it blocks new governed actions according to its own authority domain.
- This file is a derived evaluation. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No verification daemon or automatic validity engine is implied by this record.
