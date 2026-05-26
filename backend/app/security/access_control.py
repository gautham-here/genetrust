from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.security.jwt_handler import verify_token
from app.security.rbac import has_permission

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login", auto_error=False)


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username = verify_token(token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": username}


def get_optional_user(token: str = Depends(oauth2_scheme)) -> dict:
    if not token:
        return {"username": "anonymous", "role": "guest"}
    username = verify_token(token)
    if not username:
        return {"username": "anonymous", "role": "guest"}
    return {"username": username}