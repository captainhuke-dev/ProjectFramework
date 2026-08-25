# TASK-019 Simpler User-Facing Language — RELEASE_FULL Evidence

Captured: `2026-08-25` (session time Asia/Bangkok)

Branch: `task-019-simpler-language`
Base: `main` at `cde4e2e7fcff6f9f9e19db7795fb3269ef1c310a`

## Scope implemented

1. **Launchers** (`CHATGPT-PROJECT-INSTRUCTIONS.md`, `CLAUDE-PROJECT-INSTRUCTIONS.md`): shared-contract body rewritten in plain language. All canonical tokens preserved verbatim; both launchers restored to ceiling compliance at **4,481** Unicode characters each (previously 4,737/4,732 — over the `<=4,500` limit). Marker bodies remain byte-identical.
2. **README.md**: new plain-language TL;DR section ("What this is and how to use it") ahead of the existing canonical content, which is unchanged.
3. **SKILL.md Required References**: every reference now carries a one-line purpose note; list order and requirement status unchanged (latest amendment remains first required read).
4. **Pressure scenarios 151–152** appended: plain language never renames canonical tokens; launcher ceiling compliance.

Out of scope (unchanged): `core-governance-rules.md`, historical amendments, templates, tests other than scenario additions.

## Commits

- `3754476` — docs: simplify launcher contract language within ceiling (TASK-019)
- `69fbcc3` — docs: plain-language TL;DR and annotated required references (TASK-019)
- `8c6c08d` — test: add plain language and launcher ceiling pressure scenarios

## Verification results

Affected verification on the candidate: `AFFECTED VERIFICATION PASS 10/10`

RELEASE_FULL after the candidate stopped changing: `RELEASE_FULL PASS 24/24`

Checks covered: release identity F`1.3.1`/S`1.0.0`/format 3; latest-amendment pointer; SKILL first-amendment alignment with descriptor; registered commands across core governance/SKILL/both launchers; comparison vocabulary; yes ≠ mutation approval; Direct-to-Latest path classes; response-close fields; reserved slots `18–19`; slot `91` ownership; historical amendments untouched; launcher lengths ≤4,500 both; marker bodies byte-identical; scenarios 136–152 exactly once each; new scenarios normatively supported; no executable artifacts added; `git diff --check` clean; clean worktree.

Candidate HEAD after evidence commit is recorded below in the completion checkpoint. `commit ≠ push` remains binding; no push performed by this task.

`INTEGRATION_GATE: NOT_APPLICABLE` — no branch/worktree integration performed in this execution.
