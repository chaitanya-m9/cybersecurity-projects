# Architecture

Plaintext → Fernet authenticated encryption → ciphertext. Decryption reverses the process after loading the locally generated key.

Key material is local and excluded from Git.