from pathlib import Path


PROFILE_IDS = {
    "high-assurance",
    "humanizer",
    "openviking",
    "projectframework",
    "reusable-procedures",
}


def test_profile_set_is_exact(production_root: Path) -> None:
    profiles = production_root / "profiles"
    assert {path.name for path in profiles.iterdir() if path.is_dir()} == PROFILE_IDS
    assert [
        path.relative_to(profiles).as_posix()
        for path in profiles.rglob("*")
        if path.is_file() and path.name != "PROFILE.md"
    ] == []


def test_profiles_are_opt_in_and_non_authoritative(
    production_root: Path, required_file
) -> None:
    for profile_id in PROFILE_IDS:
        path = required_file(production_root / "profiles" / profile_id / "PROFILE.md")
        text = path.read_text(encoding="utf-8").lower()
        assert "optional" in text, profile_id
        assert "non-normative" in text, profile_id
        assert "presence does not activate" in text, profile_id
        assert "cannot create authority" in text, profile_id


def test_projectframework_profile_never_installs_framework(
    production_root: Path, required_file
) -> None:
    path = required_file(
        production_root / "profiles" / "projectframework" / "PROFILE.md"
    )
    text = path.read_text(encoding="utf-8").lower()
    assert "already separately adopted" in text
    assert "does not install or upgrade projectframework" in text
