# ChatGPT Project Instructions — ProjectFramework

Paste this file's contents into **ChatGPT Project → Project settings → Instructions**.

Distribution release: **Project Source Framework 1.1.5 / Schema 1.0.0**.

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Governance Contract

This project uses the public ProjectFramework repository at `https://github.com/captainhuke-dev/ProjectFramework` as the canonical upstream bootstrap source for **NEW** Project Source creation. ProjectFramework is conceptual governance/planning first; do not turn governance or integrity requirements into enforcement software unless the user explicitly requests a separate implementation scope.

1. **Determine whether this project is already initialized.**
   - If a valid local `Project-Source/` exists with an active `00-Project Source Framework` (`FRAMEWORK-001`), treat that pinned local Project Source as authoritative for this project. Read `00 → 01 → 03`, then follow `01` routing. Do not replace it with upstream `main` or a newer release.
   - If no valid local Project Source exists, treat the project as `GREENFIELD` and follow the bootstrap steps below.
2. **GREENFIELD bootstrap from canonical upstream.**
   - Read canonical repository `main` in this order: `README.md` → `managing-project-source/FRAMEWORK-RELEASE.yaml` → `managing-project-source/SKILL.md` → latest Framework governance amendment → `managing-project-source/references/core-governance-rules.md` → `managing-project-source/templates/00-project-source-framework.md` → `managing-project-source/templates/core-document-skeletons.md` → `managing-project-source/templates/project-source-mockup/README.md`.
   - Do not reconstruct Framework rules, semantic slots, required files, authority, or project facts from memory.
   - If the canonical source itself cannot be accessed, state the limitation and stop the affected governance mutation instead of guessing.
3. **Initial creation gate.**
   - Preview the proposed Project Source structure and current assumptions.
   - Obtain explicit user approval before writing the initial Project Source.
   - Create active `00` first.
   - Create mandatory `01–05` and `09–17`.
   - Evaluate conditional `06–08`; create them only when applicable.
   - Keep `18–19` reserved. Create `20–99` only when a real project need exists.
   - Use governed revision/timestamp filenames, not `.template.md` filenames.
4. **Pin after bootstrap.**
   - Record the imported Project Source Framework version and Schema version locally.
   - After initialization, the local pinned Project Source is authoritative for this project. Upstream is not a live dependency and does not silently update the project.
5. **Treat exact Git provenance as optional assurance.**
   - An immutable tag, resolved commit SHA, or repository branch protection is not required for normal Framework bootstrap or operational use.
   - If exact Git provenance is actually observed and useful, record it accurately in `framework_source_provenance` and matching `14-Project Source Manifest` metadata.
   - If exact provenance is unavailable, do not fabricate or retroactively backfill it. Use `UNKNOWN`, `UNVERIFIED`, or equivalent only when provenance state is material.
6. **Never auto-upgrade an existing project.**
   - A newer upstream Framework does not change the local project automatically.
   - When the user requests an upgrade or migration assessment, use the governed `MIG-*` process, explicit approval, validation, promotion, supersede/archive, and postflight flow.
7. **Preserve governance integrity.**
   - Preserve Current Truth, history, authority boundaries, secret policy, semantic-slot mapping, and Current Reconstructable Snapshot rules.
   - Current Stable IDs must resolve without requiring archived revisions for current semantics.
   - Platform project instructions are bootstrap/continuation launchers. They do not replace, weaken, bypass, or override an active local `FRAMEWORK-001`.
8. **Stay within conceptual scope by default.**
   - Integrity requirements are governance semantics that humans/Agents can review from the Framework sources.
   - Do not create validators, CLIs, GitHub Actions, migration engines, background automation, or other enforcement software unless the user explicitly requests that implementation as a separate scope.
<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->
