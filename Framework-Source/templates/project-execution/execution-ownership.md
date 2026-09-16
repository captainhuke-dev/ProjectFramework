# Execution Ownership Template

Declarative records of **authoritative execution ownership** for one execution attempt. `Coordination Claim ≠ Execution Ownership Grant.` Multica remains a coordination/claim owner only; the declared execution-control owner grants authoritative execution ownership. **No executor self-grants ownership or AUTH.**

```yaml
record_type: EXECUTION_OWNERSHIP_GRANT
record_version: "1.0"
ownership_ref: "<contract-local ref>"
ownership_domain_ref: "<declared execution-control domain>"
ownership_scope_ref: "<bounded scope, normally execution attempt>"
task_ref: "TASK-xxx"
execution_ref: "<attempt>"
owner_ref: "<executor>"
ownership_epoch: "<generation within domain/scope>"
coordination_claim_ref: "<claim when applicable>"
granted_at: "<timestamp>"
validity_basis:
  mode: "LEASE_BASED | EXPLICIT_REVOCATION | SOURCE_NATIVE"
  evidence_ref: "<source-native basis>"
fencing_requirement:
  minimum_assurance: "COORDINATION_ONLY | ACCEPTANCE_FENCED | SIDE_EFFECT_FENCED"
grant_evidence_ref: "<evidence>"
```

Observed ownership state:

```yaml
record_type: EXECUTION_OWNERSHIP_EVIDENCE
record_version: "1.0"
evidence_ref: "<contract-local ref>"
ownership_ref: "<grant>"
state: "ACTIVE | SUSPECT | EXPIRED | REVOKED | COMPLETED | UNKNOWN"
observed_epoch: "<generation observed>"
source_native_evidence_ref: "<source-native observation>"
observed_at: "<timestamp>"
```

Rules:

- **Scoped epochs:** epochs are comparable only within the same ownership domain and scope. Continuous lease renewal of one ownership generation does **not** increment the epoch. Reassignment or reacquisition after ownership termination creates a **new epoch**, even if the same executor returns.
- `SUSPECT` and `UNKNOWN` are not proof of current ownership and **fail closed** where current ownership is materially required.
- Fencing assurance orders `COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED` and is evaluated **per material operation path/target**, not merely per executor. A runtime cannot silently downgrade a required assurance level.
- Unknown possibly-applied non-idempotent stale effects require `RESULT_VERIFICATION_REQUIRED` before unsafe retry or reassignment.
- Correct epoch claims do not prove producer authentication; cryptographic producer identity belongs to Wave B.
- This file is evidence/authorization metadata. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No lease service, heartbeat daemon, fencing-token generator, or automatic grant/revoke runtime is implied by these records.
