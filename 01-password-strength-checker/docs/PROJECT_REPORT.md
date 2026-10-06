# Project Report — Password Strength Checker

## Abstract
A local Python utility that evaluates password quality through length, character diversity, common-password detection, repetition checks, and approximate entropy.

## Problem Statement
Weak passwords are a major authentication risk. Users need immediate feedback without sending passwords to an external service.

## Objectives
- Evaluate password characteristics locally.
- Explain weaknesses clearly.
- Estimate entropy.
- Avoid password storage/transmission.

## Modules
1. Input
2. Validation
3. Character-class analysis
4. Common-password check
5. Entropy calculation
6. Rating and recommendations

## Example
Input: `BlueRiver!47Moon`
Expected: strong/very strong classification with high estimated entropy.

## Limitations
The score is educational and is not a substitute for enterprise password policy or password-breach screening.

## Future Scope
Use zxcvbn-style analysis, breached-password checks through privacy-preserving methods, GUI support, and configurable organizational policies.