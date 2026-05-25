from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr


# ---------------------------------------------------
# USER MODELS
# ---------------------------------------------------

class User(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    role: str
    organization_id: Optional[str] = None
    is_active: bool = True
    created_at: datetime = datetime.utcnow()


# ---------------------------------------------------
# ORGANIZATION MODELS
# ---------------------------------------------------

class Organization(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    created_at: datetime = datetime.utcnow()


# ---------------------------------------------------
# GENOME MODELS
# ---------------------------------------------------

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

    uploaded_at: datetime = datetime.utcnow()


# ---------------------------------------------------
# RISK ANALYSIS MODELS
# ---------------------------------------------------

class RiskAnalysis(BaseModel):
    genome_id: str

    risk_level: str
    risk_score: int

    findings: List[str]
    recommendations: List[str]

    generated_at: datetime = datetime.utcnow()


# ---------------------------------------------------
# THREAT ALERT MODELS
# ---------------------------------------------------

class ThreatAlert(BaseModel):
    id: str

    genome_id: Optional[str] = None

    severity: str
    title: str
    description: str

    created_at: datetime = datetime.utcnow()


# ---------------------------------------------------
# AUDIT LOG MODELS
# ---------------------------------------------------

class AuditLog(BaseModel):
    id: str

    user_id: str
    action: str

    genome_id: Optional[str] = None

    status: str

    timestamp: datetime = datetime.utcnow()


# ---------------------------------------------------
# ACCESS REQUEST MODELS
# ---------------------------------------------------

class AccessRequest(BaseModel):
    id: str

    requester_id: str
    genome_id: str

    access_type: str

    status: str

    requested_at: datetime = datetime.utcnow()


# ---------------------------------------------------
# AUTH MODELS
# ---------------------------------------------------

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