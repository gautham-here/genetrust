from typing import Dict, List
import hashlib


# ---------------------------------------------------
# HASH GENERATION
# ---------------------------------------------------

def generate_genome_hash(
    genome_label: str
) -> str:
    """
    Generates irreversible hashed identifier
    for anonymized genomic references.
    """

    encoded = genome_label.encode("utf-8")

    return hashlib.sha256(
        encoded
    ).hexdigest()[:16]


# ---------------------------------------------------
# FEATURE SANITIZATION
# ---------------------------------------------------

def anonymize_feature_record(
    feature_record: Dict
) -> Dict:
    """
    Removes sensitive genomic identifiers
    and prepares AI-safe payload.
    """

    anonymized_record = {
        "genome_reference": generate_genome_hash(
            feature_record.get(
                "genome_label",
                "unknown"
            )
        ),

        "sequence_length": feature_record.get(
            "sequence_length"
        ),

        "gc_content": feature_record.get(
            "gc_content"
        ),

        "entropy_score": feature_record.get(
            "entropy_score"
        ),

        "mutation_count": feature_record.get(
            "mutation_count"
        ),

        "marker_density": feature_record.get(
            "marker_density"
        ),
    }

    return anonymized_record


# ---------------------------------------------------
# BULK ANONYMIZATION
# ---------------------------------------------------

def anonymize_features(
    feature_records: List[Dict]
) -> List[Dict]:
    """
    Processes multiple genomic feature records
    into AI-safe anonymized payloads.
    """

    anonymized_records = []

    for record in feature_records:

        sanitized = anonymize_feature_record(
            record
        )

        anonymized_records.append(
            sanitized
        )

    return anonymized_records