# Test Plan and Results — Text Encryption Tool

| ID | Test | Expected |
|---|---|---|
| TX-01 | Encrypt normal text | Ciphertext produced |
| TX-02 | Decrypt valid ciphertext | Original plaintext restored |
| TX-03 | Empty text | Safe handling |
| TX-04 | Modified ciphertext | Authentication/decryption failure |
| TX-05 | Wrong key | Decryption failure |
| TX-06 | Unicode text | Correct round trip |
| TX-07 | Missing key | Tool creates/handles key according to implementation |

## Acceptance criteria
Confidentiality and integrity are preserved for supported inputs; invalid ciphertext does not crash the application; secret material is not committed.
