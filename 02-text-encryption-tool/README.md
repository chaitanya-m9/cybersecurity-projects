# Text Encryption Tool

## Author
**Chaitanya Mediboyina** — https://github.com/chaitanya-m9

## Purpose
A Python command-line demonstration of authenticated symmetric encryption for text using Fernet from the cryptography library.

## Objectives
- Demonstrate confidentiality and integrity.
- Show correct use of a generated symmetric key.
- Demonstrate rejection of modified ciphertext or an incorrect key.

## Workflow
Plaintext → Fernet encryption → authenticated ciphertext → Fernet decryption → original plaintext.

## Run
pip install -r requirements.txt
python src/text_crypto.py

## Security
The key is sensitive. Never commit generated keys, passwords, tokens, or secrets. This project is for learning and should not be treated as a complete enterprise key-management solution.

## Testing
python -m pytest tests

## Limitations
The interactive demo does not implement key rotation, secure storage, identity management, or access control.

## Future Work
File encryption, OS keyring integration, key rotation, structured error handling, and expanded tests.
