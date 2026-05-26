from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import uuid
from app.utils.timestamp import utcnow_iso
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)

_organizations = [
    {"id": str(uuid.uuid4()), "name": "GenomeX Labs", "type": "Research", "description": "Advanced genomic research facility.", "created_at": utcnow_iso()},
    {"id": str(uuid.uuid4()), "name": "BioSecure Hospital", "type": "Healthcare", "description": "Clinical genomic analysis center.", "created_at": utcnow_iso()},
    {"id": str(uuid.uuid4()), "name": "Pharma BioTrust", "type": "Pharmaceutical", "description": "Drug genomics research organization.", "created_at": utcnow_iso()},
]


class OrgCreatePayload(BaseModel):
    name: str
    type: str
    description: Optional[str] = None


@router.get("/organizations")
def get_organizations():
    return {
        "success": True,
        "data": {"organizations": _organizations, "count": len(_organizations)},
        "message": "Organizations retrieved.",
    }


@router.post("/organizations")
def create_organization(payload: OrgCreatePayload):
    org = {
        "id": str(uuid.uuid4()),
        "name": payload.name,
        "type": payload.type,
        "description": payload.description or "",
        "created_at": utcnow_iso(),
    }
    _organizations.append(org)
    return {"success": True, "data": org, "message": "Organization created."}