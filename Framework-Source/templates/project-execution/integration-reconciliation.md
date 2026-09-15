# Integration Reconciliation Template

Declarative **derived** reconciliation record for one integration. It captures how a verified candidate related to the canonical resulting state after integration.

```yaml
record_type: INTEGRATION_RECONCILIATION
record_version: "1.0"
task_ref: "TASK-xxx"
verified_candidate_sha: "<exact verified candidate commit SHA>"
integration_strategy: "FAST_FORWARD_EXACT | MERGE_COMMIT_PRESERVING_CANDIDATE | TRANSFORMING_INTEGRATION"
target: "<canonical integration target ref>"
pre_integration_target_sha: "<exact target SHA before integration>"
resulting_sha: "<exact resulting SHA after integration>"
candidate_relation: "<how the resulting state relates to the verified candidate>"
verification_state: "REUSED_EXACT | REVERIFIED | REUSE_NOT_SHOWN"
source_native_evidence:
  - "<Git/GitHub or source-native evidence reference>"
result: "PASS | FAIL | UNKNOWN"
```

Rules:

- Git / the declared canonical Git hosting target remains the **source of truth** for Git integration facts. This record is a derived reconciliation, not that truth.
- `FAST_FORWARD_EXACT`: the canonical result equals the verified candidate; `verification_state` may be `REUSED_EXACT.`
- `MERGE_COMMIT_PRESERVING_CANDIDATE`: candidate proof is retained about that candidate, but the canonical resulting state requires this reconciliation.
- `TRANSFORMING_INTEGRATION` (squash/rebase/conflict-resolution/cherry-pick): candidate verification is **not** automatically inherited. `verification_state: REUSED_EXACT` requires deterministic exact-equivalence evidence, and exact-equivalence proof reuse covers only the proof domains where equivalence was actually shown. Otherwise `REVERIFIED` is required.
- `verification_state: REUSE_NOT_SHOWN` means no equivalence was shown; the canonical result must be reverified.
- `result` is exactly `PASS | FAIL | UNKNOWN.`
- Unknown shared/non-idempotent outcomes use `RESULT_VERIFICATION_REQUIRED`; no blind retry is allowed after an ambiguous push/merge response.
- This file is a derived reconciliation record. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, Git truth, or a Stable-ID family.
- No runtime, merge bot, merge queue, or automatic reconciler is implied by this record.
