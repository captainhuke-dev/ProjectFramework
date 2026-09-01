# TASK-027 Project Tool / MCP Execution Profile — Design

**Task:** TASK-027 — Project Tool / MCP Execution Profile
**Design state:** USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL
**Set 1 position:** 2 of 5
**Depends on:** TASK-033
**Target Framework:** 1.12.0
**Project Source Schema:** 1.0.0
**Release format:** 3

## 1. Purpose

Projects need a durable vendor-neutral execution-tool policy instead of relying on transient chat instructions such as “CEO-only” or product-specific UI configuration.

TASK-027 introduces an optional governed root representation:

```text
<Project-Root>/Project-Execution/
├── README.md
└── tools.md
```

`Project-Execution/` is outside the `Project-Source/00–99` semantic-slot namespace. It is a governed Project artifact that inherits from active `FRAMEWORK-001`, but it is not Root Governance, Project Location Binding, `AUTH-*`, current branch/worktree, Integration Target, Implementation Source, or Runtime authority.

Core invariant:

```text
Tool selection policy ≠ Tool availability ≠ Location ≠ Authority
Tool/MCP profile ≠ permission to mutate
```

## 2. `tools.md` contract

A maintained profile uses compact YAML frontmatter:

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
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

IDs are profile labels, not credentials, secret values, MCP workspace IDs, repository identity, or Project Stable IDs.

`primary_tool` SHOULD also appear in `allowed_tools` when the profile is ACTIVE. `disallowed_tools` wins over allowed/fallback declarations. Duplicate/conflicting declarations fail closed until repaired.

## 3. Selection and fallback semantics

Resolution order for an execution action is:

```text
resolve active Project authority/location/binding as applicable
→ read active Project-Execution/tools.md when applicable
→ check requested capability against profile
→ verify tool availability/authentication/target identity for this action
→ use PRIMARY when eligible
→ otherwise apply fallback_mode
→ then apply normal AUTH/Risk/shared-state/platform/tool gates
```

`fallback_mode: NONE` means no alternative execution tool may be substituted automatically. `ORDERED_ALLOW_LIST` allows only the declared deterministic fallback order. Availability, recency, ranking, or “currently connected” status never creates fallback eligibility.

`failure_policy: FAIL_CLOSED` blocks the affected execution when no eligible tool is available. `READ_ONLY_DIAGNOSTIC_ONLY` permits bounded read-only diagnostics needed to explain/repair tool availability but does not permit material mutation through an undeclared substitute.

## 4. Separation from MCP/Workspace Location

The profile says **which tool may execute**. Active `FRAMEWORK-001`/Project Location Binding says **where Project work belongs**. A tool may be allowed yet unusable because it cannot prove the bound repository/workspace. Conversely, a connected MCP at the correct workspace is not eligible if the active tool profile disallows it.

MCP workspace IDs, UI handles, connector names, and local process IDs remain runtime routing evidence only.

## 5. Authority boundary

The profile does not grant:

- Project mutation authority;
- push/publication authority;
- destructive-operation authority;
- secret access or disclosure;
- Root/Binding mutation;
- deployment/runtime authority.

An explicit user instruction may authorize an otherwise allowed action but does not silently rewrite the persistent tool profile. Persistent profile changes use the normal governed Project change/Preview/approval path when material.

## 6. Bootstrap routing

`PROJECT-BOOTSTRAP.md` continues to resolve Project authority first. It does not embed the full tool policy. After `FRAMEWORK-001 → 01 → 03`, the active `01` or task-specific routing MAY point to `Project-Execution/tools.md` when execution policy is applicable.

Thus:

```text
bootstrap discovers authority
Project-Execution declares execution policy
AUTH/Risk rules decide permission
runtime/tool checks prove actual capability/target
```

## 7. Unavailable/stale/renamed tools

If the primary or fallback tool is unavailable, unauthenticated, renamed, stale, or cannot prove bound Project identity:

- do not substitute by recency or similarity;
- apply declared fallback mode/policy;
- surface `VERIFICATION_REQUIRED` where identity/authentication cannot be established;
- preserve current profile until governed change is approved;
- never store credentials in the profile.

## 8. GREENFIELD/Brownfield

The execution profile is optional/applicability-driven. GREENFIELD may Preview `Project-Execution/` only when a durable tool policy is useful; no default “all tools allowed” or “CEO-only” policy is invented. Brownfield Projects do not acquire a restrictive/permissive profile automatically on upgrade.

## 9. Shared Set 1 profile directory

TASK-027 owns the initial `Project-Execution/README.md` and `tools.md`. TASK-034 and TASK-037 later extend the same directory with `capabilities.md` and `trust.md`. Each file has one responsibility; no file grants authority held by another governance home.

## 10. Affected surfaces and verification

Implementation affects current release/amendment/Core/SKILL/README/migration/templates/task/tests plus maintained `Framework-Source/templates/project-execution/README.md` and `tools.md`. No MCP runtime, `.lnwjud` profile, vendor settings, router, credential store, daemon, or automatic tool switcher is created.

Pressure/AFFECTED checks must prove deterministic PRIMARY/fallback behavior, `FALLBACK_NONE` equivalent, disallowed precedence, fail-closed unavailable/identity behavior, location/authority separation, no credential values, bootstrap-after-authority routing, GREENFIELD optionality, Brownfield no auto-adoption, and no runtime implementation.
