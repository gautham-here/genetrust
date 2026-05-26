from fastapi import APIRouter
from app.security.rbac import ROLE_PERMISSIONS
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)


@router.get("/permissions")
def get_permissions():
    return {
        "success": True,
        "data": {
            "roles": list(ROLE_PERMISSIONS.keys()),
            "role_permissions": {role: list(perms) for role, perms in ROLE_PERMISSIONS.items()},
        },
        "message": "Permissions retrieved.",
    }