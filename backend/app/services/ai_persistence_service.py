import uuid

from app.database.queries import (
    save_ai_analysis
)

from app.utils.timestamp import utcnow_iso
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def persist_ai_analysis(
    genome_id: str,
    ai_result: dict,
):

    payload = {

        "id": str(uuid.uuid4()),

        "genome_id": genome_id,

        "risk_level":
            ai_result.get(
                "ai_risk_level"
            ),

        "risk_score":
            ai_result.get(
                "ai_risk_score"
            ),

        "summary":
            ai_result.get(
                "ai_summary"
            ),

        "threat_indicators":
            ai_result.get(
                "threat_indicators",
                []
            ),

        "privacy_concerns":
            ai_result.get(
                "privacy_concerns",
                []
            ),

        "recommendations":
            ai_result.get(
                "security_recommendations",
                []
            ),

        "backend_used":
            ai_result.get(
                "ai_backend_used"
            ),

        "created_at":
            utcnow_iso(),
    }

    try:

        save_ai_analysis(
            payload
        )

    except Exception as e:

        logger.error(
            f"AI persistence failed: {e}"
        )