import argparse, os
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_FILE=Path("image_secret.key")

def key():
    if KEY_FILE.exists(): return KEY_FILE.read_bytes()
    k=AESGCM.generate_key(bit_length=256); KEY_FILE.write_bytes(k); return k

def encrypt(src,dst):
    data=Path(src).read_bytes(); nonce=os.urandom(12); ct=AESGCM(key()).encrypt(nonce,data,None)
    Path(dst).write_bytes(b"IMG1"+nonce+ct)

def decrypt(src,dst):
    blob=Path(src).read_bytes()
    if not blob.startswith(b"IMG1"): raise ValueError("Unsupported encrypted file")
    data=AESGCM(key()).decrypt(blob[4:16],blob[16:],None); Path(dst).write_bytes(data)

p=argparse.ArgumentParser(); p.add_argument("action",choices=["encrypt","decrypt"]); p.add_argument("src"); p.add_argument("dst"); a=p.parse_args()
(encrypt if a.action=="encrypt" else decrypt)(a.src,a.dst); print("Operation completed.")
