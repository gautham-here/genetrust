from typing import Dict, List


# ---------------------------------------------------
# REPEAT PATTERN DETECTION
# ---------------------------------------------------

def detect_repeat_patterns(
    sequence: str
) -> Dict:
    """
    Detects suspicious repeat patterns
    inside genomic sequences.
    """

    sequence = sequence.upper()

    repeat_patterns = {
        "AAA": sequence.count("AAA"),
        "TTT": sequence.count("TTT"),
        "GGGG": sequence.count("GGGG"),
        "CCCC": sequence.count("CCCC"),
    }

    total_repeats = sum(
        repeat_patterns.values()
    )

    return {
        "repeat_patterns": repeat_patterns,
        "total_repeat_events": total_repeats,
    }


# ---------------------------------------------------
# CG ISLAND DETECTION
# ---------------------------------------------------

def detect_cg_islands(
    sequence: str
) -> Dict:
    """
    Detects CG-rich regions
    which may indicate genomic markers.
    """

    sequence = sequence.upper()

    cg_count = sequence.count("CG")

    density = (
        cg_count / len(sequence)
        if sequence else 0
    )

    return {
        "cg_island_count": cg_count,
        "cg_density": round(density, 4),
    }


# ---------------------------------------------------
# ENTROPY RISK ANALYSIS
# ---------------------------------------------------

def evaluate_entropy_risk(
    entropy_score: float
) -> str:
    """
    Evaluates genomic entropy complexity.
    """

    if entropy_score >= 1.9:
        return "high"

    if entropy_score >= 1.5:
        return "medium"

    return "low"


# ---------------------------------------------------
# MUTATION ANALYSIS PIPELINE
# ---------------------------------------------------

def analyze_mutation_signatures(
    feature_records: List[Dict]
) -> List[Dict]:
    """
    Generates mutation intelligence
    from extracted genomic features.
    """

    mutation_reports = []

    for record in feature_records:

        preview = record.get(
            "sequence_preview",
            ""
        )

        entropy_score = record.get(
            "entropy_score",
            0
        )

        repeat_analysis = detect_repeat_patterns(
            preview
        )

        cg_analysis = detect_cg_islands(
            preview
        )

        mutation_report = {
            "genome_label": record.get(
                "genome_label"
            ),

            "entropy_risk": evaluate_entropy_risk(
                entropy_score
            ),

            "repeat_analysis": repeat_analysis,

            "cg_analysis": cg_analysis,

            "mutation_risk_score": (
                repeat_analysis[
                    "total_repeat_events"
                ]
                + cg_analysis[
                    "cg_island_count"
                ]
            ),
        }

        mutation_reports.append(
            mutation_report
        )

    return mutation_reports