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
    checks = [(r"[a-z]", "lowercase"), (r"[A-Z]", "uppercase"), (r"\d", "digits"), (r"[^A-Za-z0-9]", "special characters")]
    for pattern, label in checks:
        if re.search(pattern, password): score += 1
        else: reasons.append(f"Add {label}.")
    if password.lower() in COMMON:
        score = 0
        reasons.append("This password is commonly used and should not be used.")
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1); reasons.append("Avoid repeated characters.")
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    rating = labels[min(score, 4)]
    return rating, entropy(password), reasons

if __name__ == "__main__":
    p = input("Enter a password to evaluate (local processing only): ")
    rating, ent, reasons = check(p)
    print(f"Strength: {rating}\nEstimated entropy: {ent:.1f} bits")
    for reason in reasons: print(f"- {reason}")
