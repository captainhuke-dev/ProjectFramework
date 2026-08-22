from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

import jsonschema
import yaml


ALLOWED_PRODUCTION_SUFFIXES = {".md", ".yaml", ".yml"}
LAW_IDS = tuple(f"CONST-{number:03d}" for number in range(1, 26))


def production_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def law_files(production_root: Path) -> list[Path]:
    return sorted((production_root / "laws").glob("CONST-*.md"))


def template_schema_findings(repo_root: Path) -> list[str]:
    mapping_path = repo_root / "uaac-conformance" / "template-schema-map.yaml"
    if not mapping_path.is_file():
        return ["missing developer template-schema map"]

    mapping = load_yaml(mapping_path)
    if not isinstance(mapping, dict) or not isinstance(mapping.get("pairs"), list):
        return ["invalid developer template-schema map"]

    findings: list[str] = []
    for pair in mapping["pairs"]:
        pair_id = pair.get("id", "UNIDENTIFIED")
        template_path = repo_root / pair.get("template", "")
        schema_path = repo_root / pair.get("schema", "")
        if not template_path.is_file() or not schema_path.is_file():
            findings.append(f"template/schema path missing: {pair_id}")
            continue
        instance = load_yaml(template_path)
        schema = load_yaml(schema_path)
        errors = sorted(
            error.message
            for error in jsonschema.Draft202012Validator(schema).iter_errors(instance)
        )
        findings.extend(
            f"template/schema violation: {pair_id}: {error}" for error in errors
        )
    return findings


def distribution_findings(repo_root: Path) -> list[str]:
    production_root = repo_root / "universal-ai-agent-constitution"
    findings: list[str] = []
    if not (production_root / "UAAC-v5.0-CONSTITUTION.md").is_file():
        findings.append("missing UAAC-v5.0-CONSTITUTION.md")
    findings.extend(
        f"runtime extension: {path.relative_to(repo_root).as_posix()}"
        for path in production_files(production_root)
        if path.suffix.lower() not in ALLOWED_PRODUCTION_SUFFIXES
    )
    observed_law_ids = tuple(path.stem for path in law_files(production_root))
    if observed_law_ids != LAW_IDS:
        findings.append("law IDs differ from CONST-001..CONST-025")
    findings.extend(template_schema_findings(repo_root))
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the UAAC distribution")
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)

    findings = distribution_findings(args.repository_root.resolve())
    if findings:
        for finding in findings:
            print(f"UAAC_CONFORMANCE_FINDING {finding}")
        return 1

    print("UAAC_CONFORMANCE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
