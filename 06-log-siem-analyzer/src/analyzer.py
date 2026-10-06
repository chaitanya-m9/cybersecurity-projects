"""Defensive authentication-log analyzer.
Author: Chaitanya Mediboyina
"""
import argparse
import re
from collections import Counter

FAIL = re.compile(r"(?P<ts>\S+)\s+FAILED_LOGIN\s+user=(?P<user>\S+)\s+src=(?P<src>\S+)")

def analyze(path):
    ips, users = Counter(), Counter()
    total = 0
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = FAIL.search(line)
            if match:
                total += 1
                ips[match["src"]] += 1
                users[match["user"]] += 1
    return total, ips, users

def main():
    parser = argparse.ArgumentParser(description="Analyze synthetic authentication logs.")
    parser.add_argument("log")
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()
    if args.threshold < 1:
        parser.error("threshold must be positive")
    total, ips, users = analyze(args.log)
    print(f"Failed logins: {total}")
    print("By source IP:")
    for ip, count in ips.most_common():
        print(f"{ip}: {count}")
    print("By username:")
    for user, count in users.most_common():
        print(f"{user}: {count}")
    print("Alerts:")
    for ip, count in ips.items():
        if count >= args.threshold:
            print(f"ALERT {ip}: {count} failed logins")

if __name__ == "__main__":
    main()
