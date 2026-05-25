from fastapi import APIRouter, HTTPException
from app.security.jwt_handler import create_access_token

router = APIRouter(tags=["Auth"])


FAKE_USERS = {
    "admin": "admin123",
    "researcher": "research123"
}


@router.post("/auth/login")
def login(payload: dict):

    username = payload.get("username")
    password = payload.get("password")

    if username not in FAKE_USERS:
        raise HTTPException(status_code=401, detail="Invalid user")

    if FAKE_USERS[username] != password:
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({"sub": username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }