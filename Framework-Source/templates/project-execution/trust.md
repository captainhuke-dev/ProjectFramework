# Security & Trust Boundary Profile Template

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
surfaces:
  - surface_id: "repository"
    surface_type: "REPOSITORY | WORKSPACE | TOOL_MCP | AGENT_MODEL | EXTERNAL_SERVICE | ARTIFACT | RUNTIME | EFFECT_GATEWAY | DEPLOYMENT_TARGET | OTHER"
    trust_class: "TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN"
    source_ref: "<BOUND_PROJECT_OR_SOURCE_NATIVE_POINTER>"
    allowed_crossings: ["DATA_READ", "DATA_WRITE", "CODE_EXECUTION", "ARTIFACT_TRANSFER", "EXTERNAL_DISCLOSURE", "PRIVILEGED_OPERATION"]
    review_trigger: "<EVENT_OR_NOT_APPLICABLE>"

runtime_boundaries:
  runtime_store: "<surface_id or NOT_APPLICABLE>"
  executor_workspace: "<surface_id or NOT_APPLICABLE>"
  effect_gateway: "<surface_id or NOT_APPLICABLE>"
  source_native_target: "<surface_id or NOT_APPLICABLE>"
  mutation_secret_holder: "<trusted boundary reference or NOT_APPLICABLE>"
```

Core rules:

```text
Trust classification ≠ Authority
Trusted/Privileged surface ≠ AUTH
Trusted surface ≠ permission to disclose secrets
Tool eligibility ≠ trust equivalence
Capability ≠ trust ≠ authority
UNKNOWN trust for materially sensitive action → VERIFICATION_REQUIRED / fail closed
Effect Gateway trust ≠ permission; Gateway still requires current AUTH/R4/fence/preconditions
```

- `PRIVILEGED` means elevated consequence, not greater authority or general trust.
- `EXTERNAL` means outside Project-local control and still requires purpose-specific disclosure/authority review.
- `surface_id` is profile-local metadata, not a Project Stable ID, secret value, hostname authority, MCP workspace identity, or Project Location Binding.
- When TASK-058 runtime control applies, runtime store, executor workspace, Effect Gateway, source-native target, and mutation-secret boundary are treated as distinct trust surfaces when materially different.
- An executor workspace that retains an uncontrolled equivalent Material-Effect route cannot satisfy effect-surface closure merely because the Gateway is trusted.
- Material crossings still require applicable provenance, tool/capability eligibility, TASK-026 disclosure/secret checks, AUTH/Risk/Decision/shared-state gates, and TASK-058 runtime/effect checks when applicable.
- Actual secret values MUST NOT be stored here or copied into runtime journal/checkpoint/evidence merely for observability.
- Brownfield adoption never infers trust merely from successful prior use.
- TASK-057 filter-before-rank remains authoritative; UNKNOWN trust for materially sensitive work fails closed before preference ranking.
