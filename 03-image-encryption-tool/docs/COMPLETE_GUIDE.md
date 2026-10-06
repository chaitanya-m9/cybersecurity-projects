# Complete Project Guide — Image Encryption Tool

## Abstract
A Python utility that protects image bytes using AES-GCM, combining confidentiality with authenticated integrity.

## Objectives
- Demonstrate AES-GCM.
- Generate a random nonce.
- Encrypt image bytes.
- Detect modified ciphertext.
- Restore original bytes after authentication.

## Setup and Commands
```powershell
cd 03-image-encryption-tool
python -m pip install -r requirements.txt
python src/image_crypto.py encrypt input.jpg encrypted.bin
python src/image_crypto.py decrypt encrypted.bin restored.jpg
```

## Step-by-step
1. Choose a non-sensitive test image.
2. Run encryption.
3. Confirm encrypted.bin exists.
4. Keep the generated key safe.
5. Run decryption.
6. Open restored.jpg.
7. Compare the restored result with the original.
8. Modify a copy of encrypted data and verify rejection.

## Architecture
CLI → key management → image bytes → random nonce → AES-GCM → encrypted container → decrypt/authenticate → restored image.

## Cryptographic Concepts
AES is symmetric encryption. GCM provides authenticated encryption. A unique nonce is required for each encryption operation under the same key.

## Test Plan
| ID | Test | Expected |
|---|---|---|
| IM-01 | JPEG encryption | Encrypted file |
| IM-02 | JPEG decryption | Valid restored image |
| IM-03 | PNG encryption | Successful |
| IM-04 | Modified ciphertext | Authentication failure |
| IM-05 | Wrong key | Failure |
| IM-06 | Missing file | Clear error |

## Troubleshooting
- Dependency issue: install requirements.
- File not found: verify the path.
- Authentication failure: check key and file integrity.
- Broken output: verify original input and output paths.

## Security
Never commit encryption keys. Do not overwrite originals by default. Test with copies.

## Future Enhancements
Secure key storage, metadata validation, key rotation, unit tests, GUI, and structured errors.

## Viva Q&A
**Why use AES-GCM?** It provides confidentiality plus authentication.
**What is a nonce?** A value used with encryption to make operations distinct; it must not be improperly reused with the same key.
**What happens if ciphertext changes?** Authentication should fail.

## Flowchart
```mermaid
flowchart TD
A[Start]-->B{Encrypt or decrypt}
B-->C[Load AES key]
C-->D[Read image bytes]
D-->E[Generate nonce]
E-->F[AES-GCM encrypt]
F-->G[Write encrypted container]
B-->H[Load key]
H-->I[Read container]
I-->J[Extract nonce]
J-->K[Decrypt and authenticate]
K-->L{Valid?}
L-->|Yes|M[Write restored image]
L-->|No|N[Reject]
G-->O[End]
M-->O
N-->O
```
