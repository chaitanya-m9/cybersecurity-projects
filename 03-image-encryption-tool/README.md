# Image Encryption Tool

Educational image confidentiality tool using AES-GCM. It encrypts image bytes and stores nonce plus ciphertext in a binary container; the original image is never modified.

## Install
```bash
pip install -r requirements.txt
```
## Run
```bash
python src/image_crypto.py encrypt input.jpg encrypted.bin
python src/image_crypto.py decrypt encrypted.bin restored.jpg
```
Keep the generated key private.