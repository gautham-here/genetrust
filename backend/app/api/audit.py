from fastapi import APIRouter, Query
from datetime import datetime, timezone
from app.services.audit_service import get_audit_logs
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)


@router.get("/audit/logs")
def get_logs(limit: int = Query(default=50, ge=1, le=500)):
    logs = get_audit_logs(limit=limit)
    return {
        "success": True,
        "data": {
            "logs": logs,
            "count": len(logs),
        },
        "message": "Audit logs retrieved.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }