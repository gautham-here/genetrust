import hashlib
import secrets


def sha256_hex(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_short(value: str, length: int = 16) -> str:
    return sha256_hex(value)[:length]


def generate_token(n: int = 32) -> str:
    return secrets.token_hex(n)