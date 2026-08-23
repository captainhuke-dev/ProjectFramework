---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.5"
project_source_framework_version: "1.2.6"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_APPROVAL_REVISION_2"
compatibility: "BACKWARD_COMPATIBLE_BOOTSTRAP_LOCATION_AND_FILE_STORAGE_GOVERNANCE"
---

# Framework 1.2.6 — Bootstrap Location and File Storage Governance Amendment

Framework `1.2.6` preserves Framework `1.2.1–1.2.5` semantics unless explicitly refined here. Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`; upstream movement does not auto-upgrade them. Project Source Schema remains `1.0.0`; this amendment adds no semantic slot, Stable-ID family, Project lifecycle state, Git freshness state, branch-authority field, Epistemic Status value, or executable enforcement scope.

## Bootstrap Location Semantics

Project-specific bootstrap/execution configuration may declare six distinct concepts:

```text
Framework Source
Remote Location
File Storage Location
MCP Location
Local Workspace
current branch/worktree
```

They remain distinct from one another and from governed Project Location Binding, Canonical Integration Target, Canonical Implementation Source, and Runtime Location.

- **Framework Source** is Framework upstream/read-through only. It does not identify or override an initialized consuming Project merely because values coincide.
- **Remote Location** is the deterministic remote Project Source discovery starting point before active governance resolves. It defines no branch authority. Explicit discovery indirection may legitimately differ from the final governed repository; a direct identity contradiction that would route Material work elsewhere is a material mismatch.
- **File Storage Location** is a bootstrap locator for zero-or-more durable non-repository Project file/object scopes. It is not itself governed File Storage Binding.
- **MCP Location** is an environment-scoped execution-adapter locator. MCP workspace IDs, editor handles, active/recent workspace state, and similar runtime identifiers are evidence only.
- **Local Workspace** is an environment-specific local Project-root locator compatible with the governed Local Workspace Binding. Different host/container path syntax is valid when an explicit mapping and source identity establish the same Project.
- **current branch/worktree** is volatile observed Git execution state. Persist only dynamic intent such as `DYNAMIC / VERIFY_EACH_SESSION`; fresh-observe current branch/ref, HEAD, worktree, and status whenever Material Git execution state matters.

When a valid active local `FRAMEWORK-001` is resolved, its Project Location Binding is the initialized-Project routing authority. Bootstrap locators become non-authoritative discovery/routing evidence. A bootstrap/root mismatch that would route Material work to an incompatible Project target blocks the affected mutation and is surfaced; neither side is silently rewritten. A persistent location change requires explicit approval and coordinated governed propagation. A one-off exact target remains action-specific.

Location correctness never grants mutation authority. Existing `AUTH-*`, `DEL-*`, approval, scope, Risk, Requirements/Decisions, integration, implementation, runtime, persistence, and verification gates remain independently binding.

## Governed File Storage Binding

For initialized Framework `1.2.6` Projects, non-Google-Drive external Project file/object routing is governed under active `FRAMEWORK-001` Project Location Binding as purpose/content-scoped File Storage Binding.

File Storage Binding reuses exactly:

```text
binding_state: BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED
verification_status: VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED
```

`BOUND` requires a provider-appropriate durable identity and may pair only with `VERIFIED` or `USER_CONFIRMED`; it MUST NOT pair with `verification_status: VERIFICATION_REQUIRED`. Known-applicable but unresolved storage is `VERIFICATION_REQUIRED` and is fail-closed for Material mutation while read/search/discovery needed to resolve it may proceed. A Project with no external/non-repository storage may omit generic storage entries; do not synthesize provider `NOT_APPLICABLE` entries merely to fill a template. Missing or unresolved storage never authorizes fallback to a recent, search-ranked, similarly named, mounted, synced, or otherwise accessible target.

Generic non-Drive provider vocabulary may include:

```text
S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER
```

Use provider-appropriate durable identity rather than display-name similarity or environment-specific mount letters where a stable identity exists. Multiple storage bindings are allowed for distinct governed content scopes. One governed content scope has one declared authoritative owner at a time; backup, mirror, replica, cache, mount, or synced copy does not transfer current authority by existence or recency.

Framework `1.2.6` preserves `project_location_binding.google_drive` as the canonical Root Governance representation for Google Drive Project-root/content routing. A bootstrap `GOOGLE_DRIVE` File Storage Location maps to that dedicated Drive binding. Generic File Storage MUST NOT duplicate the same Google Drive target/content scope. Normalizing Drive into the generic model is outside Framework `1.2.6` and would require separately governed migration with history preservation.

Mounted/synced/cached paths are routing or mapping evidence only and do not become Local Workspace, Canonical Implementation Source, Runtime/Data/Persistent-State, backup, deployment, or other authority merely because they are accessible. The same physical storage target may participate in multiple roles only when each role is separately declared and governed.

Actual storage credentials are prohibited in Bootstrap Location or Project Location metadata. Access keys, passwords, tokens, secret-bearing signed URLs, and comparable secret material remain external; use existing `SECRET-*` reference semantics when credential routing must be recorded.

## Compatibility and Adoption

Existing initialized Projects do not automatically gain Framework `1.2.6` storage semantics. Adoption uses the existing governed migration/assessment/approval/validation/promotion/history-preservation flow and MUST NOT invent provider applicability, storage identity, or placeholder bindings from accessibility alone.

This amendment authorizes governance/documentation/bootstrap semantics only. It does not authorize automatic discovery, storage synchronization, workspace selection, validators, hooks, bots, CI/CD, schedulers, watchers, credential stores, branch switching, or runtime enforcement.
