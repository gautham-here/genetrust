import uuid
from typing import Dict, List, Optional
from app.utils.logger import setup_logger
from app.utils.timestamp import utcnow_iso

logger = setup_logger(__name__)

_threat_store: List[Dict] = []


def add_threat(
    severity: str,
    title: str,
    message: str,
    genome_id: Optional[str] = None
) -> Dict:

    threat = {

        "id": str(uuid.uuid4()),

        "severity": severity,

        "title": title,

        "message": message,

        "genome_id": genome_id,

        "created_at": utcnow_iso(),

        "status": "active"
    }

    _threat_store.append(threat)

    logger.warning(
        f"[{severity.upper()}] {title}"
    )

    return threat


def get_all_threats():

    return list(
        reversed(_threat_store)
    )


def evaluate_genome_threats(
    risk_result: Dict,
    mutation_report: Dict,
    feature_record: Dict,
    genome_id: str
) -> List[Dict]:

    generated = []

    score = risk_result.get(
        "risk_score",
        0
    )

    entropy = feature_record.get(
        "entropy_score",
        0
    )

    mutation_count = feature_record.get(
        "mutation_count",
        0
    )

    repeat_events = (

        mutation_report
        .get(
            "repeat_analysis",
            {}
        )
        .get(
            "total_repeat_events",
            0
        )
    )

    cg_density = (

        mutation_report
        .get(
            "cg_analysis",
            {}
        )
        .get(
            "cg_density",
            0
        )
    )


    # high overall risk

    if score >= 75:

        generated.append(

            add_threat(

                severity="high",

                title="High Genomic Risk Profile",

                message=f"{genome_id} scored {score}/100 risk score.",

                genome_id=genome_id
            )
        )


    # entropy anomaly

    if entropy >= 1.9:

        generated.append(

            add_threat(

                severity="medium",

                title="Entropy Anomaly",

                message=(
                    "High sequence entropy detected. "
                    "Potential biological complexity exposure."
                ),

                genome_id=genome_id
            )
        )


    # mutation spike

    if mutation_count >= 5:

        generated.append(

            add_threat(

                severity="medium",

                title="Mutation Spike",

                message=(
                    f"{mutation_count} mutation indicators detected."
                ),

                genome_id=genome_id
            )
        )


    # repeat signatures

    if repeat_events >= 5:

        generated.append(

            add_threat(

                severity="low",

                title="Repeated Pattern Signature",

                message=(
                    f"{repeat_events} repeat events observed."
                ),

                genome_id=genome_id
            )
        )


    # methylation signature

    if cg_density >= 0.1:

        generated.append(

            add_threat(

                severity="low",

                title="CG Island Density Elevated",

                message=(
                    f"CG density={cg_density}"
                ),

                genome_id=genome_id
            )
        )


    return generated