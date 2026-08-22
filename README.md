# ProjectFramework

This repository publishes two separate, independently adoptable products and keeps their support/history boundaries explicit.

## Project Source Framework 1.2.5

ProjectFramework is under [`managing-project-source/`](managing-project-source/).

- Release descriptor: [`FRAMEWORK-RELEASE.yaml`](managing-project-source/FRAMEWORK-RELEASE.yaml)
- Managing procedure: [`SKILL.md`](managing-project-source/SKILL.md)
- Core governance: [`core-governance-rules.md`](managing-project-source/references/core-governance-rules.md)
- Framework version: **1.2.5**
- Project Source Schema: **1.0.0**

Framework semantics are readable contracts; they do not require a validator, CLI, runtime service, scheduler, or CI system.

## Universal AI Agent Constitution (UAAC) 5.0.0

UAAC production is under [`universal-ai-agent-constitution/`](universal-ai-agent-constitution/).

- Navigation: [`UAAC.md`](UAAC.md)
- Constitution: [`UAAC-v5.0-CONSTITUTION.md`](universal-ai-agent-constitution/UAAC-v5.0-CONSTITUTION.md)
- Installer: [`INSTALL-UAAC.md`](universal-ai-agent-constitution/INSTALL-UAAC.md)
- Adoption guide: [`ADOPTION-GUIDE.md`](universal-ai-agent-constitution/ADOPTION-GUIDE.md)
- Migration/rollback: [`MIGRATION-v4.2-TO-v5.0.md`](universal-ai-agent-constitution/MIGRATION-v4.2-TO-v5.0.md)
- Human walkthrough (Thai): [`HUMAN-INSTALL-WALKTHROUGH-TH.md`](HUMAN-INSTALL-WALKTHROUGH-TH.md)

The production boundary contains only Markdown/YAML. Operational constitutional requirements live only in the 25 stable law files. A capable LLM can operate from locally pinned content without Python, OpenViking, Serena, MCP, RAG, vector storage, native Skills, CI, or network access.

```text
Install UAAC != install or upgrade ProjectFramework
```

UAAC adoption does not install or change ProjectFramework. Framework adoption does not adopt or upgrade UAAC. A Project using both pins them separately.

## Optional UAAC profiles

Profiles under [`universal-ai-agent-constitution/profiles/`](universal-ai-agent-constitution/profiles/) are opt-in and non-normative. Presence does not activate a profile or create authority.

## Developer-only conformance

[`uaac-conformance/`](uaac-conformance/) contains developer-only Python, JSON Schema, tests, fixtures, and acceptance material. It is non-normative, is not installed into Projects, and may be deleted without breaking UAAC Core.

## Historical/reference v4.2

- Immutable reconstruction: [`docs/uaac-history/v4.2/`](docs/uaac-history/v4.2/)
- Preserved historical fixture: [`uaac-v4.2-reference-project/`](uaac-v4.2-reference-project/)
- Release commit: `5a309d8d38046bf3e8cd4beb2fc82a872f211cad`
- Package tree: `3e62912bcbd88d91339dfa772dc6776ee95c77c5`
- Completed fixture snapshot: `5cc9488427c8034a67f4898ace5f1c5806760b85`

Historical material is not an active v5 dependency and never resolves current v5 files as if they were 4.2.

## Repository development records

The [UAAC 5.0 design](docs/superpowers/specs/2026-08-23-uaac-5.0-constitution-first-runtime-free-design.md) and [implementation plan](docs/superpowers/plans/2026-08-23-uaac-5.0-constitution-first-runtime-free.md) document this release work. Development records are not copied into adopting Projects.

Patch audit: [`docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-REPORT.md`](docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-REPORT.md) and [`docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-STATE.yaml`](docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-STATE.yaml).
