# CONST-022 — Version, amendment, migration, rollback, and identity

## Constitutional requirements

- A constitutional amendment must produce a distinguishable version and preserve the authority and provenance of the change.
- Adoption and migration must identify the exact content being adopted through a source-appropriate immutable or verifiable identity.
- No particular identity or integrity mechanism is universally mandatory; the mechanism must be appropriate to the source system and consequence.
- A migration must preserve material Project truth, authority, history, and a truthful account of compatibility.
- Rollback must be qualified by changes made under the newer version and must not silently lose or misinterpret state.

## Compliance

Change is compliant when version identity, amendment authority, migration effects, and rollback limits are sufficiently verifiable for the adopting Project.

## Non-prescription

Git identities, content digests, signed revisions, immutable object IDs, or equivalent mechanisms may be used. UAAC requires none of them universally and does not require repeated runtime hashing.
