# TASK-042 — Response Finalization Hardening Design

**Status:** USER_APPROVED_ARCHITECTURE / WRITTEN_SPEC_APPROVED_BY_GOAL
**Target:** Project Source Framework `1.9.1` / Schema `1.0.0`
**Scope:** Documentation/governance hardening only; no runtime interceptor, transport hook, parser, CLI, validator service, MCP daemon change, scheduler, watcher, or UI automation
**Source:** User-reported dropped response-close regression + user-approved three-layer hardening design + persistent `[Goal]` on 2026-09-01

## 1. Problem

Framework `1.9.0` already requires every Framework-governed response to end with the mandatory two-heading/four-field close and already defines a Response Close Completeness Gate before emit. However, the current thin ChatGPT/Claude Project Settings adapters say:

```text
Read Project Bootstrap before Material Project work.
```

That trigger is narrower than the response-close invariant. A read-only Project question, status request, MCP/tool diagnostic, failure explanation, or another early-return path may be treated as non-Material and answered before the Agent resolves `PROJECT-BOOTSTRAP.md → active FRAMEWORK-001`. The Agent may therefore never load the local mandatory response-close contract for that response.

The user supplied a concrete diagnostic response whose body was generated but whose mandatory close pattern was absent. Current pressure scenarios do not directly force closure preservation on the exceptional/early-return paths that can expose this gap.

## 2. Root Cause

TASK-042 treats the root cause as two coupled gaps:

1. **Bootstrap timing gap:** current thin adapters trigger Project Bootstrap only before Material Project work, while the close invariant applies to every Project-governed response.
2. **Exceptional-path coverage gap:** Core defines a pre-emit close gate, but maintained regression scenarios do not explicitly test that tool/MCP failures, timeouts, connector errors, refusals, partial results, diagnostic returns, and exception recovery still reach the same finalization gate.

The canonical response-close format itself is not missing and is not redesigned by this Task.

## 3. Goals

TASK-042 makes the following statements true:

- Project bootstrap is resolved before the **first Project-governed response in each chat/session** when the adapter/root is available.
- Read-only, status, diagnostic, explanatory, and failure-report responses are not exempt from first-response bootstrap merely because no Material mutation is planned.
- Material Project work retains all existing additional binding/authority/risk/mutation gates; first-response bootstrap grants no new mutation authority.
- Every Project-governed final response routes through the Response Close Completeness Gate.
- No early-return, tool/MCP failure, timeout, connector error, refusal, partial result, exception-recovery, or diagnostic path may bypass the close gate.
- `PERSISTENCE_PENDING` responses still obey existing lifecycle coupling: `CONTINUE_CURRENT_CHAT` plus one concrete persistence/recovery action.
- Pressure scenarios make these behaviors regression-visible.

## 4. Non-Goals

TASK-042 does not:

- change the canonical response-close headings, field labels, order, or lifecycle tokens;
- duplicate the full response-close block inside every thin vendor launcher;
- turn Project Settings, README, or `PROJECT-BOOTSTRAP.md` into Project authority;
- require a filesystem/repository bootstrap when the Agent genuinely cannot access the Project root or supplied Project Bootstrap;
- claim control over downstream transport/UI rendering;
- create a runtime response middleware, hook, interceptor, parser, validator executable, CLI, daemon, watcher, scheduler, or vendor UI automation;
- auto-upgrade initialized Projects;
- change semantic slots, Stable-ID families, Project Source Schema, Goal families, authority families, or Project Location Binding;
- weaken tool/platform/safety/authentication controls.

## 5. Architecture

The target response path is:

```text
Project Settings / Project Instructions
        |
        | before FIRST Project-governed response in this chat
        v
resolve Project Bootstrap
        |
        v
PROJECT-BOOTSTRAP.md
        |
        v
active FRAMEWORK-001
        |
        v
normal response / status / diagnostic / failure / partial result
        |
        v
UNSKIPPABLE Response Close Completeness Gate
        |
        v
final response
```

The existing authority chain remains unchanged:

```text
Project Settings / README / PROJECT-BOOTSTRAP.md = discovery/locator only
active FRAMEWORK-001 = Project governance authority
```

## 6. First Project-Response Bootstrap Invariant

Current thin adapter wording changes from the Material-only trigger to a first-response trigger with an explicit non-exemption rule.

Canonical intent:

```text
Read Project Bootstrap before the first Project-governed response in each chat.
Read-only, status, diagnostic, and failure-report responses are not exempt.
Before Material Project work, also apply all existing binding, authority, risk, and mutation gates.
```

The adapter still falls back to the consuming Project README managed bootstrap block if its absolute Project Bootstrap path cannot be resolved.

If neither the Project Settings path nor the README fallback can safely resolve bootstrap, the Agent reports the limitation rather than inventing a path or governance state. The inability to resolve bootstrap does not authorize Material Project mutation.

## 7. Unskippable Pre-Emit Response Gate

Core Governance strengthens the existing Response Close Completeness Gate with one explicit control-flow invariant:

```text
Every Project-governed final response must pass the Response Close Completeness Gate immediately before emit.
No early-return path may bypass it.
```

The explicit covered paths include:

- normal successful response;
- read-only/status/diagnostic response;
- tool/MCP exception;
- connector unavailable/disconnected;
- timeout;
- partial tool result;
- refusal or blocked-action response;
- persistence failure / `PERSISTENCE_PENDING`;
- exception recovery / degraded-mode response;
- bootstrap repair/verification-required response.

The gate validates the final response representation, not intermediate drafts/tool outputs.

## 8. Failure Semantics

A failure changes response content and lifecycle state when applicable; it does not remove the close.

Examples:

```text
Tool failure with safe retry available
→ report failure truthfully
→ concrete recovery Next Action
→ CONTINUE_CURRENT_CHAT
→ mandatory close still present

Required persistence failed
→ PERSISTENCE_PENDING
→ concrete persistence/recovery Next Action
→ CONTINUE_CURRENT_CHAT
→ mandatory close still present

No remaining action
→ ไม่มีขั้นตอนถัดไป
→ START_NEW_CHAT
→ mandatory close still present
```

A tool exception alone does not automatically mean `PERSISTENCE_PENDING`; that state is used only when required durable continuation state is actually unpersisted.

## 9. Affected Framework Surfaces

Expected implementation surfaces:

- `Framework-Source/FRAMEWORK-RELEASE.yaml` — patch release `1.9.1` and latest amendment;
- new TASK-042 Framework amendment;
- `Framework-Source/references/core-governance-rules.md` — first-response bootstrap and unskippable finalization invariant;
- `Framework-Source/SKILL.md` — workflow/response-bootstrap semantics;
- `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md` and `CLAUDE-PROJECT-INSTRUCTIONS.md` — thin first-response bootstrap wording;
- `Framework-Source/templates/PROJECT-BOOTSTRAP.md` — first-response relationship where useful;
- `Framework-Source/templates/project-location-bootstrap.md` — canonical thin adapter wording;
- `README.md` — upstream explanation/managed bootstrap block wording where current text still says Material-only;
- `Framework-Source/templates/00-project-source-framework.md`, `core-document-skeletons.md`, and maintained mockup README/starters where the current bootstrap wording is propagated;
- `Framework-Source/MIGRATION-NOTES.md` — `1.9.0 → 1.9.1` guidance;
- `Framework-Source/tests/pressure-scenarios.md` — exceptional-path regression scenarios following scenario 268;
- `docs/superpowers/PROJECT-TASKS.md` and Project Source lifecycle/evidence.

Historical amendments/specs/plans/evidence remain historical and are not globally rewritten.

## 10. Brownfield and Upgrade Behavior

Existing initialized Projects remain pinned. They do not silently acquire TASK-042 behavior merely because upstream moves to `1.9.1`.

On governed `[Project Upgrade]` to a release containing TASK-042:

- preserve local `FRAMEWORK-001`, Project-specific rules, bindings, Stable IDs, history, and authority;
- update only the approved current launcher/bootstrap/governance surfaces;
- preserve the existing response-close format;
- do not synthesize Goal/Auth/ENV objects;
- verify resulting bootstrap/close behavior proportionally and apply the existing final-release evidence rules.

## 11. Version Classification

TASK-042 targets **Framework `1.9.1` / Schema `1.0.0`**.

Rationale: this is a backward-compatible reliability hardening of the `1.9.0` bootstrap/finalization contract. It changes no semantic slot, object schema, Stable-ID family, lifecycle vocabulary, or authority model.

## 12. Verification Contract

Implementation acceptance must demonstrate at least:

1. Current baseline reproduces the gap: thin launcher uses Material-only bootstrap wording before implementation.
2. New scenarios are written first and fail for the missing hardening before production-doc changes.
3. ChatGPT and Claude thin adapters use equivalent first-response bootstrap semantics.
4. Thin adapters remain small and do not duplicate the full governance/response-close block.
5. Read-only/status/diagnostic responses are explicitly not exempt from bootstrap.
6. Material Project work still applies independent binding/authority/risk gates.
7. Core explicitly prohibits every early-return path from bypassing the pre-emit gate.
8. Tool/MCP exception scenario retains the mandatory close.
9. Connector unavailable/disconnected scenario retains the mandatory close.
10. Timeout scenario retains the mandatory close.
11. Partial-result scenario retains the mandatory close.
12. Refusal/blocked-action scenario retains the mandatory close.
13. `PERSISTENCE_PENDING` scenario uses `CONTINUE_CURRENT_CHAT` plus concrete recovery action and retains the mandatory close.
14. Bootstrap-unavailable/repair scenario retains the mandatory close when a Project-governed response can still be produced from the resolved applicable contract; no path/authority is fabricated.
15. Exact two headings + four semantic fields + order + canonical lifecycle tokens + nothing after Required Read remain unchanged.
16. Existing initialized Projects do not auto-upgrade.
17. ProjectFramework local Project Source pin remains Framework `1.7.0` / Schema `1.0.0`.
18. No new runtime/CLI/validator/interceptor/automation artifact is added.
19. `git diff --check` passes.
20. affected verification passes.
21. exactly one final `RELEASE_FULL` passes on the unchanged release candidate and is captured as state-bound evidence.

## 13. Security and Authority Boundary

First-response bootstrap is discovery/governance loading, not authorization. It grants no push, destructive action, Root/Binding mutation, runtime, deployment, external disclosure, or secret-value access. Existing tool/platform/safety controls remain higher-level gates.

## 14. Approved Design Decisions

The user approved the following three-layer design before implementation:

1. **First-response bootstrap:** resolve Project Bootstrap before the first Project-governed response in each chat; read-only/status/diagnostic work is not exempt.
2. **Unskippable pre-emit gate:** no early return, tool/MCP failure, timeout, connector error, refusal, partial result, or exception recovery may bypass Response Close Completeness Gate.
3. **Exceptional-path regression coverage:** maintain pressure scenarios that prove the close survives those paths.

The user then invoked `[goal] ยืนยันและทำจนจบ`, authorizing bounded continuous local TASK-042 work through verified completion while preserving publication and other exact opt-in boundaries.

## 15. Success Statement

TASK-042 is successful when a capable Agent entering a Project cannot legitimately treat a read-only diagnostic as an excuse to skip Project bootstrap, and every Project-governed final response—successful, degraded, blocked, partial, or failed—must still pass the same mandatory response-close gate before emit.
