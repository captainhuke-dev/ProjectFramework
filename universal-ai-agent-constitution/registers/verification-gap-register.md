# Verification Gap Register — UAAC v4.2.0

```yaml
document_type: VERIFICATION_GAP_REGISTER
constitution_id: UAAC-001
constitution_version: "4.2.0"
policy: KEEP_REQUIREMENT_AND_REGISTER_BEST_AVAILABLE_CHECK
```

A scenario proves behavior in a constructed case, not universal behavior. The following gaps remain visible:

| ID | Law | Gap | Best available check |
|---|---|---|---|
| R-01 | CONST-003 | self-interested authority widening can resemble ordinary advice | independent human review of authority-scope proposals |
| R-02 | CONST-005/008 | ordinary work cannot prove what the agent actually read | source locator + coverage receipt + spot audit |
| R-03 | CONST-012 | artifact order cannot prove reasoning order | separate earlier countercase artifact for high-risk work |
| R-04 | CONST-012 | credibility of countercase needs domain judgment | qualified human/independent reviewer |
| R-05 | CONST-013 | semantic drift can evade string comparison | claim-level semantic review |
| R-06 | CONST-013 | selective omission can change apparent balance | authorized selection criteria and human review |
| R-07 | CONST-025 | silence about a mandatory check can resemble a clean result | unconditional check receipt |
| R-08 | CONST-024 | stale memory may be correct by coincidence | provenance, quarantine workflow, sampled audits |
| R-09 | CONST-018 | false blocks are context-dependent | observe false-block rate and review causes |
| R-10 | CONST-015/021 | static convergence receipts do not prove every future Agent session will resolve the same state | rerun convergence after governance/agent/access changes and sample runtime boots |
| R-11 | CONST-014 | distributed continuation stores can fail between pointer and effect writes | transactional store where available, effect receipts, reconciliation and chaos tests |
| R-12 | CONST-021/023 | semantic mapping cannot prove that a PRD/procedure is substantively adequate | Project-qualified review and behavioral task tests |

| R-13 | CONST-002/021 | filesystem identity cannot universally prove human-intended Project boundary | explicit binding receipt, origin/root comparison, human review for rebind |
| R-14 | CONST-015 | matching remote identity at install time cannot guarantee future connector access | runtime access sampling and revalidation after connector/policy changes |
| R-15 | CONST-023 | adapter invocation evidence is platform-specific and may be incomplete | platform behavioral tests and Boot receipt sampling |
| R-16 | CONST-014/016 | distributed pre-write checks cannot make non-transactional external effects atomic | idempotency keys, effect receipts, reconciliation/compensation |

A gap does not authorize weakening. At each release, review whether a new mechanism converts the gap into an inspectable requirement.

<!-- END_OF_DOCUMENT: Verification Gap Register v4.2.0 -->
