# Migrate UAAC 4.2 to 5.0

Status: **NON-NORMATIVE MIGRATION GUIDE**

UAAC 5.0 is a breaking architectural release. Migrate side-by-side and preserve the last effective 4.2 route until the 5.0 route is coherent.

## Preserve before change

Record the effective 4.2 release pin, launcher, Project identity/binding, Project rules, canonical documents and state, continuation, evidence, and rollback source. Historical 4.2 core resolves to release commit `5a309d8d38046bf3e8cd4beb2fc82a872f211cad`, package tree `3e62912bcbd88d91339dfa772dc6776ee95c77c5`.

## Side-by-side sequence

1. Vendor the exact 5.0 Markdown/YAML distribution beside 4.2.
2. Create the 5.0 adoption record and `governance/UAAC.md` without changing the active launcher.
3. Map actual 4.2 Project truth to direct 5.0 routes.
4. Verify the same material rules, sources, Current Truth, evidence, and sufficient continuation are recoverable.
5. Fresh-read the complete 5.0 route locally.
6. Switch the persistent launcher only after coherence is established.
7. Archive or supersede old machinery only under applicable Project authority.
8. Retain the old immutable pin and migration evidence for reconstruction.

## Mechanism mapping

| UAAC 4.2 mechanism | UAAC 5.0 treatment |
|---|---|
| Binding | `project.id` and `project.boundary` |
| Adoption | Minimal `UAAC-ADOPTION.yaml` |
| Kernel / boot procedure | Persistent launcher plus small Project router |
| Project Law / document registry | Direct locators to actual rules and sources |
| State map | Direct routes or optional high-assurance profile |
| Continuation index / lineage | Actual continuation route or optional assurance |
| Skill / capability / adapter machinery | Optional reusable-procedures or high-assurance profile |
| Claim records / receipts | Historical evidence or optional assurance |
| Wiki / retrieval substrate | Optional retrieval profile |
| Installation validation | Historical migration evidence, never constitutional authority |

## Qualified rollback

Rollback is not universally state-transform-free. Before v5-only material work, reverting launcher and adoption may be sufficient when state is still 4.2-compatible.

After material work under 5.0:

1. assess compatibility with the old 4.2 readers and rules;
2. identify state changed under 5.0;
3. verify 4.2 can resolve it;
4. remap incompatible state when necessary;
5. preserve evidence and history; and
6. only then revert launcher and adoption.

Rollback must not silently lose, stale, or reinterpret Project state.
