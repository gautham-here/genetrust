from fastapi import (

    Depends,
    HTTPException,
    status,
)

from fastapi.security import (
    OAuth2PasswordBearer
)

from app.security.jwt_handler import (
    decode_access_token
)

from app.security.rbac import (
    has_permission
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(
        oauth2_scheme
    )
):

    payload = decode_access_token(
        token
    )

    if not payload:

        raise HTTPException(

            status_code=
                status.HTTP_401_UNAUTHORIZED,

            detail="Invalid token."
        )

    return payload


def require_permission(
    permission: str
):

    def checker(
        user=Depends(
            get_current_user
        )
    ):

        role = user.get("role")

        if not has_permission(
            role,
            permission
        ):

            raise HTTPException(

                status_code=
                    status.HTTP_403_FORBIDDEN,

                detail=(
                    "Insufficient permissions."
                )
            )

        return user

    return checker