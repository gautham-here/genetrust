from typing import Dict, List
from collections import Counter
import math
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def calculate_entropy(sequence: str) -> float:
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    counts = Counter(sequence)
    total = len(sequence)
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())
    return round(entropy, 4)


def estimate_mutation_count(sequence: str) -> int:
    sequence = sequence.upper()
    unusual = ["AAA", "TTT", "GGGG", "CCCC", "ATATAT", "GCGCGC"]
    return sum(sequence.count(p) for p in unusual)


def calculate_marker_density(sequence: str) -> float:
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    marker_count = sequence.count("CG") + sequence.count("AT")
    return round(marker_count / len(sequence), 4)


def calculate_at_content(sequence: str) -> float:
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    a = sequence.count("A")
    t = sequence.count("T")
    return round(((a + t) / len(sequence)) * 100, 2)


def extract_genomic_features(parsed_records: List[Dict]) -> List[Dict]:
    features = []
    for record in parsed_records:
        sequence=record.get(
            "full_sequence",
            record.get("sequence_preview","")
        )
        f = {
            "genome_label": record.get("genome_label"),
            "sequence_length": record.get("sequence_length"),
            "gc_content": record.get("gc_content"),
            "at_content": calculate_at_content(sequence),
            "entropy_score": calculate_entropy(sequence),
            "mutation_count": estimate_mutation_count(sequence),
            "marker_density": calculate_marker_density(sequence),
            "sequence_preview": sequence,
        }
        features.append(f)
        logger.debug(f"Extracted features for {f['genome_label']}: entropy={f['entropy_score']}, gc={f['gc_content']}")
    return features