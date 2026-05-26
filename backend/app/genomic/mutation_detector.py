from typing import Dict, List
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def detect_repeat_patterns(sequence: str) -> Dict:
    sequence = sequence.upper()
    patterns = {
        "AAA": sequence.count("AAA"),
        "TTT": sequence.count("TTT"),
        "GGGG": sequence.count("GGGG"),
        "CCCC": sequence.count("CCCC"),
        "ATATAT": sequence.count("ATATAT"),
        "GCGCGC": sequence.count("GCGCGC"),
    }
    return {
        "repeat_patterns": patterns,
        "total_repeat_events": sum(patterns.values()),
    }


def detect_cg_islands(sequence: str) -> Dict:
    sequence = sequence.upper()
    cg_count = sequence.count("CG")
    density = cg_count / len(sequence) if sequence else 0
    return {
        "cg_island_count": cg_count,
        "cg_density": round(density, 4),
    }


def evaluate_entropy_risk(entropy_score: float) -> str:
    if entropy_score >= 1.9:
        return "high"
    if entropy_score >= 1.5:
        return "medium"
    return "low"


def detect_homopolymer_runs(sequence: str, min_length: int = 5) -> List[str]:
    sequence = sequence.upper()
    runs = []
    i = 0
    while i < len(sequence):
        j = i
        while j < len(sequence) and sequence[j] == sequence[i]:
            j += 1
        if (j - i) >= min_length:
            runs.append(f"{sequence[i]}x{j - i}")
        i = j
    return runs


def analyze_mutation_signatures(feature_records: List[Dict]) -> List[Dict]:
    reports = []
    for record in feature_records:
        preview = record.get("sequence_preview", "")
        entropy_score = record.get("entropy_score", 0)
        repeat_analysis = detect_repeat_patterns(preview)
        cg_analysis = detect_cg_islands(preview)
        homopolymers = detect_homopolymer_runs(preview)
        mutation_risk_score = (
            repeat_analysis["total_repeat_events"] + cg_analysis["cg_island_count"]
        )
        reports.append({
            "genome_label": record.get("genome_label"),
            "entropy_risk": evaluate_entropy_risk(entropy_score),
            "repeat_analysis": repeat_analysis,
            "cg_analysis": cg_analysis,
            "homopolymer_runs": homopolymers,
            "mutation_risk_score": mutation_risk_score,
        })
    return reports