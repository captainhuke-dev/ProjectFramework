# Framework Governance Amendment — TASK-033 Task Dependency & Portfolio Planning

**Framework:** 1.12.0
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT WITHIN SET1 CANDIDATE
**Task:** TASK-033 — Task Dependency & Portfolio Planning

## Purpose

Framework 1.12.0 introduces explicit development/backlog Task planning metadata so agents do not infer sequencing from Task number, proximity, or chat history.

Binding invariants:

```text
Task dependency metadata ≠ Project-management DEP-* objects
Task readiness ≠ Task lifecycle status
Recommended order ≠ execution authority
Task number/proximity ≠ dependency evidence
```

## Canonical fields

A durable Task source MAY declare:

```yaml
depends_on: ["TASK-XXX"]
blocks: ["TASK-YYY"]
enables: ["TASK-ZZZ"]
parallelizable_with: ["TASK-AAA"]
priority: "CRITICAL | HIGH | NORMAL | LOW | UNSET"
readiness: "READY | WAITING | BLOCKED | UNKNOWN"
```

These fields are planning metadata only. They add no Stable-ID family, semantic slot, scheduler, queue daemon, or agent orchestrator.

## Readiness

- `READY` — declared required Task dependencies are satisfied and no known blocker prevents start.
- `WAITING` — an explicit sequencing prerequisite/dependency is not yet satisfied.
- `BLOCKED` — a material blocker prevents progress independent of ordinary sequencing.
- `UNKNOWN` — dependency/readiness evidence is unresolved, contradictory, cyclic, or references unknown Tasks.

Readiness does not change lifecycle. A Task may be `TODO + READY`; `READY` never means `DONE`.

## Priority

```text
CRITICAL > HIGH > NORMAL > LOW > UNSET
```

Priority is advisory planning order after dependency/safety constraints. It never bypasses `depends_on`, `AUTH-*`, Risk, binding, review, or explicit user decisions.

## Validation

Current planning validation detects self-dependency, cycles, unknown Task references, stale/superseded dependency targets, contradictory `parallelizable_with` declarations, and `READY` claims that conflict with unresolved required dependencies.

Cycles/contradictions fail closed as `UNKNOWN` or `BLOCKED` as supported. The Framework performs no automatic graph repair.

## DEP-* separation

`DEP-*` in `91 Project Management Control` remains the canonical home for material Project outcome/work dependencies. Task planning edges describe backlog/development sequencing only and are not mirrored to/from `DEP-*` automatically.

## Recommended execution order

An Agent MAY compute an advisory recommended order from declared dependency/readiness/priority/blocker metadata. User reprioritization remains authoritative, but reprioritization does not silently erase dependency facts. Automatic execution is not introduced.

## Set 1 application

Set 1 records the explicit chain:

```text
TASK-033
→ TASK-027
→ TASK-034
→ TASK-035
→ TASK-037
```

This order is declared by Task metadata and Set 1 Goal evidence, not inferred from numbering.

## Adoption

GREENFIELD materializes planning metadata only when Task dependencies/priorities are actually known. Brownfield preserves existing Task history; missing relationships remain unset/UNKNOWN until assessed. Framework upgrades never invent dependencies from numbering or prior execution order.

TASK-033 adds no scheduler, queue daemon, automatic Task executor, or agent orchestrator.
