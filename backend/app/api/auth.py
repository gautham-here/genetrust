from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.auth_service import authenticate_user, create_user_token, register_user
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)


class LoginPayload(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str


class RegisterPayload(BaseModel):
    username: str
    email: str
    password: str
    full_name: str
    role: str = "researcher"


@router.post("/auth/login")
def login(payload: LoginPayload):
    identifier = payload.username or payload.email
    if not identifier:
        raise HTTPException(status_code=400, detail="Username or email is required.")

    username = identifier.split("@")[0] if "@" in identifier else identifier

    user = authenticate_user(username, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    token = create_user_token(user)
    return {
        "success": True,
        "data": {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "username": user["username"],
                "email": user["email"],
                "full_name": user["full_name"],
                "role": user["role"],
            },
        },
        "message": "Authentication successful.",
    }


@router.post("/auth/register")
def register(payload: RegisterPayload):
    try:
        user = register_user(
            username=payload.username,
            email=payload.email,
            password=payload.password,
            full_name=payload.full_name,
            role=payload.role,
        )
        token = create_user_token(user)
        return {
            "success": True,
            "data": {"access_token": token, "token_type": "bearer"},
            "message": "User registered successfully.",
        }
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))