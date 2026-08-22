from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "installed-project"
INSTALL_VALIDATOR = ROOT / "tools" / "validate_installation.py"
PACKAGE_VALIDATOR = ROOT / "tools" / "validate_package.py"


def run_install_validator(project: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALL_VALIDATOR), "--project", str(project), "--package", str(ROOT)],
        text=True,
        capture_output=True,
        timeout=60,
    )


def run_package_validator(package: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PACKAGE_VALIDATOR), "--package", str(package), "--check"],
        text=True,
        capture_output=True,
        timeout=90,
    )


def copy_example(tmp_path: Path) -> Path:
    target = tmp_path / "project"
    shutil.copytree(EXAMPLE, target)
    return target


def test_human_walkthrough_is_explicitly_non_executable():
    path = ROOT / "HUMAN-INSTALL-WALKTHROUGH-TH.md"
    frontmatter, body = _frontmatter(path)
    assert frontmatter == {
        "document_type": "UAAC_HUMAN_INSTALL_WALKTHROUGH",
        "audience": "HUMAN",
        "normative": False,
        "authority_effect": "NONE",
        "truth_authority": "NONE",
        "agent_execution": "DO_NOT_EXECUTE",
        "canonical_agent_install_protocol": "INSTALL-UAAC.md",
        "example_values_are_current_truth": False,
    }
    assert "FOR HUMAN READING ONLY" in body
    assert "INSTALL-UAAC.md" in body


def test_human_walkthrough_is_not_an_agent_execution_dependency():
    forbidden = "HUMAN-INSTALL-WALKTHROUGH-TH.md"
    execution_paths = [
        ROOT / "INSTALL-UAAC.md",
        ROOT / "templates" / "BOOTSTRAP-KERNEL.md",
        ROOT / "templates" / "AGENTS-UAAC-BOOTSTRAP.md",
        ROOT / "templates" / "CHATGPT-PROJECT-INSTRUCTIONS-SHORT.md",
        ROOT / "skills" / "uaac-boot" / "SKILL.md",
    ]
    for path in execution_paths:
        assert forbidden not in path.read_text(encoding="utf-8"), path


def test_bootstrap_kernel_precedes_skill_discovery():
    kernel = ROOT / "templates" / "BOOTSTRAP-KERNEL.md"
    text = kernel.read_text(encoding="utf-8")
    assert "UAAC-BOOTSTRAP-KERNEL:START" in text
    assert "resolve Project binding" in text
    assert "governance/UAAC-BOOT.md" in text
    assert "before Skill Registry" in text
    assert "PROJECT_BINDING_MISMATCH" in text
    assert "BOOTSTRAP KERNEL != SKILL" in text


def test_project_binding_mismatch_is_detected(tmp_path: Path):
    project = copy_example(tmp_path)
    path = project / "governance" / "PROJECT-BINDING.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["canonical_repository"] = "example/another-project"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = run_install_validator(project)
    assert result.returncode != 0
    assert "PROJECT_BINDING_MISMATCH" in result.stdout


def test_nested_project_front_door_is_not_parent_conflict(tmp_path: Path):
    project = copy_example(tmp_path)
    child = project / "apps" / "child"
    (child / "governance").mkdir(parents=True)
    (child / "governance" / "PROJECT-BINDING.yaml").write_text(
        yaml.safe_dump(
            {
                "schema_version": "1.0",
                "document_type": "PROJECT_BINDING",
                "project_id": "child-project",
                "project_root": ".",
                "canonical_repository": "example/monorepo",
                "canonical_ref_policy": "main",
                "governance_front_door": "governance/UAAC-BOOT.md",
                "parent_project_id": "example-installed-project",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (child / "governance" / "UAAC-BOOT.md").write_text(
        "---\ndocument_type: UAAC_PROJECT_BOOTSTRAP\nstatus: EFFECTIVE\n"
        "project_id: child-project\nauthority_effect: NONE\ntruth_authority: NONE\n---\n",
        encoding="utf-8",
    )
    result = run_install_validator(project)
    assert result.returncode == 0, result.stdout + result.stderr


def test_stale_task_context_before_write_is_detected(tmp_path: Path):
    project = copy_example(tmp_path)
    path = project / "governance" / "BOOT-RECEIPT.yaml"
    receipt = yaml.safe_load(path.read_text(encoding="utf-8"))
    receipt["pre_write_check"]["observed_continuation_index_identity"] = "CONT-INDEX-STALE"
    path.write_text(yaml.safe_dump(receipt, sort_keys=False), encoding="utf-8")
    result = run_install_validator(project)
    assert result.returncode != 0
    assert "TASK_CONTEXT_STALE" in result.stdout


def test_receiver_inaccessible_canonical_surface_is_detected(tmp_path: Path):
    project = copy_example(tmp_path)
    path = project / "governance" / "INSTALLATION-VALIDATION.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["cross_agent_convergence"]["resolutions"][0]["canonical_access"]["status"] = "FAIL"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = run_install_validator(project)
    assert result.returncode != 0
    assert "CANONICAL_SURFACE_NOT_VISIBLE" in result.stdout


def test_boot_freshness_reuse_requires_unchanged_identities(tmp_path: Path):
    project = copy_example(tmp_path)
    path = project / "governance" / "BOOT-RECEIPT.yaml"
    receipt = yaml.safe_load(path.read_text(encoding="utf-8"))
    receipt["boot_mode"] = "LIGHT"
    receipt["freshness"]["reused_prior_scope"] = True
    receipt["freshness"]["invalidated_by"] = ["PROJECT_LAW_IDENTITY_CHANGED"]
    path.write_text(yaml.safe_dump(receipt, sort_keys=False), encoding="utf-8")
    result = run_install_validator(project)
    assert result.returncode != 0
    assert "BOOT_FRESHNESS_INVALID" in result.stdout


def test_platform_adapter_file_only_is_not_invocation_proof(tmp_path: Path):
    project = copy_example(tmp_path)
    path = project / "governance" / "AGENT-ADAPTER-REGISTRY.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["adapters"][0]["status"] = "FILE_ONLY"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = run_install_validator(project)
    assert result.returncode != 0
    assert "PLATFORM_ADAPTER_UNVERIFIED" in result.stdout


def test_read_only_agent_uses_pending_canonical_publication_visibility():
    path = EXAMPLE / "governance" / "BOOT-RECEIPT.yaml"
    receipt = yaml.safe_load(path.read_text(encoding="utf-8"))
    visibility = receipt["visibility"]
    assert visibility["local_state"] == "CANONICAL_VISIBLE"
    assert visibility["receiver_visible"] is True
    assert visibility["unpublished_state_token"] == "PENDING_CANONICAL_PUBLICATION"


def test_material_task_floor_is_defined_in_boot_skill():
    text = (ROOT / "skills" / "uaac-boot" / "SKILL.md").read_text(encoding="utf-8")
    for term in [
        "source/artifact mutation",
        "commit/push/merge",
        "Project state",
        "requirements",
        "status claim",
        "checkpoint/handoff",
        "external effect",
        "publish/deploy",
        "UNKNOWN materiality",
    ]:
        assert term in text


def test_atomic_publication_contract_rejects_effective_branch_staging():
    data = yaml.safe_load((ROOT / "PUBLICATION-CONTRACT.yaml").read_text(encoding="utf-8"))
    assert data["strategy"] == "ATOMIC_TREE_REPLACEMENT"
    assert data["staging_on_effective_branch"] is False
    assert data["base_freshness_recheck"] == "REQUIRED_BEFORE_REF_UPDATE"
    assert data["expected_old_ref_guard"] == "REQUIRED"


def test_v42_package_validator_accepts_complete_package():
    result = run_package_validator(ROOT)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PACKAGE_VALIDATION_PASS" in result.stdout


def _frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    end = text.find("\n---\n", 4)
    assert end > 0
    return yaml.safe_load(text[4:end]), text[end + 5 :]
