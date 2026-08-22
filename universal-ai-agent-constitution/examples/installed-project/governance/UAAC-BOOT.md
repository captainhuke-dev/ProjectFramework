---
document_type: UAAC_PROJECT_BOOTSTRAP
bootstrap_schema_version: '1.0'
status: EFFECTIVE
project_id: example-installed-project
authority_effect: NONE
truth_authority: NONE
governance_source:
  repository: example/installed-project
  canonical_ref_policy: main
  canonical_url: https://github.com/example/installed-project/blob/main/governance/UAAC-BOOT.md
  bootstrap_path: governance/UAAC-BOOT.md
  observed_identity: git:example-install-commit
adoption:
  locator: governance/CONSTITUTION-ADOPTION.yaml
project_law:
  locator: governance/PROJECT-LAWS/PROJECT_RULES.md
state_authority_map:
  locator: governance/STATE-AUTHORITY-MAP.yaml
project_document_registry:
  locator: governance/PROJECT-DOCUMENT-REGISTRY.yaml
project_capability_pack:
  locator: governance/PROJECT-CAPABILITY-PACK.yaml
continuation_index:
  locator: governance/CURRENT-CONTINUATION.yaml
skill_registry:
  locator: governance/SKILL-REGISTRY.yaml
claim_contract_registry:
  locator: governance/CLAIM-CONTRACT-REGISTRY.yaml
project_wiki:
  locator: governance/LLM-WIKI/index.md
installation_validation:
  locator: governance/INSTALLATION-VALIDATION.yaml
bootstrap_kernel:
  locator: governance/BOOTSTRAP-KERNEL.md
project_binding:
  locator: governance/PROJECT-BINDING.yaml
boot_receipt:
  locator: governance/BOOT-RECEIPT.yaml
agent_adapter_registry:
  locator: governance/AGENT-ADAPTER-REGISTRY.yaml
auto_boot:
  required_for: MATERIAL_TASKS
  procedure_id: UAAC-BOOT
  freshness_policy: IDENTITY_AND_TRIGGER_BASED
  skill_selection: AUTOMATIC_BY_APPLICABILITY
  user_restatement_required: false
---

# Example installed Project governance bootstrap

This is a router with no authority or truth effect. Follow the locators above, verify identities, then read the applicable lineage pointer before work.
