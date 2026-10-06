# Password Strength Checker

## Author
**Chaitanya Mediboyina** — https://github.com/chaitanya-m9

## Purpose
A local Python security utility that evaluates password quality using length, character diversity, common-password detection, and predictable-pattern checks.

## Objectives
- Demonstrate password-security fundamentals.
- Provide immediate local feedback without storing the password.
- Teach validation, scoring, regular expressions, and defensive coding.

## Workflow
Input → validation rules → score calculation → strength classification → security recommendations.

## Project Structure
- src/password_checker.py — application source
- tests/ — repeatable tests
- docs/ARCHITECTURE.md — design
- docs/PROJECT_REPORT.md — project report
- requirements.txt — dependencies

## Run
python src/password_checker.py

## Testing
python -m pytest tests

## Security
Use only test passwords. Never commit real credentials. The program does not intentionally transmit or persist passwords.

## Limitations
Rule-based scoring cannot prove that a password has not appeared in a breach. It is an educational checker, not an enterprise password policy engine.

## Future Work
Entropy estimation, offline breached-password screening, configurable policy rules, GUI, and stronger automated testing.
