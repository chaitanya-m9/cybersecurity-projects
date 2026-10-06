# Implementation Guide — Password Strength Checker

## Problem
Weak and reused passwords are common authentication risks. This project provides local feedback before a password is used.

## Requirements
Python 3.x. No external service is required.

## Implementation
1. Read the password without echoing it when possible.
2. Check minimum and preferred length.
3. Detect lowercase, uppercase, digits, and special characters.
4. Reject common-password matches.
5. Reduce confidence for repeated or predictable patterns.
6. Estimate character-pool entropy.
7. Return a human-readable classification.

## Testing
Run: python -m pytest tests

Test categories include strong passwords, common passwords, and short passwords.

## Security Review
The application should not log the password. Demonstrations must use synthetic credentials.

## Deliverable Evidence
Source, tests, README, architecture, project report, and Git history document the implementation.
