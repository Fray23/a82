import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from config import SALT

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=SALT,
    iterations=390000,
)

class Cipher:
    def __init__(self, master_key: str):
        key = bytes(master_key, encoding='utf8')
        key = base64.urlsafe_b64encode(kdf.derive(key))
        self.cipher = Fernet(key)

    def decrypt(self, val: str) -> str:
        # return  self.cipher.decrypt(val).decode("utf-8")
        return val

    def crypt(self, val):
        # return self.cipher.encrypt(bytes(val, encoding='utf8'))
        return val
