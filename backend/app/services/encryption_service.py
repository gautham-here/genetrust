from app.utils.encryption import encrypt_bytes, decrypt_bytes


def encrypt_file(data: bytes) -> bytes:
    return encrypt_bytes(data)


def decrypt_file(data: bytes) -> bytes:
    return decrypt_bytes(data)