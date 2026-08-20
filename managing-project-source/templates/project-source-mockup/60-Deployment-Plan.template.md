---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<DEPLOYMENT_PLAN_DOCUMENT_ID>"
document_type: "DEPLOYMENT_PLAN"
semantic_slot: "60"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 60 — Deployment Plan

> **CONDITIONAL:** Create when installation/deployment/operation is part of Project scope.

## Deployment Scope
<SCOPE>

## Deployment Support
`<SOURCE_ONLY | DOCKER_ONLY | SOURCE_AND_DOCKER | NOT_APPLICABLE>`

## Common Prerequisites
<OS_PLATFORM_ARCH_RUNTIME_EXTERNAL_SERVICES_PERMISSIONS>

## Configuration / Secret References
<CONFIG_AND_SECRET_REFS>

## Source Installation View
<ACQUISITION_RUNTIME_DEPENDENCIES_CONFIG_DATA_INIT_START_STOP_VERIFY_UPGRADE_ROLLBACK_CLEANUP>

## Docker Installation View
<CONTAINER_RUNTIME_IMAGE_RESPONSIBILITY_CONFIG_SECRETS_VOLUME_NETWORK_PORTS_ORDER_START_STOP_HEALTH_LOGS_UPGRADE_ROLLBACK_BACKUP_CLEANUP>

## Verification / Health
<RESULTING_STATE_CHECKS>

## Logs / Diagnostics
<LOGS_AND_DIAGNOSTICS>

## Upgrade
<UPGRADE_CONTRACT>

## Rollback
<ROLLBACK_CONTRACT>

## Backup / Restore
<BACKUP_RESTORE_CONTRACT>

## Uninstall / Cleanup
<CLEANUP>

## Troubleshooting
<TROUBLESHOOTING>

## Known Limitations / Deployment Mode Variance
<VARIANCES>

## Related
<REQ / DEC / RISK / DEP / CR / GATE / EVD>

Concrete commands/paths belong here only when they are verified Project truth; templates/synthetic examples must not invent executable commands.
