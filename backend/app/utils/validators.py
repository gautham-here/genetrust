from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class LoginSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str


class RegisterSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str
    role: str = "researcher"


class AIAnalyzeSchema(BaseModel):
    genome_id: Optional[str] = None
    features: Optional[dict] = None
    context: Optional[str] = None