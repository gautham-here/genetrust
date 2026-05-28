from typing import Dict


def evaluate_abac_access(
    user: Dict,
    resource: Dict,
    action: str,
) -> bool:

    role = user.get("role")

    user_id = user.get("user_id")

    organization_id = user.get(
        "organization_id"
    )

    # =====================================================
    # ADMIN
    # =====================================================

    if role == "admin":
        return True

    # =====================================================
    # PATIENT
    # =====================================================

    if role == "patient":

        return (
            resource.get("owner_id")
            == user_id
        )

    # =====================================================
    # RESEARCHER
    # =====================================================

    if role == "researcher":

        return (

            resource.get(
                "organization_id"
            )

            ==

            organization_id
        )

    # =====================================================
    # SECURITY ANALYST
    # =====================================================

    if role == "security_analyst":

        return (

            resource.get(
                "organization_id"
            )

            ==

            organization_id
        )

    return False