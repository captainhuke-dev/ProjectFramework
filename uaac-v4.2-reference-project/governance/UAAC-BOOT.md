---
document_type: UAAC_PROJECT_BOOTSTRAP
bootstrap_schema_version: '1.0'
status: STAGED
project_id: uaac-v42-reference
authority_effect: NONE
truth_authority: NONE
project_boundary: uaac-v4.2-reference-project
governance_source:
  repository: captainhuke-dev/ProjectFramework
  canonical_ref_policy: hz-framework
  bootstrap_path: uaac-v4.2-reference-project/governance/UAAC-BOOT.md
bootstrap_kernel:
  locator: governance/BOOTSTRAP-KERNEL.md
project_binding:
  locator: governance/PROJECT-BINDING.yaml
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
agent_adapter_registry:
  locator: governance/AGENT-ADAPTER-REGISTRY.yaml
reference_validation:
  locator: governance/REFERENCE-VALIDATION.yaml
auto_boot:
  required_for: MATERIAL_TASKS
  procedure_id: UAAC-BOOT
  skill_selection: AUTOMATIC_BY_APPLICABILITY
  user_restatement_required: false
---

# UAAC v4.2 remote-backed reference Project

This file is the Project front door and router only. It has no independent
authority or truth effect. Resolve Project Binding first, then the pinned
Constitution, Project Law, documents, Skills, and current lineage.
