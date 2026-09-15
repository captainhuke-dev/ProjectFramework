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
