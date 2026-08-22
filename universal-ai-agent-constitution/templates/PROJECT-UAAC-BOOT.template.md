---
document_type: UAAC_PROJECT_BOOTSTRAP
bootstrap_schema_version: '1.0'
status: STAGED
project_id: <project-id>
authority_effect: NONE
truth_authority: NONE
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
governance_source:
  repository: <owner/repository-or-canonical-locator>
  canonical_ref_policy: <branch/tag/ref-policy>
  canonical_url: <canonical-UAAC-BOOT-url>
  bootstrap_path: governance/UAAC-BOOT.md
  observed_identity: <commit/hash/revision>
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
---

# Project governance bootstrap

This file is the standard Project front door. It routes to governing and canonical sources. It is not Constitution, Project Law, authority, or Current Truth.

## Required read order

1. Run the Minimal Bootstrap Kernel; resolve Project Binding, Project boundary, and canonical governance identity before Skill discovery.
2. Read `governance/CONSTITUTION-ADOPTION.yaml`.
3. Read the pinned local Constitution and applicable laws.
4. Read Project Law and applicable constraints.
5. Read State Authority Map.
6. Resolve Project Document Registry and current Project sources.
7. Resolve Agent Adapter Registry, Project Capability Pack, and engaged procedures from Skill Registry; file presence is not invocation proof.
8. Resolve Project Continuation Index and the applicable lineage pointer.
9. Follow Project LLM Wiki only for routing to canonical sources.

Do not substitute conversation, memory, retrieval, Skill text, local branch assumptions, or this router for Current Truth.

If a required source cannot be resolved or local/canonical governance differs unexpectedly, report the applicable state and stop affected governed work:

```text
GOVERNANCE_BOOTSTRAP_UNAVAILABLE
GOVERNANCE_BOOT_CONFLICT
GOVERNANCE_DRIFT
```

## Boot freshness and write safety

Use `FULL` on new session, changed binding/governance/Project Law/requirements/authority, handoff, publish/deploy, or unresolved uncertainty. `DELTA`/`LIGHT` may reuse only identities proven unchanged. Before material write, recheck the attempt preconditions; mismatch produces `TASK_CONTEXT_STALE`.

Cross-Agent continuation requires a receiver-visible canonical surface. Local-only work must remain `LOCAL_ONLY` or `PENDING_CANONICAL_PUBLICATION` until remote readback.
