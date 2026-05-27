"""
blockchain/routes.py
────────────────────
FastAPI router — exposes the Chain lane endpoints to the rest of the platform.
Mount with:  app.include_router(blockchain_router, prefix="/api/v1/chain")
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional

from app.blockchain.chain_service import get_chain_service, ChainService

router = APIRouter(tags=["blockchain"])


def chain_svc() -> ChainService:
    try:
        return get_chain_service()
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Chain service unavailable: {exc}")


# ── Request / Response models ─────────────────────────────────────────────────

class RegisterGenomeRequest(BaseModel):
    anonymized_sequence: str = Field(..., description="Anonymized genomic string (no raw seq)")
    sample_id: str           = Field(..., description="Opaque internal sample ID")
    patient_address: Optional[str] = Field(None, description="Patient wallet for access policy")

class VerifyGenomeRequest(BaseModel):
    record_id: str
    anonymized_sequence: str

class RevokeRequest(BaseModel):
    record_id: str

class ConsentRequest(BaseModel):
    record_id: str
    consent: bool

class GrantRoleRequest(BaseModel):
    record_id: str
    grantee_address: str
    role: str  # "patient" | "lab" | "admin"

class AuthCheckRequest(BaseModel):
    record_id: str
    caller_address: str
    min_role: str = "patient"

class LogEventRequest(BaseModel):
    event_type: str
    payload: dict
    description: str
    record_id: Optional[str] = None


# ── Endpoints ─────────────────────────────────────────────────────────────────

@router.post("/register")
async def register_genome(req: RegisterGenomeRequest, svc: ChainService = Depends(chain_svc)):
    """
    Hash + register an anonymized genome sequence on-chain.
    Optionally creates an AccessPolicy for the patient wallet.
    """
    try:
        result = svc.register_genome(req.anonymized_sequence, req.sample_id)

        if req.patient_address:
            policy_result = svc.create_policy(result["record_id"], req.patient_address)
            result["policy_tx"] = policy_result["tx_hash"]

        # Auto-log the upload event
        svc.log_event(
            "upload",
            {"sample_id": req.sample_id, "record_id": result["record_id"]},
            f"Genome upload: {req.sample_id}",
            result["record_id"],
        )
        return result

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/verify")
async def verify_genome(req: VerifyGenomeRequest, svc: ChainService = Depends(chain_svc)):
    """Re-hash and verify a genome record on-chain."""
    try:
        return svc.verify_genome(req.record_id, req.anonymized_sequence)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/revoke")
async def revoke_genome(req: RevokeRequest, svc: ChainService = Depends(chain_svc)):
    """Revoke a genome record (consent withdrawal / data correction)."""
    try:
        result = svc.revoke_genome(req.record_id)
        svc.log_event("revocation", {"record_id": req.record_id}, "Genome revoked", req.record_id)
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/consent")
async def set_consent(req: ConsentRequest, svc: ChainService = Depends(chain_svc)):
    """Patient gives or withdraws consent for their record."""
    try:
        result = svc.set_consent(req.record_id, req.consent)
        svc.log_event(
            "consent",
            {"record_id": req.record_id, "consent": req.consent},
            f"Consent {'granted' if req.consent else 'withdrawn'}",
            req.record_id,
        )
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/grant-role")
async def grant_role(req: GrantRoleRequest, svc: ChainService = Depends(chain_svc)):
    """Grant a role to a wallet address for a genome record."""
    try:
        result = svc.grant_role(req.record_id, req.grantee_address, req.role)
        svc.log_event(
            "role_change",
            {"record_id": req.record_id, "grantee": req.grantee_address, "role": req.role},
            f"Role '{req.role}' granted to {req.grantee_address[:10]}…",
            req.record_id,
        )
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/check-access")
async def check_access(req: AuthCheckRequest, svc: ChainService = Depends(chain_svc)):
    """Check whether a wallet is authorised to access a record."""
    try:
        authorised = svc.is_authorised(req.record_id, req.caller_address, req.min_role)
        return {"authorised": authorised}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/log-event")
async def log_event(req: LogEventRequest, svc: ChainService = Depends(chain_svc)):
    """Manually append an audit entry (AI analysis, anomaly, export, etc.)"""
    try:
        return svc.log_event(req.event_type, req.payload, req.description, req.record_id)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/audit/{record_id}")
async def get_audit_trail(record_id: str, svc: ChainService = Depends(chain_svc)):
    """Fetch the full on-chain audit trail for a genome record."""
    try:
        return {"record_id": record_id, "entries": svc.get_audit_trail(record_id)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))