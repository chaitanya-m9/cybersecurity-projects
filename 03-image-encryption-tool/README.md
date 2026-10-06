# Image Encryption Tool

## Author
**Chaitanya Mediboyina** — https://github.com/chaitanya-m9

## Purpose
An educational binary-file encryption project that demonstrates how an image can be protected using authenticated symmetric encryption.

## Objectives
- Protect image confidentiality.
- Detect ciphertext modification.
- Verify that decrypted bytes match the original file.

## Workflow
Image bytes → authenticated encryption → encrypted file → authenticated decryption → recovered image.

## Run
pip install -r requirements.txt
python src/image_crypto.py

## Validation
Compare SHA-256 hashes of the original and recovered files after decryption. Matching hashes demonstrate byte-for-byte recovery.

## Security
Keep the encryption key outside GitHub. Do not use real sensitive images for demonstrations.

## Limitations
This project does not provide enterprise key management, authorization, secure deletion, or encrypted metadata handling.

## Future Work
GUI, batch processing, secure key storage, metadata controls, and automated integrity tests.
