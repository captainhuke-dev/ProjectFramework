# Security & Trust Boundary Profile Template

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
surfaces:
  - surface_id: "repository"
    surface_type: "REPOSITORY | WORKSPACE | TOOL_MCP | AGENT_MODEL | EXTERNAL_SERVICE | ARTIFACT | RUNTIME | EFFECT_GATEWAY | CREDENTIAL_BOUNDARY | DEPLOYMENT_TARGET | OTHER"
    trust_class: "TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN"
    source_ref: "<BOUND_PROJECT_OR_SOURCE_NATIVE_POINTER>"
    allowed_crossings: ["DATA_READ", "DATA_WRITE", "CODE_EXECUTION", "ARTIFACT_TRANSFER", "EXTERNAL_DISCLOSURE", "PRIVILEGED_OPERATION"]
    review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
runtime_boundaries:
  runtime_store_ref: "<runtime surface or NOT_APPLICABLE>"
  executor_workspace_ref: "<executor surface or NOT_APPLICABLE>"
  effect_gateway_ref: "<gateway surface or NOT_APPLICABLE>"
  credential_boundary_ref: "<credential surface or NOT_APPLICABLE>"
  source_native_target_refs:
    - "<target surface or NOT_APPLICABLE>"
```

Core rules:

```text
Trust classification ≠ Authority
Trusted surface ≠ permission to disclose secrets
Tool eligibility ≠ trust equivalence
Capability ≠ trust ≠ authority
Runtime trust ≠ AUTH
Effect Gateway trust ≠ AUTH
UNKNOWN trust for materially sensitive action → VERIFICATION_REQUIRED / fail closed
```

- `PRIVILEGED` means elevated consequence, not greater authority or general trust.
- `EXTERNAL` means outside Project-local control and still requires purpose-specific disclosure/authority review.
- `surface_id` is profile-local metadata, not a Project Stable ID, credential, hostname authority, MCP workspace identity, Project Location Binding, Effect Permit, or runtime authority grant.
- Material data/code/artifact/execution crossings require applicable provenance, tool eligibility, capability eligibility, TASK-026 disclosure/secret checks, and AUTH/Risk/Decision/shared-state gates.
- When deterministic runtime/effect mediation applies, treat Runtime Store, Executor workspace, Effect Gateway, source-native target, and credential boundary as independently reviewable trust surfaces rather than one implicit trusted process.
- A model/RLM/child workspace that can directly reach a mutation credential or uncontrolled effect route does not satisfy autonomous Effect-Surface Closure merely because the Effect Gateway itself is trusted.
- Runtime Event Journal/checkpoint/evidence stores use minimum durable secret-safe representations (`REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata`) and MUST NOT persist raw secret values merely for observability.
- Tool/model output is untrusted data; prompt injection cannot create AUTH, Effect Permit, lease/fence, Verification PASS, or Task DONE.
- Actual secret values MUST NOT be stored here.
- Brownfield adoption never infers trust merely from successful prior use.
- TASK-057 trust policy remains one filter in deterministic filter-before-rank executor selection; UNKNOWN trust for materially sensitive work fails closed before any preference ranking.
