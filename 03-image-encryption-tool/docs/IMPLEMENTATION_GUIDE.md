# Implementation Guide — Image Encryption Tool

## Problem
Image files can contain sensitive personal or business information and may require confidentiality.

## Technology
Python AES-GCM from the cryptography package.

## Implementation
1. Read image bytes.
2. Generate a fresh 96-bit nonce.
3. Encrypt and authenticate with AES-GCM.
4. Store a small file marker, nonce, and ciphertext.
5. During decryption, validate the marker and authenticate the ciphertext.
6. Write the recovered bytes to a new file.

## Verification
Use SHA-256 on the original and recovered files. Equal hashes indicate identical bytes.

## Security
Never reuse a nonce with the same AES-GCM key. Keep keys outside the repository.

## Testing
Run: python -m pytest tests
