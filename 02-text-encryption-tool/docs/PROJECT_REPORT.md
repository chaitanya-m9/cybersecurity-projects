# Project Report — Text Encryption Tool

## Abstract
A local command-line application demonstrating symmetric authenticated encryption with Fernet.

## Objectives
- Generate encryption keys securely.
- Encrypt text locally.
- Decrypt valid ciphertext.
- Detect tampering or invalid keys.

## Workflow
Plaintext → key → authenticated encryption → ciphertext → authenticated decryption → plaintext.

## Example
Plaintext: `Confidential project note`
Encryption produces a token that can only be decrypted with the corresponding key.

## Security
The key is more sensitive than the ciphertext. Key exposure defeats confidentiality. The generated key must never be committed to Git.

## Testing
Test normal encryption/decryption, tampering, wrong keys, missing keys, Unicode text, and empty text.

## Future Scope
OS keyring integration, file encryption, GUI, key rotation, and secure secret-management integration.