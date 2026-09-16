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
effect_mediation:
  effect_policy_ref: "./effect-policy.md"
  mediated_effect_classes:
    - "<effect class or NONE>"
  prohibited_effect_routes:
    - "<uncontrolled route or NONE>"
  target_precondition_support:
    - "<SHA | ETAG | RESOURCE_VERSION | ROW_VERSION | OBJECT_HASH | CAS | OTHER | NONE>"
  idempotency_support:
    - "<IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN>"
  reconciliation_support:
    - "<NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK | NATIVE_READBACK | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE>"
```

Rules:

- `PRIMARY` means the declared `primary_tool` when ACTIVE and eligible.
- `primary_tool` SHOULD be present in `allowed_tools` when ACTIVE.
- `disallowed_tools` wins over allowed/fallback declarations.
- `fallback_mode: NONE` means no automatic substitute.
- `ORDERED_ALLOW_LIST` means only `fallback_order` entries are eligible, in declared order.
- An undeclared tool is never eligible merely because it is available, connected, recent, similar, or highly ranked.
- Execution eligibility requires applicable tool/capability availability, active policy eligibility, verified bound Project/workspace/repository target identity, and applicable runtime/effect-policy constraints.
- `FAIL_CLOSED` blocks the affected execution when no eligible tool exists.
- `READ_ONLY_DIAGNOSTIC_ONLY` allows only bounded read-only diagnosis; it never authorizes mutation through an undeclared tool.
- `CHECKPOINT_FAILBACK` never switches MCPs in the middle of the current bounded action/checkpoint. Finish/persist/verify that checkpoint, reverify Primary, append recovery/failback history, then use Primary for the next action.
- Unknown potentially-applied side effects enter `RESULT_VERIFICATION_REQUIRED`; verify resulting state before retrying or transitioning to another declared fallback. A fallback tool MUST NOT blind-replay an unresolved previous effect.
- For a mediated Material Effect, tool support does not prove Effect Gateway conformance by itself. Applicable routes also require effect-surface closure, current generation/fence, JIT single-use Effect Permit, target precondition policy, and source-native/result reconciliation.
- A tool that lacks a usable target-precondition primitive MUST declare that limitation through the effect policy; absence never means freshness may be assumed.
- Material fallback mutation requires the applicable append-only `fallback-log.md` incident event to be persisted first; inability to persist it is `FAIL_CLOSED`.
- Tool IDs are policy labels, not credentials, MCP workspace IDs, repository identity, Project Stable IDs, Effect Permits, or authority.
- TASK-057 filter-before-rank selection remains binding; an undeclared/ineligible tool does not become eligible through availability or preference, and `NO_ELIGIBLE_EXECUTOR` fails closed without invented fallback.
- Actual secret values MUST NOT be stored here.
