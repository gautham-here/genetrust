from typing import Dict, Set

ROLE_PERMISSIONS: Dict[str, Set[str]] = {
    "admin": {
        "upload_genome",
        "view_genomes",
        "delete_genome",
        "view_audit_logs",
        "view_threats",
        "manage_users",
        "manage_organizations",
        "run_ai_analysis",
        "view_permissions",
    },
    "researcher": {
        "upload_genome",
        "view_genomes",
        "run_ai_analysis",
        "view_threats",
    },
    "security_analyst": {
        "view_genomes",
        "view_audit_logs",
        "view_threats",
        "run_ai_analysis",
    },
    "patient": {
        "view_genomes",
    },
}


def has_permission(role: str, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())


def get_role_permissions(role: str) -> Set[str]:
    return ROLE_PERMISSIONS.get(role, set())