# Project Adapter Template

Declarative **owner/locator mapping** for one Project. The Project Adapter maps generic contracts to Project-specific owners and locators. It does **not** become those owners.

```text
Project Adapter
≠ Project Source
≠ Task Source
≠ Git
≠ GitHub
≠ Runtime Authority
≠ AUTH
```

```yaml
adapter_name: "<PROJECT_ID>"
adapter_state: "ACTIVE | DISABLED"
owner_mappings:
  - contract_field: "<generic contract field, e.g. task_source>"
    owner: "<Project-specific owner, e.g. docs/superpowers/PROJECT-TASKS.md>"
    locator: "<path or source-native pointer>"
  - contract_field: "project_source_root"
    owner: "Project-Source/"
    locator: "Project-Source/"
  - contract_field: "canonical_git"
    owner: "<canonical Git repository>"
    locator: "<repository URL or bound ref>"
locator_mappings:
  - concept: "<generic concept>"
    locator: "<Project-specific locator>"
```

Rules:

- The adapter **locates** owners and locators; it does **not** own or override them. The mapped owner remains the source of truth.
- The adapter is a translation/locator boundary. It is not Root Governance, `AUTH-*`, Project Source, Task Source, Git/GitHub truth, or Runtime authority.
- Unknown Brownfield mappings remain `UNKNOWN` rather than guessed.
- This file is a locator mapping. It is not a Stable-ID family and introduces no new Project Source semantic slot.
- No runtime, executable adapter, MCP router, or automatic mapper is implied by this file.

## Framework 1.20 Wave A V2 locator mappings (TASK-058)

When a Project uses Wave A V2 execution contracts, the adapter gains locator mappings for:

```yaml
locator_mappings:
  - concept: "operational_aggregate_owner"
    locator: "<declared execution-state owner for operational aggregate storage/versioning>"
  - concept: "ownership_owner"
    locator: "<declared execution-control owner that grants authoritative execution ownership>"
  - concept: "runtime_local_resource_ref"
    locator: "<scope declaration for runtime-local logical resource identities>"
  - concept: "source_native_result_owner"
    locator: "<source-native system that owns result truth for non-Git result kinds>"
```

Rules:

- The adapter still **locates** these owners; it does not become them. `Project Adapter ≠ owner` remains absolute.
- These mappings are translation metadata only; they grant no authority and create no Stable-ID family.
- Projects without a declared runtime leave these mappings absent or `UNKNOWN`; absence never implies a default owner.