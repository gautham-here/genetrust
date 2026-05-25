from typing import Dict, List


# ---------------------------------------------------
# RISK SCORE CALCULATION
# ---------------------------------------------------

def calculate_risk_score(
    feature_record: Dict,
    mutation_report: Dict
) -> int:
    """
    Generates genomic privacy risk score.
    """

    score = 0

    gc_content = feature_record.get(
        "gc_content",
        0
    )

    entropy_score = feature_record.get(
        "entropy_score",
        0
    )

    mutation_count = feature_record.get(
        "mutation_count",
        0
    )

    marker_density = feature_record.get(
        "marker_density",
        0
    )

    mutation_risk_score = mutation_report.get(
        "mutation_risk_score",
        0
    )

    # ---------------------------------------------------
    # HEURISTIC RISK WEIGHTS
    # ---------------------------------------------------

    if gc_content >= 55:
        score += 15

    if entropy_score >= 1.9:
        score += 25

    if mutation_count >= 5:
        score += 20

    if marker_density >= 0.2:
        score += 20

    score += min(
        mutation_risk_score,
        20
    )

    return min(score, 100)


# ---------------------------------------------------
# RISK LEVEL CLASSIFICATION
# ---------------------------------------------------

def classify_risk_level(
    score: int
) -> str:
    """
    Converts numeric score
    into platform risk category.
    """

    if score >= 75:
        return "high"

    if score >= 45:
        return "medium"

    return "low"


# ---------------------------------------------------
# EXPOSURE PROBABILITY
# ---------------------------------------------------

def estimate_exposure_probability(
    score: int
) -> str:
    """
    Estimates genomic exposure severity.
    """

    if score >= 75:
        return "critical"

    if score >= 50:
        return "elevated"

    if score >= 25:
        return "moderate"

    return "minimal"


# ---------------------------------------------------
# FINDINGS GENERATION
# ---------------------------------------------------

def generate_findings(
    feature_record: Dict,
    mutation_report: Dict,
    score: int
) -> List[str]:
    """
    Generates explainable genomic
    privacy/security findings.
    """

    findings = []

    entropy_score = feature_record.get(
        "entropy_score",
        0
    )

    marker_density = feature_record.get(
        "marker_density",
        0
    )

    mutation_events = mutation_report[
        "repeat_analysis"
    ][
        "total_repeat_events"
    ]

    if entropy_score >= 1.9:
        findings.append(
            "Elevated genomic entropy profile detected."
        )

    if marker_density >= 0.2:
        findings.append(
            "High genomic marker density observed."
        )

    if mutation_events > 0:
        findings.append(
            "Repeated genomic anomaly signatures identified."
        )

    if score >= 75:
        findings.append(
            "Potential re-identification exposure risk detected."
        )

    if not findings:
        findings.append(
            "No major genomic exposure indicators identified."
        )

    return findings


# ---------------------------------------------------
# SECURITY RECOMMENDATIONS
# ---------------------------------------------------

def generate_recommendations(
    score: int
) -> List[str]:
    """
    Generates governance/security
    recommendations.
    """

    recommendations = [
        "Enable encrypted genomic vault storage.",
        "Restrict external genomic sharing.",
        "Activate continuous audit monitoring.",
    ]

    if score >= 50:
        recommendations.append(
            "Require multi-party authorization for access."
        )

    if score >= 75:
        recommendations.append(
            "Initiate advanced genomic threat surveillance."
        )

    return recommendations


# ---------------------------------------------------
# MAIN RISK ANALYSIS PIPELINE
# ---------------------------------------------------

def generate_risk_analysis(
    feature_records: List[Dict],
    mutation_reports: List[Dict]
) -> List[Dict]:
    """
    Generates complete genomic
    privacy risk analysis.
    """

    analysis_results = []

    for feature_record, mutation_report in zip(
        feature_records,
        mutation_reports
    ):

        risk_score = calculate_risk_score(
            feature_record,
            mutation_report
        )

        risk_level = classify_risk_level(
            risk_score
        )

        exposure_probability = (
            estimate_exposure_probability(
                risk_score
            )
        )

        findings = generate_findings(
            feature_record,
            mutation_report,
            risk_score
        )

        recommendations = (
            generate_recommendations(
                risk_score
            )
        )

        result = {
            "genome_label": feature_record.get(
                "genome_label"
            ),

            "risk_level": risk_level,

            "risk_score": risk_score,

            "exposure_probability": (
                exposure_probability
            ),

            "findings": findings,

            "recommendations": (
                recommendations
            ),
        }

        analysis_results.append(
            result
        )

    return analysis_results