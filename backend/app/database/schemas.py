from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field


# ---------------------------------------------------
# AUTH SCHEMAS
# ---------------------------------------------------

class RegisterRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str
    role: str


class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str


class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------------------------------------------------
# GENOME UPLOAD SCHEMAS
# ---------------------------------------------------

class GenomeUploadResponseSchema(BaseModel):
    genome_id: str
    filename: str
    status: str
    uploaded_at: datetime


# ---------------------------------------------------
# GENOMIC FEATURE SCHEMAS
# ---------------------------------------------------

class ParsedGenomeSchema(BaseModel):
    genome_label: str
    sequence_length: int
    gc_content: float
    sequence_preview: str


class GenomicFeatureSchema(BaseModel):
    gc_content: float
    entropy_score: float
    mutation_count: int
    marker_density: float


# ---------------------------------------------------
# RISK ANALYSIS SCHEMAS
# ---------------------------------------------------

class RiskAnalysisSchema(BaseModel):
    risk_level: str
    risk_score: int
    exposure_probability: str

    findings: List[str]
    recommendations: List[str]


# ---------------------------------------------------
# THREAT ALERT SCHEMAS
# ---------------------------------------------------

class ThreatAlertSchema(BaseModel):
    id: str

    severity: str
    title: str
    description: str

    created_at: datetime


# ---------------------------------------------------
# AUDIT LOG SCHEMAS
# ---------------------------------------------------

class AuditLogSchema(BaseModel):
    id: str

    user_id: str
    action: str

    genome_id: Optional[str] = None

    status: str
    timestamp: datetime


# ---------------------------------------------------
# ACCESS CONTROL SCHEMAS
# ---------------------------------------------------

class AccessRequestSchema(BaseModel):
    genome_id: str
    requester_id: str
    access_type: str


class AccessApprovalSchema(BaseModel):
    request_id: str
    approved: bool


# ---------------------------------------------------
# ORGANIZATION SCHEMAS
# ---------------------------------------------------

class OrganizationCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None


class OrganizationResponseSchema(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

    created_at: datetime


# ---------------------------------------------------
# STANDARD API RESPONSE
# ---------------------------------------------------

class APIMessageSchema(BaseModel):
    success: bool
    message: str