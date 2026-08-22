from pathlib import Path
import re
import subprocess
from collections.abc import Callable
from typing import Any

import pytest
import yaml


MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@pytest.fixture(scope="session")
def production_root(repo_root: Path) -> Path:
    return repo_root / "universal-ai-agent-constitution"


@pytest.fixture
def required_file() -> Callable[[Path], Path]:
    def require(path: Path) -> Path:
        assert path.is_file(), f"required file is missing: {path}"
        return path

    return require


@pytest.fixture
def required_yaml(required_file: Callable[[Path], Path]) -> Callable[[Path], Any]:
    def load(path: Path) -> Any:
        return yaml.safe_load(required_file(path).read_text(encoding="utf-8"))

    return load


@pytest.fixture
def markdown_targets() -> Callable[[Path], list[str]]:
    def targets(path: Path) -> list[str]:
        return MARKDOWN_LINK.findall(path.read_text(encoding="utf-8"))

    return targets


@pytest.fixture
def git_stdout(repo_root: Path) -> Callable[..., str]:
    def run(*args: str) -> str:
        completed = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    return run
