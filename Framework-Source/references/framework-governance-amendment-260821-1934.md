---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.2"
project_source_framework_version: "1.2.3"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-21T19:34:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_DEVELOPMENT_WORKSPACE_AND_RUNTIME_AUTHORITY"
---

# Framework Governance Amendment — Development Workspace & Runtime Authority Boundary

## Binding Change

Framework `1.2.3` adds **Development Workspace and Runtime Authority** governance while preserving Project Source Schema `1.0.0`, the existing semantic-slot namespace, existing Stable-ID families, Project-local Framework pinning, and Framework `1.2.2` Git Base Freshness / Forward-Port semantics.

The binding changes are:

1. When implementation exists and the distinction is material, a Project MUST be able to identify a **Canonical Implementation Source** for the affected scope: the durable declared source location whose verified state determines current `IMPLEMENTATION` Truth.
2. For Git-backed Projects, the Canonical Implementation Source is normally the verified Git/source tree governed by the Project's repository/workspace contract.
3. Canonical implementation durability is defined against the Project's declared development/recovery lifecycle. It does not require physical host-local storage. A host Git repository, Git worktree, remote/VM durable workspace, or Dev Container backed by durable source storage may all be valid when declared and verifiable.
4. Fresh runtime observation remains authoritative for `RUNTIME` Truth. Runtime execution or interactive editing does not silently transfer `IMPLEMENTATION` authority.
5. A runtime-only hotfix or edit MUST NOT be treated as canonical implementation completion until accepted intent is transferred through the governed change path into the Canonical Implementation Source and reverified.
6. When Canonical Implementation Source and Runtime should align but differ materially, existing `DRIFT-*` semantics apply. No parallel workspace/runtime drift Stable-ID family is created.
7. `40 Technical Design` may carry a **Development Workspace Contract** including Canonical Implementation Source, repository/source identity, workspace type/location/durability, Human/Agent edit location, execution environment, Source-to-Runtime Mapping, dependency isolation, Runtime Mutability Boundary, Persistent-State Boundary, and related verification/drift context.
8. Workspace and source-to-runtime labels are descriptive blueprint vocabulary only. They do not create new Project states, Epistemic Status values, or Stable-ID families.
9. `60 Deployment Plan` may carry Deployment Source/Artifact Acquisition, Source-to-Runtime Mapping, Runtime Mutability Expectation, Persistent-State Boundary, Data/Storage Authority, Replacement/Recreation Expectation, and material Development-vs-Production mapping differences.
10. State that applicable `REQ-*`, `DEC-*`, Technical Design, or Deployment contracts require to survive expected runtime replacement MUST have a declared persistent-state authority/mechanism compatible with that lifecycle. Rebuildable cache/temp/scratch/generated state MAY remain ephemeral when no survival requirement applies.
11. Disposable/recreatable runtime components MUST NOT become the sole authoritative implementation copy merely because code can execute or be edited there.
12. Docker, host-local source storage, immutable production images, and production source mounts remain Project-specific/applicability-driven. Framework does not universally require or prohibit them.
13. Durable Dev Container and remote development topologies remain valid when their source identity, durability, recovery, authority, and persistence contracts are explicit enough for the affected scope.
14. Framework `1.2.2` Git Base Freshness remains unchanged: `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, `STACKED_WORK`, and the Pre-Merge Base Freshness Gate retain their existing semantics. **Mergeable ≠ Acceptable.**
15. Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`; upstream Framework `1.2.3` does not auto-upgrade them. Adoption uses existing `MIG-*` assessment, approval, validation, promotion, and history-preservation rules.
16. Unknown workspace/source/runtime/persistence topology MUST remain explicit uncertainty until verified from actual Project source/runtime evidence; do not invent host paths, container mappings, storage authorities, or Git identity.

## Recommended Reference Pattern

For many AI-first software Projects, a useful non-mandatory pattern is:

```text
canonical Git/source authority
        ↓
primary durable workspace + optional Git worktrees
        ↓
Human / AI edits canonical durable source
        ↓
Docker / Dev Container / native runtime for execution and test
        ↓
versioned/identifiable production artifact when Project requirements call for it
```

A common development topology may use a durable Git repo/worktree bind-mounted into Docker. A Dev Container may itself expose the durable canonical workspace. A native non-Docker Project remains valid. The governing rule is durability and declared authority, not one physical storage/container arrangement.

## Scope Boundary

This amendment changes governance/workflow/blueprint semantics only. It does not authorize creation of application source code, Dockerfile, Compose/Kubernetes/Helm runtime artifacts, Dev Container configuration, installers, Git hooks, GitHub Actions, bots, validator/CLI, schedulers, merge queues, branch-protection automation, or runtime-enforcement services.

Concrete implementation/runtime artifacts remain a separate explicit scope.

## Compatibility

Framework `1.2.3` is backward compatible with Schema `1.0.0`. It adds no semantic slot, no Stable-ID namespace, and no new Project lifecycle/execution or Git-freshness state. Existing Projects continue under their approved local Framework pin until a governed migration explicitly upgrades them.