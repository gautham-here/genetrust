from typing import Dict, List
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def calculate_risk_score(feature_record: Dict, mutation_report: Dict) -> int:
    score = 0
    gc_content = feature_record.get("gc_content", 0)
    entropy_score = feature_record.get("entropy_score", 0)
    mutation_count = feature_record.get("mutation_count", 0)
    marker_density = feature_record.get("marker_density", 0)
    at_content = feature_record.get("at_content", 0)
    mutation_risk_score = mutation_report.get("mutation_risk_score", 0)

    if gc_content >= 65:
        score += 20
    elif gc_content >= 55:
        score += 15
    elif gc_content <= 30:
        score += 10

    if entropy_score >= 1.95:
        score += 30
    elif entropy_score >= 1.9:
        score += 25
    elif entropy_score >= 1.5:
        score += 10

    if mutation_count >= 10:
        score += 25
    elif mutation_count >= 5:
        score += 20
    elif mutation_count >= 2:
        score += 10

    if marker_density >= 0.3:
        score += 25
    elif marker_density >= 0.2:
        score += 20
    elif marker_density >= 0.1:
        score += 10

    score += min(mutation_risk_score, 20)

    repeat_events = mutation_report.get("repeat_analysis", {}).get("total_repeat_events", 0)
    if repeat_events >= 10:
        score += 10
    elif repeat_events >= 5:
        score += 5

    cg_density = mutation_report.get("cg_analysis", {}).get("cg_density", 0)
    if cg_density >= 0.1:
        score += 10

    logger.debug(f"Risk score calculated: {min(score, 100)} for {feature_record.get('genome_label', 'unknown')}")
    return min(score, 100)


def classify_risk_level(score: int) -> str:
    if score >= 75:
        return "high"
    if score >= 45:
        return "medium"
    return "low"


def estimate_exposure_probability(score: int) -> str:
    if score >= 75:
        return "critical"
    if score >= 50:
        return "elevated"
    if score >= 25:
        return "moderate"
    return "minimal"


def generate_findings(feature_record: Dict, mutation_report: Dict, score: int) -> List[str]:
    findings = []
    entropy_score = feature_record.get("entropy_score", 0)
    marker_density = feature_record.get("marker_density", 0)
    gc_content = feature_record.get("gc_content", 0)
    mutation_count = feature_record.get("mutation_count", 0)
    repeat_events = mutation_report.get("repeat_analysis", {}).get("total_repeat_events", 0)
    cg_density = mutation_report.get("cg_analysis", {}).get("cg_density", 0)
    entropy_risk = mutation_report.get("entropy_risk", "low")

    if entropy_score >= 1.9:
        findings.append("Elevated genomic entropy profile detected — high biological complexity signature.")
    if marker_density >= 0.2:
        findings.append("High genomic marker density observed — elevated re-identification potential.")
    if repeat_events > 0:
        findings.append(f"Repeated genomic anomaly signatures identified ({repeat_events} events).")
    if score >= 75:
        findings.append("Potential re-identification exposure risk detected — immediate governance required.")
    if gc_content >= 60:
        findings.append(f"Elevated GC content ({gc_content}%) detected — characteristic biological signature.")
    if mutation_count >= 5:
        findings.append(f"High mutation signal count ({mutation_count}) — potential genomic instability markers.")
    if cg_density >= 0.08:
        findings.append(f"CG island density ({cg_density}) exceeds baseline — methylation signature risk.")
    if entropy_risk == "high":
        findings.append("High sequence entropy risk — complex genomic structure with broad identifiability.")
    if not findings:
        findings.append("No major genomic exposure indicators identified — profile within normal parameters.")
    return findings


def generate_recommendations(score: int) -> List[str]:
    recs = [
        "Enable AES-256 encrypted genomic vault storage.",
        "Restrict external genomic sharing and API access.",
        "Activate continuous audit monitoring for all access events.",
        "Apply genomic data minimization before any third-party transfer.",
    ]
    if score >= 45:
        recs.append("Require multi-party authorization for genomic data access.")
        recs.append("Apply selective genomic masking for lineage-sensitive regions.")
    if score >= 75:
        recs.append("Initiate advanced genomic threat surveillance protocol.")
        recs.append("Restrict all external data export until re-identification risk is mitigated.")
        recs.append("Engage compliance review for GDPR/HIPAA genomic data handling.")
    return recs


def generate_risk_analysis(feature_records: List[Dict], mutation_reports: List[Dict]) -> List[Dict]:
    results = []
    for feature_record, mutation_report in zip(feature_records, mutation_reports):
        risk_score = calculate_risk_score(feature_record, mutation_report)
        risk_level = classify_risk_level(risk_score)
        exposure_probability = estimate_exposure_probability(risk_score)
        findings = generate_findings(feature_record, mutation_report, risk_score)
        recommendations = generate_recommendations(risk_score)
        results.append({
            "genome_label": feature_record.get("genome_label"),
            "risk_level": risk_level,
            "risk_score": risk_score,
            "exposure_probability": exposure_probability,
            "findings": findings,
            "recommendations": recommendations,
        })
    return results