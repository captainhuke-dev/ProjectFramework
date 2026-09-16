# Execution Input Manifest Template

Declarative record of **which materially relevant execution inputs** participated in one execution attempt. The Revision Set answers which source state; the Input Manifest answers which material inputs.

```yaml
record_type: EXECUTION_INPUT_MANIFEST
record_version: "1.0"
input_manifest_ref: "<contract-local reference>"
source_revision_set_ref: "<Revision Set>"
digest_profile_ref: "<canonicalization + digest profile>"
toolchain:
  - tool_ref: "<tool>"
    version_or_digest: "<exact observed identity>"
dependencies:
  - dependency_manifest_ref: "<lock/manifest source>"
    digest: "<digest>"
configuration:
  - config_ref: "<material config>"
    revision_or_digest: "<exact observed identity>"
feature_state:
  - flag_set_ref: "<material flag set>"
    revision_or_digest: "<exact observed identity>"
schemas:
  - system_ref: "<system>"
    revision: "<revision>"
external_contracts:
  - contract_ref: "<contract>"
    version_or_digest: "<identity>"
material_inputs:
  - input_ref: "<material input>"
    revision_or_digest: "<identity>"
environment_constraints:
  - constraint_ref: "<declared environment constraint, if material>"
completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
manifest_digest: "<semantic digest>"
created_at: "<timestamp>"
```

Rules:

- Only input classes **declared materially relevant** by the Task Contract, Plan Contract, Execution Envelope, Project-specific requirement, or applicable policy participate in binding identity. Irrelevant environment noise does not invalidate an execution.
- A **required unknown material input prevents a complete manifest.** A requirement cannot be relaxed post hoc merely to make an execution complete.
- **Actual secret values MUST NOT enter the manifest.** Only non-secret references/revisions/digests may be recorded where required; `17 Secret Reference Registry` remains reference-only.
- Mutable business/runtime facts remain R4 current truth unless deliberately and lawfully frozen as execution inputs.
- Once referenced by an Execution State Binding, the Input Manifest is immutable evidence; source change produces a new manifest, never a rewrite.
- This file is evidence. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, dependency scanner, or automatic manifest builder is implied by this record.
