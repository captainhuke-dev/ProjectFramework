from pathlib import Path


DEFINED_CHECKS = [
    "constitutional_acceptance",
    "developer_conformance",
    "link_integrity",
    "production_distribution_boundary",
    "historical_v4_2_reconstruction",
]


def test_release_metadata_defines_checks_without_fabricated_pass(
    production_root: Path, required_yaml
) -> None:
    release = required_yaml(production_root / "CONSTITUTION-RELEASE.yaml")
    assert release["assurance"] == {
        "status": "DEFINED_NOT_RECORDED",
        "checks": DEFINED_CHECKS,
        "evidence_route": "../docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-STATE.yaml",
    }


def test_release_metadata_preserves_v42_predecessor_identity(
    production_root: Path, required_yaml
) -> None:
    release = required_yaml(production_root / "CONSTITUTION-RELEASE.yaml")
    assert release["predecessor"] == {
        "version": "4.2.0",
        "release_commit": "5a309d8d38046bf3e8cd4beb2fc82a872f211cad",
        "package_tree": "3e62912bcbd88d91339dfa772dc6776ee95c77c5",
    }
