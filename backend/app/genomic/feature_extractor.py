from typing import Dict, List
from collections import Counter
import math


# ---------------------------------------------------
# ENTROPY CALCULATION
# ---------------------------------------------------

def calculate_entropy(
    sequence: str
) -> float:
    """
    Calculates Shannon entropy
    for genomic sequence complexity.
    """

    if not sequence:
        return 0.0

    sequence = sequence.upper()

    counts = Counter(sequence)

    probabilities = [
        count / len(sequence)
        for count in counts.values()
    ]

    entropy = -sum(
        p * math.log2(p)
        for p in probabilities
    )

    return round(entropy, 4)


# ---------------------------------------------------
# MUTATION ESTIMATION
# ---------------------------------------------------

def estimate_mutation_count(
    sequence: str
) -> int:
    """
    Simplified mutation estimation.

    Placeholder heuristic for MVP.
    """

    sequence = sequence.upper()

    unusual_patterns = [
        "AAA",
        "TTT",
        "GGGG",
        "CCCC",
    ]

    mutation_score = 0

    for pattern in unusual_patterns:
        mutation_score += sequence.count(pattern)

    return mutation_score


# ---------------------------------------------------
# MARKER DENSITY
# ---------------------------------------------------

def calculate_marker_density(
    sequence: str
) -> float:
    """
    Calculates density of genomic markers.

    Simplified heuristic for MVP.
    """

    if not sequence:
        return 0.0

    sequence = sequence.upper()

    marker_count = (
        sequence.count("CG")
        + sequence.count("AT")
    )

    density = marker_count / len(sequence)

    return round(density, 4)


# ---------------------------------------------------
# FEATURE EXTRACTION PIPELINE
# ---------------------------------------------------

def extract_genomic_features(
    parsed_records: List[Dict]
) -> List[Dict]:
    """
    Extracts AI-safe genomic features.

    IMPORTANT:
    Raw genomic sequences should NEVER
    leave backend infrastructure.
    """

    extracted_features = []

    for record in parsed_records:

        preview = record.get(
            "sequence_preview",
            ""
        )

        features = {
            "genome_label": record.get(
                "genome_label"
            ),

            "sequence_length": record.get(
                "sequence_length"
            ),

            "gc_content": record.get(
                "gc_content"
            ),

            "entropy_score": calculate_entropy(
                preview
            ),

            "mutation_count": estimate_mutation_count(
                preview
            ),

            "marker_density": calculate_marker_density(
                preview
            ),
        }

        extracted_features.append(features)

    return extracted_features