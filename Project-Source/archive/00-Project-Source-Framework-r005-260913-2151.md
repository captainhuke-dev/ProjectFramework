---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "FRAMEWORK-001"
document_type: "PROJECT_SOURCE_FRAMEWORK"
semantic_slot: "00"
revision: 5
document_status: "ACTIVE"
supersedes: "00-Project-Source-Framework-r004-260912-2344.md"
framework_root: true
inherits_from: []
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T21:51:48.631+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.18.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Root Governance / Non-Removable Framework:** this document is the Project-local governance root. `FRAMEWORK-001` remains the stable identity in semantic slot `00`; it cannot be removed, bypassed, demoted, or replaced by a descendant rule. Every Project Source descendant inherits from this root. Root mutation requires User Explicit Approval and revision → validate → promote → supersede/archive history preservation.

## 1. Framework 1.18 Pin and Incorporated Normative Source

This canonical ProjectFramework self-host is reconciled to **ProjectFramework 1.18.0 / Project Source Schema 1.0.0** under `MIG-004` and the ACTOR-001 explicit `[Goal]` on 2026-09-13. This is canonical-upstream post-merge self-host reconciliation after PR #32, not an ordinary consuming-Project `[Project Upgrade]`.

The incorporated Framework 1.18 semantics are bound to the exact canonical merge below. PR #32 merged to canonical `main` at `f6330e9929c28977d43fc149b864d590df1c2816` and preserved the independently verified Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c`; TASK-051 and TASK-052 are the release lineage layered on the TASK-049 canonical self-hosting contract. These source files do **not** become a second Project authority: their pinned text is incorporated by this `FRAMEWORK-001`; this root remains Project governance authority.

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  canonical_branch: "main"
  canonical_merged_release_commit: "f6330e9929c28977d43fc149b864d590df1c2816"
  self_host_reconciliation_source_ref: "task055-pr32-self-host-reconcile"
  reconciliation_task: "TASK-055"
  incorporated_framework_source_tree: "929065ccac7e3ecf25fda09de5326bb40c4f8f9c"
  framework_version: "1.18.0"
  schema_version: "1.0.0"
  release_format_version: 3
  captured_at: "2026-09-13T21:51:48.631+07:00"
  provenance_status: "VERIFIED_CANONICAL_MERGE"
```

Pinned Framework 1.18 source set incorporated here:

- `Framework-Source/FRAMEWORK-RELEASE.yaml` — blob `0b708d834e92cd05bf38fa743f0e17f7a2724855`
- `Framework-Source/SKILL.md` — blob `cd21fa74d0bb19502164aaa68c7dba10d9e4e89c`
- `Framework-Source/references/framework-governance-amendment-260913-task052-project-upgrade-one-session-fast-path.md` — blob `786d951f1c17066ec1b79d47063a6b17f65537bf`
- `Framework-Source/references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md` — blob `4a1a734056a3a6b2b82ff646029e388a58390bbf`
- `Framework-Source/references/core-governance-rules.md` — blob `d1973d048ab6d379b0bc8b4ff11c449f6ff80e45`
- `Framework-Source/templates/00-project-source-framework.md` — blob `da4949406d60e8c8fac5cdc5c9570b6081d0b05a`
- `Framework-Source/templates/core-document-skeletons.md` — blob `a3ad5a551b9f65637e30174b37f4542a9eabdff8`

Normative precedence inside the incorporated Framework set is: current approved amendment → Core Governance → operational SKILL/template guidance. This `FRAMEWORK-001` owns Project-specific identity, binding, pin, and specializations and never delegates Project authority merely because a distribution file is readable. If the exact incorporated Framework source cannot be resolved when a rule omitted here is material, affected mutation fails closed; do not reconstruct missing semantics from memory or silently substitute another revision.

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
- This `MIG-004` self-host reconciliation **does not change any Project Location Binding value**; the binding above is preservation of the predecessor root truth.

## 5. Project Graph Applicability

```yaml
project_graph:
  applicability: "VERIFICATION_REQUIRED"
  relation_document_slot: "92"
  external_index:
    owner_scope: "AI_CONTROLTOWER"
    authority: "DERIVED_ONLY"
```

`92` is conditional and is not materialized by this reconciliation. No Project relation, OpenViking configuration, graph runtime, or cross-Project write authority is inferred.

## 6. Project Source Namespace and Canonical Homes

Project Source root:

```text
<Project-Root>/Project-Source/
```

Mandatory core: `00–05`, `09–17`; conditional: `06–08`, `40`, `60`, `91`, `92`; `18–19` reserved. `91` remains active because current and historical `OUT-*` outcome truth is materially applicable. This reconciliation does not materialize `06–08`, `40`, `60`, or `92`.

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

`MIG-002` remains the historical `ASSESSED_PATH` 1.7.0 → 1.15.0 Project upgrade described in active `16`. `MIG-004` is the current canonical self-host post-merge reconciliation and is not an ordinary consuming-Project `[Project Upgrade]`. Preservation, rollback, evidence, history, verification, and promotion gates are not skipped.

Material Git-backed Task completion requires affected verification plus observed completion commit; WIP ≠ DONE. Logical Checkpoint ≠ RELEASE_FULL. Integration/publication re-resolves Base Freshness/evidence validity. Mergeable ≠ Acceptable.

Material connector work persists at Logical Checkpoints to its source-native durable owner; transient reads need not persist. Required persistence failure is `PERSISTENCE_PENDING` and must retain a concrete recovery action.

## 10. Registered Commands and Current Framework 1.18 Response Semantics

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

Framework 1.18 mandatory visible response close in the pinned Framework semantics is:

```text
### ทำอะไรไป?

<concise result>

### และถัดไปคืออะไร?

[Next Action]: <one exact action or ไม่มีขั้นตอนถัดไป>

[Next Goal]: <one bounded copy-ready Goal suggestion or ไม่มี>

[Reason]: <concise reason>
```

Nothing follows `[Reason]` under the pinned Framework 1.18 contract. `[Next Goal]` is presentation-only and never creates authority. `[Chat]` and `[Required Read]` remain valid internal Handoff/continuation semantics but are not mandatory visible Framework 1.18 close fields.

## 11. Optional Framework 1.10–1.14 Surfaces

The cumulative 1.18 pin supports, without automatically materializing:

- optional `Project-Knowledge/` advisory/provenance layer;
- optional `Project-Execution/` tool/capability/trust profiles;
- optional derived/rebuildable `Project-Change-Feed/`;
- conditional `92 / REL-*` Project Graph and relation reconciliation;
- advisory impact analysis and notification governance;
- `[Project Audit]` plus separately authorized remediation workflow.

Optionality remains applicability-driven. Absence is valid. This self-host reconciliation creates no watcher, crawler, daemon, scheduler, notification sender, graph sync, model/tool router, validator/CLI, CI/CD, application runtime, or auto-repair engine.

## 12. Project-Specific Rules

No `PSR-*` is materialized at this revision. Add a Project-Specific Rule only through a governed future `FRAMEWORK-001` revision with required approval; it may specialize but never weaken pinned Framework 1.18 semantics.

## 13. ProjectFramework Instantiation Record

```text
Project ID: PROJECTFRAMEWORK
Project Name: ProjectFramework
Project UUID: 00575e76-17ce-4dd3-ad24-377494a4a45b
Repository: captainhuke-dev/ProjectFramework
Project Source Root: Project-Source/
Framework Distribution Root: Framework-Source/
Project Source Framework Pin: 1.18.0
Project Source Schema: 1.0.0
Google Drive: NOT_APPLICABLE
External File Storage: NOT_APPLICABLE
Application Runtime: NOT_APPLICABLE — ProjectFramework is documentation/governance first and contains no application runtime merely by virtue of this Project Source
Self-Host Reconciliation: MIG-004 / CANONICAL_SELF_HOST_POST_MERGE_RECONCILIATION / authorized 2026-09-13
```

The Framework distribution and this Project's authoritative `Project-Source/` remain distinct. Upstream/distribution movement after the pinned Framework-Source tree recorded above never silently auto-upgrades ordinary consuming Projects; canonical ProjectFramework self-host convergence follows the separately governed post-merge reconciliation contract.
