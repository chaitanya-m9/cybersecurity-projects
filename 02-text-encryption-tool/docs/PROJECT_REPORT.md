# Project Report — Text Encryption Tool

## 1. Introduction
This project demonstrates authenticated symmetric encryption for text using Fernet.

## 2. Objectives
- Explain confidentiality and integrity.
- Demonstrate key generation.
- Encrypt and decrypt text locally.
- Show rejection of invalid ciphertext or keys.

## 3. Technology
Python and the cryptography library.

## 4. Methodology
A Fernet key is generated or supplied. Plaintext is encoded as bytes, encrypted, authenticated, and represented as a token. The matching key is required for successful decryption.

## 5. Example
Plaintext: Cybersecurity lab message
Result: authenticated ciphertext token
Decryption: original plaintext

## 6. Testing
Run: python -m pytest tests

The test suite validates round-trip encryption and wrong-key rejection.

## 7. Key Management
The encryption key must remain secret. Production systems should use managed secret storage rather than source-code files.

## 8. Limitations
The project is a learning utility and does not implement enterprise identity, key rotation, access control, or centralized key management.

## 9. Future Enhancements
Encrypted files, key rotation, OS keyring integration, and richer automated testing.

## 10. Conclusion
The project provides a practical demonstration of authenticated symmetric encryption and secure key-handling principles.
