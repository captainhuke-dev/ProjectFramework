# Project Source Framework Governance Amendment

```yaml
amendment_status: USER_APPROVED
approved_at: 2026-08-14T08:08:00+07:00
supersedes_term: "00-Project Source Rule"
canonical_term: "00-Project Source Framework"
framework_document_id: "FRAMEWORK-001"
framework_version: "1.1.0"
```

## Binding Amendment

1. Every Project MUST retain an active `00-Project Source Framework` in `Project-Source/`.
2. `FRAMEWORK-001` is the non-removable Root Governance object and highest governance layer inside Project Source.
3. Every governed artifact created after the Framework inherits from it. Markdown descendants declare `inherits_from: ["FRAMEWORK-001"]`; non-Markdown artifacts inherit via their canonical Registry/Manifest entry.
4. Descendant governance, including Project-Specific Rules, may extend/specialize/add constraints but MUST NOT weaken, contradict, bypass, demote, delete, or replace Framework invariants.
5. A Root invariant can change only by revising the Framework itself with explicit user approval. The stable identity remains `FRAMEWORK-001`; the previous revision is superseded and archived, never erased.
6. A Project Source with no active Framework is `INVALID + NOT_OPERATIONALLY_READY`.
7. All new Project Source templates, documentation, handoffs, decisions, requirements, migrations, exports, and future governance additions must be interpreted as descendants of this Framework.

## Compatibility

Prior references to `00-Project Source Rule` are historical terminology. For new work, the canonical name is `00-Project Source Framework`. The approved design specification remains historical rationale; this amendment takes precedence where terminology or prior child-over-core precedence conflicts with the Root Framework model.
