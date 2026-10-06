from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE = Path("secret.key")

def get_key():
    if KEY_FILE.exists(): return KEY_FILE.read_bytes()
    key = Fernet.generate_key(); KEY_FILE.write_bytes(key); return key

def main():
    f = Fernet(get_key())
    print("1) Encrypt  2) Decrypt")
    choice = input("Choice: ").strip()
    if choice == "1":
        text = input("Plaintext: ")
        print("Ciphertext:", f.encrypt(text.encode()).decode())
    elif choice == "2":
        token = input("Ciphertext: ")
        try: print("Plaintext:", f.decrypt(token.encode()).decode())
        except Exception: print("Decryption failed: invalid ciphertext or key.")
    else: print("Invalid choice")

if __name__ == "__main__": main()
