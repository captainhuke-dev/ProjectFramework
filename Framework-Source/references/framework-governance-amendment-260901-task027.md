# Framework Governance Amendment — TASK-027 Project Tool / MCP Execution Profile

**Framework:** 1.12.0
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT / SET1_INCREMENTAL
**Task:** TASK-027 — Project Tool / MCP Execution Profile

## 1. Purpose

Framework 1.12.0 adds an optional governed `Project-Execution/` policy surface for durable vendor-neutral execution-tool selection. This policy constrains which tool/MCP may execute; it is not Project authority, Project Location Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime authority, or credentials.

```text
Tool selection policy ≠ Tool availability ≠ Location ≠ Authority
Tool/MCP profile ≠ permission to mutate
```

## 2. Maintained representation

When applicable and approved:

```text
<Project-Root>/Project-Execution/
├── README.md
└── tools.md
```

The directory is outside `Project-Source/00–99`, has no Project Source semantic slot or Stable-ID family, and is read only after active Project authority resolves.

## 3. Tool policy contract

`tools.md` uses:

```text
PRIMARY
allowed_tools
disallowed_tools
fallback_mode: NONE | ORDERED_ALLOW_LIST
fallback_order
failure_policy: FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY
```

`disallowed_tools` takes precedence. `fallback_mode: NONE` permits no automatic substitute. `ORDERED_ALLOW_LIST` permits only the declared deterministic order. Recency, connected status, search ranking, similarity, or MCP workspace handles never create eligibility.

## 4. Resolution

```text
resolve active Project authority/location/binding as applicable
→ read active Project-Execution/tools.md when applicable
→ test action/tool against policy
→ verify availability/authentication/bound-target identity
→ use PRIMARY when eligible
→ otherwise apply declared fallback_mode/failure_policy
→ then apply AUTH/Risk/shared-state/platform/tool gates
```

`FAIL_CLOSED` blocks the affected execution when no eligible tool is available. `READ_ONLY_DIAGNOSTIC_ONLY` permits bounded read-only diagnosis needed to explain or repair availability/identity, never material mutation through an undeclared substitute.

## 5. Separation

The Tool/MCP Execution Profile says which execution route is eligible. Active `FRAMEWORK-001` Project Location Binding says where work belongs. `AUTH-*` and Risk/Decision/shared-state gates say whether an action is permitted. None substitutes for another.

Allowed tool + wrong/unverified bound target = not executable. Correctly connected MCP + disallowed tool = not eligible.

## 6. Bootstrap and persistence

`PROJECT-BOOTSTRAP.md` resolves Project authority first and does not embed full tool policy. `01` or task-specific routing may point to `Project-Execution/tools.md` after authority resolution. Persistent profile changes follow governed Project change/Preview/approval flow when material. One-off user instructions do not silently rewrite the profile.

## 7. Unavailable, stale, or renamed tools

Unavailable, unauthenticated, stale, renamed, or target-unverified tools do not trigger heuristic substitution. Apply the declared fallback/failure policy; unresolved identity uses `VERIFICATION_REQUIRED` for the affected action. Credentials and actual secret values never belong in this profile.

## 8. GREENFIELD and Brownfield

The profile is applicability-driven. GREENFIELD invents neither “all tools allowed” nor a restrictive `CEO-only` policy without approved facts. Brownfield upgrades do not auto-create, loosen, or restrict tool policy from prior usage/vendor settings.

## 9. Runtime boundary

TASK-027 defines documentation/governance only. It adds no MCP router, `.lnwjud` mutation, vendor tool routing, credential store, daemon, automatic failover service, or runtime enforcement.
