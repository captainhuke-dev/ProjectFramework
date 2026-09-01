# Framework Governance Amendment — TASK-042 Response Finalization Hardening

**Framework:** 1.9.1
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT / APPROVED
**Task:** TASK-042 — Response Finalization Hardening

## 1. Purpose

Framework 1.9.1 hardens the existing bootstrap and mandatory response-close contracts after an observed Project diagnostic response omitted the required close. The response-close format itself already existed and remains unchanged. The defect boundary is narrower: Framework 1.9.0 thin vendor adapters told Agents to read Project Bootstrap only before **Material Project work**, while the mandatory response-close applies to **every Project-governed response**. Read-only/status/diagnostic/early-return paths could therefore answer before local governance was resolved.

This amendment closes that bootstrap-timing gap and makes exceptional-path response finalization explicit without adding runtime middleware or a new authority/state family.

## 2. First Project Response Bootstrap Invariant

When an Agent is operating in a Project and the applicable Project Settings / Project Instructions, consuming README fallback, or Project root is accessible, the Agent MUST resolve Project Bootstrap **before the first Project-governed response in each chat/session**.

Canonical thin-adapter semantics are:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before the first Project-governed response in each chat.
Read-only, status, diagnostic, and failure-report responses are not exempt.
Before Material Project work, also apply all existing binding, authority, risk, and mutation gates.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

This is a **governance-loading/discovery rule**, not mutation authority. First-response bootstrap does not grant Git push, destructive operation, Root/Binding change, Risk acceptance, implementation/runtime, secret access, or external-disclosure authority.

Read-only commands such as `[Project Status]`, Project explanation, troubleshooting, MCP/tool diagnostics, bootstrap repair reports, and other non-Material responses are not exempt merely because no mutation is planned.

If Project Bootstrap cannot be safely resolved, use the governed README fallback when available. If neither route resolves safely, report the limitation / `VERIFICATION_REQUIRED` as applicable; never invent a path, workspace, Project Source, or authority from recency, active editor/MCP handles, mounts, ranking, memory, or similarly named locations.

## 3. Unskippable Response Finalization Invariant

The existing Response Close Completeness Gate remains the canonical pre-emit validation. Framework 1.9.1 adds this control-flow invariant:

> **Every Project-governed final response MUST pass the Response Close Completeness Gate immediately before emit. No early-return path may bypass it.**

The following paths are explicitly included and MUST converge on the same final-response gate:

- ordinary successful response;
- read-only/status/diagnostic response;
- tool/MCP failure or exception;
- connector unavailable/disconnected handling;
- timeout handling;
- partial-result / degraded-mode response;
- refusal or blocked-action response;
- persistence failure / `PERSISTENCE_PENDING` response;
- exception-recovery path;
- bootstrap repair / unresolved-bootstrap response when a Project-governed response is being produced.

Intermediate tool output, error payloads, logs, drafts, or exception objects are not final responses. The gate applies to the assistant final-response representation after content, truth limits, lifecycle state, and next action have been resolved.

## 4. Mandatory Close Contract Remains Unchanged

TASK-042 does not rename, reorder, or weaken the existing close. Every Framework-governed response still ends with exactly the two mandatory headings and exactly one semantic field each for:

```text
[Next Action]:
[Chat]:
[Reason]:
[Required Read]:
```

The existing lifecycle coupling remains:

- `ไม่มีขั้นตอนถัดไป` → `START_NEW_CHAT`;
- `CONTINUE_CURRENT_CHAT` requires one concrete Next Action;
- `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus one concrete persistence/recovery action;
- nothing follows `[Required Read]`.

A tool/MCP/connector exception does **not** automatically mean `PERSISTENCE_PENDING`. Use that state only when required durable continuation state is actually unpersisted.

## 5. Failure and Partial-Result Semantics

Exceptional conditions change the truthful response body and lifecycle fields when applicable; they do not remove finalization requirements.

```text
tool/connector failure with safe retry
→ report failure/limits truthfully
→ set concrete recovery Next Action when work remains
→ close normally

required persistence failed
→ PERSISTENCE_PENDING
→ CONTINUE_CURRENT_CHAT
→ concrete persistence/recovery Next Action
→ close normally

partial result
→ distinguish verified subset from unknown/unavailable portions
→ choose next action from actual remaining work
→ close normally

blocked/refused action
→ block/refuse only the affected operation when appropriate
→ preserve exact authority/tool/safety boundary
→ close normally
```

## 6. Thin Launcher Boundary

Do not solve this regression by restoring the pre-TASK-041 full governance launcher. ChatGPT/Claude/other maintained vendor adapters remain thin locators plus first-response bootstrap guidance. The full response-close and governance semantics continue to come from `PROJECT-BOOTSTRAP.md → active FRAMEWORK-001` and current Framework sources.

Thin launcher ≠ Project authority. Launcher correctness does not transfer `AUTH-*`, Risk, binding, branch, implementation, runtime, secret, or disclosure authority.

## 7. GREENFIELD and Brownfield

Framework 1.9.1 GREENFIELD Projects use the first-response adapter wording from initial installation handoff. The consuming README managed fallback and root `PROJECT-BOOTSTRAP.md` route remain locator-only.

Existing initialized Projects remain pinned. They do not silently acquire this hardening when upstream moves. Brownfield adoption is governed `[Project Upgrade]` work that preserves local `FRAMEWORK-001`, Stable IDs, Project-specific rules, bindings, history, authority, and the existing response-close format.

## 8. Non-Runtime Boundary

TASK-042 is documentation/governance hardening only. It creates no:

- response middleware/interceptor;
- transport/UI hook;
- executable validator or CLI;
- parser service;
- MCP daemon/runtime change;
- watcher/scheduler/background automation;
- new semantic slot or Stable-ID family;
- new lifecycle/authority state family.

The Framework defines the invariant; product/runtime implementations may implement compatible enforcement separately only under their own explicit scope.

## 9. Verification Requirements

Current release acceptance must prove:

1. TDD RED scenarios 269–280 existed and failed before production changes.
2. Project Settings launchers use first-response bootstrap, explicit non-exemption, and Material additional-gate wording.
3. launchers remain thin and do not duplicate the full close block.
4. Core/SKILL state no early-return/tool-MCP failure/connector/timeout/partial/refusal/exception-recovery bypass.
5. exact canonical response-close semantics are unchanged.
6. `PERSISTENCE_PENDING` coupling remains unchanged.
7. current bootstrap/README/starter/migration guidance is aligned.
8. historical provenance remains preserved.
9. ProjectFramework local Project Source pin remains 1.7.0 / Schema 1.0.0.
10. AFFECTED verification passes.
11. exactly one final `RELEASE_FULL` passes on an unchanged candidate with state-bound evidence.

## 10. Precedence

This amendment is the latest Framework 1.9.1 amendment. It specializes current bootstrap timing and response-finalization control-flow semantics. It does not override unrelated authority, location, Git, Risk, disclosure, secret, Goal, Meeting, runtime, or migration rules.
