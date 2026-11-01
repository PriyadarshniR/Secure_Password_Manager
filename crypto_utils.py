import hashlib
import base64
from cryptography.fernet import Fernet

def generate_key(master_password):
    return hashlib.sha256(master_password.encode()).digest()

def get_fernet(master_password):
    key = generate_key(master_password)
    return Fernet(base64.urlsafe_b64encode(key))

def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
