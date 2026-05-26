import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def _derive_key(secret: str, salt: bytes = b"genetrust_salt_v1") -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(secret.encode()))


def _get_fernet() -> Fernet:
    raw_key = os.getenv("GENOME_ENCRYPTION_KEY", "")
    if not raw_key:
        raw_key = os.getenv("GENOME_KEY", "genetrust_default_dev_key_32chars!!")
    try:
        key = base64.urlsafe_b64decode(raw_key + "==")
        if len(key) == 32:
            key = base64.urlsafe_b64encode(key)
        else:
            key = raw_key.encode()
            if len(key) < 32:
                key = key.ljust(32, b"0")
            key = base64.urlsafe_b64encode(key[:32])
    except Exception:
        key = _derive_key(raw_key)
    return Fernet(key)


def encrypt_bytes(data: bytes) -> bytes:
    try:
        return _get_fernet().encrypt(data)
    except Exception as e:
        logger.error(f"Encryption error: {e}")
        raise


def decrypt_bytes(data: bytes) -> bytes:
    try:
        return _get_fernet().decrypt(data)
    except Exception as e:
        logger.error(f"Decryption error: {e}")
        raise