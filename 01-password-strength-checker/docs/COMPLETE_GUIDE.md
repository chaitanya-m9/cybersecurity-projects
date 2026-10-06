# Complete Project Guide — Password Strength Checker

## Abstract
A defensive Python tool that evaluates password quality using length, character diversity, entropy estimation, common-password detection, repetition detection, and recommendations.

## Objectives
- Measure password characteristics.
- Detect common/predictable patterns.
- Produce a human-readable strength category.
- Teach authentication-security fundamentals.
- Never store or transmit passwords.

## Requirements
Python 3.10+; standard library; Windows/Linux/macOS terminal.

## Setup and Usage
1. Enter the project directory.
2. Run ```powershell
python src/password_checker.py
```
3. Enter only a fictional test password.
4. Review the category and recommendations.
5. Repeat with several test cases.

Example: 'BlueTiger!2026' should generally score better than 'abc123'. Exact scoring depends on the implementation.

## Architecture
Input → validation → character-set analysis → common/repetition checks → entropy estimate → scoring → category → recommendations.

## Algorithm
1. Read password.
2. Calculate length.
3. Detect lowercase, uppercase, digits, and special characters.
4. Estimate character pool and entropy.
5. Check common-password set.
6. Check repeated characters.
7. Calculate score.
8. Assign strength category.
9. Display recommendations.

## Test Plan
| ID | Case | Expected |
|---|---|---|
| PW-01 | Empty | Safe handling |
| PW-02 | abc | Very Weak/Weak |
| PW-03 | password | Common-password warning |
| PW-04 | Fictional mixed password | Higher score |
| PW-05 | Repeated characters | Repetition warning |
| PW-06 | Long fictional passphrase | Strong depending on composition |

## Troubleshooting
- If Python is not found, install Python or use the Python launcher.
- If the score seems unexpected, inspect length, character classes, repetition, and common-password matching.
- Never debug with a real password.

## Security
Do not log, save, upload, or commit entered passwords. A score is only an estimate.

## Future Enhancements
Dictionary scoring, privacy-preserving breach checks, unit tests, GUI, configurable scoring, and passphrase guidance.

## Viva Q&A
**What is entropy?** An estimate of uncertainty based on length and assumed character space.
**Why check common passwords?** A complex-looking password can still be easy to guess if common.
**Does this prove a password is secure?** No; it is an educational heuristic.
**Why should passwords not be logged?** Logs can expose credentials.

## Flowchart
```mermaid
flowchart TD
A[Start]-->B[Read fictional test password]
B-->C[Measure length]
C-->D[Detect character classes]
D-->E[Common password check]
E-->F[Repetition check]
F-->G[Estimate entropy]
G-->H[Calculate score]
H-->I[Assign category]
I-->J[Recommendations]
J-->K[Display result]
K-->L[End]
```
\n
## Recruiter Review — Sample Input, Output & Technical Evidence

### Sample Input 1 — Weak Password
~~~text
Enter password: abc123
~~~

### Sample Output
~~~text
Length: 6
Lowercase: Yes
Uppercase: No
Digits: Yes
Special characters: No
Common/predictable pattern: Detected
Strength: Weak
Recommendation: Use a longer, unique passphrase with stronger diversity.
~~~

### Sample Input 2 — Stronger Fictional Password
~~~text
Enter password: BlueTiger!2026
~~~

### Representative Output
~~~text
Length: 14
Lowercase: Yes
Uppercase: Yes
Digits: Yes
Special characters: Yes
Common password: No
Repeated-character warning: No
Estimated entropy: [calculated by implementation]
Strength: Strong
~~~

The exact numerical score is implementation-dependent; the important engineering evidence is that multiple security characteristics contribute to the result.

### Test Evidence
| Test | Input | Expected |
|---|---|---|
| PW-01 | Empty | Safe handling |
| PW-02 | abc123 | Weak classification |
| PW-03 | password | Common-password warning |
| PW-04 | BlueTiger!2026 | Higher score |
| PW-05 | AAAAAAAAAAAA | Repetition warning |
| PW-06 | Long fictional passphrase | Stronger result |

### What a Recruiter Can Evaluate
- Python input handling and validation
- Regular-expression based character analysis
- Entropy/security concepts
- Rule-based risk scoring
- Defensive treatment of credential data
- Ability to explain limitations rather than overclaiming security

### Technical Interview Discussion
**Why is length important?** Increasing length generally increases the search space substantially.

**Why is a common-password check necessary?** Attackers prioritize known/common passwords instead of blindly trying every combination.

**Why is this only a heuristic?** Real password security also depends on uniqueness, breach exposure, MFA, authentication controls, and password storage.

### Portfolio Demonstration
A recruiter can reproduce the project locally, compare weak and strong fictional inputs, inspect the source code, and review the documented test cases without requiring any external service.
