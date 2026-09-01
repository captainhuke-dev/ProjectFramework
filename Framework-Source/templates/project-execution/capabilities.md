# Agent / Model Capability Profile Template

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
work_classes:
  - work_class: "IMPLEMENTATION"
    required_capabilities: ["REASONING", "CODING"]
    preferred_capabilities: ["REVIEW"]
    provider_scope: "LOCAL_ONLY | LOCAL_OR_EXTERNAL | EXTERNAL_ALLOWED"
    independent_review: "REQUIRED | OPTIONAL | NOT_REQUIRED"
    tool_profile_ref: "./tools.md"
    failure_mode: "FAIL_CLOSED | DEGRADED_ALLOWED"
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

Canonical capability classes:

```text
REASONING | CODING | RESEARCH | REVIEW | COUNCIL
```

Execution-time availability:

```text
FULL | DEGRADED | UNAVAILABLE | UNKNOWN
```

Rules:

- `Capability ≠ Authority` and capability eligibility ≠ tool eligibility.
- `LOCAL_ONLY` forbids external provider eligibility for that work class.
- External provider use still requires TASK-026 disclosure/provider/minimization/secret rules.
- `DEGRADED_ALLOWED` permits only genuinely supported bounded work; required review and safety/authority gates remain.
- `UNKNOWN` fails closed for materially sensitive required capability.
- `independent_review: REQUIRED` requires an eligible independent reviewer where practicable; do not fabricate reviewer capability/availability/independence.
- `[Meeting]` remains TASK-024 advisory behavior even when `COUNCIL` is required.
- Profile values are eligibility constraints, not mutation, approval, deployment, disclosure, or binding authority.
