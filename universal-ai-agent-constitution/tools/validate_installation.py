#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import json
import re
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator

SHARED_START = 'UAAC-SHARED-BOOT-CONTRACT:START'
SHARED_END = 'UAAC-SHARED-BOOT-CONTRACT:END'
REQUIRED_DOC_ROLES = {'PROJECT_DEFINITION', 'REQUIREMENTS', 'CURRENT_STATE'}
ALL_OUTCOMES = {'BOOT', 'REPORT', 'RECALL', 'CHECKPOINT', 'HANDOFF', 'DECISION', 'COMMUNICATION'}
TERMINAL = {'CLOSED', 'FAILED', 'CANCELLED', 'ABANDONED', 'SUPERSEDED'}
CONVERGENCE_KEYS = [
    'project_id',
    'constitution_identity',
    'project_law_identity',
    'state_authority_map_identity',
    'continuation_index_identity',
    'project_document_registry_identity',
    'skill_registry_identity',
    'adapter_registry_identity',
]


@dataclass
class Finding:
    code: str
    message: str
    path: str | None = None


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding='utf-8'))


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise ValueError('missing YAML frontmatter')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError('unterminated YAML frontmatter')
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


def extract_shared_block(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    start = text.find(SHARED_START)
    end = text.find(SHARED_END)
    if start < 0 or end < start:
        raise ValueError('shared boot markers missing')
    return text[start:end + len(SHARED_END)]


def validate_schema(instance_path: Path, schema_path: Path, findings: list[Finding]) -> None:
    try:
        instance = load_yaml(instance_path)
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    except Exception as exc:
        findings.append(Finding('SCHEMA_VALIDATION_FAIL', str(exc), str(instance_path)))
        return
    for error in errors:
        location = '.'.join(str(x) for x in error.path) or '<root>'
        findings.append(Finding('SCHEMA_VALIDATION_FAIL', f'{location}: {error.message}', str(instance_path)))


def find_placeholders(value: Any, prefix: str = '') -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            found.extend(find_placeholders(item, f'{prefix}.{key}' if prefix else str(key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(find_placeholders(item, f'{prefix}[{index}]'))
    elif isinstance(value, str) and re.fullmatch(r'<[^>]+>', value.strip()):
        found.append(prefix)
    return found




def resolve_project_locator(
    project: Path, locator: Any, findings: list[Finding], *, source: str, code: str = 'LOCATOR_OUTSIDE_PROJECT'
) -> Path | None:
    if not isinstance(locator, str) or not locator.strip():
        findings.append(Finding('REQUIRED_LOCATOR_MISSING', source))
        return None
    raw = Path(locator)
    if raw.is_absolute():
        findings.append(Finding(code, f'{source}: absolute locator is not allowed: {locator}'))
        return None
    candidate = (project / raw).resolve(strict=False)
    try:
        candidate.relative_to(project)
    except ValueError:
        findings.append(Finding(code, f'{source}: locator escapes Project boundary: {locator}'))
        return None
    return candidate

def required_outcomes(pack: dict[str, Any]) -> set[str]:
    profile = pack.get('profile', {})
    required = {'BOOT', 'REPORT'}
    if profile.get('multi_session') or profile.get('multi_agent'):
        required |= {'RECALL', 'CHECKPOINT', 'HANDOFF'}
    if profile.get('decision_support'):
        required.add('DECISION')
    if profile.get('human_facing_transformation'):
        required.add('COMMUNICATION')
    return required


def nested_project_roots(project: Path) -> set[Path]:
    roots: set[Path] = set()
    for binding in project.rglob('governance/PROJECT-BINDING.yaml'):
        root = binding.parent.parent.resolve()
        if root != project:
            roots.add(root)
    return roots


def is_under_nested_project(path: Path, nested_roots: set[Path]) -> bool:
    resolved = path.resolve()
    for root in nested_roots:
        try:
            resolved.relative_to(root)
            return True
        except ValueError:
            continue
    return False


def validate_installation(project: Path, package: Path | None = None) -> tuple[list[Finding], dict[str, Any]]:
    project = project.resolve()
    package = (package or Path(__file__).resolve().parents[1]).resolve()
    findings: list[Finding] = []
    try:
        project_locator = project.relative_to(package).as_posix()
    except ValueError:
        project_locator = str(project)
    summary: dict[str, Any] = {'project': project_locator}

    if not project.is_dir():
        return [Finding('PROJECT_NOT_FOUND', 'project directory does not exist', str(project))], summary

    nested_roots = nested_project_roots(project)
    boot_candidates: list[tuple[Path, dict[str, Any]]] = []
    for path in project.rglob('UAAC-BOOT.md'):
        if is_under_nested_project(path, nested_roots):
            continue
        try:
            fm, _ = parse_frontmatter(path)
            if fm.get('status') != 'ARCHIVED':
                boot_candidates.append((path, fm))
        except Exception as exc:
            findings.append(Finding('GOVERNANCE_BOOT_INVALID', str(exc), str(path)))

    expected_boot = project / 'governance' / 'UAAC-BOOT.md'
    if len(boot_candidates) != 1:
        findings.append(Finding('GOVERNANCE_BOOT_CONFLICT', f'expected one effective front door, found {len(boot_candidates)}', str(project)))
        if not boot_candidates:
            return findings, summary
    boot_path, boot = boot_candidates[0]
    if boot_path != expected_boot:
        findings.append(Finding('GOVERNANCE_BOOT_PATH_INVALID', 'effective front door must be governance/UAAC-BOOT.md', str(boot_path)))
    if boot.get('authority_effect') != 'NONE' or boot.get('truth_authority') != 'NONE':
        findings.append(Finding('GOVERNANCE_BOOT_AUTHORITY_INVALID', 'front door must have no authority/truth effect', str(boot_path)))
    if boot.get('project_id') is None:
        findings.append(Finding('PROJECT_ID_MISSING', 'front door project_id missing', str(boot_path)))

    locator_fields = {
        'bootstrap_kernel': 'governance/BOOTSTRAP-KERNEL.md',
        'project_binding': 'governance/PROJECT-BINDING.yaml',
        'boot_receipt': 'governance/BOOT-RECEIPT.yaml',
        'agent_adapter_registry': 'governance/AGENT-ADAPTER-REGISTRY.yaml',
        'adoption': 'governance/CONSTITUTION-ADOPTION.yaml',
        'project_law': 'governance/PROJECT-LAWS/PROJECT_RULES.md',
        'state_authority_map': 'governance/STATE-AUTHORITY-MAP.yaml',
        'project_document_registry': 'governance/PROJECT-DOCUMENT-REGISTRY.yaml',
        'project_capability_pack': 'governance/PROJECT-CAPABILITY-PACK.yaml',
        'continuation_index': 'governance/CURRENT-CONTINUATION.yaml',
        'skill_registry': 'governance/SKILL-REGISTRY.yaml',
        'claim_contract_registry': 'governance/CLAIM-CONTRACT-REGISTRY.yaml',
        'project_wiki': 'governance/LLM-WIKI/index.md',
        'installation_validation': 'governance/INSTALLATION-VALIDATION.yaml',
    }
    resolved: dict[str, Path] = {}
    for field, standard in locator_fields.items():
        value = boot.get(field, {})
        locator = value.get('locator') if isinstance(value, dict) else None
        if not locator:
            findings.append(Finding('REQUIRED_LOCATOR_MISSING', field, str(boot_path)))
            continue
        path = resolve_project_locator(project, locator, findings, source=f'front_door.{field}')
        if path is None:
            continue
        resolved[field] = path
        if not path.exists():
            findings.append(Finding('REQUIRED_LOCATOR_UNRESOLVED', locator, str(boot_path)))
        if field != 'project_wiki' and locator != standard:
            findings.append(Finding('STANDARD_LOCATOR_DRIFT', f'{field}: {locator} != {standard}', str(boot_path)))

    if len(resolved) != len(locator_fields) or any(not p.exists() for p in resolved.values()):
        return findings, summary

    binding = load_yaml(resolved['project_binding'])
    boot_receipt = load_yaml(resolved['boot_receipt'])
    adapters = load_yaml(resolved['agent_adapter_registry'])
    adoption = load_yaml(resolved['adoption'])
    state_map = load_yaml(resolved['state_authority_map'])
    docs = load_yaml(resolved['project_document_registry'])
    pack = load_yaml(resolved['project_capability_pack'])
    continuation = load_yaml(resolved['continuation_index'])
    skills = load_yaml(resolved['skill_registry'])
    claims = load_yaml(resolved['claim_contract_registry'])
    installation = load_yaml(resolved['installation_validation'])

    schema_pairs = [
        (resolved['project_binding'], package/'schemas/project-binding.schema.json'),
        (resolved['boot_receipt'], package/'schemas/boot-receipt.schema.json'),
        (resolved['agent_adapter_registry'], package/'schemas/agent-adapter-registry.schema.json'),
        (resolved['adoption'], package/'schemas/constitution-adoption.schema.json'),
        (resolved['state_authority_map'], package/'schemas/state-authority-map.schema.json'),
        (resolved['claim_contract_registry'], package/'schemas/claim-contract-registry.schema.json'),
        (resolved['project_document_registry'], package/'schemas/project-document-registry.schema.json'),
        (resolved['project_capability_pack'], package/'schemas/project-capability-pack.schema.json'),
        (resolved['continuation_index'], package/'schemas/current-continuation.schema.json'),
        (resolved['skill_registry'], package/'schemas/skill-registry.schema.json'),
        (resolved['installation_validation'], package/'schemas/installation-validation.schema.json'),
    ]
    for instance, schema in schema_pairs:
        validate_schema(instance, schema, findings)

    project_id = boot.get('project_id')
    id_sources = {
        'binding': binding.get('project_id'),
        'boot_receipt': boot_receipt.get('project_id'),
        'adapters': adapters.get('project_id'),
        'adoption': adoption.get('project', {}).get('id'),
        'state_map': state_map.get('project_id'),
        'documents': docs.get('project_id'),
        'capability_pack': pack.get('project_id'),
        'continuation': continuation.get('project_id'),
        'skills': skills.get('project_id'),
        'claims': claims.get('project_id'),
        'installation': installation.get('project_id'),
    }
    for source, value in id_sources.items():
        if value != project_id:
            findings.append(Finding('PROJECT_ID_MISMATCH', f'{source}={value!r}, expected {project_id!r}'))

    if adoption.get('constitution', {}).get('version') != '4.2.0':
        findings.append(Finding('CONSTITUTION_VERSION_MISMATCH', 'standard v4.2 installation example must pin 4.2.0', str(resolved['adoption'])))
    if adoption.get('governance_source', {}).get('bootstrap_path') != 'governance/UAAC-BOOT.md':
        findings.append(Finding('GOVERNANCE_SOURCE_INVALID', 'bootstrap_path mismatch', str(resolved['adoption'])))
    placeholder_sources = {
        'front_door': (boot, boot_path),
        'project_binding': (binding, resolved['project_binding']),
        'boot_receipt': (boot_receipt, resolved['boot_receipt']),
        'agent_adapter_registry': (adapters, resolved['agent_adapter_registry']),
        'adoption': (adoption, resolved['adoption']),
        'state_authority_map': (state_map, resolved['state_authority_map']),
        'project_document_registry': (docs, resolved['project_document_registry']),
        'project_capability_pack': (pack, resolved['project_capability_pack']),
        'continuation_index': (continuation, resolved['continuation_index']),
        'skill_registry': (skills, resolved['skill_registry']),
        'claim_contract_registry': (claims, resolved['claim_contract_registry']),
        'installation_validation': (installation, resolved['installation_validation']),
    }
    for source_name, (document, source_path) in placeholder_sources.items():
        for item in find_placeholders(document):
            findings.append(Finding('UNRESOLVED_PLACEHOLDER', f'{source_name}.{item}', str(source_path)))

    # Project binding and nested-boundary coherence.
    repository = adoption.get('governance_source', {}).get('repository')
    if binding.get('status') != 'VERIFIED':
        findings.append(Finding('PROJECT_BINDING_MISMATCH', f'binding status={binding.get("status")}', str(resolved['project_binding'])))
    if binding.get('project_root') not in ('.', ''):
        findings.append(Finding('PROJECT_BINDING_MISMATCH', f'validated Project root must bind to current root, got {binding.get("project_root")!r}', str(resolved['project_binding'])))
    if binding.get('canonical_repository') != repository:
        findings.append(Finding('PROJECT_BINDING_MISMATCH', f'canonical_repository={binding.get("canonical_repository")!r}, adoption={repository!r}', str(resolved['project_binding'])))
    if binding.get('canonical_ref_policy') != adoption.get('governance_source', {}).get('canonical_ref_policy'):
        findings.append(Finding('PROJECT_BINDING_MISMATCH', 'canonical ref policy differs from adoption', str(resolved['project_binding'])))
    if binding.get('governance_front_door') != 'governance/UAAC-BOOT.md':
        findings.append(Finding('PROJECT_BINDING_MISMATCH', 'governance front door mismatch', str(resolved['project_binding'])))
    if binding.get('nested_project_policy') not in ('EXCLUDE_DECLARED_NESTED_PROJECTS', 'NO_NESTED_PROJECTS'):
        findings.append(Finding('PROJECT_BINDING_MISMATCH', 'nested project policy missing/invalid', str(resolved['project_binding'])))

    # Project document roles and locators.
    document_entries = docs.get('documents', [])
    roles = [entry.get('role') for entry in document_entries]
    if len(roles) != len(set(roles)):
        findings.append(Finding('DUPLICATE_PROJECT_DOCUMENT_ROLE', 'duplicate semantic document role', str(resolved['project_document_registry'])))
    by_role = {entry.get('role'): entry for entry in document_entries}
    missing_roles = REQUIRED_DOC_ROLES - set(by_role)
    if missing_roles:
        findings.append(Finding('PROJECT_DOCUMENTS_UNRESOLVED', f'missing roles: {sorted(missing_roles)}', str(resolved['project_document_registry'])))
    for role in REQUIRED_DOC_ROLES & set(by_role):
        entry = by_role[role]
        if entry.get('status') != 'RESOLVED':
            findings.append(Finding('PROJECT_DOCUMENTS_UNRESOLVED', f'{role} status={entry.get("status")}', str(resolved['project_document_registry'])))
        locator = entry.get('locator')
        doc_path = resolve_project_locator(project, locator, findings, source=f'project_document.{role}') if locator else None
        if doc_path is not None and not doc_path.exists():
            findings.append(Finding('PROJECT_DOCUMENT_LOCATOR_UNRESOLVED', f'{role}: {locator}', str(resolved['project_document_registry'])))
    if docs.get('conflicts'):
        findings.append(Finding('PROJECT_DOCUMENT_CONFLICT', 'document registry contains unresolved conflicts', str(resolved['project_document_registry'])))

    # Capability Pack and active procedures.
    declared = set(pack.get('required_functional_outcomes', []))
    expected = required_outcomes(pack)
    if not expected <= declared:
        findings.append(Finding('CAPABILITY_PACK_INCOMPLETE', f'missing outcomes {sorted(expected-declared)}', str(resolved['project_capability_pack'])))
    if not declared <= ALL_OUTCOMES:
        findings.append(Finding('CAPABILITY_PACK_INVALID', f'unknown outcomes {sorted(declared-ALL_OUTCOMES)}', str(resolved['project_capability_pack'])))
    procedures = skills.get('procedures', [])
    pids = [p.get('procedure_id') for p in procedures]
    if len(pids) != len(set(pids)):
        findings.append(Finding('DUPLICATE_PROCEDURE_ID', 'duplicate procedure ID', str(resolved['skill_registry'])))
    active_functions = {p.get('function') for p in procedures if p.get('status') == 'ACTIVE'}
    if not declared <= active_functions:
        findings.append(Finding('PROCEDURE_MATERIALIZATION_REQUIRED', f'missing ACTIVE functions {sorted(declared-active_functions)}', str(resolved['skill_registry'])))
    for proc in procedures:
        if proc.get('authority_effect') != 'NONE' or proc.get('volatile_truth_embedded') is not False:
            findings.append(Finding('PROCEDURE_CONTRACT_INVALID', proc.get('procedure_id', '<unknown>'), str(resolved['skill_registry'])))
        entrypoint = proc.get('entrypoint')
        procedure_path = resolve_project_locator(project, entrypoint, findings, source=f'procedure.{proc.get("procedure_id")}') if entrypoint else None
        if procedure_path is not None and not procedure_path.exists():
            findings.append(Finding('PROCEDURE_ENTRYPOINT_UNRESOLVED', entrypoint, str(resolved['skill_registry'])))

    # Auto-Boot and platform adapter invocation evidence.
    auto_boot = pack.get('auto_boot', {})
    if (
        auto_boot.get('status') != 'ACTIVE'
        or auto_boot.get('trigger') != 'EVERY_MATERIAL_TASK'
        or auto_boot.get('procedure_id') != 'UAAC-BOOT'
        or auto_boot.get('automatic_skill_selection') is not True
        or auto_boot.get('user_restatement_required') is not False
        or auto_boot.get('freshness_policy') != 'IDENTITY_AND_TRIGGER_BASED'
    ):
        findings.append(Finding('AUTO_BOOT_UNVERIFIED', 'Capability Pack does not prove required Auto-Boot contract', str(resolved['project_capability_pack'])))
    boot_procs = [proc for proc in procedures if proc.get('function') == 'BOOT' and proc.get('status') == 'ACTIVE']
    if len(boot_procs) != 1 or 'material_task' not in set(boot_procs[0].get('triggers', [])):
        findings.append(Finding('AUTO_BOOT_UNVERIFIED', 'one ACTIVE BOOT procedure with material_task trigger is required', str(resolved['skill_registry'])))

    adapter_entries = adapters.get('adapters', [])
    adapter_ids = [entry.get('adapter_id') for entry in adapter_entries]
    if len(adapter_ids) != len(set(adapter_ids)):
        findings.append(Finding('DUPLICATE_AGENT_ADAPTER', 'duplicate adapter ID', str(resolved['agent_adapter_registry'])))
    intended_agents = {item.get('agent_id') for item in adoption.get('conformance', {}).get('agents', [])}
    verified_agents = {
        item.get('agent_id') for item in adapter_entries
        if item.get('status') == 'VERIFIED'
        and item.get('boot_procedure_id') == 'UAAC-BOOT'
        and item.get('invocation_trigger') == 'EVERY_MATERIAL_TASK'
        and item.get('invocation_evidence', {}).get('status') == 'PASS'
    }
    if not intended_agents <= verified_agents:
        findings.append(Finding('PLATFORM_ADAPTER_UNVERIFIED', f'missing VERIFIED invocation evidence for {sorted(intended_agents-verified_agents)}', str(resolved['agent_adapter_registry'])))

    # Boot freshness, visibility, and pre-write context.
    if boot_receipt.get('status') != 'PASS':
        findings.append(Finding('AUTO_BOOT_UNVERIFIED', f'boot receipt status={boot_receipt.get("status")}', str(resolved['boot_receipt'])))
    freshness = boot_receipt.get('freshness', {})
    if freshness.get('reused_prior_scope') and freshness.get('invalidated_by'):
        findings.append(Finding('BOOT_FRESHNESS_INVALID', f'reused scope despite invalidators {freshness.get("invalidated_by")}', str(resolved['boot_receipt'])))
    if boot_receipt.get('boot_mode') in ('DELTA', 'LIGHT') and not freshness.get('checked_identities'):
        findings.append(Finding('BOOT_FRESHNESS_INVALID', 'DELTA/LIGHT boot requires checked identities', str(resolved['boot_receipt'])))
    pre = boot_receipt.get('pre_write_check', {})
    mismatch_fields = []
    for field in ('governance_identity', 'project_law_identity', 'continuation_index_identity', 'artifact_base_identity'):
        if pre.get(f'expected_{field}') != pre.get(f'observed_{field}'):
            mismatch_fields.append(field)
    if pre.get('required') and (pre.get('status') != 'PASS' or mismatch_fields):
        findings.append(Finding('TASK_CONTEXT_STALE', f'pre-write mismatch/status: {mismatch_fields or pre.get("status")}', str(resolved['boot_receipt'])))
    if boot_receipt.get('continuation_index_identity') != continuation.get('index_id') or boot_receipt.get('continuation_index_epoch') != continuation.get('index_epoch'):
        findings.append(Finding('TASK_CONTEXT_STALE', 'boot receipt continuation observation differs from canonical index', str(resolved['boot_receipt'])))
    visibility = boot_receipt.get('visibility', {})
    if pack.get('profile', {}).get('multi_agent') and (visibility.get('receiver_visible') is not True or visibility.get('local_state') != 'CANONICAL_VISIBLE'):
        findings.append(Finding('CANONICAL_SURFACE_NOT_VISIBLE', 'multi-agent current state is not receiver-visible', str(resolved['boot_receipt'])))

    # Continuation index and lineage pointers.
    lineages = continuation.get('lineages', [])
    lineage_ids = [x.get('lineage_id') for x in lineages]
    if len(lineage_ids) != len(set(lineage_ids)):
        findings.append(Finding('DUPLICATE_LINEAGE_ID', 'duplicate lineage in continuation index', str(resolved['continuation_index'])))
        findings.append(Finding('CONTINUATION_CONFLICT', 'duplicate lineage in continuation index', str(resolved['continuation_index'])))
    focus = continuation.get('current_focus_lineage_id')
    if focus is not None and focus not in lineage_ids:
        findings.append(Finding('CONTINUATION_FOCUS_INVALID', f'unknown focus lineage {focus}', str(resolved['continuation_index'])))
    terminal_seen = False
    for entry in lineages:
        pointer_locator = str(entry.get('pointer_locator', ''))
        pointer_path = resolve_project_locator(project, pointer_locator, findings, source=f'continuation.{entry.get("lineage_id")}')
        if pointer_path is None:
            continue
        if not pointer_path.exists():
            findings.append(Finding('CONTINUATION_POINTER_UNRESOLVED', pointer_locator, str(resolved['continuation_index'])))
            continue
        validate_schema(pointer_path, package/'schemas/continuation-pointer.schema.json', findings)
        pointer = load_yaml(pointer_path)
        for item in find_placeholders(pointer):
            findings.append(Finding('UNRESOLVED_PLACEHOLDER', f'continuation_pointer.{item}', str(pointer_path)))
        if pointer.get('project_id') != project_id or pointer.get('lineage_id') != entry.get('lineage_id'):
            findings.append(Finding('CONTINUATION_POINTER_MISMATCH', str(pointer_path)))
        if pointer.get('pointer_id') != entry.get('pointer_identity') or pointer.get('status') != entry.get('status'):
            findings.append(Finding('CONTINUATION_POINTER_MISMATCH', f'identity/status mismatch for {entry.get("lineage_id")}', str(pointer_path)))
        if entry.get('status') in TERMINAL:
            terminal_seen = True
            if pointer.get('exact_next_action') in (None, ''):
                findings.append(Finding('TERMINAL_CONTINUATION_INCOMPLETE', 'terminal pointer lacks exact_next_action', str(pointer_path)))
    if not terminal_seen:
        summary['terminal_lineage_retention'] = 'NOT_DEMONSTRATED'
    else:
        summary['terminal_lineage_retention'] = 'PASS'

    # Shared boot contract across installed wrappers.
    wrapper_paths = [project/'AGENTS.md', project/'governance/platform/CHATGPT-PROJECT-INSTRUCTIONS.md']
    existing_wrappers = [p for p in wrapper_paths if p.exists()]
    if pack.get('profile', {}).get('multi_agent') and len(existing_wrappers) < 2:
        findings.append(Finding('AGENT_ENTRYPOINTS_INCOMPLETE', 'multi-agent profile requires at least two installed wrappers'))
    try:
        blocks = [extract_shared_block(p) for p in existing_wrappers]
        if blocks and any(block != blocks[0] for block in blocks[1:]):
            findings.append(Finding('BOOT_CONTRACT_DRIFT', 'installed Agent wrappers differ'))
        canonical_block = extract_shared_block(package/'templates/platform/AGENTS.md')
        if blocks and blocks[0] != canonical_block:
            findings.append(Finding('BOOT_CONTRACT_DRIFT', 'installed shared contract differs from package template'))
    except Exception as exc:
        findings.append(Finding('BOOT_CONTRACT_DRIFT', str(exc)))

    # Claim contracts and installation/effective status.
    tokens = {c.get('token'): c for c in claims.get('contracts', [])}
    for required_token in ['INSTALLATION_VALIDATED', 'EFFECTIVE', 'BOOTSTRAP_CONVERGENCE_FAILED', 'PROJECT_BINDING_MATCH', 'TASK_CONTEXT_CURRENT', 'CANONICAL_SURFACE_VISIBLE', 'PLATFORM_ADAPTER_INVOKED', 'AUTO_BOOT_VALID', 'BASE_FRESHNESS_MATCH', 'ATOMIC_PUBLICATION_VERIFIED']:
        if required_token not in tokens:
            findings.append(Finding('CLAIM_CONTRACT_MISSING', required_token, str(resolved['claim_contract_registry'])))

    validated_claim = installation.get('status') == 'INSTALLATION_VALIDATED'
    required_static_checks = {
        'ONE_EFFECTIVE_FRONT_DOOR',
        'REQUIRED_LOCATORS_RESOLVE',
        'PROJECT_DOCUMENTS_RESOLVED',
        'CAPABILITY_PACK_RESOLVED',
        'CONTINUATION_VALID',
        'PROJECT_BINDING_VALID',
        'NESTED_BOUNDARY_VALID',
        'AUTO_BOOT_CONFIGURED',
        'PLATFORM_ADAPTERS_VERIFIED',
        'RECEIVER_CANONICAL_ACCESS',
        'PRE_WRITE_CONTEXT_VALID',
        'BASE_FRESHNESS_VALID',
        'ATOMIC_PUBLICATION_VALID',
    }
    static_checks = {item.get('check'): item.get('status') for item in installation.get('static_checks', [])}
    if validated_claim:
        missing_or_failed = sorted(name for name in required_static_checks if static_checks.get(name) != 'PASS')
        if missing_or_failed:
            findings.append(Finding('INSTALLATION_CLAIM_UNSUBSTANTIATED', f'static checks not PASS: {missing_or_failed}', str(resolved['installation_validation'])))
        if installation.get('cross_agent_convergence', {}).get('status') != 'PASS':
            findings.append(Finding('BOOTSTRAP_CONVERGENCE_FAILED', 'positive installation requires convergence status PASS', str(resolved['installation_validation'])))
        required_scenarios = {'S-INSTALL-01', 'S-INSTALL-02', 'S-INSTALL-13', 'S-INSTALL-14', 'S-INSTALL-15', 'S-INSTALL-16', 'S-INSTALL-17', 'S-INSTALL-18', 'S-INSTALL-19', 'S-INSTALL-20', 'S-INSTALL-21', 'S-INSTALL-22', 'S-INSTALL-23'}
        declared_scenarios = set(installation.get('behavioral_scenarios', []))
        if not required_scenarios <= declared_scenarios:
            findings.append(Finding('INSTALLATION_CLAIM_UNSUBSTANTIATED', f'missing required installation scenarios {sorted(required_scenarios-declared_scenarios)}', str(resolved['installation_validation'])))

    resolutions = installation.get('cross_agent_convergence', {}).get('resolutions', [])
    if pack.get('profile', {}).get('multi_agent') and len(resolutions) < 2:
        findings.append(Finding('BOOTSTRAP_CONVERGENCE_FAILED', 'multi-agent installation has fewer than two resolution receipts'))
    if resolutions:
        for resolution in resolutions:
            access = resolution.get('canonical_access', {})
            if access.get('status') != 'PASS' or not access.get('locator') or not access.get('observed_identity'):
                findings.append(Finding('CANONICAL_SURFACE_NOT_VISIBLE', f'{resolution.get("agent_id")} cannot prove canonical access', str(resolved['installation_validation'])))
        baseline = {key: resolutions[0].get(key) for key in CONVERGENCE_KEYS}
        for resolution in resolutions[1:]:
            current = {key: resolution.get(key) for key in CONVERGENCE_KEYS}
            if current != baseline:
                findings.append(Finding('BOOTSTRAP_CONVERGENCE_FAILED', f'{resolution.get("agent_id")} differs from baseline', str(resolved['installation_validation'])))
        expected_identity = {
            'project_id': project_id,
            'constitution_identity': adoption.get('constitution', {}).get('pinned_reference'),
            'state_authority_map_identity': state_map.get('map_id'),
            'continuation_index_identity': continuation.get('index_id'),
            'project_document_registry_identity': docs.get('registry_id'),
            'skill_registry_identity': skills.get('registry_id'),
            'adapter_registry_identity': adapters.get('registry_id'),
        }
        for key, value in expected_identity.items():
            if baseline.get(key) != value:
                findings.append(Finding('BOOTSTRAP_CONVERGENCE_FAILED', f'{key}: {baseline.get(key)!r} != {value!r}', str(resolved['installation_validation'])))

    effective_claim = adoption.get('installation', {}).get('lifecycle_state') == 'EFFECTIVE'
    if validated_claim and findings:
        findings.append(Finding('INSTALLATION_CLAIM_UNSUBSTANTIATED', 'positive installation status present while checks fail', str(resolved['installation_validation'])))
    if effective_claim:
        effective = installation.get('effective_adoption', {})
        expected_authority = adoption.get('installation', {}).get('effective_authority_ref')
        if (
            not validated_claim
            or effective.get('status') != 'EFFECTIVE'
            or not expected_authority
            or effective.get('authority_ref') != expected_authority
        ):
            findings.append(Finding('EFFECTIVE_CLAIM_UNSUBSTANTIATED', 'effective adoption lacks matching validated installation/authority receipt', str(resolved['adoption'])))

    summary.update({
        'project_id': project_id,
        'front_door_count': len(boot_candidates),
        'nested_project_count': len(nested_roots),
        'document_roles': len(document_entries),
        'required_outcomes': sorted(declared),
        'lineage_count': len(lineages),
        'agent_resolution_count': len(resolutions),
        'finding_count': len(findings),
    })
    return findings, summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', required=True, type=Path)
    parser.add_argument('--package', type=Path)
    args = parser.parse_args()
    findings, summary = validate_installation(args.project, args.package)
    for finding in findings:
        suffix = f' [{finding.path}]' if finding.path else ''
        print(f'{finding.code}: {finding.message}{suffix}')
    if findings:
        print(f'INSTALLATION_VALIDATION_FAIL findings={len(findings)}')
        return 1
    print(f'INSTALLATION_VALIDATION_PASS project={summary.get("project_id")} lineages={summary.get("lineage_count")} agents={summary.get("agent_resolution_count")}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
