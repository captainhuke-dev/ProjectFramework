# Project Location Bootstrap Preamble

Use this copyable Project/environment configuration **before active `FRAMEWORK-001` authority is resolved** when deterministic discovery/routing locators are needed. This file is a distribution/bootstrap artifact outside the `00–99` Project Source semantic-slot namespace. It is **not** `FRAMEWORK-001`, Root Governance, or a second Project Location Binding.

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
