# Troubleshooting — Text Encryption Tool

## Missing cryptography package
```powershell
python -m pip install -r requirements.txt
```

## Invalid token error
The ciphertext may be corrupted, altered, or encrypted with another key.

## Decryption stopped working after key deletion
Restore the original key if it was legitimately backed up. A new key cannot decrypt old ciphertext.

## Git shows `secret.key`
Stop and remove the key from the working tree before committing. Verify `.gitignore` and never publish the secret.
