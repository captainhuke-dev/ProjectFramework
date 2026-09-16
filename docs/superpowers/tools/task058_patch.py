from pathlib import Path
import re

ROOT = Path('.')
OLD = 'project_source_framework_version: "1.19.0"'
NEW = 'project_source_framework_version: "1.20.0"'


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def write(path, text):
    (ROOT / path).write_text(text, encoding='utf-8', newline='\n')


def replace_once(path, old, new):
    text = read(path)
    count = text.count(old)
    assert count == 1, f'{path}: expected exactly 1 match for {old!r}, found {count}'
    write(path, text.replace(old, new, 1))


# 1) Canonical pressure suite: consolidate staged RED scenarios 557-602.
pressure_path = 'Framework-Source/tests/pressure-scenarios.md'
staging_path = ROOT / 'Framework-Source/tests/task058-pressure-scenarios-staging.md'
pressure = read(pressure_path)
staging = staging_path.read_text(encoding='utf-8')
assert '## Scenario 556 ' in pressure
assert '## Scenario 557 ' not in pressure
assert '## Scenario 557 ' in staging and '## Scenario 602 ' in staging
scenario_tail = staging[staging.index('## Scenario 557 '):].strip()
write(pressure_path, pressure.rstrip() + '\n\n' + scenario_tail + '\n')
staging_path.unlink()

# 2) Core Governance TASK-058 projection.
core_path = 'Framework-Source/references/core-governance-rules.md'
core = read(core_path)
marker = '## Framework 1.20.0 Deterministic Execution Runtime Contract (TASK-058)'
assert marker not in core
core_block = r'''

## Framework 1.20.0 Deterministic Execution Runtime Contract (TASK-058)

Framework `1.20.0` extends TASK-057 declarative PLAN/TASK/VERIFY governance with language-neutral deterministic runtime **contract semantics only**. It does not ship an AI-ControlTower runtime, scheduler, database, queue, worker daemon, Effect Gateway service, credential broker, RLM runtime, model/MCP router, CI/merge bot, or automatic Task-DONE updater.

Ownership remains separated:

```text
ProjectFramework = governance/protocol semantics
Project Source = canonical Project governance truth
Durable Task Source = canonical Task lifecycle truth
AUTH-* / explicit User authority = operation/mutation authority
R4_CTX = current truth from its owner
Multica = claim/coordination only
AI-ControlTower Runtime Store = execution-control facts only
Runtime Event Journal = canonical runtime observation inside the runtime domain
Checkpoint / Snapshot = derived recovery accelerator
Effect Gateway = mediated Material-Effect consequence boundary
Effect Permit = short-lived dispatch-eligibility proof, never AUTH
```

Core invariants:

```text
Runtime decision != Authority
Model proposal != Runtime decision
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
Task lifetime != model-turn/chat/MCP lifetime
Worker lifetime != Execution lifetime
Execution lifetime != canonical Task lifecycle
Runtime Event Journal > Checkpoint / Snapshot
ACKNOWLEDGED != resulting-state proof
Cancellation != rollback
Compensation != rollback
Exactly-once execution is not assumed
Fail closed != retry forever
```

Keep four lifecycle domains separate: canonical Task lifecycle; TASK-057 Operational Execution state; Execution Attempt state; Action/Effect state. Attempt loss/termination never directly closes Operational Execution or Task. Model `CANDIDATE_COMPLETE` is only a proposal for governed verification/completion evaluation.

A conforming runtime uses durable Execution/Attempt identity with pinned Task/Plan/Envelope fingerprints, `runtime_contract_version`, `event_schema_version`, `runtime_generation`, `fence_epoch`, and `state_version`. Material contract fingerprint changes invalidate continuation or require governed replanning/revalidation; runtime state transitions use compare-and-set or equivalent atomic semantics. Control identity is `(runtime_generation, fence_epoch)`; a new generation invalidates prior leases/fences/Effect Permits and requires unresolved-effect reconciliation before new dispatch.

For mediated Material Effects, every effect-capable route is `MEDIATED_BY_EFFECT_GATEWAY` or explicitly prohibited/confined. Policy-only instruction without enforceable Effect-Surface Closure is not sufficient conformance. The Effect Gateway fresh-checks current execution/attempt identity, generation/fence, Task/Plan/Envelope fingerprints, applicable AUTH, R4, tool/capability/trust eligibility, target identity/precondition, effect semantics, budget/retry policy, and Effect Permit immediately before dispatch as applicable.

Every Gateway-mediated Material Effect requires a short-lived JIT Effect Permit that is single-use, non-transferable, attempt/action/action-hash/target/tool/generation/fence/contract/envelope-bound. `PERMIT_ACTIVE -> PERMIT_CONSUMED` is atomic/CAS-equivalent; `PERMIT_CONSUMED != effect APPLIED`. Source-native target preconditions are mandatory when supported; mismatch yields `PRECONDITION_CONFLICT`. Unsupported preconditions are explicit and route to declared reconciliation/fail-closed handling rather than assumed freshness.

One Permit maps to one independently reconcilable Material Effect unless a verified source-native atomic transaction makes the group independently reconcilable as one unit. Effect policy classifies idempotency `IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN`, reconciliation strategy, and reversibility `REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN`. ProjectFramework does not claim universal exactly-once external execution.

TASK-057 `RESULT_VERIFICATION_REQUIRED` remains binding. Possibly-dispatched effects reconcile to `APPLIED | NOT_APPLIED | AMBIGUOUS`; `NON_IDEMPOTENT | UNKNOWN` plus no valid reconciliation path and ambiguous result becomes `MANUAL_RESOLUTION_REQUIRED`/blocking. Fallback tools never blind-replay an unresolved prior effect.

Executor/model proposal schema is separate from runtime-owned event schema. Allowed bounded reports include `ACTION_PROPOSAL | CANDIDATE_COMPLETE | WAIT_REQUEST | INPUT_REQUEST | YIELD | BLOCKED_REPORT | ERROR_REPORT`. Models cannot authoritatively emit `AUTH_GRANTED`, `LEASE_ACQUIRED`, `FENCE_ADVANCED`, `PERMIT_ISSUED`, `VERIFIED`, `INTEGRATED`, or `TASK_DONE`; unknown privileged fields fail closed.

Budgets are durable and hierarchical across model turns/restarts/children; `parent consumption + sum(child allocations) <= root budget`. Child recursion cannot manufacture authority or budget. Budget exhaustion is blocked/waiting truth, never Task DONE. Long waits use durable WAIT/wakeup semantics rather than unbounded model polling.

Cancellation blocks new governed dispatch but does not erase possibly-applied source-native facts. In-flight effects are reconciled. Compensation is a new governed effect with its own Action identity, AUTH check, Permit, budget, evidence, and reconciliation; `ROLLED_BACK` requires source-native proof of real atomic rollback.

Process/store recovery validates journal continuity, uses only compatible derived checkpoints, replays the journal tail, identifies lost Attempts, reconciles unresolved dispatch, invalidates stale generation/fence/permit state, fresh-resolves AUTH/R4/fingerprints, and schedules only safely runnable work. Missing journal continuity yields `RECOVERY_BLOCKED`; model/chat memory is not runtime truth. Active executions remain version-pinned as `BACKWARD_COMPATIBLE | REQUIRES_MIGRATION | INCOMPATIBLE` across runtime upgrades.

Runtime journals/checkpoints/evidence never store raw secret values merely for observability. Use minimum sufficient `REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata`. Tool/model output remains untrusted data and cannot create authority or bypass effect controls.

TASK-058 starter/profile surfaces under `Project-Execution/` remain optional/applicability-driven. Non-ControlTower Projects remain valid. No new Project Source semantic slot, Stable-ID family, Risk level, or Registered Command is introduced.
'''
write(core_path, core.rstrip() + core_block + '\n')

# 3) Migration notes: 1.19 -> 1.20 becomes current.
migration_path = 'Framework-Source/MIGRATION-NOTES.md'
migration = read(migration_path)
old_heading = '## 1.18.0 → 1.19.0 (current)'
assert migration.count(old_heading) == 1
migration = migration.replace(old_heading, '## 1.18.0 → 1.19.0 (previous)', 1)
insert_marker = '## 1.18.0 → 1.19.0 (previous)'
section = r'''## 1.19.0 → 1.20.0 (current)

### Affected distribution surfaces

- Framework identity becomes `1.20.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-058 Deterministic Execution Runtime Contract.
- TASK-057 PLAN/TASK/VERIFY, `R4_CTX`, Task Ready Gate, Operational Execution state, Expected/Actual IPOCV, Verification Record, Multica coordination-only ownership, exact-candidate verification, `INTEGRATION_GATE`, and canonical Task DONE ownership remain unchanged.
- TASK-058 adds declarative runtime-control semantics: separate Execution Attempt and Action/Effect domains, deterministic Supervisor, Runtime Event Journal > derived Checkpoint, lease/heartbeat/fence/control-generation semantics, atomic `state_version` transitions, Effect-Surface Closure, Effect Gateway, single-use JIT Effect Permit, source-native target preconditions, deterministic ambiguity/reconciliation, hierarchical budgets, typed Executor proposals, cancellation/compensation, recovery, and runtime/event-schema version pinning.
- Five optional Project-Execution starters are added: `runtime-contract.md`, `execution-attempt.md`, `execution-checkpoint.md`, `action-journal.md`, `effect-policy.md`.
- Existing `task-contract.md`, `task-record.md`, `executor-profile.md`, `tools.md`, `trust.md`, and Project-Execution README are aligned without transferring authority or turning Task Record into an event log.
- Adoption is additive/applicability-driven. Brownfield historical Tasks are not retrofitted. Non-ControlTower Projects remain valid.
- No new semantic slot, Stable-ID family, Registered Command, Risk level, schema version, or release-format version.
- No AI-ControlTower/Multica runtime, Python supervisor, runtime database, scheduler/queue/worker daemon, lease/fencing service, Effect Gateway service, credential broker, sandbox/network policy, model/MCP router, RLM runtime, API server, CI/merge/release bot, or automatic Task DONE updater is introduced.

### Upgrade checklist

1. Preserve local pin, Project truth, Stable IDs, Project-specific rules, bindings, history, authority, and canonical Task lifecycle until governed promotion.
2. Preserve `Claim ≠ Lease ≠ Fence ≠ Authority`, `Effect Permit ≠ AUTH`, `Verification PASS ≠ Task DONE`, and `Runtime Event Journal > Checkpoint / Snapshot`.
3. Adopt runtime/effect starters only when deterministic runtime integration is applicable; do not materialize them merely for completeness.
4. Preserve `RESULT_VERIFICATION_REQUIRED`; ambiguous non-idempotent effects are reconciled or manually resolved, never blind-retried.
5. Require Effect-Surface Closure for autonomous mediated Material Effects; a policy instruction alone is not enforcement.
6. Preserve exact TASK-048 Primary/fallback/`CHECKPOINT_FAILBACK` semantics and TASK-037/TASK-026 trust/disclosure/secret boundaries.
7. Verify scenarios `557–602` while preserving cumulative scenarios `1–602` contiguous/unique.
8. Run cumulative affected verification, independent review, then one final `RELEASE_FULL` on the exact unchanged candidate.

---

'''
migration = migration.replace(insert_marker, section + insert_marker, 1)
write(migration_path, migration)

# 4) Root README current release + 1.20 summary.
readme_path = 'README.md'
readme = read(readme_path)
assert readme.count('- Project Source Framework: **1.19.0**') == 1
readme = readme.replace('- Project Source Framework: **1.19.0**', '- Project Source Framework: **1.20.0**', 1)
readme_marker = '## Framework 1.19.0 AI-ControlTower Governance Support Layer'
assert readme.count(readme_marker) == 1
readme_section = r'''## Framework 1.20.0 Deterministic Execution Runtime Contract

Framework `1.20.0` adds a language-neutral deterministic **execution-runtime contract** on top of the Framework 1.19 declarative governance layer. ProjectFramework still ships no runtime. A future AI-ControlTower may own bounded execution-control facts while Project Source, Task Source, AUTH, Verification, Git/source-native truth, release/deployment truth, and Task DONE stay with their existing owners.

Key additions are separate Execution/Attempt/Action domains; Runtime Event Journal > derived Checkpoint; lease/heartbeat/fence/control-generation semantics; atomic state transitions; Effect-Surface Closure; Effect Gateway + single-use JIT Effect Permit; source-native target preconditions; deterministic ambiguous-result reconciliation without universal exactly-once claims; durable hierarchical budgets; typed model proposal vs runtime-event namespaces; cancellation/in-flight reconciliation; compensation as a new governed effect; restart/store-restore recovery; and runtime/event-schema version pinning.

Maintained optional starters now include `runtime-contract.md`, `execution-attempt.md`, `execution-checkpoint.md`, `action-journal.md`, and `effect-policy.md` under `Framework-Source/templates/project-execution/`, alongside the TASK-057 contracts. Non-ControlTower Projects remain valid; Brownfield historical Tasks are not retrofitted. No Python supervisor, scheduler, database, Effect Gateway service, credential broker, model/MCP router, RLM runtime, CI bot, or automatic Task-DONE service is introduced.

'''
readme = readme.replace(readme_marker, readme_section + readme_marker, 1)
write(readme_path, readme)

# 5) SKILL current routing/guidance.
skill_path = 'Framework-Source/SKILL.md'
skill = read(skill_path)
replace_from = 'Current distribution: **Framework 1.19.0 / Schema 1.0.0**.'
assert skill.count(replace_from) == 1
skill = skill.replace(replace_from, 'Current distribution: **Framework 1.20.0 / Schema 1.0.0**.', 1)
skill_marker = 'Framework `1.19.0` adds the declarative AI-ControlTower Governance Support Layer:'
assert skill.count(skill_marker) == 1
skill_para = ('Framework `1.20.0` adds deterministic execution-runtime contract semantics without shipping a runtime: '
              'Task/Operational Execution/Attempt/Action domains remain separate; Runtime Event Journal outranks derived Checkpoints; '
              'claim/lease/fence/AUTH remain distinct; mediated Material Effects require Effect-Surface Closure, fresh Effect Gateway validation, '
              'single-use JIT Effect Permit, source-native preconditions when supported, and deterministic reconciliation before retry. '
              'Typed model proposals cannot author runtime/governance state; budgets are durable/hierarchical; cancellation does not erase in-flight facts; '
              'compensation is a new governed effect. `Runtime decision ≠ Authority`; `Effect Permit ≠ AUTH`; `Verification PASS ≠ Task DONE`. '
              'No AI-ControlTower/Multica runtime, Python supervisor, scheduler, database, router, or automatic executor is introduced.\n\n')
skill = skill.replace(skill_marker, skill_para + skill_marker, 1)
ref_old = '- `references/framework-governance-amendment-260914-task057-ai-controltower-governance-support-layer.md` — latest amendment: TASK-057 AI-ControlTower Governance Support Layer'
assert skill.count(ref_old) == 1
ref_new = ('- `references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md` — latest amendment: TASK-058 Deterministic Execution Runtime Contract\n'
           '- `references/framework-governance-amendment-260914-task057-ai-controltower-governance-support-layer.md` — previous amendment: TASK-057 AI-ControlTower Governance Support Layer')
skill = skill.replace(ref_old, ref_new, 1)
write(skill_path, skill)

# 6) Framework root/skeleton/mockup maintained current representations.
root_template = 'Framework-Source/templates/00-project-source-framework.md'
replace_once(root_template, OLD, NEW)
root_text = read(root_template)
root_marker = '### 5.2 Concept-First Technical / Tooling Boundary'
assert root_text.count(root_marker) == 1
root_add = r'''### 5.1A Framework 1.20 Deterministic Execution Runtime Contract

When deterministic AI-ControlTower-compatible execution is applicable, use the optional `Project-Execution/` TASK-057/TASK-058 contracts after active Project authority resolves. Keep Task/Operational Execution/Attempt/Action truth separate. Runtime control facts never grant AUTH or Task DONE. Mediated Material Effects require enforceable Effect-Surface Closure plus current Gateway/Permit/precondition/reconciliation semantics. Runtime Event Journal outranks derived Checkpoint/Snapshot; ambiguous effects use verify-before-retry; cancellation does not erase source-native results; compensation is a new governed effect. No runtime service is materialized by this root template merely because the contract exists.

'''
root_text = root_text.replace(root_marker, root_add + root_marker, 1)
write(root_template, root_text)

skeleton_path = 'Framework-Source/templates/core-document-skeletons.md'
skeleton = read(skeleton_path)
assert OLD in skeleton
skeleton = skeleton.replace(OLD, NEW)
skel_marker = '## Framework 1.19.0 AI-ControlTower Governance Support Layer Semantics'
assert skeleton.count(skel_marker) == 1
skel_add = r'''## Framework 1.20.0 Deterministic Execution Runtime Contract Semantics

Framework `1.20.0` preserves Schema `1.0.0` and TASK-057 ownership while adding optional deterministic runtime-control contracts. Task/Operational Execution/Attempt/Action remain separate; Runtime Event Journal outranks derived Checkpoint; claim/lease/fence/AUTH remain distinct; mediated Material Effects require Effect-Surface Closure, JIT single-use Effect Permit, precondition/reconciliation policy, and no blind retry. Typed model proposals cannot author runtime-owned state; budgets are hierarchical; cancellation and compensation preserve source-native truth. No runtime implementation, new semantic slot, Stable-ID family, Risk level, or Registered Command is introduced.

'''
skeleton = skeleton.replace(skel_marker, skel_add + skel_marker, 1)
write(skeleton_path, skeleton)

mockup_dir = ROOT / 'Framework-Source/templates/project-source-mockup'
mockups = sorted(mockup_dir.glob('*.template.md'))
assert len(mockups) == 22, f'expected 22 maintained mockups, got {len(mockups)}: {[p.name for p in mockups]}'
for p in mockups:
    text = p.read_text(encoding='utf-8')
    count = text.count(OLD)
    assert count == 1, f'{p}: expected one 1.19 stamp, got {count}'
    p.write_text(text.replace(OLD, NEW, 1), encoding='utf-8', newline='\n')
mockup_readme_path = 'Framework-Source/templates/project-source-mockup/README.md'
mockup_readme = read(mockup_readme_path)
old_intro = 'for **Framework 1.18.0 / Schema 1.0.0**.'
assert mockup_readme.count(old_intro) == 1
mockup_readme = mockup_readme.replace(old_intro, 'for **Framework 1.20.0 / Schema 1.0.0**.', 1)
mockup_marker = '## Framework 1.18.0 Project Upgrade One-Session Fast Path Semantics'
assert mockup_readme.count(mockup_marker) == 1
mockup_add = r'''## Framework 1.20.0 Deterministic Execution Runtime Contract Semantics

Framework `1.20.0` keeps Schema `1.0.0` and adds optional deterministic runtime/effect contract starters under `Project-Execution/`. Runtime control never becomes Project/Task/AUTH/Verification authority; Runtime Event Journal > Checkpoint; mediated effects require Effect-Surface Closure, Gateway + single-use Permit, precondition/reconciliation semantics, bounded budgets, and truthful cancellation/compensation recovery. This mockup remains Project Source documentation only and materializes no runtime service.

## Framework 1.19.0 AI-ControlTower Governance Support Layer Semantics

Framework `1.19.0` adds optional declarative PLAN/TASK/VERIFY execution contracts, Expected/Actual IPOCV, state-bound verification, Task Ready Gate, Operational Execution state, Multica coordination-only semantics, Executor/Profile/Adapter selection, and exact-candidate integration reconciliation without adding a runtime or changing canonical Task lifecycle.

'''
mockup_readme = mockup_readme.replace(mockup_marker, mockup_add + mockup_marker, 1)
write(mockup_readme_path, mockup_readme)

# 7) Persist approval/execution truth in spec + Task ledger.
spec_path = 'docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md'
spec = read(spec_path)
spec = spec.replace('Design state: `DESIGN_V3_USER_APPROVED / FROZEN / WRITTEN_SPEC_PENDING_EXPLICIT_REVIEW`',
                    'Design state: `DESIGN_V3_USER_APPROVED / FROZEN / WRITTEN_SPEC_APPROVED`', 1)
head = '## 35. Written-spec approval gate'
assert head in spec
pre = spec.split(head, 1)[0]
new_tail = r'''## 35. Written-spec approval and execution gate

ACTOR-001 explicitly approved this Written Spec on `2026-09-16`. The TASK-058 implementation plan was then written/self-reviewed and execution was explicitly authorized on `2026-09-16`.

Current governed state during implementation:

```text
TASK-058 = IN_PROGRESS
WRITTEN_SPEC = APPROVED
IMPLEMENTATION_PLAN = WRITTEN / SELF_REVIEWED
EXECUTION = AUTHORIZED / IN_PROGRESS
AI_CONTROLTOWER_RUNTIME_IMPLEMENTATION = NOT AUTHORIZED_BY_TASK058
```

Execution still follows TASK-057 Planner/Execution Handoff semantics: current Task/Plan/Envelope, AUTH, `R4_CTX`, Ready Gate, tool/capability/trust/executor eligibility, workspace/target truth, and independent Verifier requirements remain binding. Planning/execution authorization does not authorize merge, tag/GitHub Release, consuming-Project upgrade, self-host promotion, or AI-ControlTower runtime mutation.
'''
write(spec_path, pre + new_tail + '\n')

tasks_path = 'docs/superpowers/PROJECT-TASKS.md'
tasks = read(tasks_path)
start = tasks.index('## Task #58 — ProjectFramework 1.20 Deterministic Execution Runtime Contract')
block = tasks[start:]
assert block.count('- **Status:** `TODO`') == 1
block = block.replace('- **Status:** `TODO`', '- **Status:** `IN_PROGRESS`', 1)
block = block.replace('- **readiness:** `DESIGN_V3_FROZEN / WRITTEN_SPEC_PENDING_EXPLICIT_REVIEW / IMPLEMENTATION_NOT_STARTED`',
                      '- **readiness:** `WRITTEN_SPEC_APPROVED / IMPLEMENTATION_PLAN_SELF_REVIEWED / EXECUTION_IN_PROGRESS / CANDIDATE_NOT_FROZEN`', 1)
block = block.replace('- **Design State:** `DESIGN_V3_USER_APPROVED / FROZEN / WRITTEN_SPEC_PENDING_EXPLICIT_REVIEW`.',
                      '- **Design State:** `DESIGN_V3_USER_APPROVED / FROZEN / WRITTEN_SPEC_APPROVED`.', 1)
plan_line = '- **Implementation Plan:** `docs/superpowers/plans/2026-09-16-task058-deterministic-execution-runtime-contract.md`.\n- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTION_AUTHORIZED`.\n'
insert_after = '- **Design State:** `DESIGN_V3_USER_APPROVED / FROZEN / WRITTEN_SPEC_APPROVED`.\n'
assert insert_after in block
block = block.replace(insert_after, insert_after + plan_line, 1)
old_next = '- **Exact Next Step:** ACTOR-001 reviews and explicitly approves the written spec; only after that gate may the TASK-058 implementation plan be written. No implementation/runtime work starts before written-spec approval.'
assert old_next in block
block = block.replace(old_next, '- **Exact Next Step:** Complete canonical Framework 1.20 propagation/verification on `task058-framework120`; then independent review → candidate freeze → one final `RELEASE_FULL`. AI-ControlTower runtime remains out of scope.', 1)
write(tasks_path, tasks[:start] + block)

# 8) Record that the prior tooling blocker was resolved through an ephemeral branch-only patch executor.
checkpoint_path = 'docs/superpowers/evidence/2026-09-16-task058-execution-checkpoint.md'
checkpoint = read(checkpoint_path)
resume_note = r'''

## 9. Resume — bounded patch capability restored

Execution resumed after the prior checkpoint using an ephemeral branch-only GitHub Actions helper whose sole purpose was to apply exact bounded text patches to large Markdown surfaces inside a real repository checkout. The helper is not a Framework runtime/CI feature, is removed before candidate review, and grants no Project authority. This resume operation consolidated scenarios `557–602` into the canonical pressure suite, projected TASK-058 into Core/current guidance/migration/templates, and advanced durable Task truth to `IN_PROGRESS`. Candidate freeze still requires Structural GREEN, AFFECTED, independent review, and final release verification.
'''
assert '## 9. Resume — bounded patch capability restored' not in checkpoint
write(checkpoint_path, checkpoint.rstrip() + resume_note + '\n')

# 9) Structural checks for the consolidation batch.
pressure = read(pressure_path)
nums = [int(x) for x in re.findall(r'^## Scenario (\d+)\b', pressure, re.M)]
assert nums == list(range(1, 603)), (len(nums), nums[-10:])
assert len(nums) == len(set(nums)) == 602
for token in ['runtime_generation', 'Effect Permit', 'Runtime Event Journal', 'MEDIATED_BY_EFFECT_GATEWAY',
              'PERMIT_CONSUMED', 'PRECONDITION_CONFLICT', 'MANUAL_RESOLUTION_REQUIRED', 'state_version',
              'CANDIDATE_COMPLETE', 'max_recursion_depth', 'PARTIALLY_COMPENSATED', 'event_schema_version']:
    combined = read(core_path) + '\n' + read('Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md')
    assert token in combined, token
release = read('Framework-Source/FRAMEWORK-RELEASE.yaml')
assert 'framework_version: "1.20.0"' in release
assert 'schema_version: "1.0.0"' in release
assert 'release_format_version: 3' in release
assert 'framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md' in release
assert 'Framework 1.20.0 / Schema 1.0.0' in read(skill_path)
assert 'Project Source Framework: **1.20.0**' in read(readme_path)
assert staging_path.exists() is False
for p in mockups:
    text = p.read_text(encoding='utf-8')
    assert OLD not in text and NEW in text, p
assert OLD not in read(root_template) and NEW in read(root_template)
assert OLD not in read(skeleton_path) and NEW in read(skeleton_path)
assert '- **Status:** `IN_PROGRESS`' in read(tasks_path)[start:]
assert 'WRITTEN_SPEC_APPROVED' in read(spec_path)
print('TASK058_CONSOLIDATION_STRUCTURAL PASS')
