from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
INSTALL_VALIDATOR = ROOT / "tools" / "validate_installation.py"
EXAMPLE = ROOT / "examples" / "installed-project"


def run_install_validator(project: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALL_VALIDATOR), "--project", str(project)],
        text=True,
        capture_output=True,
    )


def test_required_installation_documents_exist():
    required = [
        ROOT / "INSTALL-UAAC.md",
        ROOT / "ADOPTION-RUNBOOK.md",
        ROOT / "INSTALLATION-THREAT-MODEL.md",
        ROOT / "templates" / "PROJECT-UAAC-BOOT.template.md",
        ROOT / "templates" / "PROJECT-GOVERNANCE-README.template.md",
        ROOT / "templates" / "PROJECT-CAPABILITY-PACK.template.yaml",
        ROOT / "templates" / "PROJECT-DOCUMENT-REGISTRY.template.yaml",
        ROOT / "templates" / "CONTINUATION-POINTER.template.yaml",
        ROOT / "templates" / "INSTALLATION-VALIDATION.template.yaml",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    assert not missing, missing


def test_valid_installed_project_passes():
    result = run_install_validator(EXAMPLE)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "INSTALLATION_VALIDATION_PASS" in result.stdout


def test_front_door_is_router_not_authority():
    text = (EXAMPLE / "governance" / "UAAC-BOOT.md").read_text(encoding="utf-8")
    assert "authority_effect: NONE" in text
    assert "truth_authority: NONE" in text
    assert "governance/CONSTITUTION-ADOPTION.yaml" in text
    assert "governance/CURRENT-CONTINUATION.yaml" in text


def test_project_document_registry_maps_required_semantic_roles():
    data = yaml.safe_load((EXAMPLE / "governance" / "PROJECT-DOCUMENT-REGISTRY.yaml").read_text())
    roles = {entry["role"]: entry for entry in data["documents"]}
    assert {"PROJECT_DEFINITION", "REQUIREMENTS", "CURRENT_STATE"} <= roles.keys()
    assert all(roles[role]["status"] == "RESOLVED" for role in ["PROJECT_DEFINITION", "REQUIREMENTS", "CURRENT_STATE"])


def test_continuation_index_preserves_active_and_terminal_lineages():
    data = yaml.safe_load((EXAMPLE / "governance" / "CURRENT-CONTINUATION.yaml").read_text())
    assert data["document_type"] == "PROJECT_CONTINUATION_INDEX"
    statuses = {item["lineage_id"]: item["status"] for item in data["lineages"]}
    assert statuses["LINEAGE-ACTIVE"] == "IN_PROGRESS"
    assert statuses["LINEAGE-CLOSED"] == "CLOSED"


def test_installation_report_proves_cross_agent_convergence():
    data = yaml.safe_load((EXAMPLE / "governance" / "INSTALLATION-VALIDATION.yaml").read_text())
    assert data["status"] == "INSTALLATION_VALIDATED"
    resolutions = data["cross_agent_convergence"]["resolutions"]
    keys = [
        "project_id",
        "constitution_identity",
        "project_law_identity",
        "state_authority_map_identity",
        "continuation_index_identity",
        "project_document_registry_identity",
        "skill_registry_identity",
    ]
    baseline = {key: resolutions[0][key] for key in keys}
    for resolution in resolutions[1:]:
        assert {key: resolution[key] for key in keys} == baseline


def copy_installed_project(tmp_path: Path) -> Path:
    import shutil
    dst = tmp_path / 'installed'
    shutil.copytree(EXAMPLE, dst)
    return dst


def test_duplicate_effective_front_door_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    extra = project / 'legacy' / 'UAAC-BOOT.md'
    extra.parent.mkdir(parents=True)
    extra.write_text((project/'governance/UAAC-BOOT.md').read_text(), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'GOVERNANCE_BOOT_CONFLICT' in result.stdout


def test_missing_required_document_role_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/PROJECT-DOCUMENT-REGISTRY.yaml'
    data = yaml.safe_load(path.read_text())
    data['documents'] = [item for item in data['documents'] if item['role'] != 'REQUIREMENTS']
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'PROJECT_DOCUMENTS_UNRESOLVED' in result.stdout


def test_cross_agent_resolution_mismatch_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/INSTALLATION-VALIDATION.yaml'
    data = yaml.safe_load(path.read_text())
    data['cross_agent_convergence']['resolutions'][1]['continuation_index_identity'] = 'OTHER-INDEX'
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'BOOTSTRAP_CONVERGENCE_FAILED' in result.stdout


def test_missing_active_required_skill_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/SKILL-REGISTRY.yaml'
    data = yaml.safe_load(path.read_text())
    for item in data['procedures']:
        if item['function'] == 'HANDOFF':
            item['status'] = 'STALE'
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'PROCEDURE_MATERIALIZATION_REQUIRED' in result.stdout


def test_lineage_pointer_status_mismatch_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/continuation/LINEAGE-ACTIVE/CURRENT.yaml'
    data = yaml.safe_load(path.read_text())
    data['status'] = 'BLOCKED'
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'CONTINUATION_POINTER_MISMATCH' in result.stdout


def test_front_door_locator_cannot_escape_project(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/UAAC-BOOT.md'
    text = path.read_text(encoding='utf-8')
    text = text.replace('locator: governance/PROJECT-LAWS/PROJECT_RULES.md', 'locator: ../../outside-project-rules.md')
    path.write_text(text, encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'LOCATOR_OUTSIDE_PROJECT' in result.stdout


def test_positive_installation_requires_all_static_checks_pass(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/INSTALLATION-VALIDATION.yaml'
    data = yaml.safe_load(path.read_text())
    data['static_checks'][0]['status'] = 'FAIL'
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'INSTALLATION_CLAIM_UNSUBSTANTIATED' in result.stdout


def test_positive_installation_requires_convergence_pass(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/INSTALLATION-VALIDATION.yaml'
    data = yaml.safe_load(path.read_text())
    data['cross_agent_convergence']['status'] = 'NOT_RUN'
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'BOOTSTRAP_CONVERGENCE_FAILED' in result.stdout


def test_duplicate_lineage_id_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project/'governance/CURRENT-CONTINUATION.yaml'
    data = yaml.safe_load(path.read_text())
    data['lineages'].append(dict(data['lineages'][0]))
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'DUPLICATE_LINEAGE_ID' in result.stdout


def test_unresolved_placeholder_outside_adoption_fails(tmp_path: Path):
    project = copy_installed_project(tmp_path)
    path = project / 'governance' / 'PROJECT-CAPABILITY-PACK.yaml'
    data = yaml.safe_load(path.read_text())
    data['pack_id'] = '<unresolved-pack-id>'
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    result = run_install_validator(project)
    assert result.returncode != 0
    assert 'UNRESOLVED_PLACEHOLDER' in result.stdout
