from fastapi import APIRouter

router = APIRouter(tags=["Permissions"])


@router.get("/permissions")
def permissions():

    return {
        "roles": [
            "admin",
            "researcher",
            "security_analyst",
            "patient"
        ]
    }