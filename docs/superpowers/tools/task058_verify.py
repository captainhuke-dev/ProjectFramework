from pathlib import Path
import re, subprocess, sys

ROOT = Path('.')
BASE = 'f81992064d49c1f50f80c790667ec5be9b9ada0f'
checks = []

def ok(name, cond, detail=''):
    checks.append((name, bool(cond), detail))

def text(path):
    return (ROOT/path).read_text(encoding='utf-8')

def has_all(s, vals):
    return all(v in s for v in vals)

# Pressure scenarios
p = text('Framework-Source/tests/pressure-scenarios.md')
nums = [int(x) for x in re.findall(r'^## Scenario (\d+)\b', p, re.M)]
ok('scenario_continuity_1_602', nums == list(range(1,603)) and len(set(nums)) == 602, f'count={len(nums)} last={nums[-1] if nums else None}')
ok('staging_pressure_removed', not Path('Framework-Source/tests/task058-pressure-scenarios-staging.md').exists())
for n in range(557,603):
    m = re.search(rf'^## Scenario {n}\b(.*?)(?=^## Scenario \d+\b|\Z)', p, re.M|re.S)
    ok(f'scenario_{n}_shape', bool(m) and has_all(m.group(1), ['**Prompt:**','**Temptation:**','**Pass:**','**Fail:**','**GREEN expectation:**']))

core = text('Framework-Source/references/core-governance-rules.md')
amend = text('Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md')
combined = core + '\n' + amend
required = [
 'runtime_generation','fence_epoch','state_version','Runtime Event Journal > Checkpoint / Snapshot',
 'Effect-Surface Closure','MEDIATED_BY_EFFECT_GATEWAY','Effect Permit','PERMIT_ACTIVE','PERMIT_CONSUMED',
 'PRECONDITION_CONFLICT','IDEMPOTENT','CONDITIONALLY_IDEMPOTENT','NON_IDEMPOTENT','MANUAL_RESOLUTION_REQUIRED',
 'RESULT_VERIFICATION_REQUIRED','CANDIDATE_COMPLETE','AUTH_GRANTED','LEASE_ACQUIRED','FENCE_ADVANCED','PERMIT_ISSUED',
 'max_recursion_depth','PARTIALLY_COMPENSATED','event_schema_version','BACKWARD_COMPATIBLE','REQUIRES_MIGRATION','INCOMPATIBLE',
 'Cancellation != rollback','Compensation != rollback','Exactly-once execution is not assumed','Fail closed != retry forever']
for token in required:
    ok('token_'+re.sub(r'\W+','_',token).strip('_')[:45], token in combined, token)
ok('canonical_task_lifecycle_preserved', 'TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED' in core)
for s in ['PROPOSED','READY_FOR_CLAIM','CLAIMED','EXECUTING','RESULT_RECORDED','VERIFYING','VERIFIED','INTEGRATION_PENDING','INTEGRATED','CLOSED']:
    ok('task057_exec_state_'+s, s in core)
ok('multica_boundary', has_all(combined, ['Multica claim','runtime lease','runtime fence','Effect Permit','AUTH']))
ok('task_record_journal_separation', 'Task Record' in amend and 'Runtime Event Journal' in amend and 'unbounded' in text('Framework-Source/templates/project-execution/task-record.md'))
ok('no_exactly_once_claim', 'MUST NOT claim arbitrary exactly-once' in amend or 'does not claim universal exactly-once' in core)

# New starters
new_starters = ['runtime-contract.md','execution-attempt.md','execution-checkpoint.md','action-journal.md','effect-policy.md']
for f in new_starters:
    path = Path('Framework-Source/templates/project-execution')/f
    ok('starter_exists_'+f, path.exists())
starter_blob = '\n'.join(text(Path('Framework-Source/templates/project-execution')/f) for f in new_starters)
for token in ['runtime_generation','fence_epoch','Runtime Event Journal','Effect Permit','PRECONDITION_CONFLICT','IDEMPOTENT','COMPENSATABLE','max_recursion_depth']:
    ok('starter_token_'+re.sub(r'\W+','_',token), token in starter_blob, token)

# Existing execution surfaces
existing = ['README.md','task-contract.md','task-record.md','executor-profile.md','tools.md','trust.md']
for f in existing:
    ok('existing_surface_'+f, (Path('Framework-Source/templates/project-execution')/f).exists())
tools = text('Framework-Source/templates/project-execution/tools.md')
ok('task048_checkpoint_failback_preserved', 'CHECKPOINT_FAILBACK' in tools)
ok('task048_unknown_result_preserved', 'RESULT_VERIFICATION_REQUIRED' in tools)
ok('task048_ordered_fallback_preserved', 'ORDERED_ALLOW_LIST' in tools and 'fallback_order' in tools)
trust = text('Framework-Source/templates/project-execution/trust.md')
ok('trust_authority_separation', 'Trust classification ≠ Authority' in trust)
ok('trust_raw_secrets_forbidden', 'Actual secret values MUST NOT be stored here' in trust)
exec_readme = text('Framework-Source/templates/project-execution/README.md')
for f in new_starters:
    ok('exec_readme_lists_'+f, f in exec_readme)

# Release and propagation
release = text('Framework-Source/FRAMEWORK-RELEASE.yaml')
ok('release_1_20', 'framework_version: "1.20.0"' in release)
ok('schema_1_0', 'schema_version: "1.0.0"' in release)
ok('release_format_3', 'release_format_version: 3' in release)
ok('latest_amendment_task058', 'framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md' in release)
mig = text('Framework-Source/MIGRATION-NOTES.md')
ok('migration_current_119_120', '## 1.19.0 → 1.20.0 (current)' in mig)
ok('migration_prev_118_119', '## 1.18.0 → 1.19.0 (previous)' in mig)
skill = text('Framework-Source/SKILL.md')
ok('skill_current_1_20', 'Current distribution: **Framework 1.20.0 / Schema 1.0.0**.' in skill)
ok('skill_latest_task058', 'latest amendment: TASK-058' in skill)
readme = text('README.md')
ok('readme_current_1_20', 'Project Source Framework: **1.20.0**' in readme)
ok('readme_task058_section', '## Framework 1.20.0 Deterministic Execution Runtime Contract' in readme)
root = text('Framework-Source/templates/00-project-source-framework.md')
skel = text('Framework-Source/templates/core-document-skeletons.md')
ok('root_stamp_1_20', 'project_source_framework_version: "1.20.0"' in root)
ok('root_task058_semantics', 'Framework 1.20 Deterministic Execution Runtime Contract' in root)
ok('skeleton_stamp_1_20', 'project_source_framework_version: "1.20.0"' in skel)
ok('skeleton_task058_semantics', 'Framework 1.20.0 Deterministic Execution Runtime Contract Semantics' in skel)
mockups = sorted(Path('Framework-Source/templates/project-source-mockup').glob('*.template.md'))
ok('mockup_count_22', len(mockups)==22, str(len(mockups)))
for f in mockups:
    t=f.read_text(encoding='utf-8')
    ok('mockup_stamp_'+f.name, t.count('project_source_framework_version: "1.20.0"')==1 and 'project_source_framework_version: "1.19.0"' not in t)
mockread = text('Framework-Source/templates/project-source-mockup/README.md')
ok('mockup_readme_current_1_20', 'for **Framework 1.20.0 / Schema 1.0.0**' in mockread)

# Approval/task lifecycle consistency
spec = text('docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md')
plan = text('docs/superpowers/plans/2026-09-16-task058-deterministic-execution-runtime-contract.md')
tasks = text('docs/superpowers/PROJECT-TASKS.md')
task58 = tasks[tasks.index('## Task #58 —'):]
ok('spec_approved', 'WRITTEN_SPEC_APPROVED' in spec)
ok('plan_self_reviewed', 'IMPLEMENTATION_PLAN = WRITTEN / SELF_REVIEWED' in plan)
ok('task58_in_progress', '- **Status:** `IN_PROGRESS`' in task58)
ok('backlog_count_consistent', 'Current backlog: `TODO=0 / IN_PROGRESS=1 / BLOCKED=0` (TASK-058 IN_PROGRESS).' in tasks)

# Diff scope / preservation
subprocess.run(['git','diff','--check',BASE+'..HEAD'], check=True)
names = subprocess.check_output(['git','diff','--name-only',BASE+'..HEAD'], text=True).splitlines()
ok('no_project_source_self_host_mutation', not any(n.startswith('Project-Source/') or n=='PROJECT-BOOTSTRAP.md' for n in names), str([n for n in names if n.startswith('Project-Source/') or n=='PROJECT-BOOTSTRAP.md']))
ok('launchers_unchanged', not any(n in {'Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md','Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md'} for n in names))
allowed = {'.md','.yaml'}
non_docs = [n for n in names if Path(n).suffix not in allowed]
ok('candidate_scope_docs_yaml_only', not non_docs, str(non_docs))
ok('no_temp_task058_helpers', not Path('.github/workflows/task058-consolidate.yml').exists() and not Path('docs/superpowers/tools/task058_patch.py').exists())

# Baseline current command names remain present in core, with no TASK-058 command introduced.
commands = ['[Project Status]','[Project Path]','[Project Upgrade]','[Project Audit]','[Session]','[Goal]','[Meeting]']
for c in commands:
    ok('command_preserved_'+re.sub(r'\W+','_',c), c in core)
ok('no_new_runtime_command', '[Runtime]' not in core and '[ControlTower]' not in core)

passed=sum(1 for _,v,_ in checks if v)
failed=[(n,d) for n,v,d in checks if not v]
print(f'TASK058_STRUCTURAL {passed}/{len(checks)} PASS' if not failed else f'TASK058_STRUCTURAL {passed}/{len(checks)} FAIL')
for n,d in failed:
    print('FAIL',n,d)
if failed:
    sys.exit(1)
print(f'TASK058_AFFECTED {passed}/{len(checks)} PASS')
