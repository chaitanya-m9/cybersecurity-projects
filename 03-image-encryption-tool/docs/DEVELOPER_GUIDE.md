# Developer Guide — Image Encryption Tool

## Architecture
CLI → key management → input file read → AES-GCM encryption/decryption → output file.

## File format
The implementation stores a small version marker followed by nonce and authenticated ciphertext. This permits the decryptor to recover the nonce while keeping the encrypted content opaque.

## Main security properties
- AES-GCM provides confidentiality.
- Authentication detects unauthorized modification.
- Random nonces prevent unsafe nonce reuse when generated correctly.

## Extension points
- Add file metadata validation.
- Add key rotation.
- Add secure OS-backed key storage.
- Add automated round-trip tests.
- Add a GUI with explicit input/output paths.

## Secure coding
Do not overwrite originals by default. Validate paths and handle exceptions without exposing key material.
