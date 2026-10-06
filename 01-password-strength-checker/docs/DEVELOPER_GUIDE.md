# Developer Guide — Password Strength Checker

## Architecture
Input → validation → character-set analysis → common/repetition checks → entropy estimate → score/category → recommendations.

## Main concepts
- Regular expressions identify character classes.
- Entropy is estimated from password length and the detected character pool.
- A common-password check prevents misleading high scores for predictable values.
- Repeated-character detection identifies simple patterns.

## Extension points
1. Add dictionary checks.
2. Add breach-password checking through an approved privacy-preserving service.
3. Add unit tests.
4. Add a GUI.
5. Separate scoring logic from CLI input for easier testing.

## Secure coding notes
Never log passwords. Avoid writing entered passwords to files. If a GUI is added, disable password echo and clear sensitive variables where practical.

## Suggested development workflow
Create a small change → run existing tests → add a regression test → update documentation → commit.
