"""Authenticated text encryption demo using Fernet.
Author: Chaitanya Mediboyina
"""
from cryptography.fernet import Fernet, InvalidToken

def generate_key() -> str:
    return Fernet.generate_key().decode()

def encrypt_text(plaintext: str, key: str) -> str:
    return Fernet(key.encode()).encrypt(plaintext.encode()).decode()

def decrypt_text(ciphertext: str, key: str) -> str:
    try:
        return Fernet(key.encode()).decrypt(ciphertext.encode()).decode()
    except InvalidToken as exc:
        raise ValueError("Invalid key or modified ciphertext.") from exc

def main():
    key = input("Fernet key (press Enter to generate): ").strip()
    if not key:
        key = generate_key()
        print("Generated key - store it securely:", key)
    choice = input("1) Encrypt  2) Decrypt: ").strip()
    if choice == "1":
        print("Ciphertext:", encrypt_text(input("Plaintext: "), key))
    elif choice == "2":
        print("Plaintext:", decrypt_text(input("Ciphertext: "), key))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
