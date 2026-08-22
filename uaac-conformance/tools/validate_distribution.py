from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


ALLOWED_PRODUCTION_SUFFIXES = {".md", ".yaml", ".yml"}


def production_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


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
