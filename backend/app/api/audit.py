from fastapi import APIRouter
from datetime import datetime

router = APIRouter(tags=["Audit"])


FAKE_AUDIT_LOGS = [
    {
        "event": "Genome uploaded",
        "user": "researcher_01",
        "time": "2026-05-14 09:00"
    },
    {
        "event": "Threat scan completed",
        "user": "ai_engine",
        "time": "2026-05-14 09:10"
    }
]


@router.get("/audit/logs")
def get_logs():
    return {
        "logs": FAKE_AUDIT_LOGS,
        "generated_at": datetime.utcnow()
    }