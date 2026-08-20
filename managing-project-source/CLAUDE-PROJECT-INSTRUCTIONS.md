# Claude Project Instructions — ProjectFramework

Paste this file's contents into **Claude Project → Set project instructions**.

Distribution release: **Project Source Framework 1.1.3 / Schema 1.0.0**.

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Governance Contract

This project uses the public ProjectFramework repository at `https://github.com/captainhuke-dev/ProjectFramework` as the canonical upstream bootstrap source for **NEW** Project Source creation.

1. **Determine whether this project is already initialized.**
   - If a valid local `Project-Source/` exists with an active `00-Project Source Framework` (`FRAMEWORK-001`), treat that pinned local Project Source as the authoritative governance source for this project. Read `00 → 01 → 03`, then follow `01` routing. Do not replace it with upstream `main`.
   - If no valid local Project Source exists, treat the project as `GREENFIELD` and follow the bootstrap steps below.
2. **GREENFIELD bootstrap from canonical upstream.**
   - Read repository `main` in this order: `README.md` → `managing-project-source/SKILL.md` → latest Framework governance amendment → `managing-project-source/references/core-governance-rules.md` → `managing-project-source/templates/00-project-source-framework.md` → `managing-project-source/templates/core-document-skeletons.md` → `managing-project-source/templates/project-source-mockup/README.md`.
   - Do not reconstruct Framework rules, semantic slots, or required files from memory.
   - If the upstream repository cannot be accessed, state the limitation and stop the affected governance mutation. Ask the user to provide/add the required source instead of guessing.
3. **Initial creation gate.**
   - Preview the proposed Project Source structure and current assumptions.
   - Obtain explicit user approval before writing the initial Project Source.
   - Create active `00` first.
   - Create mandatory `01–05` and `09–17`.
   - Evaluate conditional `06–08`; create them only when applicable.
   - Keep `18–19` reserved. Create `20–99` only when a real project need exists.
   - Use governed revision/timestamp filenames, not `.template.md` filenames.
4. **Pin after bootstrap.**
   - Record the imported Project Source Framework version and Schema version in the local Project Source.
   - After initialization, the local pinned Project Source is authoritative for this project. The upstream repository is not a live dependency.
5. **Never auto-upgrade an existing project.**
   - A newer upstream Framework does not change the local project automatically.
   - When the user requests an upgrade or migration assessment, compare the pinned local version with upstream and use the governed `MIG-*` process, explicit approval, validation, promotion, supersede/archive, and postflight flow.
6. **Preserve governance integrity.**
   - Never invent project facts, authority, current state, Stable IDs, semantic slots, or missing source.
   - Preserve Current Truth, history, authority boundaries, secret policy, and Current Reconstructable Snapshot rules.
   - Current Stable IDs must resolve without requiring archived revisions for current semantics.
   - Platform project instructions are a bootstrap/continuation launcher. They do not replace, weaken, or override an active local `FRAMEWORK-001`.
7. **Stay within requested scope.**
   - Do not expand documentation/governance requests into executable validators, CLIs, migration engines, background automation, or other software unless the user explicitly requests it.
<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->
