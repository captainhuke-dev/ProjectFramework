# Project Location Bootstrap Preamble

Use this copyable Project/environment configuration **before active `FRAMEWORK-001` authority is resolved** when deterministic environment/location discovery locators are needed. This distribution artifact is outside the `00–99` Project Source semantic-slot namespace. It is **not** `FRAMEWORK-001`, Root Governance, a second Project Location Binding, or the Framework `1.7.0+` Project-root `PROJECT-BOOTSTRAP.md` discovery entrypoint.

## Project Settings Representation — Thin Bootstrap Adapter

Framework `1.12.1` current vendor-facing Project Settings / Project Instructions use exactly two bootstrap locators plus one rule:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <PROJECT_BOOTSTRAP_ABSOLUTE_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before the first Project-governed response in each chat.
Read-only, status, diagnostic, and failure-report responses are not exempt.
Before Material Project work, also apply all existing binding, authority, risk, and mutation gates.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

`ProjectFramework Upstream` maps to canonical `framework_source` read-through/upgrade discovery. `Project Bootstrap` is the verified absolute path to the consuming Project's root `PROJECT-BOOTSTRAP.md`; it is an environment-specific locator and not Project authority. The Project README managed block provides the portable relative fallback `./PROJECT-BOOTSTRAP.md`.

A ready-to-paste Project Bootstrap path MUST be verified. First-response bootstrap is discovery/governance loading only; it grants no mutation authority, and Material work keeps its additional gates. When unresolved, report `VERIFICATION_REQUIRED`; never fill it from recency, editor/MCP handles, mounts, search ranking, memory, or similarly named folders.

The detailed Git/Storage/MCP/Workspace concepts below remain the **internal/pre-authority discovery representation**. They are not removed merely because current vendor Project Settings are thinner.

## Canonical Bootstrap Representation

```yaml
framework_source:
  repository: "<FRAMEWORK_OWNER_REPOSITORY>"
  url: "<FRAMEWORK_CANONICAL_URL>"
  bootstrap_ref: "main"

remote_location:
  repository: "<REMOTE_DISCOVERY_OWNER_REPOSITORY_OR_UNKNOWN>"
  url: "<REMOTE_DISCOVERY_URL_OR_UNKNOWN>"
  project_source_path: "<OPTIONAL_PROJECT_SOURCE_DISCOVERY_PATH_OR_UNKNOWN>"

file_storage_locations:
  - storage_key: "<PROJECT_DEFINED_STORAGE_KEY>"
    storage_type: "<GOOGLE_DRIVE | S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER>"
    canonical_locator: "<PROVIDER_APPROPRIATE_STABLE_LOCATOR_OR_UNKNOWN>"
    content_scope: "<DECLARED_CONTENT_SCOPE>"

mcp_location:
  environment: "<EXECUTION_ENVIRONMENT>"
  path: "<MCP_TARGET_PATH_OR_UNKNOWN>"

local_workspace:
  environment: "<EXECUTION_ENVIRONMENT>"
  path: "<ABSOLUTE_LOCAL_PROJECT_PATH_OR_UNKNOWN>"

current_branch_worktree:
  state: "DYNAMIC"
  rule: "VERIFY_EACH_SESSION"
```

## `[Project Path]` Command

`[Project Path]` is a registered read/verify command over location semantics that already exist. Literal brackets are required for registered-command identity; matching inside brackets is case-insensitive. The command may carry an explicit path-change request, but it creates no new authority.

Current Framework `1.12.1` vendor settings do not require the legacy five labels. When legacy/Brownfield settings or internal bootstrap representations contain angle-bracket placeholders, those values remain **unset / not configured** and never authorize fallback.

On `[Project Path]` (case-insensitive inside brackets):

1. Read applicable current location semantics from the thin Project Settings adapter, root bootstrap/README fallback, internal Bootstrap Location representation, and active `FRAMEWORK-001` Project Location Binding as available.
2. Surface Framework/Git/Storage/MCP/Workspace semantics from their applicable canonical/discovery sources before Material work.
3. Verify available repository identity/remote, MCP target, local workspace, storage locator/reachability as applicable, and active `FRAMEWORK-001` Project Location Binding when present.
4. Report each comparison as `MATCH`, `MISMATCH`, or `NOT_VERIFIED`. These are diagnostic display labels, not Framework lifecycle, epistemic, binding, or authority states.
5. A Material mismatch fails closed for the affected mutation. Do not silently rewrite Project Settings, a repo reference, or `FRAMEWORK-001`.
6. If the user explicitly requests a path change, distinguish one-off action targeting from persistent configuration/binding change; persistent governed changes retain explicit approval plus applicable `FRAMEWORK-001` revision/validate/promote/history flow.

## Optional / Legacy Repo-Native Location Reference

For repo-native entry that does not begin in GPT/Claude Project Settings, the same configured values MAY be mirrored at:

```text
<repo-root>/PROJECT-CONFIG.md
```

`PROJECT-CONFIG.md` is an optional/legacy portable **location-reference** representation only. It is not the canonical Project-root discovery entrypoint introduced in Framework `1.7.0`; that role belongs to `<Project-Root>/PROJECT-BOOTSTRAP.md`. `PROJECT-CONFIG.md` is not a semantic slot, not Root Governance, and never overrides active `FRAMEWORK-001`. Do not store secrets in it. When Project Settings, `PROJECT-CONFIG.md`, root bootstrap, and active governance disagree materially, surface the mismatch rather than choosing by recency. After valid active `FRAMEWORK-001` resolves, its governed Project Location Binding remains authoritative.

## Semantics

- **Framework Source** is Framework upstream/read-through only. It does not define the consuming Project or auto-upgrade an initialized Project.
- **Remote Location** is the deterministic remote Project Source discovery start before authority resolves. It is not Repository Location Binding or branch/integration authority.
- **File Storage Location** is a bootstrap locator, not governed File Storage Binding. Omit the list when no external/non-repository storage is applicable; multiple entries are allowed for distinct content scopes.
- A `GOOGLE_DRIVE` bootstrap locator maps to the dedicated `project_location_binding.google_drive` authority after active `FRAMEWORK-001` resolves. Do not create duplicate generic Drive authority for the same target/content scope.
- **MCP Location** is execution-adapter routing. MCP workspace IDs, active/recent workspace lists, editor handles, and similar runtime identifiers are evidence only.
- **Local Workspace** is an environment-local locator. It remains distinct from governed Local Workspace Binding. Explicit verified mappings may allow different host/container/mount paths to refer to the same Project/source identity.
- **current branch/worktree** is volatile observed Git state. Never persist a concrete branch/worktree as Bootstrap authority; fresh-observe Git when material.
- Bootstrap locators may share the same physical value while retaining different semantic roles.
- Once a valid active local `FRAMEWORK-001` resolves, its Project Location Binding controls initialized-Project repository/Drive/file-storage/local-workspace routing. A material bootstrap/root contradiction is fail-closed for the affected mutation; neither side is silently rewritten.
- Location correctness does not grant `AUTH-*`, `DEL-*`, scope, Risk, branch/integration, implementation, or runtime authority.
- Actual credentials are forbidden. Do not place access keys, passwords, tokens, SAS tokens, secret-bearing signed URLs, or equivalent secret material here; use existing `SECRET-*` external-reference semantics where applicable.
