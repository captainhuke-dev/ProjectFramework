# Framework Governance Amendment — TASK-045 Response Close + Next Goal

Status: APPROVED_BY_USER_GOAL / CURRENT_AMENDMENT
Framework target: `1.15.0`
Schema: `1.0.0`
Release format: `3`

## Purpose

TASK-045 simplifies the mandatory visible Framework response close while preserving Project continuation, read routing, persistent Goal authority, and the unskippable final-response control-flow invariant established by TASK-042/TASK-043.

The mandatory visible close is exactly:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Next Goal]:** <one copy-ready [Goal] ... / [Goal] CHANGE ... command or ไม่มี>

**[Reason]:** <concise reason>
```

Nothing follows `[Reason]`.

`[Chat]` and `[Required Read]` are removed only from the mandatory visible response close. Chat lifecycle and required-read routing remain internal Project continuation semantics, primarily in `09 Handoff` and the sources it references.

## Next Goal Safety Contract

`[Next Goal]` is presentation-only. Displaying it does not invoke `[Goal]` and never creates or changes `OUT-*`, `AUTH-*`, `ACT-*`, or `ENV-*`. Authority exists only after an explicit Human `[Goal]` invocation is processed through the active Goal contract.

NG-1. If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, `[Next Goal]` MUST be `ไม่มี`.

NG-2. If a current compatible active Goal already covers the same bounded continuation, `[Next Goal]` SHOULD be `ไม่มี`; do not suggest redundant authority.

NG-3. When a clear bounded future outcome exists and no active Goal covers it, `[Next Goal]` MAY contain one copy-ready command beginning with literal `[Goal]`.

NG-4. When the exact next persistent instruction is a grounded change to an active Goal, `[Next Goal]` MAY contain one copy-ready `[Goal] CHANGE ...` command.

NG-5. A non-`ไม่มี` suggestion MUST identify a bounded outcome sufficiently to avoid silently broadening scope, prohibited zones, or success criteria.

NG-6. Ambiguous, conflicting, under-specified, or materially uncertain Goal scope MUST yield `[Next Goal]: ไม่มี` until resolved.

NG-7. The assistant MUST NOT synthesize new push/publication, destructive-operation, Root/Binding mutation, external-disclosure, R3, or secret-value opt-ins into `[Next Goal]`. Such effects require their own exact Human instruction under existing authority rules.

NG-8. `PERSISTENCE_PENDING` recovery remains an immediate continuation obligation. `[Next Action]` MUST name the concrete persistence/recovery action, and `[Next Goal]` MUST NOT be used to bypass or obscure that recovery.

NG-9. Material conflict among Goals or governed sources fails closed for the affected suggestion. A later suggested Goal never wins by recency.

## Continuity and Required Read

Canonical lifecycle vocabulary `CONTINUE_CURRENT_CHAT | START_NEW_CHAT` remains valid for internal continuation state and Handoff. Existing Handoff records may preserve `Chat Continuity`, `Required Read Before Continue`, `authority_transfer: false`, and exact continuation pointers. TASK-045 does not require those fields to be rendered visibly at the end of every assistant response.

Historical pre-1.15 response-close examples and evidence remain historical truth and are not globally rewritten.

## Finalization Gates

TASK-042 remains fully in force: every Project-governed final response, including success, read-only/status/diagnostic, error, refusal, blocked-action, timeout, connector-failure, partial-result, `PERSISTENCE_PENDING`, exception-recovery, and bootstrap-repair paths, passes the Response Close Completeness Gate immediately before emit.

TASK-043 remains fully in force: for recognized Registered Commands, the Command Contract Completeness Gate runs before the Response Close Completeness Gate.

For Framework 1.15.0, the Response Close Completeness Gate verifies:

1. exactly the two mandatory headings, in order;
2. exactly one visible `[Next Action]:` field;
3. exactly one visible `[Next Goal]:` field immediately after `[Next Action]:`;
4. exactly one visible `[Reason]:` field immediately after `[Next Goal]:`;
5. no mandatory visible `[Chat]:` field;
6. no mandatory visible `[Required Read]:` field;
7. nothing after `[Reason]`;
8. NG-1..NG-9 consistency and no hidden authority expansion.

Markdown-safe wrapping remains presentation-only; semantic labels remain `[Next Action]:`, `[Next Goal]:`, and `[Reason]:`.

## Migration and Compatibility

Initialized Projects remain locally pinned and do not auto-adopt Framework 1.15.0. Brownfield adoption occurs only through the normal governed `[Project Upgrade]` path. Internal Handoff lifecycle/read-routing semantics are preserved during upgrade; only the mandatory visible close changes.

The Registered Command set remains exactly seven commands. TASK-045 adds no command, semantic slot, Stable-ID family, lifecycle state, parser, middleware, UI hook, validator/CLI, bot, scheduler, watcher, daemon, or other runtime implementation.

`commit ≠ push`; this amendment grants no publication authority.
