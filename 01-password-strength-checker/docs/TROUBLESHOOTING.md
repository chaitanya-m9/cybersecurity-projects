# Troubleshooting — Password Strength Checker

## `python` is not recognized
Install Python and enable PATH, or use the Python launcher:
```powershell
py src/password_checker.py
```

## Unexpected score
Check password length, character classes, repeated characters, and whether the value appears in the common-password set.

## Program closes immediately
Run it from PowerShell/Command Prompt so the output remains visible.

## Security issue during testing
Do not paste a real password. Create a fictional test password instead.
