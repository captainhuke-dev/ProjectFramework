---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "FRAMEWORK-001"
document_type: "PROJECT_SOURCE_FRAMEWORK"
semantic_slot: "00"
revision: 3
document_status: "ACTIVE"
supersedes: "00-Project-Source-Framework-r002-260829-1901.md"
framework_root: true
inherits_from: []
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T14:59:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Root Governance / Non-Removable Framework:** this document is the Project-local governance root. `FRAMEWORK-001` remains the stable identity in semantic slot `00`; it cannot be removed, bypassed, demoted, or replaced by a descendant rule. Every Project Source descendant inherits from this root. Root mutation requires User Explicit Approval and revision → validate → promote → supersede/archive history preservation.

## 1. Framework 1.15 Pin and Incorporated Normative Source

This initialized Project is explicitly upgraded and pinned to **ProjectFramework 1.15.0 / Project Source Schema 1.0.0** under `MIG-002` and the ACTOR-001 post-Preview approval of 2026-09-11T14:59:00+07:00.

The generic Framework 1.15 semantics incorporated into this Project-local root are resolved from the exact verified Framework distribution state below. These source files do **not** become a second Project authority: their pinned text is incorporated by this `FRAMEWORK-001`; this root remains the Project governance authority.

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  published_baseline_commit: "6e3dd6c987eacdbe8430dbd906c59f5678a07843"
  framework_source_tree: "835c5a24c909ef7de2d413c46a6451746ed5fbf0"
  framework_version: "1.15.0"
  schema_version: "1.0.0"
  release_format_version: 3
  captured_at: "2026-09-11T14:59:00+07:00"
  provenance_status: "VERIFIED"
```

Pinned Framework 1.15 source set incorporated here:

- `Framework-Source/FRAMEWORK-RELEASE.yaml` — blob `720518e929c2880c46a4b531dde6bca1a2a0ccfa`
- `Framework-Source/SKILL.md` — blob `79984f8da37069acad5c1061b421bbf781808c43`
- `Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md` — blob `e6eb24c9615887fa710ff8334672921ddeade199`
- `Framework-Source/references/core-governance-rules.md` — blob `5b30d146d668f429aa04e27521657c48712a6244`
- `Framework-Source/templates/00-project-source-framework.md` — blob `a46d4ee8a8b5ab96ff4ca56109e73a48608a5acb`
- `Framework-Source/templates/core-document-skeletons.md` — blob `00a6635d39c5e24d91fca724f8498bc87d903352`

Normative precedence inside the incorporated Framework set is: current approved amendment → Core Governance → operational SKILL/template guidance. This `FRAMEWORK-001` owns Project-specific identity, binding, pin, and specializations and never delegates Project authority merely because an upstream/distribution file is readable. If the exact pinned Framework source cannot be resolved when a rule omitted here is material, affected mutation fails closed; do not reconstruct missing semantics from memory or silently substitute a later upstream revision.

## 2. Authority and Inheritance

```text
0. User Explicit Instruction / Approval
1. 00 / FRAMEWORK-001 — this Project-local root
2. Framework-compliant Project-Specific Rules
3. Canonical Project Source documents / Decisions / Requirements
4. Task / Handoff / Prompt / Agent Instruction
```

Descendants may extend/specialize/add constraints but may not weaken this root or the incorporated pinned Framework semantics. Governed Markdown descendants declare `inherits_from: ["FRAMEWORK-001"]`; non-Markdown Project artifacts inherit through canonical registry/manifest/project identity routing.

If no valid active `FRAMEWORK-001` exists, Project Source is `INVALID + NOT_OPERATIONALLY_READY` for affected governed mutation.

## 3. Project Identity

```yaml
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
```

`project_uuid` is immutable. Rename, merge, split, migration, or repository movement must preserve reconstructable lineage.

## 4. Project Location Binding

This block is the canonical Project Location Binding. `03`, `09`, bootstrap adapters, tools, MCP/workspace IDs, branches, mounts, and recent activity may reference or evidence it but do not replace it.

```yaml
project_location_binding:
  github:
    binding_state: "BOUND"
    repository: "captainhuke-dev/ProjectFramework"
    repository_url: "https://github.com/captainhuke-dev/ProjectFramework"
    project_source_path: "Project-Source/"
    verification_status: "VERIFIED"
    last_verified_at: "2026-09-11T14:59:00+07:00"

  google_drive:
    binding_state: "NOT_APPLICABLE"
    project_root_id: "NOT_APPLICABLE"
    project_root_url: "NOT_APPLICABLE"
    display_path: "NOT_APPLICABLE"
    designated_progress_file: "NOT_APPLICABLE"
    designated_progress_file_id: "NOT_APPLICABLE"
    designated_progress_file_url: "NOT_APPLICABLE"
    verification_status: "USER_CONFIRMED"
    last_verified_at: "2026-08-29T17:07:00+07:00"

  local_workspaces:
    - environment_scope: "WINDOWS_PRIMARY"
      binding_state: "BOUND"
      canonical_path: 'E:\GitHub\ProjectFramework'
      repository: "captainhuke-dev/ProjectFramework"
      repository_url: "https://github.com/captainhuke-dev/ProjectFramework"
      verification_status: "VERIFIED"
      last_verified_at: "2026-08-29T17:07:00+07:00"
```

No generic non-Google-Drive external File Storage binding is applicable to this Project at this revision.

Binding rules:

- Binding state is exactly `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`; unresolved applicable routing is fail-closed for Material mutation.
- Repository Location Binding ≠ Local Workspace Binding ≠ current branch/worktree ≠ Canonical Integration Target ≠ Canonical Implementation Source ≠ Runtime/Persistent-State authority.
- Project Location Binding does not create `canonical_branch` authority.
- A one-off exact target is action-specific. Persistent binding change requires User Explicit Approval and another governed `FRAMEWORK-001` revision/promotion.
- Correct location grants no mutation, Risk, publication, implementation, runtime, disclosure, or secret authority.
- This `MIG-002` upgrade **does not change any Project Location Binding value**; the binding above is preservation of the predecessor root truth.

## 5. Project Graph Applicability

```yaml
project_graph:
  applicability: "VERIFICATION_REQUIRED"
  relation_document_slot: "92"
  external_index:
    owner_scope: "AI_CONTROLTOWER"
    authority: "DERIVED_ONLY"
```

`92` is conditional and is not materialized by this upgrade. No Project relation, OpenViking configuration, graph runtime, or cross-Project write authority is inferred.

## 6. Project Source Namespace and Canonical Homes

Project Source root:

```text
<Project-Root>/Project-Source/
```

Mandatory core: `00–05`, `09–17`; conditional: `06–08`, `40`, `60`, `91`, `92`; `18–19` reserved. `91` remains active because `OUT-014` terminal outcome history is materially applicable. This upgrade does not materialize `06–08`, `40`, `60`, or `92`.

Canonical object homes remain:

```text
DEC-* → 04         REQ-* → 05
ISS/DRIFT/CONFLICT-* → 08
CHG-* → 10         ACTOR/INST-* → 11
AUTH/DEL-* → 12    EVD-* → 13
ACT/ENV-* → 15     MIG-* → 16
SECRET-* → 17
RISK/ASM/MS/OUT/DEP/CR/GATE-* → 91
REL-* → 92 when active
```

Active canonical registries are materialized current projections, not delta chains. Referenced current Stable IDs must resolve without archive traversal. Archive is historical truth only. Historical terminated records may remain only in archived predecessor revisions when no current canonical record depends on their payload.

## 7. Bootstrap and Routing

Canonical route after Project-root access:

```text
PROJECT-BOOTSTRAP.md
→ active 00 / FRAMEWORK-001
→ active 01 / Project Source Index
→ active 03 / Current State
→ task-specific routing
→ active 09 / Handoff when continuation applies
```

`PROJECT-BOOTSTRAP.md`, Project Settings, README managed fallback, vendor launchers, MCP locations, and workspace IDs are discovery/routing surfaces only. They never replace Root Governance or grant authority.

A bootstrap/root mismatch that could route Material work to an incompatible target fails closed. Do not choose by recency or silently rewrite either side.

## 8. Truth, Freshness, Risk, Authority, and Secrets

Truth Domains remain `GOVERNANCE | INTENT | REQUIREMENTS | IMPLEMENTATION | RUNTIME | DATA | IDENTITY | AUTHORITY | HISTORY | EXTERNAL`.

Epistemic Status remains `VERIFIED | USER_CONFIRMED | INFERRED | ASSUMED | UNKNOWN | CONFLICTED | STALE`. Freshness remains `IMMUTABLE | STABLE | CHANGEABLE | VOLATILE`.

Risk classes remain:

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

Before R2/R3 mutation, fresh-read applicable authority and mutable prerequisites. Responsibility ≠ Authority. `ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED`. `DEP AVAILABLE ≠ DEP SATISFIED`. `commit ≠ push ≠ merge ≠ release ≠ artifact publication ≠ deployment`.

Actual secret values are prohibited in Project Source/evidence/bootstrap. `SECRET-*` stores reference metadata only.

## 9. Migration, Promotion, Verification, and Persistence

Existing initialized Projects never auto-upgrade. Framework upgrades use Direct-to-Latest cumulative migration by default and classify exactly `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`.

Promotion lifecycle:

```text
Preview / assessment
→ explicit required approval
→ candidate
→ affected/risk-scoped verification
→ one RELEASE_FULL on final unchanged candidate when required by path
→ promote
→ supersede/archive predecessor
→ sync Index/Manifest/current routing/evidence
→ postflight resulting-state confirmation
```

`MIG-002` is `ASSESSED_PATH`; its approved scope is the 1.7.0 → 1.15.0 Project upgrade described in active `16`. Intermediate release execution is not required, but preservation, rollback, evidence, history, verification, and promotion gates are not skipped.

Material Git-backed Task completion requires affected verification plus observed completion commit; WIP ≠ DONE. Logical Checkpoint ≠ RELEASE_FULL. Integration/publication re-resolves Base Freshness/evidence validity. Mergeable ≠ Acceptable.

Material connector work persists at Logical Checkpoints to its source-native durable owner; transient reads need not persist. Required persistence failure is `PERSISTENCE_PENDING` and must retain a concrete recovery action.

## 10. Registered Commands and Framework 1.15 Response Semantics

Registered commands are exactly seven:

```text
[Project Status]
[Project Path]
[Project Upgrade]
[Project Audit]
[Session]
[Goal]
[Meeting]
```

Recognized commands are Strict Governed Interfaces. Command Contract Completeness Gate runs before the final Response Close Completeness Gate.

Framework 1.15 mandatory visible response close in the pinned Framework semantics is:

```text
### ทำอะไรไป?

<concise result>

### และถัดไปคืออะไร?

[Next Action]: <one exact action or ไม่มีขั้นตอนถัดไป>

[Next Goal]: <one bounded copy-ready Goal suggestion or ไม่มี>

[Reason]: <concise reason>
```

Nothing follows `[Reason]` under the pinned Framework 1.15 contract. `[Next Goal]` is presentation-only and never creates authority. `[Chat]` and `[Required Read]` remain valid internal Handoff/continuation semantics but are not mandatory visible Framework 1.15 close fields.

## 11. Optional Framework 1.10–1.14 Surfaces

The cumulative 1.15 pin supports, without automatically materializing:

- optional `Project-Knowledge/` advisory/provenance layer;
- optional `Project-Execution/` tool/capability/trust profiles;
- optional derived/rebuildable `Project-Change-Feed/`;
- conditional `92 / REL-*` Project Graph and relation reconciliation;
- advisory impact analysis and notification governance;
- `[Project Audit]` plus separately authorized remediation workflow.

Optionality remains applicability-driven. Absence is valid. This Project upgrade creates no watcher, crawler, daemon, scheduler, notification sender, graph sync, model/tool router, validator/CLI, CI/CD, application runtime, or auto-repair engine.

## 12. Project-Specific Rules

No `PSR-*` is materialized at this revision. Add a Project-Specific Rule only through a governed future `FRAMEWORK-001` revision with required approval; it may specialize but never weaken Framework 1.15 semantics.

## 13. ProjectFramework Instantiation Record

```text
Project ID: PROJECTFRAMEWORK
Project Name: ProjectFramework
Project UUID: 00575e76-17ce-4dd3-ad24-377494a4a45b
Repository: captainhuke-dev/ProjectFramework
Project Source Root: Project-Source/
Framework Distribution Root: Framework-Source/
Project Source Framework Pin: 1.15.0
Project Source Schema: 1.0.0
Google Drive: NOT_APPLICABLE
External File Storage: NOT_APPLICABLE
Application Runtime: NOT_APPLICABLE — ProjectFramework is documentation/governance first and contains no application runtime merely by virtue of this Project Source
Upgrade: MIG-002 / ASSESSED_PATH / approved 2026-09-11
```

The Framework distribution and this Project's authoritative `Project-Source/` remain distinct. Upstream/distribution movement after the pinned Framework-Source tree recorded above never silently auto-upgrades this initialized Project.
