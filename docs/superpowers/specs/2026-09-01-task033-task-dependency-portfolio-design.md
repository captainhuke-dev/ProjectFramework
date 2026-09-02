# TASK-033 Task Dependency & Portfolio Planning — Design

**Task:** TASK-033 — Task Dependency & Portfolio Planning
**Design state:** USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL
**Set 1 position:** 1 of 5
**Target Framework:** 1.12.0
**Project Source Schema:** 1.0.0
**Release format:** 3

## 1. Purpose

ProjectFramework's durable Task source records Task lifecycle but currently lacks canonical metadata for Task-to-Task dependency, blocking, enablement, safe parallelism, priority, and readiness. Agents therefore risk inferring order from Task number, proximity, or chat history.

TASK-033 defines a bounded planning contract for development/backlog Tasks while preserving the invariant:

```text
Task dependency metadata ≠ Project-management DEP-* objects
Task readiness ≠ Task lifecycle status
Recommended order ≠ execution authority
Task number/proximity ≠ dependency evidence
```

## 2. Canonical Task planning vocabulary

A Task MAY declare these planning fields when material:

```yaml
depends_on: ["TASK-XXX"]
blocks: ["TASK-YYY"]
enables: ["TASK-ZZZ"]
parallelizable_with: ["TASK-AAA"]
priority: "CRITICAL | HIGH | NORMAL | LOW | UNSET"
readiness: "READY | WAITING | BLOCKED | UNKNOWN"
```

These are Task-registry planning fields, not Project Source Stable-ID families. They do not create `TASKDEP-*`, do not replace `DEP-*` in `91 Project Management Control`, and do not alter canonical Task lifecycle states such as `TODO | IN_PROGRESS | DONE`.

`depends_on` is directional and normative for sequencing when declared. `blocks` and `enables` are explanatory/derived relationship declarations and MUST be consistent with the declared dependency graph when both sides are maintained. `parallelizable_with` means no known sequencing dependency under the current scope; it does not guarantee conflict-free implementation if mutable prerequisites change.

## 3. Readiness semantics

```text
READY   = all declared required Task dependencies are terminally satisfied and no known blocker prevents start
WAITING = sequencing dependency or explicitly deferred prerequisite is not yet satisfied
BLOCKED = a material blocker prevents progress even if dependency order would otherwise permit work
UNKNOWN = required dependency/readiness evidence is insufficient or contradictory
```

Readiness is evaluated from current Task source plus referenced evidence. It is not authority and MUST NOT auto-start work. A Task may remain `TODO` while `READY`.

## 4. Priority semantics

Priority is a planning signal only:

```text
CRITICAL > HIGH > NORMAL > LOW > UNSET
```

Priority never overrides `depends_on`, safety/authority gates, explicit user reprioritization, or semantic base freshness. Equal-priority Tasks may be ordered by declared enablement/dependencies; Task number is not a tie-breaker unless the user explicitly chooses it.

## 5. Validation rules

Planning validation MUST detect and surface:

- self-dependency;
- direct or transitive dependency cycles;
- references to unknown Task IDs;
- dependency on cancelled/superseded Tasks without an explicit replacement disposition;
- contradictory `parallelizable_with` versus `depends_on` declarations;
- stale dependency metadata after Task scope changes;
- declared `READY` while a required dependency is not satisfied.

A cycle or unresolved dependency contradiction yields `readiness: UNKNOWN` or `BLOCKED` as supported; it never authorizes automatic graph repair.

## 6. Recommended-order contract

An Agent MAY compute a recommended execution order from declared dependencies, readiness, priority, and current blockers. The result is advisory. The user may reprioritize any Task, but an override does not silently erase dependencies; if the user asks to start a blocked Task, the Agent reports which prerequisites remain and proceeds only within the scope that is genuinely independent and authorized.

Task planning may identify parallelizable groups, but ProjectFramework does not introduce a scheduler, agent orchestrator, queue daemon, or background executor.

## 7. Relationship to Project Source `DEP-*`

`DEP-*` in `91` remains the canonical Project-management object for material external/internal dependencies of outcomes/work. TASK-033 metadata is specifically for development/backlog Task sequencing in the Task registry. A Task dependency may reference a `DEP-*` as evidence/context when useful, but the two are not mirrored automatically.

## 8. Set 1 application

Set 1 is the first canonical application of TASK-033:

```text
TASK-033
→ TASK-027
→ TASK-034
→ TASK-035
→ TASK-037
```

Rationale:
- TASK-027 execution-tool policy is a foundation for TASK-034 capability/tool eligibility.
- TASK-034 gives TASK-037 an agent/model capability boundary.
- TASK-035 establishes publication/artifact/deployment distinctions consumed by TASK-037 trust-boundary review.
- TASK-037 closes the suite by integrating tools, models, external services, artifacts, runtime, and privileged surfaces.

This sequence is explicit metadata, not inferred from Task numbering.

## 9. GREENFIELD/Brownfield

Task planning metadata is applicable only when a Project maintains a durable Task source. GREENFIELD does not synthesize dependencies merely to populate fields. Brownfield adoption preserves existing Task history and adds planning metadata only after current relationships are assessed; unknown relationships remain `UNKNOWN`/unset rather than guessed.

## 10. Affected Framework surfaces

Implementation should update current maintained guidance only:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- TASK-033 Framework amendment
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `README.md`
- `Framework-Source/MIGRATION-NOTES.md`
- applicable task/project skeleton guidance
- `docs/superpowers/PROJECT-TASKS.md`
- `Framework-Source/tests/pressure-scenarios.md`

No vendor launcher expansion is required.

## 11. Verification

Pressure/AFFECTED verification must prove: explicit dependency vocabulary; cycle/unknown handling; readiness/lifecycle separation; priority cannot bypass dependencies/authority; `DEP-*` separation; no order inferred from Task number; advisory recommended order; no scheduler/orchestrator/runtime; Brownfield no invented edges; Set 1 metadata resolves consistently.
