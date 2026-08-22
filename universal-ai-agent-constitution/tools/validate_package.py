#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib
import json
import re
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator

VERSION = '4.2.0'
EXPECTED_LAWS = [f'CONST-{i:03d}' for i in range(1, 26)]
VENDOR_TERMS = ['OpenViking', 'Humanizer', 'GitHub', 'ChatGPT', 'Codex', 'Claude', 'n8n']
SHARED_START = 'UAAC-SHARED-BOOT-CONTRACT:START'
SHARED_END = 'UAAC-SHARED-BOOT-CONTRACT:END'
EPHEMERAL_PATH_PARTS = {'.pytest_cache', '__pycache__', '.mypy_cache', '.ruff_cache', '.git'}


def is_release_artifact(relative_path: str) -> bool:
    path = Path(relative_path)
    if any(part in EPHEMERAL_PATH_PARTS for part in path.parts):
        return False
    if relative_path.endswith(('.pyc', '.pyo', '~')):
        return False
    return True


@dataclass
class Finding:
    code: str
    message: str
    path: str | None = None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding='utf-8'))


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith('---\n'):
        raise ValueError('missing YAML frontmatter')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError('unterminated YAML frontmatter')
    fm = yaml.safe_load(text[4:end]) or {}
    return fm, text[end + 5:]


def parse_law(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding='utf-8')
    fm, rest = parse_frontmatter(text)
    lid = fm.get('law_id')
    title_match = re.search(rf'^# {re.escape(str(lid))} — (.+)$', rest, re.M)
    if not title_match:
        raise ValueError('missing or mismatched law heading')
    marker_re = re.compile(
        rf'<!-- END_OF_LAW: {re.escape(str(lid))} version=([0-9.]+) '
        rf'sha256=([0-9a-f]{{64}}) nonce=([0-9a-f]{{12}}) -->\s*$'
    )
    marker = marker_re.search(rest)
    if not marker:
        raise ValueError('missing or malformed END_OF_LAW marker')
    body_start = title_match.end()
    body_raw = rest[body_start:marker.start()]
    body = body_raw.lstrip('\n').rstrip('\n') + '\n'
    return {
        'frontmatter': fm,
        'title': title_match.group(1).strip(),
        'body': body,
        'body_sha256': sha256_bytes(body.encode('utf-8')),
        'body_bytes': len(body.encode('utf-8')),
        'marker_version': marker.group(1),
        'marker_sha256': marker.group(2),
        'marker_nonce': marker.group(3),
        'file_sha256': sha256_bytes(text.encode('utf-8')),
        'text': text,
    }


def extract_shared_block(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    start = text.find(SHARED_START)
    end = text.find(SHARED_END)
    if start < 0 or end < 0 or end < start:
        raise ValueError('shared boot markers missing')
    end += len(SHARED_END)
    return text[start:end]


def scenario_ids_and_declared_count(path: Path) -> tuple[list[str], int | None]:
    index_text = path.read_text(encoding='utf-8')
    parts = sorted((path.parent / 'scenarios').glob('*.md'))
    combined = '\n\n'.join(part.read_text(encoding='utf-8') for part in parts)
    ids = re.findall(r'^## (S-[A-Z0-9-]+)\b', combined, re.M)
    m = re.search(r'^scenario_count:\s*(\d+)\s*$', index_text, re.M)
    return ids, int(m.group(1)) if m else None


def validate_json(instance_path: Path, schema_path: Path, findings: list[Finding]) -> None:
    try:
        instance = load_yaml(instance_path)
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    except Exception as exc:
        findings.append(Finding('SCHEMA_VALIDATION_FAIL', f'{instance_path.name}: {exc}', str(instance_path)))
        return
    for error in errors:
        loc = '.'.join(str(x) for x in error.path) or '<root>'
        findings.append(Finding('SCHEMA_VALIDATION_FAIL', f'{instance_path.name}:{loc}: {error.message}', str(instance_path)))


def extract_normative_requirements(law_id: str, body: str) -> list[dict[str, str]]:
    # Paragraph-level extraction is deliberately conservative. It does not claim
    # semantic atomization; it guarantees every normative paragraph is visible.
    chunks = re.split(r'\n\s*\n', body)
    results: list[dict[str, str]] = []
    n = 0
    for chunk in chunks:
        clean = ' '.join(line.strip() for line in chunk.splitlines() if line.strip() and not line.strip().startswith('```'))
        if re.search(r'\bMUST(?:\s+NOT)?\b', clean):
            n += 1
            results.append({'requirement_id': f'{law_id}-M{n:03d}', 'requirement': clean})
    return results


def generate_coverage(package: Path, manifest: dict[str, Any]) -> tuple[Path, Path, int]:
    laws: list[dict[str, Any]] = []
    total = 0
    for rec in manifest['laws']:
        law = parse_law(package / rec['path'])
        requirements = extract_normative_requirements(rec['law_id'], law['body'])
        total += len(requirements)
        laws.append({
            'law_id': rec['law_id'],
            'requirement_count': len(requirements),
            'scenario_ids': rec.get('tests', []),
            'audit_id': f'AUDIT-{rec["law_id"]}',
            'execution_status': 'SPECIFIED_NOT_EXECUTED',
        })
    data = {
        'schema_version': '2.0',
        'constitution_id': 'UAAC-001',
        'constitution_version': VERSION,
        'generated': True,
        'detail_generation': 'DERIVED_AT_VALIDATION_TIME',
        'requirement_count': total,
        'laws': laws,
    }
    ypath = package / 'registers' / 'must-coverage-index.yaml'
    ypath.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding='utf-8')
    lines = [
        f'# MUST Coverage Summary — UAAC v{VERSION}', '',
        f'Generated normative paragraphs: **{total}**', '',
        'Detailed requirement text is derived from canonical law files by `tools/validate_package.py` during validation; it is not duplicated in this release.', '',
        '| Law | MUST paragraphs | Conformance scenarios | Audit | Status |',
        '|---|---:|---|---|---|',
    ]
    for item in laws:
        scenarios = ', '.join(item['scenario_ids']) or '—'
        lines.append(f"| `{item['law_id']}` | {item['requirement_count']} | {scenarios} | `{item['audit_id']}` | `SPECIFIED_NOT_EXECUTED` |")
    lines += ['', f'<!-- END_OF_DOCUMENT: MUST Coverage Summary v{VERSION} -->', '']
    mpath = package / 'registers' / 'must-coverage-index.md'
    mpath.write_text('\n'.join(lines), encoding='utf-8')
    return ypath, mpath, total


def validate_package(package: Path, *, include_release_hashes: bool = True) -> tuple[list[Finding], dict[str, Any]]:
    findings: list[Finding] = []
    summary: dict[str, Any] = {}

    manifest_path = package / 'LAW-MANIFEST.yaml'
    try:
        manifest = load_yaml(manifest_path)
    except Exception as exc:
        return [Finding('PACKAGE_DRIFT', f'cannot load manifest: {exc}', str(manifest_path))], summary

    if manifest.get('constitution_version') != VERSION:
        findings.append(Finding('VERSION_MISMATCH', 'manifest version mismatch', str(manifest_path)))

    records = manifest.get('laws', [])
    ids = [r.get('law_id') for r in records]
    if ids != EXPECTED_LAWS:
        findings.append(Finding('LAW_ID_MISMATCH', f'expected {EXPECTED_LAWS}, got {ids}', str(manifest_path)))

    parsed_laws: dict[str, dict[str, Any]] = {}
    for rec in records:
        path = package / rec.get('path', '')
        try:
            law = parse_law(path)
            parsed_laws[rec['law_id']] = law
        except Exception as exc:
            findings.append(Finding('PACKAGE_DRIFT', f'{rec.get("law_id")}: {exc}', str(path)))
            continue
        fm = law['frontmatter']
        checks = {
            'title': law['title'] == rec.get('title'),
            'version': fm.get('version') == VERSION and law['marker_version'] == VERSION,
            'derogation': fm.get('derogation') == rec.get('derogation'),
            'applies_when': fm.get('applies_when') == rec.get('applies_when'),
            'min_conformance': fm.get('min_conformance') == rec.get('min_conformance'),
            'body_bytes': law['body_bytes'] == rec.get('body_bytes'),
            'body_sha256': law['body_sha256'] == rec.get('body_sha256') == law['marker_sha256'],
            'file_sha256': law['file_sha256'] == rec.get('file_sha256'),
            'nonce': law['marker_nonce'] == rec.get('nonce') == law['body_sha256'][:12],
        }
        for name, ok in checks.items():
            if not ok:
                findings.append(Finding('PACKAGE_DRIFT', f'{rec["law_id"]} {name} mismatch', str(path)))
        for term in VENDOR_TERMS:
            if term.lower() in law['body'].lower():
                findings.append(Finding('VENDOR_TERM_IN_LAW', f'{rec["law_id"]} contains {term}', str(path)))

    # Constitution entrypoint must route to, not duplicate, canonical modular laws.
    deprecated_entries = [x for x in package.glob('UAAC-v*-CONSTITUTION.md') if x.name != 'UAAC-v4.2-CONSTITUTION.md']
    for deprecated_entry in deprecated_entries:
        findings.append(Finding('DEPRECATED_RELEASE_ARTIFACT', f'stale Constitution entrypoint remains in v4.2 package: {deprecated_entry.name}', str(deprecated_entry)))
    entrypoint_path = package / 'UAAC-v4.2-CONSTITUTION.md'
    if entrypoint_path.exists():
        entrypoint = entrypoint_path.read_text(encoding='utf-8')
        positions = []
        for rec in records:
            link = rec['path']
            pos = entrypoint.find(link)
            if pos < 0:
                findings.append(Finding('PACKAGE_DRIFT', f'Constitution entrypoint missing route to {rec["law_id"]}', str(entrypoint_path)))
            positions.append(pos)
            law_text = (package / rec['path']).read_text(encoding='utf-8').strip()
            if law_text in entrypoint:
                findings.append(Finding('DUPLICATED_CANONICAL_LAW', f'entrypoint duplicates exact {rec["law_id"]}', str(entrypoint_path)))
        if any(a >= b for a, b in zip(positions, positions[1:]) if a >= 0 and b >= 0):
            findings.append(Finding('PACKAGE_DRIFT', 'Constitution entrypoint law order differs from manifest', str(entrypoint_path)))
    else:
        findings.append(Finding('PACKAGE_DRIFT', 'Constitution entrypoint missing', str(entrypoint_path)))

    # Reading budgets.
    by_id = {r['law_id']: r for r in records}
    for profile_name, profile in manifest.get('reading_profiles', {}).items():
        profile_ids = profile.get('unconditional', [])
        actual = sum(by_id[i]['body_bytes'] for i in profile_ids if i in by_id)
        if actual != profile.get('unconditional_bytes') or len(profile_ids) != profile.get('unconditional_count'):
            findings.append(Finding('PACKAGE_DRIFT', f'{profile_name} reading budget mismatch', str(manifest_path)))
    full = sum(r.get('body_bytes', 0) for r in records)
    if full != manifest.get('size_budget', {}).get('full_law_text_bytes'):
        findings.append(Finding('PACKAGE_DRIFT', 'full law size budget mismatch', str(manifest_path)))

    # Scenarios and references.
    scenario_path = package / 'tests' / 'conformance-scenarios.md'
    scenario_ids, declared_count = scenario_ids_and_declared_count(scenario_path)
    if len(scenario_ids) != len(set(scenario_ids)):
        findings.append(Finding('DUPLICATE_SCENARIO_ID', 'scenario IDs are not unique', str(scenario_path)))
    if declared_count != len(scenario_ids):
        findings.append(Finding('SCENARIO_COUNT_MISMATCH', f'declared {declared_count}, actual {len(scenario_ids)}', str(scenario_path)))
    scenario_set = set(scenario_ids)
    for rec in records:
        missing = [x for x in rec.get('tests', []) if x not in scenario_set]
        if missing:
            findings.append(Finding('MISSING_SCENARIO_REFERENCE', f'{rec["law_id"]}: {missing}', str(manifest_path)))

    # Coverage policy must match the manifest test mapping.
    coverage_policy_path = package / 'registers' / 'coverage-policy.yaml'
    try:
        coverage_policy = load_yaml(coverage_policy_path) or {}
        if coverage_policy.get('constitution_version') != VERSION:
            findings.append(Finding('COVERAGE_POLICY_DRIFT', 'coverage policy version mismatch', str(coverage_policy_path)))
        methods = coverage_policy.get('default_methods_by_law', {})
        for rec in records:
            declared = methods.get(rec['law_id'], {}).get('scenarios', [])
            if declared != rec.get('tests', []):
                findings.append(Finding('COVERAGE_POLICY_DRIFT', f'{rec["law_id"]} scenario mapping differs from manifest', str(coverage_policy_path)))
    except Exception as exc:
        findings.append(Finding('COVERAGE_POLICY_DRIFT', str(exc), str(coverage_policy_path)))

    # Compact MUST coverage summary must match requirements derived from canonical laws.
    coverage_summary_path = package / 'registers' / 'must-coverage-index.yaml'
    try:
        coverage_summary = load_yaml(coverage_summary_path) or {}
        if 'requirements' in coverage_summary:
            findings.append(Finding('COVERAGE_SUMMARY_NOT_COMPACT', 'detailed requirements must be derived at validation time', str(coverage_summary_path)))
        summary_by_law = {item.get('law_id'): item for item in coverage_summary.get('laws', [])}
        derived_total = 0
        for rec in records:
            count = len(extract_normative_requirements(rec['law_id'], parsed_laws[rec['law_id']]['body']))
            derived_total += count
            item = summary_by_law.get(rec['law_id'], {})
            if item.get('requirement_count') != count or item.get('scenario_ids') != rec.get('tests', []):
                findings.append(Finding('COVERAGE_SUMMARY_DRIFT', rec['law_id'], str(coverage_summary_path)))
        if coverage_summary.get('requirement_count') != derived_total or len(summary_by_law) != len(records):
            findings.append(Finding('COVERAGE_SUMMARY_DRIFT', 'coverage totals/law count mismatch', str(coverage_summary_path)))
    except Exception as exc:
        findings.append(Finding('COVERAGE_SUMMARY_DRIFT', str(exc), str(coverage_summary_path)))

    # Installation templates must start from fail-safe, non-positive states.
    try:
        capability_template = load_yaml(package/'templates/PROJECT-CAPABILITY-PACK.template.yaml')
        if capability_template.get('status') != 'BLOCKED':
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Capability Pack template must default to BLOCKED', 'templates/PROJECT-CAPABILITY-PACK.template.yaml'))

        skill_template = load_yaml(package/'templates/SKILL-REGISTRY.template.yaml')
        if any(item.get('status') != 'BLOCKED' for item in skill_template.get('procedures', [])):
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Skill Registry template procedures must default to BLOCKED', 'templates/SKILL-REGISTRY.template.yaml'))

        document_template = load_yaml(package/'templates/PROJECT-DOCUMENT-REGISTRY.template.yaml')
        if any(item.get('status') != 'BLOCKED' for item in document_template.get('documents', [])):
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Project Document Registry template entries must default to BLOCKED', 'templates/PROJECT-DOCUMENT-REGISTRY.template.yaml'))

        installation_template = load_yaml(package/'templates/INSTALLATION-VALIDATION.template.yaml')
        if installation_template.get('status') != 'INSTALLATION_UNVERIFIED':
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Installation Validation template must default to INSTALLATION_UNVERIFIED', 'templates/INSTALLATION-VALIDATION.template.yaml'))
        if any(item.get('status') != 'NOT_RUN' for item in installation_template.get('static_checks', [])):
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Installation static checks must default to NOT_RUN', 'templates/INSTALLATION-VALIDATION.template.yaml'))
        convergence = installation_template.get('cross_agent_convergence', {})
        if convergence.get('status') != 'NOT_RUN' or convergence.get('resolutions') not in ([], None):
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Cross-agent convergence must default to NOT_RUN with no receipts', 'templates/INSTALLATION-VALIDATION.template.yaml'))

        continuation_template = load_yaml(package/'templates/CURRENT-CONTINUATION.template.yaml')
        if any(item.get('status') != 'QUEUED' for item in continuation_template.get('lineages', [])):
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Continuation index template lineages must default to QUEUED', 'templates/CURRENT-CONTINUATION.template.yaml'))

        pointer_template = load_yaml(package/'templates/CONTINUATION-POINTER.template.yaml')
        if pointer_template.get('status') != 'QUEUED':
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Continuation pointer template must default to QUEUED', 'templates/CONTINUATION-POINTER.template.yaml'))

        boot_fm, _ = parse_frontmatter((package/'templates/PROJECT-UAAC-BOOT.template.md').read_text(encoding='utf-8'))
        if boot_fm.get('status') != 'STAGED':
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Project UAAC front door template must default to STAGED', 'templates/PROJECT-UAAC-BOOT.template.md'))
    except Exception as exc:
        findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', str(exc), 'templates'))

    # Shared boot contract exact bytes.
    platform_files = [
        package/'templates/platform/CHATGPT-PROJECT-INSTRUCTIONS.md',
        package/'templates/platform/AGENTS.md',
        package/'templates/platform/GENERIC-AGENT-INSTRUCTIONS.md',
    ]
    try:
        blocks = [extract_shared_block(p) for p in platform_files]
        if not all(b == blocks[0] for b in blocks[1:]):
            findings.append(Finding('BOOT_CONTRACT_DRIFT', 'shared boot blocks differ', 'templates/platform'))
    except Exception as exc:
        findings.append(Finding('BOOT_CONTRACT_DRIFT', str(exc), 'templates/platform'))

    # Reference Skill package metadata and function coverage.
    skill_paths = [package/'SKILL.md', *sorted((package/'skills').glob('*/SKILL.md'))]
    skill_functions = []
    for skill_path in skill_paths:
        try:
            skill_fm, _ = parse_frontmatter(skill_path.read_text(encoding='utf-8'))
            metadata = skill_fm.get('metadata', {})
            if metadata.get('constitution_id') != 'UAAC-001' or str(metadata.get('constitution_version')) != VERSION:
                findings.append(Finding('SKILL_PACKAGE_DRIFT', 'Skill Constitution identity/version mismatch', str(skill_path)))
            if metadata.get('authority_effect') != 'NONE':
                findings.append(Finding('SKILL_PACKAGE_DRIFT', 'Skill authority_effect must be NONE', str(skill_path)))
            if metadata.get('function'):
                skill_functions.append(metadata.get('function'))
        except Exception as exc:
            findings.append(Finding('SKILL_PACKAGE_DRIFT', str(exc), str(skill_path)))
    required_skill_functions = {'BOOT', 'REPORT', 'RECALL', 'CHECKPOINT', 'HANDOFF', 'DECISION', 'COMMUNICATION'}
    if set(skill_functions) != required_skill_functions or len(skill_functions) != len(required_skill_functions):
        findings.append(Finding('SKILL_PACKAGE_DRIFT', f'reference Skill function set invalid: {skill_functions}', 'skills'))

    # Schema validation of reference fixtures.
    schema_pairs = [
        ('examples/installed-project/governance/CONSTITUTION-ADOPTION.yaml', 'schemas/constitution-adoption.schema.json'),
        ('examples/installed-project/governance/PROJECT-BINDING.yaml', 'schemas/project-binding.schema.json'),
        ('examples/installed-project/governance/BOOT-RECEIPT.yaml', 'schemas/boot-receipt.schema.json'),
        ('examples/installed-project/governance/AGENT-ADAPTER-REGISTRY.yaml', 'schemas/agent-adapter-registry.schema.json'),
        ('examples/installed-project/governance/STATE-AUTHORITY-MAP.yaml', 'schemas/state-authority-map.schema.json'),
        ('examples/installed-project/governance/CLAIM-CONTRACT-REGISTRY.yaml', 'schemas/claim-contract-registry.schema.json'),
        ('examples/installed-project/governance/PROJECT-DOCUMENT-REGISTRY.yaml', 'schemas/project-document-registry.schema.json'),
        ('examples/installed-project/governance/PROJECT-CAPABILITY-PACK.yaml', 'schemas/project-capability-pack.schema.json'),
        ('examples/installed-project/governance/CURRENT-CONTINUATION.yaml', 'schemas/current-continuation.schema.json'),
        ('examples/installed-project/governance/SKILL-REGISTRY.yaml', 'schemas/skill-registry.schema.json'),
        ('examples/installed-project/governance/INSTALLATION-VALIDATION.yaml', 'schemas/installation-validation.schema.json'),
        ('examples/installed-project/governance/continuation/LINEAGE-ACTIVE/CURRENT.yaml', 'schemas/continuation-pointer.schema.json'),
        ('examples/installed-project/governance/continuation/LINEAGE-CLOSED/CURRENT.yaml', 'schemas/continuation-pointer.schema.json'),
        ('examples/chatgpt-codex-openviking/CONTEXT-BINDING.yaml', 'schemas/context-binding.schema.json'),
    ]
    for instance, schema in schema_pairs:
        validate_json(package/instance, package/schema, findings)

    # Claim tokens unique and safe fallbacks non-empty.
    try:
        claim_data = load_yaml(package/'examples/installed-project/governance/CLAIM-CONTRACT-REGISTRY.yaml')
        tokens = [c.get('token') for c in claim_data.get('contracts', [])]
        if len(tokens) != len(set(tokens)):
            findings.append(Finding('DUPLICATE_CLAIM_TOKEN', 'claim tokens are not unique', 'examples/installed-project/governance/CLAIM-CONTRACT-REGISTRY.yaml'))
        for c in claim_data.get('contracts', []):
            if not c.get('safe_fallback'):
                findings.append(Finding('CLAIM_CONTRACT_INVALID', f'{c.get("token")} missing safe fallback'))
    except Exception as exc:
        findings.append(Finding('CLAIM_CONTRACT_INVALID', str(exc)))

    # State map invariants beyond schema.
    try:
        state_map = load_yaml(package/'examples/installed-project/governance/STATE-AUTHORITY-MAP.yaml')
        for cls, val in state_map.get('state_classes', {}).items():
            if not isinstance(val.get('canonical'), dict):
                findings.append(Finding('STATE_AUTHORITY_INVALID', f'{cls} missing canonical authority'))
    except Exception as exc:
        findings.append(Finding('STATE_AUTHORITY_INVALID', str(exc)))

    # Standard installation profile artifacts and installed-project fixture.
    required_paths = [
        'INSTALL-UAAC.md',
        'HUMAN-INSTALL-WALKTHROUGH-TH.md',
        'ADOPTION-RUNBOOK.md',
        'INSTALLATION-THREAT-MODEL.md',
        'PUBLICATION-CONTRACT.yaml',
        'templates/BOOTSTRAP-KERNEL.md',
        'templates/PROJECT-UAAC-BOOT.template.md',
        'templates/PROJECT-GOVERNANCE-README.template.md',
        'templates/PROJECT-CAPABILITY-PACK.template.yaml',
        'templates/PROJECT-DOCUMENT-REGISTRY.template.yaml',
        'templates/PROJECT-BINDING.template.yaml',
        'templates/BOOT-RECEIPT.template.yaml',
        'templates/AGENT-ADAPTER-REGISTRY.template.yaml',
        'templates/CONTINUATION-POINTER.template.yaml',
        'templates/INSTALLATION-VALIDATION.template.yaml',
        'schemas/project-binding.schema.json',
        'schemas/boot-receipt.schema.json',
        'schemas/agent-adapter-registry.schema.json',
        'tools/validate_installation.py',
        'tools/build_package.py',
        'V4.0-TO-V4.1-TRACEABILITY.md',
        'V4.1-TO-V4.2-TRACEABILITY.md',
        'reviews/UAAC-PRECOMMIT-SYSTEMS-REVIEW-2026-08-21.md',
    ]
    for rel in required_paths:
        if not (package/rel).exists():
            findings.append(Finding('INSTALLATION_PROFILE_MISSING', rel, rel))

    # Human tutorial is explanatory only and must never become an Agent execution dependency.
    human_path = package/'HUMAN-INSTALL-WALKTHROUGH-TH.md'
    try:
        human_fm, human_body = parse_frontmatter(human_path.read_text(encoding='utf-8'))
        expected_human = {
            'document_type': 'UAAC_HUMAN_INSTALL_WALKTHROUGH',
            'audience': 'HUMAN',
            'normative': False,
            'authority_effect': 'NONE',
            'truth_authority': 'NONE',
            'agent_execution': 'DO_NOT_EXECUTE',
            'canonical_agent_install_protocol': 'INSTALL-UAAC.md',
            'example_values_are_current_truth': False,
        }
        if human_fm != expected_human or 'FOR HUMAN READING ONLY' not in human_body:
            findings.append(Finding('HUMAN_GUIDE_CLASSIFICATION_INVALID', 'Human walkthrough classification is incomplete or unsafe', str(human_path)))
    except Exception as exc:
        findings.append(Finding('HUMAN_GUIDE_CLASSIFICATION_INVALID', str(exc), str(human_path)))
    execution_paths = [
        package/'INSTALL-UAAC.md', package/'templates/BOOTSTRAP-KERNEL.md',
        package/'templates/AGENTS-UAAC-BOOTSTRAP.md', package/'templates/CHATGPT-PROJECT-INSTRUCTIONS-SHORT.md',
        package/'skills/uaac-boot/SKILL.md',
    ]
    for execution_path in execution_paths:
        if execution_path.exists() and 'HUMAN-INSTALL-WALKTHROUGH-TH.md' in execution_path.read_text(encoding='utf-8'):
            findings.append(Finding('HUMAN_GUIDE_EXECUTION_DEPENDENCY', 'Human walkthrough appears in Agent execution graph', str(execution_path)))

    # Minimal Kernel must precede Skill discovery and remain an authority/truth-free route.
    try:
        kernel_text = (package/'templates/BOOTSTRAP-KERNEL.md').read_text(encoding='utf-8')
        for required in ['UAAC-BOOTSTRAP-KERNEL:START', 'resolve Project binding', 'governance/UAAC-BOOT.md', 'before Skill Registry', 'BOOTSTRAP KERNEL != SKILL']:
            if required not in kernel_text:
                findings.append(Finding('BOOTSTRAP_KERNEL_INVALID', f'missing {required}', 'templates/BOOTSTRAP-KERNEL.md'))
    except Exception as exc:
        findings.append(Finding('BOOTSTRAP_KERNEL_INVALID', str(exc), 'templates/BOOTSTRAP-KERNEL.md'))

    # New templates must also start fail-safe.
    try:
        binding_template = load_yaml(package/'templates/PROJECT-BINDING.template.yaml')
        boot_receipt_template = load_yaml(package/'templates/BOOT-RECEIPT.template.yaml')
        adapter_template = load_yaml(package/'templates/AGENT-ADAPTER-REGISTRY.template.yaml')
        if binding_template.get('status') != 'BLOCKED':
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Project Binding template must default to BLOCKED', 'templates/PROJECT-BINDING.template.yaml'))
        if boot_receipt_template.get('status') != 'NOT_RUN' or boot_receipt_template.get('pre_write_check', {}).get('status') != 'NOT_RUN':
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Boot Receipt template must default to NOT_RUN', 'templates/BOOT-RECEIPT.template.yaml'))
        if any(x.get('status') != 'BLOCKED' or x.get('invocation_evidence', {}).get('status') != 'NOT_RUN' for x in adapter_template.get('adapters', [])):
            findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', 'Agent Adapter template must default to BLOCKED/NOT_RUN', 'templates/AGENT-ADAPTER-REGISTRY.template.yaml'))
    except Exception as exc:
        findings.append(Finding('UNSAFE_TEMPLATE_DEFAULT', str(exc), 'templates'))

    # Publication contract and final package must reject effective-ref staging artifacts.
    try:
        publication = load_yaml(package/'PUBLICATION-CONTRACT.yaml')
        expected_publication = {
            'strategy': 'ATOMIC_TREE_REPLACEMENT',
            'staging_on_effective_branch': False,
            'base_freshness_recheck': 'REQUIRED_BEFORE_REF_UPDATE',
            'expected_old_ref_guard': 'REQUIRED',
        }
        for key, value in expected_publication.items():
            if publication.get(key) != value:
                findings.append(Finding('PUBLICATION_CONTRACT_INVALID', f'{key} mismatch', 'PUBLICATION-CONTRACT.yaml'))
    except Exception as exc:
        findings.append(Finding('PUBLICATION_CONTRACT_INVALID', str(exc), 'PUBLICATION-CONTRACT.yaml'))
    forbidden_parts = {'.uaac-upload', '.uaac-staging', '__do_not_create__', '__uaac-local-file-probe.txt'}
    for artifact in package.rglob('*'):
        if any(part in forbidden_parts for part in artifact.parts):
            findings.append(Finding('TEMPORARY_RELEASE_ARTIFACT', 'temporary publication artifact present', str(artifact)))

    try:
        from validate_installation import validate_installation
        install_findings, install_summary = validate_installation(package/'examples/installed-project', package)
        for item in install_findings:
            findings.append(Finding('INSTALLATION_FIXTURE_INVALID', f'{item.code}: {item.message}', item.path))
        summary['installation_fixture'] = install_summary
    except Exception as exc:
        findings.append(Finding('INSTALLATION_FIXTURE_INVALID', str(exc), 'examples/installed-project'))

    # Release artifacts must not be symlinks into another boundary.
    for artifact in package.rglob('*'):
        if artifact.is_symlink():
            findings.append(Finding('PACKAGE_SYMLINK_FORBIDDEN', 'release package contains a symlink', str(artifact)))

    # Release hashes when a finalized release exists.
    release_path = package/'CONSTITUTION-RELEASE.yaml'
    if include_release_hashes and release_path.exists():
        release = load_yaml(release_path) or {}
        if release.get('status') == 'STABLE_CORE_READY_FOR_PROJECT_INSTALLATION_AND_ADOPTION':
            if release.get('version') != VERSION:
                findings.append(Finding('VERSION_MISMATCH', 'release receipt version mismatch', str(release_path)))
            listed = {item['path'] for item in release.get('files', [])}
            excluded = {'CONSTITUTION-RELEASE.yaml', 'validation/STRUCTURAL-VALIDATION.json'}
            actual = {
                path.relative_to(package).as_posix()
                for path in package.rglob('*')
                if path.is_file()
                and path.relative_to(package).as_posix() not in excluded
                and is_release_artifact(path.relative_to(package).as_posix())
            }
            if listed != actual:
                missing = sorted(listed - actual)
                extra = sorted(actual - listed)
                findings.append(Finding('RELEASE_FILESET_MISMATCH', f'missing={missing} extra={extra}', str(release_path)))
            for item in release.get('files', []):
                fpath = package/item['path']
                if not fpath.exists() or sha256_file(fpath) != item['sha256'] or fpath.stat().st_size != item['bytes']:
                    findings.append(Finding('RELEASE_HASH_MISMATCH', item['path'], item['path']))

    summary.update({
        'law_count': len(records),
        'scenario_count': len(scenario_ids),
        'full_law_bytes': full,
        'finding_count': len(findings),
    })
    return findings, summary


def finalize(package: Path) -> tuple[list[Finding], dict[str, Any]]:
    # Generate coverage first; it is derived from current canonical laws.
    manifest = load_yaml(package/'LAW-MANIFEST.yaml')
    _, _, requirement_count = generate_coverage(package, manifest)

    findings, summary = validate_package(package, include_release_hashes=False)
    summary['requirement_count'] = requirement_count
    report = {
        'document_type': 'STRUCTURAL_VALIDATION_RECEIPT',
        'constitution_id': 'UAAC-001',
        'constitution_version': VERSION,
        'status': 'PASS' if not findings else 'FAIL',
        'summary': summary,
        'findings': [asdict(x) for x in findings],
    }
    report_path = package/'validation/STRUCTURAL-VALIDATION.json'
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if findings:
        return findings, summary

    excluded = {
        'CONSTITUTION-RELEASE.yaml',
        'validation/STRUCTURAL-VALIDATION.json',
    }
    files = []
    for path in sorted(p for p in package.rglob('*') if p.is_file()):
        rel = path.relative_to(package).as_posix()
        if rel in excluded or not is_release_artifact(rel):
            continue
        files.append({'path': rel, 'bytes': path.stat().st_size, 'sha256': sha256_file(path)})

    release = {
        'document_type': 'CONSTITUTION_RELEASE',
        'constitution_id': 'UAAC-001',
        'version': VERSION,
        'status': 'STABLE_CORE_READY_FOR_PROJECT_INSTALLATION_AND_ADOPTION',
        'release_scope': 'CORE_AND_REFERENCE_ARTIFACTS',
        'canonical_law_count': 25,
        'validation': {
            'structural': 'PASS',
            'schemas': 'PASS',
            'fixtures': 'PASS',
            'manifest': 'PASS',
            'cross_file': 'PASS',
            'agent_behavioral_certification': 'PROJECT_SPECIFIC_NOT_IMPLIED',
        },
        'behavioral_scenarios': {
            'specified': summary['scenario_count'],
            'core_release_run': 'NOT_APPLICABLE',
            'project_adoption_requirement': 'RUN_PROFILE_REQUIRED_SCENARIOS_BEFORE_MATERIAL_EFFECTS',
        },
        'requirements_indexed': requirement_count,
        'structural_validation_receipt': 'validation/STRUCTURAL-VALIDATION.json',
        'files': files,
    }
    (package/'CONSTITUTION-RELEASE.yaml').write_text(yaml.safe_dump(release, sort_keys=False, allow_unicode=True), encoding='utf-8')
    return [], summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--finalize', action='store_true')
    args = parser.parse_args()

    package = args.package.resolve()
    if args.finalize:
        findings, summary = finalize(package)
    else:
        findings, summary = validate_package(package)

    for finding in findings:
        suffix = f' [{finding.path}]' if finding.path else ''
        print(f'{finding.code}: {finding.message}{suffix}')

    if findings:
        print(f'PACKAGE_VALIDATION_FAIL findings={len(findings)}')
        return 1
    print(f'PACKAGE_VALIDATION_PASS laws={summary.get("law_count", 25)} scenarios={summary.get("scenario_count", "?")}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
