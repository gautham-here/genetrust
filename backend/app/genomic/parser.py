from typing import List, Dict

from Bio import SeqIO


# ---------------------------------------------------
# GC CONTENT CALCULATION
# ---------------------------------------------------

def calculate_gc_content(
    sequence: str
) -> float:
    """
    Calculates GC percentage
    for a genomic sequence.
    """

    if not sequence:
        return 0.0

    sequence = sequence.upper()

    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = (
        (g_count + c_count)
        / len(sequence)
    ) * 100

    return round(gc_content, 2)


# ---------------------------------------------------
# FASTA PARSER
# ---------------------------------------------------

def parse_fasta(
    file_path: str
) -> List[Dict]:
    """
    Parses FASTA genomic files.

    Returns:
    - sequence length
    - GC content
    - preview
    """

    parsed_records = []

    for record in SeqIO.parse(
        file_path,
        "fasta"
    ):

        sequence = str(record.seq)

        parsed_records.append({
            "genome_label": record.id,
            "sequence_length": len(sequence),
            "gc_content": calculate_gc_content(sequence),
            "sequence_preview": sequence[:50],
        })

    return parsed_records


# ---------------------------------------------------
# FASTQ PARSER
# ---------------------------------------------------

def parse_fastq(
    file_path: str
) -> List[Dict]:
    """
    Parses FASTQ genomic files.
    """

    parsed_records = []

    for record in SeqIO.parse(
        file_path,
        "fastq"
    ):

        sequence = str(record.seq)

        parsed_records.append({
            "genome_label": record.id,
            "sequence_length": len(sequence),
            "gc_content": calculate_gc_content(sequence),
            "sequence_preview": sequence[:50],
        })

    return parsed_records


# ---------------------------------------------------
# FILE ROUTER
# ---------------------------------------------------

def parse_genomic_file(
    file_path: str,
    filename: str
):
    """
    Detects file type
    and routes parsing.
    """

    filename = filename.lower()

    if filename.endswith(".fasta"):
        return parse_fasta(file_path)

    if filename.endswith(".fa"):
        return parse_fasta(file_path)

    if filename.endswith(".fastq"):
        return parse_fastq(file_path)

    if filename.endswith(".fq"):
        return parse_fastq(file_path)

    raise ValueError(
        "Unsupported genomic file format."
    )