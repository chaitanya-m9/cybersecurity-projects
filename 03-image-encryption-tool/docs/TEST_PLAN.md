# Test Plan and Results — Image Encryption Tool

| ID | Test | Expected |
|---|---|---|
| IM-01 | Encrypt valid JPEG | Encrypted file created |
| IM-02 | Decrypt valid encrypted file | Restored image opens |
| IM-03 | Encrypt PNG | Successful encryption |
| IM-04 | Modify encrypted bytes | Authentication failure |
| IM-05 | Wrong key | Decryption failure |
| IM-06 | Missing input | Clear error |
| IM-07 | Empty file | Safe handling/error |

## Acceptance criteria
A valid encrypted file decrypts to the original bytes; tampering is detected; keys are not committed; invalid paths are handled cleanly.
