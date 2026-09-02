# TASK-043 — Registered Command Strict-Interface & Contract Completeness Hardening Design

**Status:** USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL
**Target:** Project Source Framework `1.12.2` / Schema `1.0.0` / release format `3`
**Scope:** Documentation/governance semantic hardening only; no parser service, response interceptor, middleware, validator/CLI, runtime enforcement, tool code, daemon, watcher, scheduler, or vendor UI automation
**Source:** User-supplied Registered Command semantic-compliance proposal; TASK-043 registration; user `[Goal]` instruction on 2026-09-02 to execute TASK-043 through verified completion

## 1. Problem

ProjectFramework already has three relevant layers:

1. Registered Command identity and command-specific semantics in Core Governance and SKILL;
2. fresh-observation/fail-closed rules for commands such as `[Project Status]`;
3. TASK-042's unskippable Response Close Completeness Gate for every Project-governed final response.

A remaining gap exists between command semantics and command execution. A capable Agent may recognize a valid Registered Command, collect substantially correct facts, then replace the governed command interface with an equivalent narrative, omit a required dimension, reorder governed sections, rename canonical report labels, or rely on a stale shortcut. Such a response can be semantically useful while still violating the Registered Command contract.

Framework `1.12.1` also contains a concrete current-surface drift: Core Governance requires `[Project Status]` dimensions in this order:

```text
Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers → Continuity
```

while current `Framework-Source/SKILL.md` command text and quick reference stop at `Blockers`.

## 2. Root Cause

TASK-043 treats the defect as two coupled semantic gaps:

1. **Interface-strength gap:** Registered Commands are described as governance/interface contracts, but current wording does not explicitly state that semantic equivalence is insufficient when a command defines required structure/order/tokens/freshness/fail-closed representation.
2. **Command-body completeness gap:** TASK-042 verifies the global mandatory response close, but there is no explicit pre-emit gate for the body of a recognized Registered Command.

The problem is not missing command registration, missing brackets/case-insensitive matching, or missing Response Close finalization.

## 3. Goals

TASK-043 makes the following statements true:

- A recognized Registered Command is a **Strict Governed Interface**, not merely a natural-language request for equivalent information.
- Required command dimensions, governed order, canonical tokens/vocabulary, freshness obligations, fail-closed representation, and authority boundaries are non-discretionary unless the active command contract explicitly says otherwise.
- Missing evidence never authorizes structural omission; the governed field/dimension remains present and uses the applicable `UNKNOWN`, `VERIFICATION_REQUIRED`, or command-specific fail-closed state.
- An equivalent narrative, renamed dashboard, reordered structure, or stale-memory reconstruction does not satisfy a Registered Command contract when it bypasses governed structure.
- Flexible prose remains allowed inside fields/sections whose wording is not governed. Strict interface does not require deterministic sentences.
- Every recognized Registered Command passes a **Command Contract Completeness Gate** before TASK-042's Response Close Completeness Gate.
- Current Core/SKILL command summaries are aligned, beginning with the verified `[Project Status]` `Continuity` omission.
- Regression scenarios make correct-information/wrong-protocol failures observable.

## 4. Non-Goals

TASK-043 does not:

- register a new Project command;
- change the meaning of existing commands except to align verified current-surface drift;
- make all response prose byte-identical or deterministic;
- require one universal table/Markdown rendering when the active command contract does not govern that presentation detail;
- change the existing Response Close headings/fields/order/lifecycle tokens;
- replace TASK-042's Response Close Completeness Gate;
- create a new Stable-ID family, semantic slot, lifecycle state, Epistemic Status, health state, authority family, or Git freshness state;
- auto-upgrade initialized Projects;
- add a parser, executable schema, validator, CLI, response middleware/interceptor, bot, hook, CI/CD, scheduler, watcher, daemon, or tool/runtime enforcement;
- rewrite historical amendments/specs/plans/evidence whose prior wording was true at capture time.

## 5. Architecture

The target response path for a recognized Registered Command is:

```text
Recognize bracketed Registered Command
        |
        v
Resolve active local command contract
        |
        v
Refresh required sources / fresh-observe mutable dimensions
        |
        v
Materialize governed command skeleton
        |
        v
Populate evidence-supported values
        |
        v
Command Contract Completeness Gate
        |
        v
TASK-042 Response Close Completeness Gate
        |
        v
Emit final response
```

The two gates have different responsibilities:

```text
Command Contract Completeness Gate = command body/interface compliance
Response Close Completeness Gate   = global mandatory response close compliance
```

Neither gate grants mutation, disclosure, binding, Git, runtime, or other authority.

## 6. Registered Command Strict-Interface Contract

Core Governance adds a normative rule with this semantic meaning:

> A recognized Registered Command is a governed interface invocation, not merely a request for equivalent information. Once command identity is resolved, the Agent MUST execute the active local command contract and preserve every required structural/semantic element governed by that contract. The Agent MUST NOT replace the governed command response with an equivalent narrative, renamed/reordered structure, omitted required dimension, inferred shortcut, or stale-memory reconstruction unless the active command contract explicitly permits that variation.

### 6.1 No-discretion elements

When governed by the active command contract, the Agent MUST preserve:

- Registered Command identity;
- required report dimensions/sections;
- required dimension order;
- canonical status/report vocabulary and tokens;
- command-specific freshness requirements;
- explicit unavailable-evidence representation;
- authority and mutation boundaries;
- command-specific lifecycle/result states;
- composition with the mandatory Response Close contract.

### 6.2 Flexible elements

Unless otherwise governed, the Agent MAY adapt:

- explanatory prose inside a required section;
- Thai/English prose around canonical tokens;
- sentence length and concise rationale;
- optional notes that do not displace required structure;
- table versus compact key/value rendering only when the command contract does not require a stricter representation.

When uncertain whether an element is structural or stylistic, preserve the canonical structure.

## 7. Command Contract Completeness Gate

For every recognized Registered Command, immediately before the global TASK-042 Response Close Completeness Gate, the Agent performs a lightweight semantic check on the command body.

Minimum checks:

```text
Registered command identity resolved?                     YES
Active local command contract resolved?                   YES
Required dimensions/sections present?                     YES
Governed order preserved?                                 YES
Freshness obligations satisfied or explicitly unavailable? YES
Canonical tokens/vocabulary preserved?                    YES
Unsupported inference/stale-memory substitution absent?   YES
Command-specific authority boundaries preserved?          YES
```

If a required check fails, the Agent repairs the command body before final-response emit.

If the active command contract itself cannot be resolved safely, the Agent does not downgrade the invocation into an ordinary summary. It preserves whatever command structure can be established from active authority and reports unresolved elements as `VERIFICATION_REQUIRED` / `UNKNOWN` as applicable. It never reconstructs missing rules from memory.

## 8. `[Project Status]` Alignment

Current Framework `1.12.1` Core Governance is the normative current reference for `[Project Status]` dimension order:

```text
Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers → Continuity
```

TASK-043 aligns current SKILL surfaces to that contract. At minimum:

- the main Registered Project Commands section includes `Continuity`;
- the SKILL quick-reference row includes `Continuity`;
- command-body completeness semantics require all applicable dimensions to remain represented;
- unavailable mutable evidence remains explicit `UNKNOWN` / `VERIFICATION_REQUIRED` rather than causing the dimension to disappear.

TASK-043 does not change the meaning of Continuity; it only repairs current-surface drift against the already-current Core contract.

## 9. Pressure Scenarios

Append new scenarios after the current cumulative range (`1–350`). The design reserves scenarios `351–356`:

1. **351 — Correct Information, Wrong Protocol**: true facts do not excuse bypassing command structure.
2. **352 — Narrative Replacement of Registered Command**: `[Project Status]` cannot become a free-form summary.
3. **353 — Missing Fresh Observation Preserves Dimension**: unavailable Git/other evidence produces explicit fail-closed state, not omitted section.
4. **354 — Style Instruction Cannot Weaken Command Structure**: conversational/concise request may change prose but not governed sections/order/tokens.
5. **355 — Command Gate Precedes Response Close Gate**: a response with a perfect mandatory close but incomplete command body still fails.
6. **356 — Core/SKILL `[Project Status]` Alignment**: both current surfaces include the exact governed dimension sequence through `Continuity`.

## 10. Affected Framework Surfaces

Implementation scope is intentionally bounded to current canonical surfaces needed to make the semantic change durable and releasable:

- `Framework-Source/references/framework-governance-amendment-260902-task043.md` — new current patch amendment;
- `Framework-Source/references/core-governance-rules.md` — Strict-Interface rule + Command Contract Completeness Gate;
- `Framework-Source/SKILL.md` — operational pipeline/gate + Core/SKILL `[Project Status]` alignment;
- `Framework-Source/tests/pressure-scenarios.md` — scenarios `351–356`;
- `Framework-Source/templates/00-project-source-framework.md` — consuming-project root template carries the strict command contract and aligned `[Project Status]` sequence;
- `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md` — maintained mockup root remains aligned with the current root template semantics where it duplicates command rules;
- `Framework-Source/FRAMEWORK-RELEASE.yaml` — patch release `1.12.2` and latest amendment pointer;
- `Framework-Source/MIGRATION-NOTES.md` — `1.12.1 → 1.12.2` migration guidance;
- current maintained Framework-version stamps in Framework starter/template surfaces where release verification requires cumulative release identity consistency;
- `README.md` only if needed to keep the current public release identity accurate; it does not need to duplicate the full strict-interface algorithm;
- `docs/superpowers/PROJECT-TASKS.md` and Project Source lifecycle/evidence for TASK-043 completion.

Thin ChatGPT/Claude launchers do not need new command-body semantics unless verification proves a current contradiction. They remain discovery adapters and must not duplicate the full contract.

Historical amendments/specs/plans/evidence are preserved.

## 11. Brownfield and Upgrade Behavior

Existing initialized Projects remain governed by their locally pinned Framework. Upstream `1.12.2` does not silently change an older local command contract.

Governed `[Project Upgrade]` adoption of TASK-043:

- preserves local `FRAMEWORK-001`, Stable IDs, Project-specific rules, bindings, history, authority, and existing command registry unless the target cumulative Framework already changes it;
- applies the Strict-Interface/command-gate semantic as part of the selected target Framework;
- aligns current command summaries without rewriting historical records;
- creates no runtime validator/enforcement requirement;
- uses existing Direct-to-Latest classification, Preview, approval, verification, and promotion rules.

## 12. Release Classification

TASK-043 targets **Framework `1.12.2` / Schema `1.0.0` / release format `3`**.

Rationale: this is a backward-compatible patch-level reliability hardening of existing Registered Command execution semantics plus repair of verified current-source drift. It adds no command identity, semantic slot, object schema, Stable-ID family, lifecycle vocabulary, or authority model.

## 13. Verification Contract

Implementation acceptance must demonstrate at least:

1. Baseline Core contains `[Project Status] ... → Continuity` while baseline SKILL current command summaries omit it.
2. New scenarios `351–356` are written first and fail against the pre-implementation Framework state for the intended missing semantics.
3. Core contains an explicit Registered Command Strict-Interface normative rule.
4. Core contains a Command Contract Completeness Gate distinct from TASK-042 Response Close Completeness Gate.
5. SKILL contains the operational sequence `Recognize → Resolve Contract → Fresh Observe → Materialize Structure → Populate → Command Contract Completeness Gate → Response Close Completeness Gate → Emit` or semantically exact equivalent.
6. `[Project Status]` Core and SKILL current dimension sequences both include `Continuity` in governed order.
7. Missing required evidence remains explicit and does not authorize omission of the governed dimension.
8. Style/conversational preference cannot weaken a command's governed structure.
9. A correct mandatory Response Close does not make an incomplete command body compliant.
10. No new Registered Command is created.
11. Existing command names/bracket/case-insensitive matching remain unchanged.
12. Existing TASK-042 mandatory response-close semantics remain unchanged and remain the final global pre-emit gate.
13. Thin launchers remain thin; no duplicate full command contract is added unless a verified contradiction requires a bounded correction.
14. ProjectFramework local Project Source pin remains Framework `1.7.0` / Schema `1.0.0`; upstream movement does not auto-upgrade it.
15. Historical amendments/specs/plans/evidence remain unchanged except for new references to them from current lifecycle records where appropriate.
16. No runtime/parser/interceptor/middleware/validator/CLI/tool/automation artifact is added.
17. `git diff --check` passes.
18. affected verification passes.
19. exactly one final `RELEASE_FULL` passes on the unchanged release candidate and is captured as state-bound evidence before TASK `DONE`.
20. TASK-043 completion is represented by an observed completion commit; `commit ≠ push` remains true.

## 14. Authority and Security Boundary

Strict command execution changes response compliance, not authority. A command cannot gain mutation, push, destructive-operation, Root/Binding, runtime, secret, or disclosure authority merely because its interface is now stricter. Existing system/developer/tool/safety/authentication controls remain independently binding.

## 15. Approved Design Decision

The user first approved registering TASK-043 with the bounded scope `Registered Command Strict-Interface + Command Contract Completeness Gate + Core/SKILL drift repair`, then invoked `[Goal] ดำเนินงาน Task จนเสร็จ` on 2026-09-02. That Goal authorizes continuous local design/planning/edit/test/fix/verify/commit/checkpoint work within TASK-043. Push/publication, destructive operations, unrelated Root/Binding changes, and external disclosure remain exact opt-ins.

## 16. Success Statement

TASK-043 is successful when a capable Agent cannot legitimately satisfy a recognized Registered Command merely by returning equivalent facts: the governed command interface must be structurally complete and evidence-correct before the existing mandatory response-close gate permits final emit, and the current Core/SKILL `[Project Status]` contract no longer disagrees about `Continuity`.
