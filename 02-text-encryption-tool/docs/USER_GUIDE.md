# User Guide — Text Encryption Tool

## 1. Purpose
Encrypt and decrypt text using Fernet authenticated symmetric encryption.

## 2. Prerequisites
- Python 3.10+
- `cryptography` package

## 3. Setup
```powershell
cd 02-text-encryption-tool
python -m pip install -r requirements.txt
```

## 4. Run
Follow the prompts in `src/text_crypto.py`. The application creates a local secret key when one does not exist.

## 5. Example workflow
1. Run the program.
2. Choose encryption.
3. Enter fictional text such as `Cybersecurity lab message`.
4. Save/copy the ciphertext produced by the program.
5. Choose decryption and provide the ciphertext.
6. Confirm that the original text is recovered.

## 6. Key management
The key is sensitive. Never commit `secret.key` to GitHub. The repository's ignore rules are intended to prevent this.

## 7. Important limitation
Loss of the correct key means encrypted data cannot be recovered. Do not delete or overwrite a required key.

## 8. Ethical use
Encrypt only data you are authorized to handle.
