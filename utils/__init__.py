
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os

def Generate_encryption_key():
    backend = default_backend()
    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    env_key = os.environ.get("KEY")
    key = base64.urlsafe_b64encode(kdf.derive(b"{}".format(env_key)))

    key = Fernet(key)
    
    
    return key
    
    