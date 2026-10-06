# User Guide — Image Encryption Tool

## Purpose
Encrypt and decrypt image files using AES-GCM, providing confidentiality and authentication.

## Setup
```powershell
cd 03-image-encryption-tool
python -m pip install -r requirements.txt
```

## Encrypt an image
```powershell
python src/image_crypto.py encrypt input.jpg encrypted.bin
```

## Decrypt
```powershell
python src/image_crypto.py decrypt encrypted.bin restored.jpg
```

## Step-by-step example
1. Copy a non-sensitive test image into the project directory.
2. Run the encryption command.
3. Confirm an encrypted binary file is produced.
4. Run the decryption command.
5. Open the restored image and compare it with the original.

## Security notes
AES-GCM uses a key, a unique nonce, ciphertext, and an authentication tag. Do not reuse a nonce with the same AES-GCM key. Do not commit the secret key.

## Testing recommendation
Use a duplicate test image rather than a personal photograph containing sensitive information.
