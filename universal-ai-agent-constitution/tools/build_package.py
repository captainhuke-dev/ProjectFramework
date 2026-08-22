#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

VERSION = "4.2.0"
ENTRYPOINT_NAME = "UAAC-v4.2-CONSTITUTION.md"
EXPECTED_LAWS = [f"CONST-{i:03d}" for i in range(1, 26)]

TEST_ADDITIONS: dict[str, list[str]] = {
    "CONST-002": ["S-INSTALL-15", "S-INSTALL-19"],
    "CONST-014": ["S-INSTALL-02", "S-INSTALL-03", "S-INSTALL-09", "S-INSTALL-16", "S-INSTALL-17"],
    "CONST-015": ["S-INSTALL-01", "S-INSTALL-02", "S-INSTALL-10", "S-INSTALL-17", "S-INSTALL-20"],
    "CONST-016": ["S-INSTALL-01", "S-INSTALL-05", "S-INSTALL-11", "S-INSTALL-16", "S-INSTALL-22", "S-INSTALL-23"],
    "CONST-017": ["S-INSTALL-06"],
    "CONST-021": [
        "S-INSTALL-01", "S-INSTALL-04", "S-INSTALL-05", "S-INSTALL-06", "S-INSTALL-08",
        "S-INSTALL-10", "S-INSTALL-11", "S-INSTALL-12", "S-INSTALL-13", "S-INSTALL-14",
        "S-INSTALL-15", "S-INSTALL-18", "S-INSTALL-19", "S-INSTALL-20", "S-INSTALL-22", "S-INSTALL-23",
    ],
    "CONST-022": ["S-INSTALL-22", "S-INSTALL-23"],
    "CONST-023": ["S-INSTALL-07", "S-INSTALL-08", "S-INSTALL-13", "S-INSTALL-18", "S-INSTALL-21"],
    "CONST-024": ["S-INSTALL-01", "S-INSTALL-10", "S-INSTALL-17", "S-INSTALL-20"],
    "CONST-025": [
        "S-INSTALL-06", "S-INSTALL-12", "S-INSTALL-15", "S-INSTALL-16", "S-INSTALL-17",
        "S-INSTALL-18", "S-INSTALL-21", "S-INSTALL-22", "S-INSTALL-23",
    ],
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump_yaml(data: Any) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True).rstrip() + "\n"


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def parse_law_source(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    fm, rest = parse_frontmatter(text)
    law_id = str(fm["law_id"])
    heading = re.search(rf"^# {re.escape(law_id)} — (.+)$", rest, re.M)
    if not heading:
        raise ValueError(f"{path}: missing law heading")
    marker = re.search(rf"\n?<!-- END_OF_LAW: {re.escape(law_id)} .*?-->\s*$", rest, re.S)
    if not marker:
        raise ValueError(f"{path}: missing law marker")
    body = rest[heading.end() : marker.start()].lstrip("\n").rstrip("\n") + "\n"
    return {"frontmatter": fm, "law_id": law_id, "title": heading.group(1).strip(), "body": body}


def write_law(path: Path, source: dict[str, Any]) -> dict[str, Any]:
    fm = dict(source["frontmatter"])
    fm["version"] = VERSION
    law_id, title, body = source["law_id"], source["title"], source["body"]
    body_hash = sha256_bytes(body.encode("utf-8"))
    nonce = body_hash[:12]
    marker = f"<!-- END_OF_LAW: {law_id} version={VERSION} sha256={body_hash} nonce={nonce} -->"
    text = "---\n" + dump_yaml(fm) + "---\n\n" + f"# {law_id} — {title}\n\n" + body + "\n" + marker + "\n"
    path.write_text(text, encoding="utf-8")
    return {
        "law_id": law_id,
        "title": title,
        "status": fm.get("status"),
        "derogation": fm.get("derogation"),
        "applies_when": fm.get("applies_when"),
        "min_conformance": fm.get("min_conformance"),
        "body_bytes": len(body.encode("utf-8")),
        "body_sha256": body_hash,
        "file_sha256": sha256_bytes(text.encode("utf-8")),
        "nonce": nonce,
    }


def update_scenarios(index_path: Path) -> tuple[set[str], int]:
    text = index_path.read_text(encoding="utf-8")
    text = re.sub(r"^# Conformance Scenarios — Universal AI Agent Constitution v[0-9.]+$", f"# Conformance Scenarios — Universal AI Agent Constitution v{VERSION}", text, count=1, flags=re.M)
    text = re.sub(r'^constitution_version:\s*["\']?[0-9.]+["\']?\s*$', f'constitution_version: "{VERSION}"', text, count=1, flags=re.M)
    parts = sorted((index_path.parent / "scenarios").glob("*.md"))
    combined = "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts) + "\n"
    ids = re.findall(r"^## (S-[A-Z0-9-]+)\b", combined, re.M)
    if len(ids) != len(set(ids)):
        dupes = sorted({x for x in ids if ids.count(x) > 1})
        raise ValueError(f"duplicate scenario IDs: {dupes}")
    text = re.sub(r"^scenario_count:\s*\d+\s*$", f"scenario_count: {len(ids)}", text, count=1, flags=re.M)
    text = re.sub(r"<!-- END_OF_DOCUMENT: Conformance Scenarios v[0-9.]+ -->\s*$", f"<!-- END_OF_DOCUMENT: Conformance Scenarios v{VERSION} -->\n", text, count=1, flags=re.M)
    index_path.write_text(text, encoding="utf-8")
    return set(ids), len(ids)


def render_entrypoint(records: list[dict[str, Any]]) -> str:
    stable_rows = "\n".join(
        f"| `{r['law_id']}` | {r['title']} | `{r['derogation']}` | `{r['applies_when']}` | `{r['min_conformance']}` |"
        for r in records
    )
    route_rows = "\n".join(
        f"| `{r['law_id']}` | {r['title']} | [`{r['path']}`]({r['path']}) |" for r in records
    )
    return f'''---
document_type: UNIVERSAL_AI_AGENT_CONSTITUTION
status: STABLE_CORE_READY_FOR_PROJECT_INSTALLATION_AND_ADOPTION
version: "{VERSION}"
supersedes: "4.1.0"
constitution_id: "UAAC-001"
title: "Universal AI Agent Constitution"
scope: "Universal AI-agent governance across projects, frameworks, domains, runtimes, and vendors"
systems_thinking_applied: true
canonical_form: "MODULAR_LAW_FILES"
agent_behavioral_certification: "PROJECT_SPECIFIC_NOT_IMPLIED_BY_CORE_RELEASE"
law_id_policy: "STABLE_NEVER_RENUMBER_NEVER_REUSE"
---

# Universal AI Agent Constitution

## Version {VERSION}

This release is a stable constitutional core ready for explicit Project installation and adoption. It validates the package and reference implementation artifacts; each adopting Project must separately validate the actual agents, platforms, adapters, access surfaces, and applicable scenarios it uses.

## Preamble

The system purpose is to keep humans, agents, tools, runtimes, and repositories aligned on what is true, who may decide or act, which state is current, which evidence supports a claim, and how work continues without relying on private conversation memory.

```text
SHARED, VERIFIABLE PROJECT CONTEXT
+ HUMAN-GROUNDED AUTHORITY
+ SAFE MULTI-AGENT CONTINUITY
+ EVIDENCE-BASED RESULT STATES
+ PRACTICAL, APPLICABILITY-DRIVEN GOVERNANCE
```

A Project does not make every Agent share memory. It makes every intended Agent resolve the same Project binding, governance, documents, artifacts, continuation, and applicable procedures from canonical sources.

# 0. Normative language

- **MUST / MUST NOT** are mandatory.
- **SHOULD** is recommended unless a recorded reason justifies deviation.
- **MAY** is permitted.

Every normative paragraph must have an identified verification method or a registered verification gap with a best available check. Difficulty of verification does not weaken the rule.

## Derogation

```text
FORBIDDEN       Project Law cannot weaken or bypass
STRICTER_ONLY   Project Law may impose more, never less
PROJECT_DEFINED the Project must declare the value/policy
```

## Core distinctions

```text
Capability != Authority
Role != Authority
Prompt != Authority
Memory/Retrieval != Current Truth
Skill/File Presence != Invocation
Handoff != Authority Transfer
Execution != Verification != Acceptance != Publication != Deployment != Closure
```

# 1. Constitutional architecture

```text
REAL-WORLD OBLIGATIONS / PLATFORM SAFETY
                  ↓
                UAAC
                  ↓
PROJECT INSTALLATION + ADOPTION + PROJECT LAW
                  ↓
PROJECT BINDING + STATE/DOCUMENT AUTHORITIES
                  ↓
MINIMAL BOOTSTRAP KERNEL → UAAC-BOOT → APPLICABLE SKILLS
                  ↓
TASK / ATTEMPT PRECONDITIONS / EFFECT
                  ↓
EVIDENCE + CONTINUATION + RECEIVER READBACK
                  ↺
```

The Minimal Bootstrap Kernel is a small, authority-free, truth-free route to the active Project binding and front door before Skill discovery. The full `UAAC-BOOT` procedure then performs applicability, freshness, bounded reading, authority/state resolution, and automatic procedure selection.

# 2. Stable law IDs

| Law ID | Subject | Derogation | Applies when | Minimum |
|---|---|---|---|---|
{stable_rows}

# 3. Canonical normative law files

The files below are the canonical normative law form. This entrypoint routes to them and does not duplicate their text.

| Law ID | Subject | Canonical file |
|---|---|---|
{route_rows}

Use `LAW-MANIFEST.yaml` for immutable body/file identities, reading profiles, budgets, and conformance mappings.

# 4. Constitutional directives

## BOOTSTRAP KERNEL

```text
1. Resolve the intended Project root/boundary and Project binding.
2. Resolve exactly one effective governance/UAAC-BOOT.md for that boundary.
3. Compare local/remote Project ID, repository/ref policy, root and front-door identity.
4. Only then route to Capability Pack, Adapter Registry, Skill Registry and full UAAC-BOOT.
5. On mismatch/unavailability, stop affected work and report; do not guess from memory.
```

## UAAC AUTO-BOOT

For Project/session entry, resume, and every material task, invoke the registered `UAAC-BOOT` procedure without requiring the user to restate UAAC or name a Skill. Auto-Boot classifies materiality, validates freshness, uses a bounded reading scope, resolves canonical state and authority, and invokes only applicable procedures.

A material-task floor includes source/artifact mutation, commit/push/merge, governance/Project-state/requirements change, material decision/status claim, checkpoint/handoff, external effect, publish/deploy, secrets, authority, cost, or risk-tier use/change. Unknown materiality with possible material impact is treated as material until resolved.

## INSTALL PROJECT CONSTITUTION

```text
1. Resolve and pin an immutable UAAC release.
2. Inventory the target Project before mutation; preserve Brownfield truth/history.
3. Establish Project binding, one effective front door per declared Project boundary, Project Law, authority/document/state maps, Capability Pack, Adapter/Skill/Claim registries, and continuation.
4. Configure the Minimal Bootstrap Kernel and platform launchers.
5. Prove Auto-Boot, applicable procedure invocation, Project binding, receiver-visible canonical access, continuation recovery, and cross-agent convergence.
6. Keep INSTALLED, INSTALLATION_VALIDATED, EFFECTIVE, PUBLISHED, and CLOSED as separate evidence-backed states.
```

## WORK AND WRITE

Preserve the Boot receipt and attempt preconditions. Immediately before a material write, commit, push, merge, state transition, checkpoint, handoff, publication, or deployment, recheck the applicable canonical identities and predecessor. On material change emit `TASK_CONTEXT_STALE`; never use silent last-write-wins.

## CONTINUITY AND VISIBILITY

Use the Project Continuation Index plus lineage-local pointers. Distinguish `LOCAL_ONLY`, `PENDING_CANONICAL_PUBLICATION`, `CANONICAL_VISIBLE`, and `REMOTE_STALE`. Cross-Agent continuation requires a mutually readable canonical surface and receiver-side readback; a local checkpoint alone is not shared state.

## HANDOFF / REPORT / DECISION / COMMUNICATION

Use the applicable registered procedures and claim contracts. Preserve exact result-state distinctions, independent authority resolution, criteria/uncertainty/countercase where applicable, semantic integrity, and receiver verification.

## PUBLICATION

Build and validate outside the effective ref. Publish one complete final tree using base-freshness and expected-old-ref checks. A failed build must leave the prior effective ref unchanged. Temporary payloads, self-mutating workflows, probes, caches, and partial front-door targets are forbidden in the final release tree.

# 5. Canonical and generated forms

Canonical normative sources are `laws/*.md` plus the normative directives in this entrypoint. `LAW-MANIFEST.yaml`, coverage summaries, validation receipts, and release receipts are generated/derived and must agree with canonical sources.

<!-- END_OF_DOCUMENT: Universal AI Agent Constitution v{VERSION} -->
'''


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate UAAC law identities, manifest, scenarios, entrypoint, and coverage mapping")
    parser.add_argument("--package", type=Path, required=True)
    args = parser.parse_args()
    package = args.package.resolve()

    scenario_ids, scenario_count = update_scenarios(package / "tests/conformance-scenarios.md")
    manifest_path = package / "LAW-MANIFEST.yaml"
    manifest = load_yaml(manifest_path) or {}
    old_records = {r["law_id"]: r for r in manifest.get("laws", [])}

    built: list[dict[str, Any]] = []
    for order, law_id in enumerate(EXPECTED_LAWS, 1):
        path = package / "laws" / f"{law_id}.md"
        info = write_law(path, parse_law_source(path))
        tests = list(old_records.get(law_id, {}).get("tests", []))
        for test_id in TEST_ADDITIONS.get(law_id, []):
            if test_id not in tests:
                tests.append(test_id)
        missing = [x for x in tests if x not in scenario_ids]
        if missing:
            raise ValueError(f"{law_id} references missing scenarios: {missing}")
        built.append({
            "law_id": law_id, "order": order, "title": info["title"], "path": f"laws/{law_id}.md",
            "status": info["status"], "derogation": info["derogation"], "applies_when": info["applies_when"],
            "min_conformance": info["min_conformance"], "body_bytes": info["body_bytes"],
            "body_sha256": info["body_sha256"], "file_sha256": info["file_sha256"], "nonce": info["nonce"],
            "tests": tests,
        })

    manifest["manifest_version"] = VERSION
    manifest["constitution_id"] = "UAAC-001"
    manifest["constitution_version"] = VERSION
    manifest["canonical_form"] = "laws/*.md"
    manifest["law_count"] = len(built)
    manifest["laws"] = built
    by_id = {r["law_id"]: r for r in built}
    for profile in manifest.get("reading_profiles", {}).values():
        ids = profile.get("unconditional", [])
        profile["unconditional_count"] = len(ids)
        profile["unconditional_bytes"] = sum(by_id[i]["body_bytes"] for i in ids)
    manifest["size_budget"] = {
        "full_law_text_bytes": sum(r["body_bytes"] for r in built),
        "l1_unconditional_bytes": manifest["reading_profiles"]["BOOT_L1"]["unconditional_bytes"],
        "l2_unconditional_bytes": manifest["reading_profiles"]["BOOT_L2"]["unconditional_bytes"],
        "largest_laws": [{"law_id": r["law_id"], "body_bytes": r["body_bytes"]} for r in sorted(built, key=lambda x: x["body_bytes"], reverse=True)[:5]],
    }
    manifest_path.write_text(dump_yaml(manifest), encoding="utf-8")

    entrypoint = package / ENTRYPOINT_NAME
    entrypoint.write_text(render_entrypoint(built), encoding="utf-8")
    for old in package.glob("UAAC-v*-CONSTITUTION.md"):
        if old != entrypoint:
            old.unlink()

    coverage_path = package / "registers/coverage-policy.yaml"
    coverage = load_yaml(coverage_path) or {}
    coverage["constitution_version"] = VERSION
    methods = coverage.setdefault("default_methods_by_law", {})
    for rec in built:
        methods.setdefault(rec["law_id"], {})["scenarios"] = list(rec["tests"])
        methods[rec["law_id"]].setdefault("inspection", "LAW_SPECIFIC")
    coverage_path.write_text(dump_yaml(coverage), encoding="utf-8")

    print(f"PACKAGE_BUILD_PASS version={VERSION} laws={len(built)} scenarios={scenario_count} full_law_bytes={manifest['size_budget']['full_law_text_bytes']} entrypoint={entrypoint.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
