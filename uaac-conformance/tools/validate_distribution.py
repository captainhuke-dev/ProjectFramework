from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


def distribution_findings(repo_root: Path) -> list[str]:
    production_root = repo_root / "universal-ai-agent-constitution"
    findings: list[str] = []
    if not (production_root / "UAAC-v5.0-CONSTITUTION.md").is_file():
        findings.append("missing UAAC-v5.0-CONSTITUTION.md")
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
