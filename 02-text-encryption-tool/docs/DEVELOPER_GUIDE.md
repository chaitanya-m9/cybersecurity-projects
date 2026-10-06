# Developer Guide — Text Encryption Tool

## Architecture
CLI input → key loading/creation → Fernet encryption/decryption → error handling → output.

## Cryptographic design
Fernet provides authenticated symmetric encryption. The same secret key is required for decryption, while authentication helps detect tampering.

## Extension points
- Separate CLI and crypto modules.
- Add file encryption using streaming-safe designs where appropriate.
- Add key rotation.
- Add secure key storage through an operating-system secret store.
- Add automated unit tests with generated test keys.

## Secure coding
Never print or commit secret keys. Do not store plaintext unnecessarily. Handle invalid tokens without exposing sensitive details.
