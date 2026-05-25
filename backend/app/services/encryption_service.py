from cryptography.fernet import Fernet
import os

KEY = os.getenv("GENOME_KEY").encode()

fernet = Fernet(KEY)

def encrypt_file(data):
    return fernet.encrypt(data)

def decrypt_file(data):
    return fernet.decrypt(data)