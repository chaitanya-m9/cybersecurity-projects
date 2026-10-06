# Test Plan and Results — Password Strength Checker

## Test matrix

| ID | Input class | Example | Expected |
|---|---|---|---|
| PW-01 | Empty | empty string | Weak result / safe handling |
| PW-02 | Short | `abc` | Very Weak/Weak |
| PW-03 | Lowercase | `password` | Common-password warning |
| PW-04 | Mixed | `BlueTiger!2026` | Stronger score |
| PW-05 | Repetition | `AAAAAAAAAAAA` | Repetition warning |
| PW-06 | Symbols | fictional mixed password | Higher diversity score |
| PW-07 | Very long | fictional passphrase | Strong/Very Strong depending on composition |

## Acceptance criteria
- Program does not crash on empty input.
- No password is written to a log.
- Common values are flagged.
- Results are reproducible for the same input.
- Recommendations are understandable.

## Manual verification
Run the CLI after each code change and compare output against the expected category.
