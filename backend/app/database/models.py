from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    role: str
    organization_id: Optional[str] = None
    is_active: bool = True
    created_at: datetime = None


class Organization(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    created_at: datetime = None


class GenomeMetadata(BaseModel):
    genome_id: str
    filename: str
    owner_id: str
    organization_id: Optional[str] = None
    gc_content: float
    sequence_length: int
    risk_level: str
    risk_score: int
    encrypted_path: str
    uploaded_at: datetime = None


class RiskAnalysis(BaseModel):
    genome_id: str
    risk_level: str
    risk_score: int
    findings: List[str]
    recommendations: List[str]
    generated_at: datetime = None


class ThreatAlert(BaseModel):
    id: str
    genome_id: Optional[str] = None
    severity: str
    title: str
    description: str
    created_at: datetime = None


class AuditLog(BaseModel):
    id: str
    user_id: str
    action: str
    genome_id: Optional[str] = None
    status: str
    timestamp: datetime = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"