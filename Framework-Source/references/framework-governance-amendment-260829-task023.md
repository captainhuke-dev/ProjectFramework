---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.6.0"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_PROJECT_ROOT_SELF_BOOTSTRAP"
---

# Framework 1.7.0 Amendment — Self-Bootstrapping Project Contract

Framework `1.7.0` preserves `1.6.0` unless refined here. Project Source Schema stays `1.0.0`; release format stays `3`. This release adds one stable Project-root discovery artifact, `PROJECT-BOOTSTRAP.md`, for vendor-neutral entry into an initialized Project's authoritative Project Source.

## 1. Stable Project-root discovery entrypoint

For NEW Projects created under Framework `1.7.0+`, the Project root MUST contain:

```text
<Project-Root>/PROJECT-BOOTSTRAP.md
```

The filename is stable and MUST NOT use revision/date suffixes. The Framework distribution maintains the source template at `templates/PROJECT-BOOTSTRAP.md`.

`PROJECT-BOOTSTRAP.md` is a discovery/locator artifact outside the `00–99` Project Source semantic-slot namespace. It has no Stable ID and is never a second Project governance root.

## 2. Canonical discovery/read route

Once an Agent can access the Project root, the canonical vendor-neutral route is:

```text
PROJECT-BOOTSTRAP.md
→ Project-Source/00 / FRAMEWORK-001
→ Project-Source/01 / Project Source Index
→ Project-Source/03 / Current State
→ task-specific routing
→ Project-Source/09 / Handoff when continuation applies
```

The root bootstrap is read as a locator only. The referenced `00` becomes authoritative only after it is validated as the active `FRAMEWORK-001` for the Project. `01`, `03`, and `09` retain their existing canonical responsibilities; the root bootstrap does not duplicate their payloads.

## 3. Authority and location separation

Precedence is:

```text
PROJECT-BOOTSTRAP.md = discovery/locator
FRAMEWORK-001        = Project governance authority
01                   = current routing/index
03                   = current-state summary
09                   = continuation/handoff
vendor adapters      = optional discovery convenience
```

Bootstrap discovery remains distinct from Repository/File Storage/Local Workspace Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime authority, and `AUTH-*`/Risk authority. Correct discovery location grants none of those authorities.

A material bootstrap/root contradiction fails closed for affected mutation. Neither side is silently rewritten and ambiguity is never resolved from recency, search ranking, active workspace IDs, cached paths, or similarly named locations.

## 4. Bootstrap file content boundary

`PROJECT-BOOTSTRAP.md` MAY carry only bounded discovery information: the relative Project Source root, first-read route, continuation route, active-root precedence, failure behavior, no-secrets rule, and optional adapter guidance.

It MUST NOT own Project requirements, decisions, authority records, risks, relations, current status, handoff state, Project Location Binding, branch/worktree, integration/implementation/runtime authority, or secret values. Volatile Git/runtime state is fresh-observed from its canonical source when material.

## 5. GREENFIELD behavior

For NEW `1.7.0+` Projects, the resulting Project MUST include `PROJECT-BOOTSTRAP.md` at root. Existing governed creation remains Preview → approval → create active `00 / FRAMEWORK-001` → create the approved Project Source starter set → materialize the root bootstrap from the maintained template → verify that it resolves the created active Project Source.

The file is mandatory in the resulting Project but never replaces the rule that `00 / FRAMEWORK-001` is governance authority.

## 6. Brownfield adoption

Existing initialized Projects remain locally pinned and MUST NOT receive `PROJECT-BOOTSTRAP.md` automatically. Adoption occurs only through governed `[Project Upgrade]` / Direct-to-Latest cumulative target-state flow.

Upgrade preparation must preserve Project-specific rules, bindings, Stable IDs, history, and existing optional location references; Preview root-bootstrap creation; apply only with existing upgrade mutation authority; verify the new root locator resolves the existing active `FRAMEWORK-001`; and record material migration/evidence/change history through existing families.

A Project that has not adopted `1.7.0+` is not invalid merely because its root lacks `PROJECT-BOOTSTRAP.md`.

## 7. Bootstrap Location and `PROJECT-CONFIG.md`

Framework `1.2.6` Bootstrap Location semantics remain separate. `templates/project-location-bootstrap.md` continues to describe pre-authority environment/location locators.

Optional repo-native `PROJECT-CONFIG.md` remains an optional/legacy Bootstrap Location reference only. It is not promoted to canonical Project discovery, is not a semantic slot, and is not automatically deleted or rewritten.

When both exist, `PROJECT-BOOTSTRAP.md` owns root discovery routing; `PROJECT-CONFIG.md` may provide optional location values; valid active `FRAMEWORK-001` governs after resolution. Material contradiction is surfaced rather than resolved by recency.

## 8. Vendor adapters

ChatGPT Project Settings, Claude Project Settings, `AGENTS.md`, `CLAUDE.md`, and similar vendor/product instruction surfaces are optional thin discovery adapters once Project-root access exists. They MAY direct an Agent to `PROJECT-BOOTSTRAP.md` and canonical Framework sources but MUST NOT become Project authority.

Official platform launchers preserve shared-marker byte identity, the `<=4,500` Unicode-character ceiling, canonical commands/lifecycle/response-close tokens, and subordination to active `FRAMEWORK-001`. Legacy/pre-1.7 discovery compatibility remains available when the root file is absent because the Project has not adopted the new release.

## 9. Failure behavior

Read-only discovery MAY continue far enough to diagnose a problem, but affected Material mutation fails closed when:

- the root bootstrap points to a missing Project Source root;
- the referenced `00` is not a valid active `FRAMEWORK-001` for the Project;
- multiple root bootstrap locations claim canonical status;
- root bootstrap routing materially contradicts the active root binding;
- a Project known to have adopted `1.7.0+` lacks its mandatory root bootstrap without a governed exception/repair state;
- a vendor adapter or optional `PROJECT-CONFIG.md` materially conflicts with the resolved authoritative Project Source.

The Framework does not claim that an Agent without filesystem/repository access can discover a Project-root file.

## 10. Historical and schema compatibility

No semantic slot or Stable-ID family is added. `18–19` remain RESERVED; standard conditional `91` and `92` retain their existing meanings; Project Source Schema remains `1.0.0`.

Historical amendments remain provenance and are not rewritten. Framework `1.7.0` is a backward-compatible minor semantic expansion for new-Project discovery plus governed Brownfield adoption.

## 11. Non-goals

This amendment adds no filesystem watcher/daemon, automatic discovery service, MCP runtime/tool routing, code-generation engine, vendor plugin runtime, automatic Brownfield upgrade, secret store, automatic path/binding repair, CI/CD, deployment automation, or TASK-024+ implementation.
