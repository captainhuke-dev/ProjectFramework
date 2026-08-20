# Claude Project Instructions — ProjectFramework

Paste this file's contents into **Claude Project → Set project instructions**.

Distribution release: **Project Source Framework 1.1.4 / Schema 1.0.0**.

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Governance Contract

This project uses the public ProjectFramework repository at `https://github.com/captainhuke-dev/ProjectFramework` as the canonical upstream discovery source for **NEW** Project Source creation. Reproducible bootstrap resolves the stable release ref declared by the distribution rather than treating mutable `main` as immutable provenance.

1. **Determine whether this project is already initialized.**
   - If a valid local `Project-Source/` exists with an active `00-Project Source Framework` (`FRAMEWORK-001`), treat that pinned local Project Source as the authoritative governance source for this project. Read `00 → 01 → 03`, then follow `01` routing. Do not replace it with upstream `main` or a newer release.
   - If no valid local Project Source exists, treat the project as `GREENFIELD` and follow the bootstrap steps below.
2. **GREENFIELD discovery and immutable release resolution.**
   - Read canonical repository `main` only as the discovery entrypoint: `README.md` → `managing-project-source/FRAMEWORK-RELEASE.yaml`.
   - Read `stable_release_tag` from `FRAMEWORK-RELEASE.yaml`, resolve that Git ref, and normally use the tagged source for the Framework bootstrap.
   - Verify that the tagged source declares the expected Framework and Schema versions before using it.
   - From the resolved tagged source, read: `managing-project-source/SKILL.md` → latest Framework governance amendment → `managing-project-source/references/core-governance-rules.md` → `managing-project-source/templates/00-project-source-framework.md` → `managing-project-source/templates/core-document-skeletons.md` → `managing-project-source/templates/project-source-mockup/README.md`.
   - Do not reconstruct Framework rules, semantic slots, release identity, or required files from memory.
3. **If immutable release resolution is unavailable.**
   - State the access/resolution limitation and stop the affected governance mutation.
   - Do not claim a release tag or immutable SHA that was not actually resolved.
   - Bootstrap from mutable `main` may proceed only after explicit user approval and must preserve degraded provenance such as `VERIFICATION_REQUIRED` / mutable-source warning.
4. **Initial creation gate.**
   - Preview the proposed Project Source structure and current assumptions.
   - Obtain explicit user approval before writing the initial Project Source.
   - Create active `00` first.
   - Create mandatory `01–05` and `09–17`.
   - Evaluate conditional `06–08`; create them only when applicable.
   - Keep `18–19` reserved. Create `20–99` only when a real project need exists.
   - Use governed revision/timestamp filenames, not `.template.md` filenames.
5. **Record exact observed provenance after bootstrap.**
   - Record the release tag/ref and the actually resolved Git commit SHA in local `framework_source_provenance` and matching `14-Project Source Manifest` continuation metadata.
   - The `resolved_commit_sha` value must come from the Git ref actually used. Never predict, fabricate, or retroactively backfill an unobserved historical SHA.
   - Record the imported Framework version and Schema version locally.
   - After initialization, the local pinned Project Source is authoritative for this project. The upstream repository is not a live dependency.
6. **Never auto-upgrade an existing project.**
   - A newer upstream Framework does not change the local project automatically.
   - When the user requests an upgrade or migration assessment, compare the pinned local version with upstream and use the governed `MIG-*` process, explicit approval, validation, promotion, supersede/archive, and postflight flow.
7. **Preserve governance integrity.**
   - Never invent project facts, authority, current state, Stable IDs, semantic slots, missing source, or release provenance.
   - Preserve Current Truth, history, authority boundaries, secret policy, and Current Reconstructable Snapshot rules.
   - Current Stable IDs must resolve without requiring archived revisions for current semantics.
   - Platform project instructions are a bootstrap/continuation launcher. They do not replace, weaken, bypass, or override an active local `FRAMEWORK-001`.
8. **Stay within requested scope.**
   - Do not expand documentation/governance requests into executable validators, CLIs, migration engines, background automation, or other software unless the user explicitly requests it.
<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->
