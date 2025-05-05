import time
import os
from typing import Optional, List, Tuple
from covert import display_main_menu as covert

def cls():
    """Clear screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

class CaesarCipher:
    def __init__(self, shift: int = 0):
        self.shift = shift
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_upper = self.alphabet.upper()

    def _validate_shift(self, shift: int) -> int:
        """Ensure shift is within valid range"""
        return shift % 26

    def encrypt(self, text: str) -> str:
        """Encrypt text using Caesar cipher"""
        result = []
        for char in text:
            if char.islower():
                idx = self.alphabet.index(char)
                new_idx = (idx + self.shift) % 26
                result.append(self.alphabet[new_idx])
            elif char.isupper():
                idx = self.alphabet_upper.index(char)
                new_idx = (idx + self.shift) % 26
                result.append(self.alphabet_upper[new_idx])
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        """Decrypt Caesar cipher text"""
        result = []
        for char in text:
            if char.islower():
                idx = self.alphabet.index(char)
                new_idx = (idx - self.shift) % 26
                result.append(self.alphabet[new_idx])
            elif char.isupper():
                idx = self.alphabet_upper.index(char)
                new_idx = (idx - self.shift) % 26
                result.append(self.alphabet_upper[new_idx])
            else:
                result.append(char)
        return ''.join(result)

class CaesarCipherCracker:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def crack(self, encrypted_text: str) -> List[Tuple[int, str]]:
        """Brute-force all possible Caesar shifts"""
        return [(shift, self.decrypt(encrypted_text, shift)) 
                for shift in range(1, 26)]

    def decrypt(self, text: str, shift: int) -> str:
        """Helper method for cracking"""
        result = []
        for char in text:
            if char.islower():
                idx = self.alphabet.index(char)
                new_idx = (idx - shift) % 26
                result.append(self.alphabet[new_idx])
            elif char.isupper():
                idx = self.alphabet.upper().index(char)
                new_idx = (idx - shift) % 26
                result.append(self.alphabet.upper()[new_idx])
            else:
                result.append(char)
        return ''.join(result)

class VigenereCipher:
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def _format_key(self, text: str) -> str:
        """Repeat keyword to match text length"""
        return (self.keyword * (len(text) // len(self.keyword) + 1))[:len(text)]

    def encrypt(self, text: str) -> str:
        """Encrypt using Vigenère cipher"""
        result = []
        key = self._format_key(text)
        for t_char, k_char in zip(text, key):
            if t_char.isalpha():
                shift = self.alphabet.index(k_char)
                if t_char.islower():
                    idx = self.alphabet.index(t_char)
                    result.append(self.alphabet[(idx + shift) % 26])
                else:
                    idx = self.alphabet.upper().index(t_char)
                    result.append(self.alphabet.upper()[(idx + shift) % 26])
            else:
                result.append(t_char)
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        """Decrypt Vigenère cipher"""
        result = []
        key = self._format_key(text)
        for t_char, k_char in zip(text, key):
            if t_char.isalpha():
                shift = self.alphabet.index(k_char)
                if t_char.islower():
                    idx = self.alphabet.index(t_char)
                    result.append(self.alphabet[(idx - shift) % 26])
                else:
                    idx = self.alphabet.upper().index(t_char)
                    result.append(self.alphabet.upper()[(idx - shift) % 26])
            else:
                result.append(t_char)
        return ''.join(result)

class EnhancedVigenereCipher(VigenereCipher):
    """Extended Vigenère with custom character sets"""
    def __init__(self, keyword: str, alphabet: Optional[str] = None):
        super().__init__(keyword)
        self.alphabet = alphabet or "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#*"

    def encrypt(self, text: str) -> str:
        """Encrypt with custom alphabet"""
        result = []
        key = self._format_key(text)
        for t_char, k_char in zip(text, key):
            if t_char in self.alphabet:
                shift = self.alphabet.index(k_char)
                idx = self.alphabet.index(t_char)
                result.append(self.alphabet[(idx + shift) % len(self.alphabet)])
            else:
                result.append(t_char)
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        """Decrypt with custom alphabet"""
        result = []
        key = self._format_key(text)
        for t_char, k_char in zip(text, key):
            if t_char in self.alphabet:
                shift = self.alphabet.index(k_char)
                idx = self.alphabet.index(t_char)
                result.append(self.alphabet[(idx - shift) % len(self.alphabet)])
            else:
                result.append(t_char)
        return ''.join(result)

def display_caesar_menu():
    """Interactive Caesar cipher menu"""
    cipher = CaesarCipher()
    original = encrypted = decrypted = ""
    
    while True:
        try:
            cls()
            print("Caesar Cipher Menu:")
            print("1. Set Shift Value (Current: {})".format(cipher.shift))
            print("2. Encrypt Text")
            print("3. Decrypt Text")
            print("4. View Texts")
            print("5. Brute Force Decrypt")
            print("6. Back")
        
            choice = input("Choice: ")
            if choice == "1":
                cls()
                cipher.shift = int(input("Enter shift value: ")).strip()
            elif choice == "2":
                cls()
                original = input("Text to encrypt: ")
                encrypted = cipher.encrypt(original)
                print("Encrypted:", encrypted)
                input("Press Enter to continue...")
            elif choice == "3":
                cls()
                encrypted = input("Text to decrypt: ")
                decrypted = cipher.decrypt(encrypted)
                print("Decrypted:", decrypted)
                input("Press Enter to continue...")
            elif choice == "4":
                cls()
                if original: print("Original:", original)
                if encrypted: print("Encrypted:", encrypted)
                if decrypted: print("Decrypted:", decrypted)
                input("\nPress Enter to continue...")
            elif choice == "5":
                cls()
                text = input("Text to brute force: ")
                results = CaesarCipherCracker().crack(text)
                for shift, msg in results:
                    print(f"Shift {shift:2}: {msg}")
                input("\nPress Enter to continue...")
            elif choice == "6":
                break
        except BaseException as e:
            print(f"{e}")
            time.sleep(1)

def display_vigenere_menu():
    """Interactive Vigenère cipher menu"""
    keyword = ""
    cipher = None
    
    while True:
        try:
            cls()
            print("Vigenère Cipher Menu:")
            print("1. Set Keyword (Current: {})".format(keyword or "None"))
            print("2. Standard Alphabet")
            print("3. Extended Alphabet")
            print("4. Back")
        
            choice = input("Choice: ")
        
            if choice == "1":
                cls()
                keyword = input("Enter keyword: ")
                if cipher:
                    cipher.keyword = keyword
            elif choice == "2":
                if not keyword:
                    cls()
                    print("Set keyword first!")
                    time.sleep(1)
                    continue
                cipher = VigenereCipher(keyword)
                text = input("Text to encrypt/decrypt: ")
                encrypted = cipher.encrypt(text)
                decrypted = cipher.decrypt(encrypted)
                print("\nEncrypted:", encrypted)
                print("Decrypted:", decrypted)
                input("\nPress Enter to continue...")
            elif choice == "3":
                if not keyword:
                    cls()
                    print("Set keyword first!")
                    time.sleep(1)
                    continue
                cipher = EnhancedVigenereCipher(keyword)
                text = input("Text to encrypt/decrypt: ")
                encrypted = cipher.encrypt(text)
                decrypted = cipher.decrypt(encrypted)
                print("\nEncrypted:", encrypted)
                print("Decrypted:", decrypted)
                input("\nPress Enter to continue...")
            elif choice == "4":
                break
        except BaseException as e:
            print(f"{e}")
            time.sleep(1)

def main():
    """Main cipher system interface"""
    while True:
        try:
            cls()
            print("Cryptography System:")
            print("1. Caesar Cipher")
            print("2. Vigenère Cipher")
            print("3. More")
            print("4. Exit")
        
            choice = input("Choice: ")
        
            if choice == "1":
                cls()
                display_caesar_menu()
            elif choice == "2":
                cls()
                display_vigenere_menu()
            elif choice == "3":
                cls()
                covert()
            elif choice == "4":
                break
            else:
                cls()
                print("Invalid choice. Please enter choice 1–4.")
                time.sleep(1)
        except BaseException as e:
            cls()
            print(f"{e}")
            time.sleep(1)

if __name__ == "__main__":
    main()