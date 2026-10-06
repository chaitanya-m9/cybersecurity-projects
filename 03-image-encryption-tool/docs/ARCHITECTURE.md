# Architecture

Image bytes → random 96-bit nonce → AES-256-GCM encryption → encrypted container. Decryption verifies the authentication tag before restoring bytes.