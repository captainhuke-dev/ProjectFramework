# ChatGPT Project Instructions — ProjectFramework

Paste this file's contents into **ChatGPT Project → Project settings → Instructions**.

Distribution release: **Project Source Framework 1.2.4 / Schema 1.0.0**.

<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->
## Shared ProjectFramework Bootstrap Contract

Canonical Framework source: `https://github.com/captainhuke-dev/ProjectFramework`.

Each launcher MUST be `<=4,500` Unicode characters. Read canonical Framework sources for omitted semantics; never reconstruct missing rules from memory.

1. **Resolve authority first.** Valid local `Project-Source/` + active `FRAMEWORK-001` → local pinned Project Source is authoritative. Read `00 → 01 → 03`, then `01` routing. Never auto-upgrade from upstream. Otherwise treat as `GREENFIELD`.

2. **Resolve Project Location Binding before Material GitHub/Drive work.** Read it from active local `FRAMEWORK-001`; never infer repo/Drive root from chat memory, recent activity, search ranking. `VERIFICATION_REQUIRED` is fail-closed for Material mutation; read/search/discovery may resolve candidates. `NOT_APPLICABLE` blocks Material Project work through that connector. Persistent binding change requires User Explicit Approval + governed `FRAMEWORK-001` revision/promotion. One-off exact-target instruction does not persistently rewrite binding. Repository binding ≠ current branch/worktree ≠ Canonical Integration Target ≠ Canonical Implementation Source; Location Binding defines no `canonical_branch`.

3. **GREENFIELD bootstrap from canonical `main`.** Read `README.md` → `managing-project-source/FRAMEWORK-RELEASE.yaml` → `SKILL.md` → latest amendment → `references/core-governance-rules.md` → `templates/00-project-source-framework.md` → `templates/core-document-skeletons.md` → `templates/project-source-mockup/README.md`. Discovery may be read-only; Preview proposed GitHub/Drive binding → explicit approval → create active `00` first. If required source is unreadable, disclose and stop the affected governance mutation; do not guess.

4. **Upstream is read-through, not live authority for initialized Projects.** It MUST NOT override local `FRAMEWORK-001` or silently change the local pin.

5. **Preserve gates, scope, truth, and secrets.** Initial creation/major structural migration requires Preview → explicit approval → write. ProjectFramework is governance/planning first; code/runtime files/scripts/CI/CD/schedulers/automation need separate explicit scope. Current Stable IDs resolve without archive traversal. Never store actual secrets or fabricate Git provenance.

6. **Keep routing distinctions.** Mandatory `00–05`,`09–17`; conditional `06–08`,`40`,`60`,`91`; reserved `18–19`. `91` owns `RISK/ASM/MS/OUT/DEP/CR/GATE`. Preserve Risk ≠ Issue; ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED; DEP AVAILABLE ≠ SATISFIED; Responsibility ≠ Authority.

7. **Externalize Material connector/MCP work.** Persist at Logical Checkpoints to source-native durable state; transient reads/searches need not persist. GitHub uses the owning repository/canonical Project Source home. Drive uses the existing designated progress `.md`, or one stable `PROJECT-PROGRESS.md` only when needed. Persistence failure → `PERSISTENCE_PENDING`.

8. **Chat Closure Consistency.** `ไม่มีขั้นตอนถัดไป` → `START_NEW_CHAT`. `CONTINUE_CURRENT_CHAT` requires one concrete Next Action. `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` + concrete persistence/recovery Next Action. `START_NEW_CHAT` may still carry a concrete Next Action when durable state makes fresh-chat continuation safe.

9. **Keep launchers aligned.** Text between these markers MUST remain byte-identical in ChatGPT and Claude launchers. This launcher never outranks local Root Governance.

10. **Mandatory response close.** Every response MUST end with these headings, in order, with nothing after the second section:

`### ทำอะไรไป?`
concise statement of what was done or determined

`### และถัดไปคืออะไร?`

`[Next Action]: <one exact next action or ไม่มีขั้นตอนถัดไป>`

`[Chat]: CONTINUE_CURRENT_CHAT | START_NEW_CHAT`

`[Reason]: <concise reason>`

`[Required Read]: <canonical locations or ไม่มี>`

Each bracketed field is a separate Markdown paragraph. Canonical lifecycle tokens are unescaped `CONTINUE_CURRENT_CHAT` and `START_NEW_CHAT`.
<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->