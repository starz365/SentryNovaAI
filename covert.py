import os
import sys
from PIL import Image, UnidentifiedImageError
from typing import List, Optional, Tuple, Dict, Union
from common import clear_screen as cls

# ==================== ENHANCED CIPHER SYSTEM ====================
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

class VigenereCipher:
    def __init__(self, key: str, alphabet: str = None):
        """
        Initialize cipher with security checks
        :param key: Encryption key (will be sanitized)
        :param alphabet: Custom alphabet (default: a-zA-Z0-9 + space)
        """
        if not key:
            raise ValueError("Encryption key cannot be empty")
        
        self.key = self._sanitize_key(key)
        self.alphabet = alphabet or "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        
        if any(char not in self.alphabet for char in self.key):
            raise ValueError("Key contains characters not in alphabet")

    def _sanitize_key(self, key: str) -> str:
        """Remove dangerous characters from key"""
        return ''.join(char for char in key if char.isalnum() or char.isspace())

    def _repeat_key(self, text: str) -> str:
        """Generate repeating key with length matching text"""
        return (self.key * ((len(text) // len(self.key)) + 1))[:len(text)]

    def encrypt(self, plaintext: str) -> str:
        """Secure encryption with input validation"""
        if not plaintext:
            raise ValueError("Plaintext cannot be empty")
            
        key = self._repeat_key(plaintext)
        encrypted_chars = []
        
        for t, k in zip(plaintext, key):
            if t not in self.alphabet:
                raise ValueError(f"Invalid character '{t}' not in alphabet")
            idx = (self.alphabet.index(t) + self.alphabet.index(k)) % len(self.alphabet)
            encrypted_chars.append(self.alphabet[idx])
            
        return ''.join(encrypted_chars)

    def decrypt(self, ciphertext: str) -> str:
        """Secure decryption with input validation"""
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty")
            
        key = self._repeat_key(ciphertext)
        decrypted_chars = []
        
        for t, k in zip(ciphertext, key):
            if t not in self.alphabet:
                raise ValueError(f"Invalid character '{t}' not in alphabet")
            idx = (self.alphabet.index(t) - self.alphabet.index(k)) % len(self.alphabet)
            decrypted_chars.append(self.alphabet[idx])
            
        return ''.join(decrypted_chars)

# ==================== STEGANOGRAPHY SYSTEM ====================
class CovertMessenger:
    CIPHER_CHOICES = {
        '1': ('Caesar Cipher', CaesarCipher),
        '2': ('Vigenère Cipher', VigenereCipher),
        '3': ('Back', None)
    }

    def __init__(self):
        """Initialize with cipher selection"""
        self.cipher = None
        self.cipher_instance = None
        self.message_terminator = "MWIKYA_END"

    def _validate_image(self, image_path: str) -> Image.Image:
        """Secure image loading with validation"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
            
        try:
            img = Image.open(image_path)
            if img.mode not in ('RGB', 'RGBA'):
                raise ValueError("Only RGB/RGBA images supported")
            return img
        except UnidentifiedImageError:
            raise ValueError("Invalid image file format")

    def _validate_output_path(self, path: str) -> str:
        """Ensure output path is writable"""
        dirname = os.path.dirname(path) or '.'
        if not os.access(dirname, os.W_OK):
            raise PermissionError(f"Cannot write to directory: {dirname}")
        return path

    def set_cipher(self, cipher_type: str, **cipher_params):
        """Configure the cipher system"""
        if cipher_type not in self.CIPHER_CHOICES:
            raise ValueError("Invalid cipher type")
        
        cipher_class = self.CIPHER_CHOICES[cipher_type][1]
        self.cipher_instance = cipher_class(**cipher_params)
        self.cipher = cipher_type

    def hide_message(self, image_path: str, message: str, output_path: str) -> None:
        """
        Securely embed encrypted message in image
        :param image_path: Source image path
        :param message: Plaintext message to hide
        :param output_path: Output image path
        """
        if not self.cipher_instance:
            raise ValueError("Cipher not configured")
        if not message:
            raise ValueError("Message cannot be empty")
            
        img = self._validate_image(image_path)
        output_path = self._validate_output_path(output_path)
        
        encrypted = self.cipher_instance.encrypt(message + self.message_terminator)
        binary_msg = ''.join(f"{ord(c):08b}" for c in encrypted)
        
        pixels = img.load()
        width, height = img.size
        max_bits = width * height * 3
        
        if len(binary_msg) > max_bits:
            raise ValueError("Message too large for image capacity")
            
        bit_index = 0
        for y in range(height):
            for x in range(width):
                if bit_index >= len(binary_msg):
                    break
                    
                r, g, b = pixels[x, y][:3]
                
                if bit_index < len(binary_msg):
                    r = (r & 0xFE) | int(binary_msg[bit_index])
                    bit_index += 1
                if bit_index < len(binary_msg):
                    g = (g & 0xFE) | int(binary_msg[bit_index])
                    bit_index += 1
                if bit_index < len(binary_msg):
                    b = (b & 0xFE) | int(binary_msg[bit_index])
                    bit_index += 1
                
                pixels[x, y] = (r, g, b)
        
        img.save(output_path)

    def reveal_message(self, image_path: str) -> str:
        """Extract and decrypt hidden message with validation"""
        if not self.cipher_instance:
            raise ValueError("Cipher not configured")
            
        img = self._validate_image(image_path)
        pixels = img.load()
        width, height = img.size
        
        bits = []
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y][:3]
                bits.extend([str(r & 1), str(g & 1), str(b & 1)])
        
        chars = []
        for i in range(0, len(bits), 8):
            byte = ''.join(bits[i:i+8])
            if len(byte) == 8:
                chars.append(chr(int(byte, 2)))
        
        decrypted = self.cipher_instance.decrypt(''.join(chars))
        term_pos = decrypted.find(self.message_terminator)
        
        if term_pos == -1:
            raise ValueError("No valid message found - tampering detected")
            
        return decrypted[:term_pos]

# ==================== UNIFIED INTERFACE ====================
def clear_screen():
    """Clear screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    """Main application menu"""
    messenger = CovertMessenger()
    
    while True:
        clear_screen()
        print("=== SECURE MESSAGING SYSTEM ===")
        print("1. Configure Cipher")
        print("2. Hide Message")
        print("3. Reveal Message")
        print("4. Exit/Back")
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            while True:
                clear_screen()
                print("Select Cipher Type:")
                for num, (name, _) in messenger.CIPHER_CHOICES.items():
                    print(f"{num}. {name}")
            
                cipher_choice = input("Choice: ").strip()
            
                if cipher_choice == '1':  # Caesar
                    cls()
                    shift = input("Enter shift value (default 3): ").strip()
                    try:
                        messenger.set_cipher(cipher_choice, shift=int(shift) if shift else 3)
                        print("Caesar cipher configured")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif cipher_choice == '2':  # Vigenère
                    cls()
                    key = input("Enter encryption key: ").strip()
                    try:
                        messenger.set_cipher(cipher_choice, key=key)
                        print("Vigenère cipher configured")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif cipher_choice == "3":
                    break
                else:
                    print("Invalid cipher choice")
            
                input("Press Enter to continue...")
            
        elif choice == "2":
            cls()
            if not messenger.cipher:
                print("Configure cipher first!")
                input("Press Enter to continue...")
                continue
                
            try:
                img_path = input("Input image path: ").strip()
                message = input("Message to hide: ").strip()
                output = input("Output path [encoded.png]: ").strip() or "encoded.png"
                
                messenger.hide_message(img_path, message, output)
                print("Message hidden successfully")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter to continue...")
            
        elif choice == "3":
            if not messenger.cipher:
                print("Configure cipher first!")
                input("Press Enter to continue...")
                continue
                
            try:
                img_path = input("Encoded image path: ").strip()
                message = messenger.reveal_message(img_path)
                print(f"Recovered message: {message}")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter to continue...")
            
        elif choice == "4":
            break

if __name__ == "__main__":
    display_main_menu()