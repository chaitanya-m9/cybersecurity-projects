"""Local password strength checker. Author: Chaitanya Mediboyina."""
import getpass
import math
import re

COMMON = {"password", "password123", "123456", "12345678", "qwerty", "admin", "letmein", "welcome"}

def entropy(password: str) -> float:
    pool = 0
    pool += 26 if re.search(r"[a-z]", password) else 0
    pool += 26 if re.search(r"[A-Z]", password) else 0
    pool += 10 if re.search(r"\d", password) else 0
    pool += 33 if re.search(r"[^A-Za-z0-9]", password) else 0
    return len(password) * math.log2(pool) if pool else 0.0

def check(password: str):
    score = 0
    reasons = []
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: reasons.append("Use at least 8 characters; 12+ is preferable.")
    for pattern, label in [(r"[a-z]", "lowercase"), (r"[A-Z]", "uppercase"), (r"\d", "digits"), (r"[^A-Za-z0-9]", "special characters")]:
        if re.search(pattern, password): score += 1
        else: reasons.append(f"Add {label}.")
    if password.lower() in COMMON:
        score = 0
        reasons.append("This password is commonly used and should not be used.")
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)
        reasons.append("Avoid repeated characters.")
    if re.search(r"(1234|abcd|qwer)", password.lower()):
        score = max(0, score - 1)
        reasons.append("Avoid predictable sequences.")
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return labels[min(score, 4)], entropy(password), reasons

def main():
    password = getpass.getpass("Enter a test password: ")
    rating, ent, reasons = check(password)
    print(f"Strength: {rating}")
    print(f"Estimated entropy: {ent:.1f} bits")
    for reason in reasons:
        print(f"- {reason}")

if __name__ == "__main__":
    main()
