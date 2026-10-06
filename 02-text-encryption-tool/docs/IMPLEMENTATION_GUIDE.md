# Implementation Guide — Text Encryption Tool

## Problem
Plaintext data can be exposed when stored or transferred without confidentiality protection.

## Technology
Python and the cryptography package using Fernet authenticated encryption.

## Implementation
1. Generate a cryptographically secure Fernet key.
2. Convert text to bytes.
3. Encrypt and authenticate the plaintext.
4. Represent ciphertext as text for demonstration.
5. Decrypt using the same key.
6. Reject invalid or modified ciphertext.

## Key Management
The key is more sensitive than the ciphertext. Do not commit it to GitHub. Production systems should use a dedicated secret-management or key-management system.

## Testing
Run: python -m pytest tests

The primary test verifies encryption/decryption round-trip and another verifies wrong-key rejection.
