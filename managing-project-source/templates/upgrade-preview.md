# Upgrade Preview

Standard structure for preparing an initialized-Project Framework upgrade. Fill from observed current state and the selected target; never invent values. This template is executable documentation, not normative authority — Core Governance and the latest amendment win on conflict.

## 1. Identity

```text
Current local pin (FRAMEWORK-001): <version / amendment pointer>
Target release:                    <version>
Target tree SHA:                   <observed SHA or UNKNOWN>
Classification:                    FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
```

## 2. Comparison result

```text
[Project Upgrade] report: UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED
Migration notes for target: <pointer or "none exist">
```

## 3. Affected surfaces

List only surfaces the target actually touches — draw from `MIGRATION-NOTES.md` when present:

```text
<surface> : <change summary>
```

## 4. Preservation checklist

Every item must be `PRESERVED` with evidence before mutation approval:

```text
[ ] current truth documents        [ ] Project-specific rules
[ ] Stable IDs                     [ ] bindings (repo/Drive/local/storage)
[ ] history / provenance           [ ] approval & rollback records
```

## 5. Rollback plan

```text
Reversal mechanism: <e.g. git branch/tag of pre-upgrade pin state>
Verification after rollback: <minimum sufficient check>
```

## 6. Verification plan

```text
FAST_PATH: proportional resulting-state confirmation if target tree SHA matches committed evidence; else one full verification.
ASSESSED_PATH / MAJOR_MIGRATION_REQUIRED: affected checks + one final RELEASE_FULL on unchanged candidate.
```

## 7. Approvals

```text
Upgrade preparation approved by: <user, date>
Mutation approval:               <separate explicit approval, date>
Outcome recorded in:             16 Migration Registry (MIG-*)
```
