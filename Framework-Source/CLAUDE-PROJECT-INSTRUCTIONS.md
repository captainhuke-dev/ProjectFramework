# Claude Project — F`1.8.0` / S`1.0.0`
Paste in Instructions.

Framework Remote Path: `<FRAMEWORK_REMOTE>`
Git Remote Path: `<GIT_REMOTE>`
Storage Path: `<STORAGE>`
MCP Path: `<MCP_PATH>`
Workspace Path: `<WS>`
`[Project Path]`: verify

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Bootstrap Contract

Canonical Framework: `https://github.com/captainhuke-dev/ProjectFramework`. Launcher `<=4,500` chars. Read canonical sources; never reconstruct rules from memory.

1. **Authority.** If Project root has `PROJECT-BOOTSTRAP.md`, read it as locator → active `Project-Source/FRAMEWORK-001` → `00 → 01 → 03`; resolve `09` for continuation. Active `FRAMEWORK-001` is authority. Missing root file may be legacy/pre-1.7: discovery-only via Framework Source, Local Workspace, Remote, MCP/File Storage roles; never auto-create/upgrade. Branch/worktree stays `DYNAMIC / VERIFY_EACH_SESSION`. Material mismatch fails closed; never silently rewrite a side.

2. **Bindings.** Before Material work resolve repo, Drive, Local Workspace, File Storage to `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`. Unresolved storage never falls back; Drive remains dedicated; generic storage is non-Drive. Recency/ranking/MCP IDs/mounts/lookalikes never prove authority. Exact named target = one action; lasting changes need approval + revision. Bindings ≠ branch/Integration Target/Implementation Source/Runtime; location grants no AUTH/Risk. No secrets.

3. **Sources/scope.** NEW Project reads `README.md`, `FRAMEWORK-RELEASE.yaml`, `SKILL.md`, latest amendment, Core Governance, `templates/PROJECT-BOOTSTRAP.md`, root template, skeletons, mockup README; location setup uses `templates/project-location-bootstrap.md`. Create/major-migrate: Preview → approval → write. Governance never authorizes code/runtime/scripts/CI/CD/schedulers/automation. Unreadable required source stops mutation. `00–05`,`09–17` mandatory; `06–08`,`40`,`60`,`91`,`92` conditional; `18–19` reserved; `91` owns `RISK/ASM/MS/OUT/DEP/CR/GATE`.

4. **Commands.** Literal brackets, case-insensitive inside. `[Project Status]` fresh-reads Identity→Health→Tasks→Git→Tree→Verification→Blockers→Continuity; Task ≠ file count; remote claims need fresh evidence. `[Project Path]` verifies Framework/Git/Storage/MCP/Workspace; `<...>` = unset. `[Project Upgrade]` reports `UP_TO_DATE|UPGRADE_AVAILABLE|SOURCE_DIVERGENCE|VERIFICATION_REQUIRED`; difference asks to prepare, not mutate. `[Session Envelope]` pre-approves bounded `ENV-*` scope but never lifts fail-closed gates. Help lists registered commands only.

5. **Persist.** Material connector/MCP work saves at Logical Checkpoints; failure → `PERSISTENCE_PENDING`. Checkpoints update `09` Resume Block; fresh sessions resume from durable state. Mutations idempotent where possible; non-idempotent intent first. DONE needs affected verification PASS + observed completion commit; WIP ≠ DONE; `commit ≠ push`. One `RELEASE_FULL` per unchanged candidate; integration rechecks Base Freshness/evidence validity.

6. **Upgrades.** Projects stay pinned. Approved upgrades compare current→target directly; no mandatory intermediate replay. Classify `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`; preserve truth/Stable IDs/rules/bindings/history/approval/rollback/validation/evidence/promotion. Root bootstrap adoption for existing Projects is upgrade-only. Latest starter is never a destructive default rebuild.

7. **Chat closure.** `ไม่มีขั้นตอนถัดไป` → `START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` needs a concrete Next Action; `PERSISTENCE_PENDING` needs it + recovery action. Before emit confirm both headings plus `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:` once each, ordered, lifecycle-consistent, nothing after. Render labels visibly; wrappers never rename tokens.

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
