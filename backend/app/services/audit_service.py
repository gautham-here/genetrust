import uuid
from datetime import datetime, timezone
from typing import List, Dict, Optional
from app.utils.logger import setup_logger
from app.utils.timestamp import utcnow_iso

logger = setup_logger(__name__)

_audit_log: List[Dict] = []


def log_event(
    action: str,
    user: str = "system",
    genome_id: Optional[str] = None,
    severity: str = "Low",
    status: str = "success",
    metadata: Optional[Dict] = None,
) -> Dict:
    entry = {
        "id": str(uuid.uuid4()),
        "action": action,
        "user": user,
        "genome": genome_id or "N/A",
        "severity": severity,
        "status": status,
        "time": utcnow_iso(),
        "metadata": metadata or {},
    }
    _audit_log.append(entry)
    logger.info(f"AUDIT [{severity}] {action} | user={user} genome={genome_id}")
    return entry


def get_audit_logs(limit: int = 100) -> List[Dict]:
    return list(reversed(_audit_log))[:limit]


def get_logs_for_genome(genome_id: str) -> List[Dict]:
    return [e for e in _audit_log if e.get("genome") == genome_id]