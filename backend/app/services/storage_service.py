import os
import uuid
from typing import Optional, Dict, List
from app.utils.logger import setup_logger
from app.utils.timestamp import utcnow_iso
from app.utils.encryption import encrypt_bytes
from app.database.queries import create_genome_metadata
from app.database.queries import get_all_genomes, get_genome_by_id

logger = setup_logger(__name__)

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
ENCRYPTED_DIR = os.getenv("ENCRYPTED_STORAGE_DIR", "encrypted_storage")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(ENCRYPTED_DIR, exist_ok=True)

_genome_store: List[Dict] = []


def save_genome_file(content: bytes, filename: str) -> str:
    file_id = str(uuid.uuid4())
    dest_path = os.path.join(UPLOAD_DIR, f"{file_id}_{filename}")
    with open(dest_path, "wb") as f:
        f.write(content)
    logger.info(f"Genome file saved: {dest_path}")
    return dest_path


def encrypt_and_store(content: bytes, genome_id: str) -> str:
    encrypted = encrypt_bytes(content)
    enc_path = os.path.join(ENCRYPTED_DIR, f"{genome_id}.enc")
    with open(enc_path, "wb") as f:
        f.write(encrypted)
    logger.info(f"Genome encrypted and stored: {enc_path}")
    return enc_path


def register_genome(
    genome_id: str,
    filename: str,
    gc_content: float,
    genome_length: int,
    risk_level: str,
    risk_score: int,
    encrypted_path: str,
    owner: str = "system",
) -> Dict:
    entry = {
        "id": str(uuid.uuid4()),
        "genome_code": genome_id,
        "filename": filename,
        "gc_content": gc_content,
        "genome_length": genome_length,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "encrypted_path": encrypted_path,
        "owner": owner,
        "created_at": utcnow_iso(),
    }
    _genome_store.append(entry)
    create_genome_metadata(entry)
    logger.info(f"Genome registered: {genome_id} risk={risk_level}({risk_score})")
    return entry


# def get_all_genomes() -> List[Dict]:
#     return list(reversed(_genome_store))


# def get_genome_by_id(genome_id: str) -> Optional[Dict]:
#     for g in _genome_store:
#         if g["genome_code"] == genome_id:
#             return g
#     return None