---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.12.2"
project_source_framework_version: "1.13.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_GOAL_TASK028_THEN_TASK032_2026-09-02"
compatibility: "BACKWARD_COMPATIBLE_INTEGRITY_REMEDIATION_SUITE"
---

# Framework 1.13.0 Amendment — Project Audit + Integrity Remediation Suite

Framework `1.13.0` preserves Framework `1.12.2` unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`. TASK-028 adds one Registered Command, `[Project Audit]`. TASK-032 is part of the same cumulative release but its repair/remediation workflow remains non-normative until TASK-028 reaches its focused completion checkpoint.

## 1. `[Project Audit]` Registered Command

Canonical identity is exactly `[Project Audit]`. Literal `[` and `]` are required; matching inside brackets is case-insensitive under the existing Registered Command contract. The bare command audits the current Project across all applicable categories. `[Project Audit] <explicit bounded focus>` narrows the audit and never expands authority.

`[Project Audit]` is read-only. It MUST NOT repair, migrate, rewrite, create/close canonical issue objects, resolve conflicts, push, change bindings, or materialize authority. The invariant is exact:

```text
Audit finds ≠ Audit fixes
Finding ≠ Issue/Drift/Conflict/Migration record
```

## 2. Strict Governed Interface

TASK-043 applies unchanged. `[Project Audit]` MUST present these top-level dimensions exactly and in this order: **Scope → Health → Categories → Findings → Unknowns → Evidence → Repair Routes → Continuity**.

```text
Scope
→ Health
→ Categories
→ Findings
→ Unknowns
→ Evidence
→ Repair Routes
→ Continuity
```

All dimensions remain present even when empty. Missing evidence is represented explicitly with `UNKNOWN` / `VERIFICATION_REQUIRED` as applicable. Equivalent narrative, reordered sections, omitted dimensions, or stale-memory reconstruction are noncompliant.

The existing execution/finalization pipeline remains unchanged:

```text
Recognize
→ Resolve Contract
→ Fresh Observe
→ Materialize Governed Structure
→ Populate
→ Command Contract Completeness Gate
→ Response Close Completeness Gate
→ Emit
```

## 3. Audit health vocabulary

Audit category health reuses exactly:

```text
GREEN | AMBER | RED | UNKNOWN
```

`GREEN` means sufficiently resolved evidence with no material inconsistency. `AMBER` means a material non-invalidating concern needs review. `RED` means a material contradiction/broken reconstructability/invalid authority-routing condition blocks safe reliance on affected scope. `UNKNOWN` means evidence is insufficient and never means healthy. No numeric aggregate score is defined.

## 4. Canonical audit categories

Evaluate applicable categories in this order:

1. **Bootstrap & Identity**
2. **Routing & Current State**
3. **Canonical Records & Stable IDs**
4. **Bindings & Git Freshness**
5. **Continuity & Persistence**
6. **Conditional Surfaces & Migration**
7. **Relations, Knowledge & Execution Profiles**

Applicability follows existing Framework rules; optional surfaces are not fabricated. `00 / 01 / 03 / 09 / 14` consistency, current Stable-ID resolvability/canonical homes, binding/freshness, persistence/continuation, conditional documents, and applicable `REL-*`/Knowledge/Execution-profile surfaces are evaluated from current authoritative evidence.

## 5. Findings, evidence, unknowns, and bounded output

An audit finding is presentation, not Project authority and not a Stable ID. Do not create `AUDIT-*`, `FINDING-*`, or another audit/finding family. Each material finding states category, observed condition, health state, authoritative/current source pointers, why it matters, existing canonical object/home when already materialized, and a governed repair or investigation route.

Freshness follows existing truth contracts. Volatile Git/worktree/remote/binding/runtime facts are freshly observed when material. Unavailable evidence remains `UNKNOWN / VERIFICATION_REQUIRED`; one unavailable source does not erase other category results.

Bound repetitive findings by aggregation only when count and affected scope remain visible. Material `RED`, `AMBER`, and `UNKNOWN` findings MUST NOT be silently suppressed. Evidence is summarized with source pointers rather than copied wholesale.

## 6. Repair Routes are advisory only

`Repair Routes` names the existing canonical route that would apply if remediation is later authorized, for example:

```text
stale current/expected truth       → DRIFT-* / current canonical owner
competing authoritative semantics  → CONFLICT-* + Decision/approval as applicable
migration/collision requirement    → MIG-*
material issue                     → ISS-*
material proposed change           → CR-* when change-control semantics apply
execution work                     → ACT-* / ENV-* under valid AUTH-*
Root/Binding mutation              → explicit approval + FRAMEWORK-001 revision flow
shared/external mutation           → applicable R2/R3 authority and target checks
```

Naming a route never creates the object and never grants mutation authority.

## 7. TASK-032 suite boundary

TASK-032 Governed Project Repair / Remediation is dependency-ordered after TASK-028. Until TASK-028 focused implementation is committed and observed, this amendment creates no repair command, no remediation Stable-ID family, and no normative repair workflow beyond preserving the separation `Audit finds ≠ Audit fixes`.

TASK-042 Response Close Completeness Gate and TASK-043 Registered Command Strict-Interface / Command Contract Completeness Gate remain unchanged.

## 8. Non-goals

Framework 1.13.0 TASK-028 creates no validator, scanner, linter executable, CLI, audit daemon, watcher, scheduler, background agent, repair bot, automatic issue materialization, auto-migration, auto-fix, or automatic conflict resolution. Existing initialized Projects remain locally pinned and adopt this contract only through governed `[Project Upgrade]` / Direct-to-Latest flow.
