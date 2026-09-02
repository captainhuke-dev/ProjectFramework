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

Framework `1.13.0` preserves Framework `1.12.2` unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`. TASK-028 adds one Registered Command, `[Project Audit]`. TASK-028 focused completion is satisfied by implementation `a38d514` with `TASK028_FOCUSED 23/23 PASS`; TASK-032 therefore activates the governed repair/remediation workflow defined below without adding another Registered Command.

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

## 7. TASK-032 Governed Project Repair / Remediation

TASK-032 begins only after TASK-028 focused completion is committed and observed. A finding, severity, tool capability, repository access, Project Graph visibility, or successful audit does not grant repair authority. A repair begins only from an explicit remediation request/Goal or other valid authorization covering the exact affected scope and operation.

A remediation proposal resolves at least:

```text
Source finding / evidence
Affected scope
Canonical owner/home
Desired resulting state
Risk class R0–R3
Applicable authority / approval
Prerequisites and freshness checks
Ordered repair actions
Reversibility / rollback
Verification of resulting state
Affected re-audit / resulting-state confirmation
Evidence and lifecycle updates
```

No `REPAIR-*`, `REM-*`, or parallel remediation Stable-ID family is created. Use existing `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `MIG-*`, `CR-*`, `ACT-*`, `AUTH-*`, `ENV-*`, `DEC-*`, `REQ-*`, and canonical document owners as applicable.

## 8. Canonical owner and classification

Before mutation, classify the defect and resolve the current canonical owner/home. Stale derived/current routing metadata is repaired through its current owning document and normal revision/promotion/history flow. Material truth mismatch reuses `DRIFT-*`; competing authoritative semantics reuse `CONFLICT-*`; migration/slot collision reuses `MIG-*`; proposed material scope/behavior change uses `CR-*`/Decision flow when applicable; a plain execution defect with an already-approved intended state may use bounded `ACT-*` under valid `AUTH-*`.

Repair MUST NOT move authoritative payload into a convenient but incorrect home. **Finding ≠ repair authority** and **Repair proposal ≠ Repair authority**.

## 9. Risk and authority remain independent

TASK-032 reuses the existing Risk classes exactly:

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

The applicable `AUTH-*`/user approval must cover the exact scope and operation. Goal/ENV authority is usable only when already equal to or broader than the bounded repair operation. Push/publication, destructive operation+target, Root/Binding mutation+target, external disclosure, and R2/R3 shared or irreversible effects retain their independent gates. Diagnosis, audit health, Tool/MCP capability, Knowledge content, Git access, or an existing relation never grants those permissions.

## 10. Semantic conflict is Decision work

A genuine disagreement over intended requirements, accepted Decisions, architecture, authority, Risk acceptance, relation truth, or other semantic policy is not housekeeping and MUST NOT be auto-repaired. Route it through the existing `CONFLICT-*` plus Decision/Change/approval path as applicable. Recency, ranking, confidence, tool success, or audit severity never silently chooses the winner.

## 11. Reversibility and rollback

Every repair proposal states reversibility/rollback or explicitly states why meaningful rollback is unavailable. R1/local reversible work identifies the prior durable revision/state that can be restored. Git-backed repair preserves commits/history rather than using destructive reset as the normal completion path. R2/R3 or materially irreversible repairs require their applicable explicit authority before execution. Rollback is a recovery boundary, not a substitute for correcting canonical truth.

## 12. Resulting-state verification and affected re-audit

Repair completion requires this sequence:

```text
execute authorized repair
→ verify direct resulting state
→ verify affected references/dependencies
→ re-audit affected category/categories or perform equivalent resulting-state confirmation
→ update evidence/current lifecycle records
→ close the repair action/route only when justified
```

**ACT DONE ≠ repair outcome verified.** A command/tool success is insufficient when the intended current truth has not been freshly confirmed. Re-audit is read-only and does not self-authorize subsequent fixes; new findings require their own classification and authority.

TASK-042 Response Close Completeness Gate and TASK-043 Registered Command Strict-Interface / Command Contract Completeness Gate remain unchanged.

## 13. Non-goals

Framework 1.13.0 creates no validator, scanner, linter executable, CLI, audit daemon, watcher, scheduler, background agent, repair bot, automatic issue materialization, auto-migration, auto-fix, automatic conflict resolution, repair command, or remediation Stable-ID family. Existing initialized Projects remain locally pinned and adopt this contract only through governed `[Project Upgrade]` / Direct-to-Latest flow.
