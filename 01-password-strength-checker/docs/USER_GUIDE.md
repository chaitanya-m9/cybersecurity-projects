# User Guide — Password Strength Checker

## 1. Purpose
This tool evaluates a password using length, character diversity, estimated entropy, common-password checks, and repeated-character checks. It is an educational password-hygiene tool; it does not crack passwords.

## 2. Prerequisites
- Python 3.10+
- Terminal / PowerShell
- No third-party packages

## 3. Setup
```powershell
cd 01-password-strength-checker
python src/password_checker.py
```

## 4. Step-by-step usage
1. Start the program.
2. Enter a test password when prompted.
3. Review the score/category.
4. Read the recommendations.
5. Test several fictional examples to understand how length and character diversity affect the result.

## 5. Example
Example input: `BlueTiger!2026`
Expected behavior: the program reports a stronger result than a short password such as `hello123`.

Never use a real password for demonstrations.

## 6. What the result means
- Very Weak: highly predictable or too short.
- Weak: limited resistance to guessing.
- Moderate: reasonable complexity but improvable.
- Strong: good length and diversity.
- Very Strong: long, diverse, and not detected as common.

## 7. Learning exercise
Modify the scoring weights, add more common passwords to the local test set, then rerun the test cases.

## 8. Ethical use
Use only fictional passwords or passwords created specifically for testing. Do not collect or store other people's credentials.
