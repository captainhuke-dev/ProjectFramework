# UAAC 4.2 Historical Reconstruction

Status: **HISTORICAL — NON-NORMATIVE — NOT A UAAC 5.0 DEPENDENCY**

UAAC 4.2 remains exactly reconstructible from repository Git objects. Current v5 paths must never be substituted for these identities.

## Immutable identities

```text
UAAC 4.2 release commit:
5a309d8d38046bf3e8cd4beb2fc82a872f211cad

UAAC 4.2 package tree:
3e62912bcbd88d91339dfa772dc6776ee95c77c5

Completed 27-file reference fixture commit:
5cc9488427c8034a67f4898ace5f1c5806760b85
```

The release commit reconstructs `universal-ai-agent-constitution/` exactly as published in 4.2. The fixture commit reconstructs `uaac-v4.2-reference-project/` after the recorded ChatGPT receiver observation. Branch names are historical provenance, not reconstruction identities.

## Classification

- The 4.2 Constitution and law files are historical normative core for Projects still pinned to 4.2.
- Old runbooks, schemas, validators, scenarios, threat/system analysis, registers, Skills, templates, and validation output are historical/developer material.
- `uaac-v4.2-reference-project/` is a historical test fixture with preserved evidence, not an active v5 installation.
- UAAC 5.0 does not depend on any historical artifact to operate.

## Safe retrieval

Use Git object lookup at the exact identities above. A mutable branch or current working-tree path is insufficient because `universal-ai-agent-constitution/` now contains v5.

Historical PASS, PARTIAL, and NOT_RUN values are claims from the original v4.2 evidence. They are not rewritten as v5 results and do not establish current platform behavior.

See `REFERENCE-INVENTORY.yaml` for the audited material categories and original path roots.
