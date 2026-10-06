# Project Report — Image Encryption Tool

## 1. Introduction
Images can contain sensitive personal and business information. This project demonstrates how binary image data can be protected with authenticated encryption.

## 2. Objectives
- Encrypt image bytes.
- Detect ciphertext modification.
- Recover the original bytes with the correct key.
- Teach nonce and authenticated-encryption concepts.

## 3. Technology
Python, AES-GCM, and the cryptography library.

## 4. Methodology
The program reads the source file as bytes, generates a fresh nonce, encrypts the bytes with AES-GCM, and stores a format marker, nonce, and authenticated ciphertext. Decryption verifies authenticity before writing the recovered bytes.

## 5. Example Workflow
Generate key → encrypt image.jpg to image.enc → decrypt image.enc to recovered.jpg → compare SHA-256 hashes.

## 6. Testing
Run: python -m pytest tests

The automated test encrypts synthetic binary data and verifies byte-for-byte recovery.

## 7. Security Considerations
Keep the AES key secret and never reuse a nonce with the same key. Do not upload sensitive images to the repository.

## 8. Limitations
No enterprise key management, access control, secure deletion, or metadata policy is included.

## 9. Future Enhancements
GUI, batch processing, secure key storage, metadata controls, and richer file validation.

## 10. Conclusion
The project demonstrates practical confidentiality and integrity protection for binary/image data.
