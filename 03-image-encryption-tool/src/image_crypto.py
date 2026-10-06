"""Authenticated binary/image encryption demo using AES-GCM.
Author: Chaitanya Mediboyina
"""
import argparse
import os
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MAGIC = b"IMG1"

def generate_key() -> str:
    return AESGCM.generate_key(bit_length=256).hex()

def encrypt(src: Path, dst: Path, key_hex: str):
    key = bytes.fromhex(key_hex)
    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, src.read_bytes(), None)
    dst.write_bytes(MAGIC + nonce + ciphertext)

def decrypt(src: Path, dst: Path, key_hex: str):
    blob = src.read_bytes()
    if not blob.startswith(MAGIC) or len(blob) < 16:
        raise ValueError("Unsupported or damaged encrypted file.")
    key = bytes.fromhex(key_hex)
    plaintext = AESGCM(key).decrypt(blob[4:16], blob[16:], None)
    dst.write_bytes(plaintext)

def main():
    parser = argparse.ArgumentParser(description="Encrypt/decrypt image files.")
    parser.add_argument("action", choices=["keygen", "encrypt", "decrypt"])
    parser.add_argument("src", nargs="?")
    parser.add_argument("dst", nargs="?")
    parser.add_argument("--key")
    args = parser.parse_args()
    if args.action == "keygen":
        print(generate_key())
        return
    if not args.src or not args.dst or not args.key:
        parser.error("encrypt/decrypt require src, dst and --key")
    if args.action == "encrypt":
        encrypt(Path(args.src), Path(args.dst), args.key)
    else:
        decrypt(Path(args.src), Path(args.dst), args.key)
    print("Operation completed:", args.dst)

if __name__ == "__main__":
    main()
