from typing import List, Dict
from Bio import SeqIO
from app.utils.logger import setup_logger
import io

logger = setup_logger(__name__)


def calculate_gc_content(sequence: str) -> float:
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    g = sequence.count("G")
    c = sequence.count("C")
    return round(((g + c) / len(sequence)) * 100, 2)


def parse_fasta(file_path: str) -> List[Dict]:
    records = []
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            sequence = str(record.seq)
            records.append({
                "genome_label": record.id,
                "sequence_length": len(sequence),
                "gc_content": calculate_gc_content(sequence),
                "sequence_preview": sequence[:100],
                "full_sequence_length": len(sequence),
            })
    except Exception as e:
        logger.error(f"FASTA parse error for {file_path}: {e}")
        raise
    return records


def parse_fasta_bytes(content: bytes, filename: str) -> List[Dict]:
    records = []
    try:
        fmt = "fasta"
        if filename.lower().endswith((".fastq", ".fq")):
            fmt = "fastq"
        handle = io.StringIO(content.decode("utf-8", errors="replace"))
        for record in SeqIO.parse(handle, fmt):
            sequence = str(record.seq)
            records.append({
                "genome_label": record.id,
                "sequence_length": len(sequence),
                "gc_content": calculate_gc_content(sequence),
                "sequence_preview": sequence[:100],
                "full_sequence_length": len(sequence),
            })
    except Exception as e:
        logger.error(f"Bytes parse error: {e}")
        raise
    return records


def parse_fastq(file_path: str) -> List[Dict]:
    records = []
    try:
        for record in SeqIO.parse(file_path, "fastq"):
            sequence = str(record.seq)
            records.append({
                "genome_label": record.id,
                "sequence_length": len(sequence),
                "gc_content": calculate_gc_content(sequence),
                "sequence_preview": sequence[:100],
                "full_sequence_length": len(sequence),
            })
    except Exception as e:
        logger.error(f"FASTQ parse error for {file_path}: {e}")
        raise
    return records


def parse_genomic_file(file_path: str, filename: str) -> List[Dict]:
    fn = filename.lower()
    if fn.endswith((".fasta", ".fa", ".txt")):
        return parse_fasta(file_path)
    if fn.endswith((".fastq", ".fq")):
        return parse_fastq(file_path)
    raise ValueError(f"Unsupported genomic file format: {filename}")