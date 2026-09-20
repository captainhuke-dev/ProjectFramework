# Execution State Binding Template

Declarative **immutable** description of the exact materially relevant execution state for one execution attempt. The binding is evidence, not authority.

```yaml
record_type: EXECUTION_STATE_BINDING
record_version: "1.0"
state_binding_ref: "<contract-local reference>"
project_ref: "<Project>"
task_ref: "TASK-xxx"
execution_ref: "<runtime/contract-local execution attempt>"
digest_profile_ref: "<canonicalization + digest profile>"
source_state:
  revision_set_ref: "<Revision Set>"
  revision_set_digest: "<digest>"
execution_inputs:
  input_manifest_ref: "<Input Manifest>"
  input_manifest_digest: "<digest>"
current_truth:
  r4_context_ref: "<state-bound R4 observation>"
  observed_revision_or_digest: "<when source supports it>"
  observed_at: "<timestamp>"
authority:
  authority_refs: ["<AUTH/user authority refs>"]
  evaluation_ref: "<state-bound dispatch evaluation>"
  observed_revision_or_digest: "<when source supports it>"
  evaluated_at: "<timestamp>"
ownership:
  ownership_ref: "<grant>"
  ownership_domain_ref: "<domain>"
  ownership_scope_ref: "<scope>"
  owner_ref: "<executor>"
  ownership_epoch: "<scoped generation>"
  assurance_at_dispatch: "COORDINATION_ONLY | ACCEPTANCE_FENCED | SIDE_EFFECT_FENCED"
  ownership_evidence_ref: "<state-bound evidence>"
workspace:
  workspace_ref: "<governed workspace>"
  workspace_identity_ref: "<state-bound identity>"
  observed_at: "<timestamp>"
completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
binding_digest: "<semantic digest>"
binding_created_at: "<timestamp>"
```

Rules:

- The binding references the **already-issued** Execution Ownership Grant and epoch. The grant MUST precede binding finalization; a binding that references an ownership state which does not yet exist is `INCOMPLETE.`
- Binding references that affect immutable identity MUST resolve to **state-bound/reconstructable evidence.** A mutable `current`, branch, locator, or `latest` pointer alone is insufficient historical binding evidence.
- The binding is **immutable historical evidence, not perpetual authority.** A complete binding does not make authority, ownership, R4, or downstream eligibility permanently valid; material mutable truth is fresh-revalidated at the appropriate boundary.
- A new world state causes **revalidation or a new binding, never a rewrite** of the historical binding.
- This file is evidence. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, state engine, or automatic binder is implied by this record.
