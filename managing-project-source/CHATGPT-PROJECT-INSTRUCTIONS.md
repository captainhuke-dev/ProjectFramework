# ChatGPT Project Instructions — ProjectFramework

Paste this file's contents into **ChatGPT Project → Project settings → Instructions**.

Distribution release: **Project Source Framework 1.2.0 / Schema 1.0.0**.

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Governance Contract

This project uses `https://github.com/captainhuke-dev/ProjectFramework` as the canonical upstream bootstrap source for **NEW** Project Source creation. ProjectFramework is conceptual governance/planning first. Technical planning may precisely document Tech Stack, installation, Source/Docker responsibilities, interfaces, and verification, but does not authorize application code, Dockerfile/Compose, scripts, CI, or automation unless the user explicitly requests that separate implementation scope.

1. **Determine whether the Project is already initialized.**
   - If valid local `Project-Source/` exists with active `00 Project Source Framework` (`FRAMEWORK-001`), the pinned local Project Source is authoritative. Read `00 → 01 → 03`, then follow `01` routing. Do not replace it with upstream `main` or a newer release.
   - Otherwise treat it as `GREENFIELD`.
2. **GREENFIELD bootstrap from canonical upstream.**
   - Read canonical `main` in this order: `README.md` → `managing-project-source/FRAMEWORK-RELEASE.yaml` → `managing-project-source/SKILL.md` → latest Framework governance amendment → `references/core-governance-rules.md` → `templates/00-project-source-framework.md` → `templates/core-document-skeletons.md` → `templates/project-source-mockup/README.md`.
   - Do not reconstruct Framework rules, semantic slots, required files, authority, or Project facts from memory. If canonical source cannot be accessed, state the limitation and stop the affected governance mutation instead of guessing.
3. **Initial creation gate and namespace.**
   - Preview proposed Project Source/current assumptions and obtain explicit user approval before initial write.
   - Create active `00` first; mandatory `01–05` and `09–17`.
   - Evaluate conditional `06–08`, `40 Technical Design`, `60 Deployment Plan`, and `91 Project Management Control`; create only when applicable.
   - Keep `18–19` reserved. `91` is standard conditional in Framework `1.2.0+`; `92–99` remain Project-specific/Governance Extension space unless governed otherwise later.
   - Use governed revision/timestamp filenames, not `.template.md` names.
4. **Use Framework 1.2.0 management-control homes.**
   - `RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*` are canonical in `91`.
   - Preserve distinctions: Risk ≠ Issue; `ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED`; `DEP AVAILABLE ≠ SATISFIED`; `CR-*` proposed/material change control ≠ `CHG-*` history.
   - Project Health is a dimensional current assessment in `03`; Review Cadence may be `TIME_BASED` or `EVENT_BASED` without implying scheduler automation.
   - Decision Revalidation stays in `04`; Responsibility Mapping stays in `11` and **Responsibility ≠ Authority**; Knowledge Debt is `ISS-* issue_type: KNOWLEDGE_DEBT` in `08`.
5. **Use technical blueprints without unrequested coding.**
   - `40` documents Tech Stack, component/interface responsibility, source-structure responsibility, configuration contract, runtime requirements, deployment-mode architecture, and Source/Docker parity/variance when applicable.
   - `60` documents prerequisites, Source/Docker installation, configuration/secret references, initialization, start/stop, verification/health, logs, upgrade, rollback, backup/restore, cleanup, troubleshooting when applicable.
   - Deployment support states are `SOURCE_ONLY / DOCKER_ONLY / SOURCE_AND_DOCKER / NOT_APPLICABLE`.
   - `SOURCE_AND_DOCKER` shares one application/configuration/data/security/persistence contract. Intentional differences require explicit Deployment Mode Variance; unexpected mismatch is `DRIFT-*`.
   - A request for Tech Stack/install/Docker planning is **not** permission to create source code, Dockerfile, Compose/Kubernetes/Helm, package manifests, install scripts, CI/CD, or automation.
6. **Pin after bootstrap and preserve current truth.**
   - Record imported Framework `1.2.0` and Schema `1.0.0` locally. After initialization, local pinned Project Source is authoritative and upstream is not a live dependency.
   - Current referenced Stable IDs must resolve without archived revisions. Active `40/60/91` required to interpret current truth belong in the Current Reconstructable Snapshot/Manifest.
7. **Treat exact Git provenance as optional assurance.**
   - Tag/SHA/branch protection are not required for normal Framework operational use. Record exact provenance only when actually observed/material; never fabricate or retroactively backfill it.
8. **Never auto-upgrade or overwrite Brownfield extension state.**
   - Framework upgrades use `MIG-*`, explicit approval, validation, promotion, supersede/archive, postflight.
   - If pre-1.2.0 slot `91` is occupied, preserve it and resolve relocation through `MIG-*` + approval before activating standard `91`.
   - Never auto-convert old free text into new management Stable IDs without sufficient current semantics/status/ownership/evidence state.
9. **Preserve authority, secrets, and scope.**
   - Platform instructions never replace/weaken active `FRAMEWORK-001`; handoff/responsibility do not transfer authority.
   - Never store actual secrets; use `SECRET-*` metadata references only.
   - Stay within requested conceptual/documentation scope unless implementation is separately explicit.
10. **Golden Reference is illustrative only.**
   - `examples/golden-reference-software-project/Project-Source/` demonstrates composition but does not become normative authority and contains no real implementation runtime.
<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->
