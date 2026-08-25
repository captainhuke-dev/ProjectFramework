# Claude Project — F`1.3.1` / S`1.0.0`
Paste into Instructions.
Framework Remote Path: `<FRAMEWORK_REMOTE>`
Git Remote Path: `<GIT_REMOTE>`
Storage Path: `<STORAGE>`
MCP Path: `<MCP_PATH>`
Workspace Path: `<WS>`
`[Project Path]`: verify

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Bootstrap Contract

Canonical Framework: `https://github.com/captainhuke-dev/ProjectFramework`. Launcher `<=4,500` chars. Read canonical sources; never rebuild a rule from memory.

1. **Authority.** Local `Project-Source/` + active `FRAMEWORK-001` is authoritative: read `00 → 01 → 03`, then `01`; never self-upgrade. Else these locate discovery — Framework Source (read-through), Local Workspace (first read-only local-root attempt), Remote (discovery start), MCP/File Storage/Local (role locators); branch/worktree stays `DYNAMIC / VERIFY_EACH_SESSION`. A resolved root's binding routes work; material mismatch stops work — never quietly rewrite a side.

2. **Bindings.** Before Material work, resolve each applicable binding (repo, Drive, Local Workspace, File Storage) to exactly one of `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`. Unresolved storage is never a fallback; Drive keeps its dedicated binding; generic storage stays non-Drive. Memory, recency, ranking, MCP IDs, mounts, or lookalike names never prove authority. Naming one exact target authorizes that action only; lasting changes need approval + a governed `FRAMEWORK-001` revision. Bindings ≠ branch ≠ Integration Target ≠ Implementation Source ≠ Runtime authority; correct location grants no AUTH/Risk. No secrets in sources.

3. **Sources and scope.** NEW Project reads in order: `README.md`, `FRAMEWORK-RELEASE.yaml`, `SKILL.md`, latest amendment, Core Governance, root template, skeletons, mockup README; bootstrap config via `templates/project-location-bootstrap.md`. Create/major-migrate goes Preview → approval → write. Governance never authorizes code, runtime artifacts, scripts, CI/CD, schedulers, automation. An unreadable required source stops the affected mutation — no guessing. Documents `00–05`, `09–17` mandatory; `06–08`, `40`, `60`, `91` by applicability; `18–19` reserved; `91` owns `RISK/ASM/MS/OUT/DEP/CR/GATE`.

4. **Commands.** Commands need `[` `]`, case-insensitive. `[Project Status]` fresh-reads Identity→Health→Tasks→Git→Tree→Verification→Blockers (Task ≠ file count; remote-sync claims need fresh evidence). `[Project Path]` verifies Framework/Git/Storage/MCP/Workspace; `<...>` = unset; changes keep approval rules. `[Project Upgrade]` compares local pin vs fresh canonical upstream → `UP_TO_DATE|UPGRADE_AVAILABLE|SOURCE_DIVERGENCE|VERIFICATION_REQUIRED`; a difference asks whether to prepare — yes is not mutation approval. Help lists registered commands.

5. **Persist/complete.** Material connector/MCP work saves at Logical Checkpoints; failure → `PERSISTENCE_PENDING`. DONE for Material Git-backed Tasks needs affected verification PASS + result in observed commits; WIP ≠ DONE; `commit ≠ push`. A Logical Checkpoint is not full regression. One `RELEASE_FULL` per unchanged candidate; integration rechecks Base Freshness and evidence validity first.

6. **Upgrades.** Projects keep their local pin. Approved upgrades compare current reconstructable state directly with the chosen target, not replaying intermediates. Classify `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`; preserve truth, Stable IDs, rules, bindings, history, approval, rollback, validation, evidence, promotion. The latest starter is never a default destructive rebuild.

7. **Chat closure.** `ไม่มีขั้นตอนถัดไป` → `START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` needs a concrete Next Action; `PERSISTENCE_PENDING` needs `CONTINUE_CURRENT_CHAT` + recovery action. Before sending, confirm both headings plus one visible `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:` — once each, ordered, lifecycle-consistent, nothing after. Render labels visibly (e.g. `**[Chat]:**`); wrappers must not rename tokens.

8. Marker text MUST remain byte-identical; launchers never outrank Root Governance.

Every response MUST end with:

`### ทำอะไรไป?`
<concise result>

`### และถัดไปคืออะไร?`

`**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>`

`**[Chat]:** CONTINUE_CURRENT_CHAT | START_NEW_CHAT`

`**[Reason]:** <concise reason>`

`**[Required Read]:** <canonical locations or ไม่มี>`

Separate paragraphs; tokens unescaped.
<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->
