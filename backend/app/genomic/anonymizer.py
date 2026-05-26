from typing import Dict, List
import hashlib


def generate_genome_hash(genome_label: str) -> str:
    return hashlib.sha256(genome_label.encode("utf-8")).hexdigest()[:16]


def anonymize_feature_record(feature_record: Dict) -> Dict:
    return {
        "genome_reference": generate_genome_hash(
            feature_record.get("genome_label", "unknown")
        ),
        "sequence_length": feature_record.get("sequence_length"),
        "gc_content": feature_record.get("gc_content"),
        "at_content": feature_record.get("at_content"),
        "entropy_score": feature_record.get("entropy_score"),
        "mutation_count": feature_record.get("mutation_count"),
        "marker_density": feature_record.get("marker_density"),
    }


def anonymize_features(feature_records: List[Dict]) -> List[Dict]:
    return [anonymize_feature_record(r) for r in feature_records]