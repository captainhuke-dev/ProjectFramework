# ProjectFramework

This repository contains two separate, independently adoptable distributions:

- **Project Source Framework 1.2.5** under `managing-project-source/`
- **Universal AI Agent Constitution (UAAC) 4.2.0** under `universal-ai-agent-constitution/`

The `hz-framework` branch preserves the UAAC release history while carrying the current ProjectFramework baseline from `main`.

## Install the product you intend

```text
Install UAAC
!=
Install or upgrade ProjectFramework
```

Adopting UAAC does not install ProjectFramework. Adopting or upgrading ProjectFramework does not adopt or upgrade UAAC. A Project that intentionally uses both pins and governs them as separate dependencies.

## ProjectFramework 1.2.5

- Package: [`managing-project-source/`](managing-project-source/)
- Release descriptor: [`managing-project-source/FRAMEWORK-RELEASE.yaml`](managing-project-source/FRAMEWORK-RELEASE.yaml)
- Managing skill: [`managing-project-source/SKILL.md`](managing-project-source/SKILL.md)
- Core governance: [`managing-project-source/references/core-governance-rules.md`](managing-project-source/references/core-governance-rules.md)
- Current Framework: **1.2.5**
- Project Source Schema: **1.0.0**

ProjectFramework is a conceptual Project-governance and planning framework. Its integrity requirements are semantic contracts that Humans and Agents can inspect. They do not require a validator, CLI, runtime service, CI/CD workflow, scheduler, or other executable enforcement.

Framework 1.2.5 adds verified Material Task completion checkpoints, progressive risk-scoped verification with evidence reuse, environment-scoped Local Workspace Binding, and response-close completeness semantics. Existing initialized Projects remain locally pinned and do not auto-upgrade.

## UAAC 4.2.0 release history

- Navigation: [`UAAC.md`](UAAC.md)
- Package: [`universal-ai-agent-constitution/`](universal-ai-agent-constitution/)
- Installer: [`universal-ai-agent-constitution/INSTALL-UAAC.md`](universal-ai-agent-constitution/INSTALL-UAAC.md)
- Constitution: [`universal-ai-agent-constitution/UAAC-v4.2-CONSTITUTION.md`](universal-ai-agent-constitution/UAAC-v4.2-CONSTITUTION.md)
- Release descriptor: [`universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml`](universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml)
- Immutable release commit: `5a309d8d38046bf3e8cd4beb2fc82a872f211cad`

The staged historical reference Project is under [`uaac-v4.2-reference-project/`](uaac-v4.2-reference-project/). It is a reference/evidence boundary, not ProjectFramework and not a requirement for every UAAC Project.

## Repository layout

```text
ProjectFramework/
├── README.md
├── LICENSE
├── HUMAN-INSTALL-WALKTHROUGH-TH.md
├── UAAC.md
├── managing-project-source/               # ProjectFramework distribution
├── universal-ai-agent-constitution/       # UAAC distribution
├── uaac-v4.2-reference-project/           # historical/reference Project
└── docs/                                  # repository development records
```

Files under `docs/superpowers/` document development of this repository and are not automatically copied into adopting Projects.

## Current-truth boundaries

- An adopting Project's local pinned sources govern that Project; upstream branch movement does not auto-upgrade it.
- Conversation, memory, retrieval, summaries, examples, and optional tools are not Current Truth or authority by themselves.
- Exact Git identities and other release-assurance mechanisms must be recorded only when actually observed.
- Missing facts, authority, provenance, or Project-specific rules are never invented merely to fill a template.

