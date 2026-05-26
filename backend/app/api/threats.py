from fastapi import APIRouter
from app.services.threat_engine import get_all_threats
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)


@router.get("/threats")
def get_threats():
    threats = get_all_threats()
    return {
        "success": True,
        "data": {
            "alerts": threats,
            "count": len(threats),
        },
        "message": "Threat intelligence retrieved.",
    }