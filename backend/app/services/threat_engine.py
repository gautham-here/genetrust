import uuid
from typing import List, Dict, Optional
from app.utils.logger import setup_logger
from app.utils.timestamp import utcnow_iso

logger = setup_logger(__name__)

_threat_store: List[Dict] = [
    {
        "id": str(uuid.uuid4()),
        "severity": "high",
        "title": "Unauthorized Genomic Export Attempt",
        "message": "Unauthorized genomic export attempt detected from external node.",
        "genome_id": None,
        "created_at": utcnow_iso(),
        "status": "active",
    },
    {
        "id": str(uuid.uuid4()),
        "severity": "medium",
        "title": "Suspicious AI Inference Access",
        "message": "Suspicious AI inference access pattern observed — anomalous query frequency.",
        "genome_id": None,
        "created_at": utcnow_iso(),
        "status": "active",
    },
    {
        "id": str(uuid.uuid4()),
        "severity": "low",
        "title": "Elevated Lineage Tracing Probability",
        "message": "Elevated lineage tracing probability identified in genomic marker analysis.",
        "genome_id": None,
        "created_at": utcnow_iso(),
        "status": "monitoring",
    },
]


def get_all_threats() -> List[Dict]:
    return list(reversed(_threat_store))


def add_threat(
    severity: str,
    title: str,
    message: str,
    genome_id: Optional[str] = None,
) -> Dict:
    threat = {
        "id": str(uuid.uuid4()),
        "severity": severity,
        "title": title,
        "message": message,
        "genome_id": genome_id,
        "created_at": utcnow_iso(),
        "status": "active",
    }
    _threat_store.append(threat)
    logger.warning(f"THREAT [{severity.upper()}] {title} | genome={genome_id}")
    return threat


def evaluate_genome_threats(risk_result: Dict, genome_id: str) -> List[Dict]:
    new_threats = []
    score = risk_result.get("risk_score", 0)
    level = risk_result.get("risk_level", "low")

    if score >= 75:
        t = add_threat(
            severity="high",
            title="High-Risk Genome Detected",
            message=f"Genome {genome_id} scored {score}/100 — immediate governance action required.",
            genome_id=genome_id,
        )
        new_threats.append(t)
    elif score >= 45:
        t = add_threat(
            severity="medium",
            title="Elevated Genomic Risk Profile",
            message=f"Genome {genome_id} presents medium risk (score: {score}) — enhanced monitoring activated.",
            genome_id=genome_id,
        )
        new_threats.append(t)

    return new_threats