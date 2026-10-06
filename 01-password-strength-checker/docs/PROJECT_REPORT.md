# Project Report — Password Strength Checker

## 1. Introduction
Password quality is a fundamental authentication-security concern. This project evaluates passwords locally using multiple characteristics.

## 2. Objectives
- Measure password quality consistently.
- Demonstrate validation and regular expressions.
- Estimate theoretical character-pool entropy.
- Provide actionable recommendations without storing passwords.

## 3. Methodology
The program checks length, character classes, common-password membership, repeated characters, and predictable sequences. A score is converted into a human-readable strength level.

## 4. Input and Output
Input is a password entered locally. Output contains strength, estimated entropy, and recommendations. The password itself is not printed by the normal input flow.

## 5. Example
A long password containing uppercase, lowercase, numbers, and symbols receives a higher score than a short common password such as password.

## 6. Testing
Run: python -m pytest tests

Tests cover strong passwords, common passwords, and short passwords.

## 7. Security Considerations
Use synthetic passwords for demonstrations. Never store or commit real credentials.

## 8. Limitations
Rule-based scoring cannot determine whether a password appears in every breach corpus and does not replace a password manager or enterprise authentication policy.

## 9. Future Enhancements
Offline breached-password screening, configurable policies, GUI support, and broader test coverage.

## 10. Conclusion
The project demonstrates practical password-security concepts while keeping processing local and simple.
