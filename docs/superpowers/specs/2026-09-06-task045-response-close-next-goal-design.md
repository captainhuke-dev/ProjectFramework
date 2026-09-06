# TASK-045 — Response Close + Next Goal Design

**Status:** USER_APPROVED_DIRECTION / WRITTEN_SPEC

**Target release:** ProjectFramework `1.15.0` / Schema `1.0.0` / release format `3`

**Goal authority:** `OUT-012 / AUTH-012 / ACT-024 / ENV-012`

**Task identity note:** the response-close work was initially referred to as TASK-044 in chat. Fresh repository discovery showed that ProjectFramework 2.0 / AI-ControlTower Protocol Integration already owns `TASK-044` in the verified V2 `v2-premerge-readiness` line. This design therefore uses `TASK-045` and preserves V2 `TASK-044` unchanged.

## 1. Problem

ProjectFramework currently requires every governed assistant response to end with two headings and four visible fields:

`[Next Action] → [Chat] → [Reason] → [Required Read]`.

`[Chat]` and `[Required Read]` are valuable continuation/governance concepts, but forcing both into every user-visible response makes the close more implementation-facing than action-facing. At the same time, the close has no concise way to offer the Human a ready-to-invoke persistent `[Goal]` command when the next bounded outcome is suitable for one-shot continuous execution.

The user explicitly directed ProjectFramework to remove the two visible fields and add `[Next Goal]` after `[Next Action]`.

## 2. Design goals

TASK-045 SHALL:

1. Change the mandatory visible Framework response close to exactly two headings followed by exactly three visible semantic fields in this order:
   - `[Next Action]`
   - `[Next Goal]`
   - `[Reason]`
2. Remove `[Chat]` and `[Required Read]` from the mandatory visible response close.
3. Preserve chat-lifecycle/continuation semantics as internal Project/Handoff state where they remain useful.
4. Preserve required-read routing as Project/Handoff/bootstrap information rather than forcing it into every response.
5. Make `[Next Goal]` a safe, copy-ready suggestion for a persistent `[Goal]` command when appropriate.
6. Ensure `[Next Goal]` never creates authority merely by being displayed.
7. Preserve all existing `[Goal]` authority, scope, success-evidence, conflict, cancellation and opt-in boundaries.
8. Keep the change documentation/governance-only; no response parser, runtime interceptor, UI hook, validator CLI, bot, scheduler or daemon is introduced.

## 3. Non-goals

TASK-045 SHALL NOT:

- remove `09 Handoff` or its continuation/read pointers;
- remove `CONTINUE_CURRENT_CHAT | START_NEW_CHAT` as internal continuity vocabulary where an active Project contract still uses it;
- remove `[Goal]`, `[Session]`, `[Meeting]`, `[Project Status]`, `[Project Path]`, `[Project Upgrade]`, or `[Project Audit]`;
- create a new Goal Stable-ID family;
- automatically invoke a Goal from a suggestion;
- infer push/publication, destructive operation, Root/Binding mutation or external-disclosure authority;
- change Project Source Schema `1.0.0`;
- modify V2 `TASK-044` or its design/pre-merge lineage;
- implement runtime enforcement.

## 4. Canonical visible response-close contract

Every Framework-governed assistant final response SHALL end with exactly the following structure:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Next Goal]:** <one copy-ready Goal command or ไม่มี>

**[Reason]:** <concise reason>
```

Nothing follows `[Reason]`.

The three semantic fields are separate Markdown paragraphs. Bold or equivalent Markdown-safe wrapping is presentation-only and does not rename the labels.

### 4.1 Field semantics

**`[Next Action]`** remains the exact immediate next operation. It may be `ไม่มีขั้นตอนถัดไป` only when no concrete next action is required.

**`[Next Goal]`** is a presentation-only suggestion for a persistent Goal command. It SHALL contain either:

- one copy-ready `[Goal] ...` command,
- one copy-ready `[Goal] CHANGE ...` command, or
- exactly `ไม่มี`.

**`[Reason]`** explains concisely why the Next Action / Next Goal disposition is appropriate.

## 5. `[Next Goal]` eligibility and decision rules

`[Next Goal]` exists to let the Human convert a clearly bounded future outcome into one explicit persistent instruction without having to formulate the command manually.

The assistant SHALL evaluate the field in this order.

### Rule NG-1 — No next action

If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, `[Next Goal]` MUST be `ไม่มี`.

Rationale: do not invent work merely to fill a Goal field.

### Rule NG-2 — Existing active Goal already covers the continuation

If a current compatible active Goal already authorizes and describes the same bounded continuation, `[Next Goal]` SHOULD be `ไม่มี` rather than suggesting a redundant Goal.

A redundant suggestion is not needed merely because work remains.

### Rule NG-3 — Existing Goal needs explicit bounded expansion

If the next useful persistent instruction is an explicit change to a current Goal and the exact expansion is already grounded in the conversation/Project state, `[Next Goal]` MAY be a copy-ready command such as:

```text
[Goal] CHANGE <existing Goal> เพื่อ <bounded new scope/outcome>
```

The suggested command itself still grants no authority until the Human invokes it.

### Rule NG-4 — New bounded persistent outcome

If no active Goal covers the work and the same user objective has a clear bounded outcome, success boundary and safe local-development scope, `[Next Goal]` MAY suggest:

```text
[Goal] <bounded outcome>
```

The command should be outcome-oriented rather than a list of low-level tool operations.

### Rule NG-5 — Ambiguous scope

If the desired outcome, target, success boundary, ownership or material scope is ambiguous, `[Next Goal]` MUST be `ไม่มี`.

The response may use `[Next Action]` to resolve the ambiguity first.

### Rule NG-6 — High-risk or separately opted-in effects

The assistant MUST NOT synthesize into `[Next Goal]` any new opt-in for:

- push/publication;
- destructive operation;
- Root Governance or Project Location Binding mutation;
- external AI/provider disclosure;
- actual secret-value handling;
- another independent R3/external/irreversible effect.

If such an effect is the unresolved hinge and the exact authorization has not already been explicitly supplied by the Human, `[Next Goal]` MUST be `ไม่มี`.

A Goal may later include one of those effects only under the existing exact opt-in rules when the Human explicitly invokes a sufficiently bounded command.

### Rule NG-7 — Persistence recovery

When required durable continuation state is `PERSISTENCE_PENDING`, `[Next Action]` MUST name the concrete persistence/recovery action. `[Next Goal]` MUST NOT be used to bypass or obscure that recovery requirement. Unless a distinct safe Goal is already clearly warranted, use `ไม่มี`.

### Rule NG-8 — Conflict

If multiple active Goals or governed sources conflict materially, `[Next Goal]` MUST be `ไม่มี` until the conflict is resolved through existing governance. A later suggested Goal never wins by recency.

### Rule NG-9 — Exactness and copy readiness

A non-`ไม่มี` `[Next Goal]` value must:

- begin with the literal registered token `[Goal]`;
- be directly usable as a user message without placeholder syntax;
- name the bounded outcome or change clearly;
- avoid secrets and ungrounded targets;
- avoid silently expanding current authority.

## 6. Authority boundary

`[Next Goal]` is not a command invocation because it is assistant output, not a Human command.

Therefore:

```text
Suggested [Goal] text ≠ User invocation
Suggested [Goal] text ≠ OUT-* materialization
Suggested [Goal] text ≠ AUTH-* grant
Suggested [Goal] text ≠ ACT-* / ENV-* execution authority
```

Only a later explicit Human message containing the registered `[Goal]` command may enter the existing Goal CREATE/SHOW/CHANGE/CANCEL workflow.

All TASK-039 persistent Goal rules remain authoritative unless TASK-045 explicitly changes presentation only.

## 7. Chat lifecycle and continuation after visible `[Chat]` removal

TASK-045 removes `[Chat]` only from the mandatory visible response close. It does not erase continuation semantics from Project state.

`09 Handoff`, `03 Current State`, Goal/Action/Envelope records, and other governed continuity surfaces may continue to use:

```text
CONTINUE_CURRENT_CHAT | START_NEW_CHAT
```

where the current Project/Framework contract needs them.

The assistant may still reason about continuation safety internally and persist it in Handoff. It no longer exposes a mandatory `[Chat]` field to the user after every response.

Existing historical records containing `[Chat]` remain historical truth and are not rewritten globally.

## 8. Required-read routing after visible `[Required Read]` removal

TASK-045 removes `[Required Read]` only from the mandatory visible response close.

Required-read semantics remain in canonical routing locations such as:

- `PROJECT-BOOTSTRAP.md`;
- active `00 / 01 / 03`;
- `09 Handoff` continuation contract;
- task/action/Goal-specific routing;
- command-specific contracts when a command explicitly requires source resolution.

An agent resuming work still reads the canonical Project sources required by governance. The user no longer needs to see that routing list at the end of every ordinary response.

Historical response examples/evidence remain historical provenance where appropriate.

## 9. Response Close Completeness Gate v2

TASK-045 revises the global final-response gate.

Before emit, every Framework-governed final response SHALL verify:

1. exactly the two mandatory headings are present once and in order;
2. exactly one visible `[Next Action]` field is present;
3. exactly one visible `[Next Goal]` field is present immediately after `[Next Action]`;
4. exactly one visible `[Reason]` field follows `[Next Goal]`;
5. there is no mandatory visible `[Chat]` field;
6. there is no mandatory visible `[Required Read]` field;
7. nothing follows `[Reason]`;
8. `[Next Action] = ไม่มีขั้นตอนถัดไป` implies `[Next Goal] = ไม่มี`;
9. any non-`ไม่มี` Next Goal is a literal copy-ready `[Goal]` or `[Goal] CHANGE` command satisfying the safety rules above;
10. contradictory or duplicate close content is corrected before emit.

TASK-042's unskippable-final-path invariant remains in force: ordinary success, read-only/status/diagnostic, failure, blocked action, timeout, partial result, persistence failure and exception-recovery paths all converge on the revised gate.

TASK-043's Command Contract Completeness Gate still runs before the Response Close Completeness Gate for recognized Registered Commands.

## 10. Registered-command interaction

TASK-045 does not add or remove a registered Project command. The registry remains exactly:

- `[Project Status]`
- `[Project Path]`
- `[Project Upgrade]`
- `[Goal]`
- `[Meeting]`
- `[Session]`
- `[Project Audit]`

For recognized commands:

```text
Recognize
→ Resolve Contract
→ Fresh Observe
→ Materialize Governed Structure
→ Populate
→ Command Contract Completeness Gate
→ Response Close Completeness Gate v2
→ Emit
```

`[Next Goal]` cannot replace command-body requirements.

## 11. Failure and edge cases

### 11.1 Tool/MCP failure

A failure response still receives the mandatory two headings and three visible fields. If a concrete recovery action exists, put it in `[Next Action]`. Do not create a speculative Goal merely because the failure interrupted work.

### 11.2 Connector unavailable

If the connector state makes the bounded outcome unclear or impossible to scope safely, `[Next Goal] = ไม่มี`.

### 11.3 Partial result

If a bounded persistent Goal would clearly continue the same user objective and no current active Goal covers it, a safe Goal suggestion may be shown. Otherwise use `ไม่มี`.

### 11.4 Refusal or blocked action

Do not use `[Next Goal]` to route around a prohibition or missing authority. It is not a bypass mechanism.

### 11.5 Active Goal completion

When an active Goal is terminal and there is no next action, both `[Next Action]` and `[Next Goal]` reflect no further work. Do not automatically invent a successor Goal.

## 12. Framework release classification

This is a user-visible Strict Governed Interface change to the mandatory response close. It is broader than a patch because consumers that validate the old four-field contract need to adapt, while Project Source Schema and Stable-ID families remain unchanged.

Classification:

```text
Framework: 1.14.0 → 1.15.0
Schema: 1.0.0 unchanged
release_format: 3 unchanged
Migration: additive/removal presentation-contract migration with preserved internal continuity semantics
```

Initialized Projects remain locally pinned and do not auto-upgrade. Brownfield Projects adopt the new close only through their normal governed `[Project Upgrade]` path.

## 13. Migration guidance

For `1.14.0 → 1.15.0`:

- update current response-close contract references from four fields to three fields;
- remove mandatory visible `[Chat]` and `[Required Read]` requirements;
- add mandatory visible `[Next Goal]` after `[Next Action]`;
- preserve historical pre-1.15 examples/evidence as provenance;
- preserve internal Handoff chat-continuity and Required Read pointers;
- preserve `[Goal]` command authority rules;
- do not synthesize Goal records merely because the new field exists;
- verify starter/current distribution surfaces and pressure scenarios;
- perform one final unchanged-candidate `RELEASE_FULL`.

## 14. Project Settings / thin-adapter boundary

Project Settings and vendor launcher surfaces are discovery adapters, not Project authority. TASK-045 SHALL update maintained guidance that tells users what response-close rule to place in Project instructions/settings when that guidance currently duplicates the old visible close.

If the thin official ChatGPT/Claude launcher does not contain the old four-field response-close payload, it need not be expanded merely for TASK-045. Thinness is preserved.

TASK-045 cannot mutate a live external ChatGPT Project Setting from repository Markdown. Repository completion means the canonical Framework distribution and copy-ready guidance are updated. A currently running chat that still has older injected Project instructions continues to obey those injected instructions until the consuming Project/settings adopt Framework 1.15.

## 15. Affected current Framework surfaces

At minimum inspect/update as applicable:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- new TASK-045 Framework amendment
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `README.md`
- `Framework-Source/MIGRATION-NOTES.md`
- `Framework-Source/templates/00-project-source-framework.md`
- `Framework-Source/templates/core-document-skeletons.md`
- `Framework-Source/templates/project-source-mockup/README.md`
- maintained Project Source mockup/starter current stamps and response-close guidance where applicable
- `Framework-Source/tests/pressure-scenarios.md`
- `docs/superpowers/PROJECT-TASKS.md`
- ProjectFramework active Project Source Goal/evidence/continuation records.

Historical amendments/specs/evidence remain unchanged unless they are current maintained routing surfaces rather than provenance.

## 16. Verification strategy

TDD is mandatory for the response contract.

### RED

Add pressure scenarios `421–432` before production Framework semantics change. Verify the existing 1.14 implementation fails the new contract expectations for the right reasons.

Scenario set:

421. exact new three-field visible order;
422. visible `[Chat]` removed;
423. visible `[Required Read]` removed;
424. copy-ready new `[Goal]` suggestion;
425. copy-ready `[Goal] CHANGE` suggestion;
426. existing active Goal already covers work → `ไม่มี`;
427. no Next Action → Next Goal `ไม่มี`;
428. ambiguous/high-risk opt-in → `ไม่มี`;
429. `PERSISTENCE_PENDING` recovery cannot be bypassed by Next Goal;
430. Handoff still preserves chat lifecycle/required-read pointers internally;
431. Command Contract Completeness Gate remains before revised response gate;
432. Markdown visibility and nothing after `[Reason]`.

### GREEN / affected verification

Verify:

- new release/amendment identity;
- Core/SKILL exact contract alignment;
- README/current templates aligned;
- seven-command registry unchanged;
- TASK-042/TASK-043 semantics preserved except the intentionally revised response gate payload;
- `[Goal]` authority model preserved;
- migration notes present;
- starter stamps/current mockup aligned where applicable;
- no runtime/code artifact introduced;
- full branch `git diff --check` passes;
- existing V2 TASK-044 worktree/files are not mutated by TASK-045.

### RELEASE_FULL

Freeze one final candidate after affected verification. Run exactly one state-bound `RELEASE_FULL` on that unchanged candidate, record candidate/tree/Framework-Source tree identities, commit release evidence, then terminalize Project Source Goal state.

## 17. Completion semantics

TASK-045 may become locally DONE only when:

- design/spec committed and approved;
- plan committed;
- RED observed before production change;
- implementation current surfaces are GREEN;
- AFFECTED verification passes;
- final candidate is frozen;
- exactly one final RELEASE_FULL passes on that unchanged candidate;
- release evidence is committed;
- completion commit(s) are freshly observed;
- Project Source records `OUT-012 ACHIEVED / AUTH-012 TERMINATED / ACT-024 DONE / ENV-012 EXPIRED`.

`commit ≠ push`. Remote publication remains a separate user authorization and is not part of this Goal.
