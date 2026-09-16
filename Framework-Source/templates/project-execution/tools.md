# Tool / MCP Execution Profile Template

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
primary_tool: "<TOOL_OR_MCP_ID>"
allowed_tools:
  - "<TOOL_OR_MCP_ID>"
disallowed_tools:
  - "<TOOL_OR_MCP_ID>"
fallback_mode: "NONE | ORDERED_ALLOW_LIST"
fallback_order:
  - "<TOOL_OR_MCP_ID>"
failure_policy: "FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY"
failback_policy: "CHECKPOINT_FAILBACK"
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
runtime_effect_support:
  mediated_effect_classes:
    - "<effect class or NONE>"
  target_preconditions:
    - "<supported source-native precondition or NONE>"
  idempotency_support:
    - "<IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN>"
  reconciliation_support:
    - "<SOURCE_READBACK | NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE>"
```

Rules:

- `PRIMARY` means the declared `primary_tool` when ACTIVE and eligible.
- `primary_tool` SHOULD be present in `allowed_tools` when ACTIVE.
- `disallowed_tools` wins over allowed/fallback declarations.
- `fallback_mode: NONE` means no automatic substitute.
- `ORDERED_ALLOW_LIST` means only `fallback_order` entries are eligible, in declared order.
- An undeclared tool is never eligible merely because it is available, connected, recent, similar, or highly ranked.
- Execution eligibility requires applicable tool/capability availability, active policy eligibility, and verified bound Project/workspace/repository target identity.
- `FAIL_CLOSED` blocks the affected execution when no eligible tool exists.
- `READ_ONLY_DIAGNOSTIC_ONLY` allows bounded read-only diagnosis only.
- `CHECKPOINT_FAILBACK` never switches tools in the middle of the current unresolved bounded action/effect.
- Unknown potentially-applied side effects remain `RESULT_VERIFICATION_REQUIRED`; reconcile resulting state before retrying, failback, or transitioning to another declared fallback. A fallback route does not reset prior Action identity.
- For a mediated Material Effect, applicable Effect Policy/Gateway rules still govern. `Tool availability != Gateway eligibility != AUTH`.
- Supported target preconditions are applied when required. Unsupported preconditions are explicit and use the declared reconciliation/fail-closed path rather than assumed freshness.
- An ambiguous non-idempotent/unknown effect without reconciliation support is not automatically retryable.
- Material fallback mutation still requires applicable `fallback-log.md` persistence first; inability to persist it is `FAIL_CLOSED`.
- Tool IDs are policy labels, not secret values, workspace IDs, repository identity, Project Stable IDs, or authority.
- Actual secret values MUST NOT be stored here.