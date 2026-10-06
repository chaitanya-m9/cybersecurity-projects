# Project Report — Image Encryption Tool

## Abstract
A file-level image encryption project using AES-256-GCM authenticated encryption.

## Objectives
- Protect image confidentiality.
- Detect unauthorized modification.
- Restore the original bytes after successful decryption.

## Workflow
Image → bytes → random nonce → AES-GCM → encrypted container → AES-GCM verification → original bytes.

## Example
`photo.jpg` → `encrypted.bin` → `restored.jpg`.

## Security
AES-GCM provides confidentiality and integrity. Nonce uniqueness is essential. Keys must be stored separately from encrypted data.

## Testing
Test JPEG/PNG files, tampered ciphertext, wrong key, missing input, and round-trip byte equality.

## Future Scope
Password-based key derivation, secure key vaults, GUI preview, batch encryption, and metadata policy controls.