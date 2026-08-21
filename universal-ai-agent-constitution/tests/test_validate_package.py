from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / 'tools' / 'validate_package.py'


def run_validator(package: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), '--package', str(package), *args],
        text=True,
        capture_output=True,
    )


def copy_package(tmp_path: Path) -> Path:
    dst = tmp_path / 'pkg'
    shutil.copytree(ROOT, dst)
    return dst


def test_valid_package_passes_check():
    result = run_validator(ROOT, '--check')
    assert result.returncode == 0, result.stdout + result.stderr
    assert 'PACKAGE_VALIDATION_PASS' in result.stdout


def test_manifest_drift_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    law = pkg / 'laws' / 'CONST-001.md'
    law.write_text(law.read_text() + '\nmutated\n', encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'PACKAGE_DRIFT' in result.stdout


def test_shared_boot_contract_drift_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    agents = pkg / 'templates' / 'platform' / 'AGENTS.md'
    agents.write_text(agents.read_text().replace('Continue only from coherent canonical Project state.', 'Continue from any available state.'), encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'BOOT_CONTRACT_DRIFT' in result.stdout


def test_invalid_state_authority_map_fixture_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    state_map = pkg / 'examples' / 'installed-project' / 'governance' / 'STATE-AUTHORITY-MAP.yaml'
    data = yaml.safe_load(state_map.read_text())
    del data['state_classes']['RUNTIME_JOBS']['canonical']['identity']
    state_map.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'SCHEMA_VALIDATION_FAIL' in result.stdout


def test_duplicate_claim_token_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    reg = pkg / 'examples' / 'installed-project' / 'governance' / 'CLAIM-CONTRACT-REGISTRY.yaml'
    data = yaml.safe_load(reg.read_text())
    data['contracts'].append(copy.deepcopy(data['contracts'][0]))
    reg.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'DUPLICATE_CLAIM_TOKEN' in result.stdout


def test_scenario_count_mismatch_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    scenarios = pkg / 'tests' / 'conformance-scenarios.md'
    text = scenarios.read_text()
    text = __import__('re').sub(r'scenario_count: \d+', 'scenario_count: 1', text, count=1)
    scenarios.write_text(text, encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'SCENARIO_COUNT_MISMATCH' in result.stdout


def test_finalize_writes_release_receipt_and_coverage(tmp_path: Path):
    pkg = copy_package(tmp_path)
    result = run_validator(pkg, '--finalize')
    assert result.returncode == 0, result.stdout + result.stderr
    release = yaml.safe_load((pkg / 'CONSTITUTION-RELEASE.yaml').read_text())
    assert release['status'] == 'STABLE_CORE_READY_FOR_PROJECT_INSTALLATION_AND_ADOPTION'
    assert all(v == 'PASS' for k, v in release['validation'].items() if k != 'agent_behavioral_certification')
    assert release['validation']['agent_behavioral_certification'] == 'PROJECT_SPECIFIC_NOT_IMPLIED'
    assert release['files']
    assert not any(item['path'].startswith('.pytest_cache/') for item in release['files'])
    assert (pkg / 'registers' / 'must-coverage-index.yaml').exists()
    assert (pkg / 'validation' / 'STRUCTURAL-VALIDATION.json').exists()
    receipt = json.loads((pkg / 'validation' / 'STRUCTURAL-VALIDATION.json').read_text(encoding='utf-8'))
    assert receipt['summary']['installation_fixture']['project'] == 'examples/installed-project'


def test_unlisted_release_file_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    finalized = run_validator(pkg, '--finalize')
    assert finalized.returncode == 0, finalized.stdout + finalized.stderr
    (pkg / 'UNLISTED.md').write_text('unlisted release content\n', encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'RELEASE_FILESET_MISMATCH' in result.stdout


def test_deprecated_consolidated_form_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    (pkg / 'UAAC-v4.0-CONSTITUTION.md').write_text('stale consolidated form\n', encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'DEPRECATED_RELEASE_ARTIFACT' in result.stdout


def test_coverage_policy_drift_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    path = pkg / 'registers' / 'coverage-policy.yaml'
    data = yaml.safe_load(path.read_text())
    data['default_methods_by_law']['CONST-021']['scenarios'] = ['S-ADP-01']
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'COVERAGE_POLICY_DRIFT' in result.stdout


def test_skill_version_drift_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    path = pkg / 'skills' / 'uaac-handoff' / 'SKILL.md'
    path.write_text(path.read_text().replace('constitution_version: 4.2.0', 'constitution_version: 4.0.0'), encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'SKILL_PACKAGE_DRIFT' in result.stdout


def test_reference_templates_start_fail_safe():
    capability = yaml.safe_load((ROOT / 'templates' / 'PROJECT-CAPABILITY-PACK.template.yaml').read_text())
    skills = yaml.safe_load((ROOT / 'templates' / 'SKILL-REGISTRY.template.yaml').read_text())
    documents = yaml.safe_load((ROOT / 'templates' / 'PROJECT-DOCUMENT-REGISTRY.template.yaml').read_text())
    installation = yaml.safe_load((ROOT / 'templates' / 'INSTALLATION-VALIDATION.template.yaml').read_text())
    continuation = yaml.safe_load((ROOT / 'templates' / 'CURRENT-CONTINUATION.template.yaml').read_text())
    pointer = yaml.safe_load((ROOT / 'templates' / 'CONTINUATION-POINTER.template.yaml').read_text())
    boot_text = (ROOT / 'templates' / 'PROJECT-UAAC-BOOT.template.md').read_text()

    assert capability['status'] == 'BLOCKED'
    assert all(item['status'] == 'BLOCKED' for item in skills['procedures'])
    assert all(item['status'] == 'BLOCKED' for item in documents['documents'])
    assert installation['status'] == 'INSTALLATION_UNVERIFIED'
    assert all(item['status'] == 'NOT_RUN' for item in installation['static_checks'])
    assert installation['cross_agent_convergence']['status'] == 'NOT_RUN'
    assert installation['cross_agent_convergence']['resolutions'] == []
    assert continuation['lineages'][0]['status'] == 'QUEUED'
    assert pointer['status'] == 'QUEUED'
    assert 'status: STAGED' in boot_text


def test_positive_default_template_is_detected(tmp_path: Path):
    pkg = copy_package(tmp_path)
    path = pkg / 'templates' / 'PROJECT-UAAC-BOOT.template.md'
    path.write_text(path.read_text().replace('status: STAGED', 'status: EFFECTIVE'), encoding='utf-8')
    result = run_validator(pkg, '--check')
    assert result.returncode != 0
    assert 'UNSAFE_TEMPLATE_DEFAULT' in result.stdout


def test_release_uses_modular_constitution_entrypoint():
    entry = ROOT / 'UAAC-v4.2-CONSTITUTION.md'
    text = entry.read_text(encoding='utf-8')
    assert entry.stat().st_size < 35000
    assert 'Canonical normative law files' in text
    for law_id in ('CONST-001', 'CONST-012', 'CONST-025'):
        assert f'laws/{law_id}.md' in text
        law_text = (ROOT / 'laws' / f'{law_id}.md').read_text(encoding='utf-8').strip()
        assert law_text not in text


def test_release_uses_compact_coverage_summary():
    data = yaml.safe_load((ROOT / 'registers' / 'must-coverage-index.yaml').read_text(encoding='utf-8'))
    assert 'requirements' not in data
    assert data['requirement_count'] >= 1
    assert len(data['laws']) == 25
    assert (ROOT / 'registers' / 'must-coverage-index.yaml').stat().st_size < 20000
    assert (ROOT / 'registers' / 'must-coverage-index.md').stat().st_size < 15000


def test_scenarios_are_split_into_modular_parts():
    index = ROOT / 'tests' / 'conformance-scenarios.md'
    parts = sorted((ROOT / 'tests' / 'scenarios').glob('*.md'))
    assert index.stat().st_size < 12000
    assert len(parts) >= 10
    assert max(path.stat().st_size for path in parts) < 20000
