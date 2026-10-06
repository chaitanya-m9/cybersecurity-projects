import argparse,re
from collections import Counter
FAIL=re.compile(r"(?P<ts>\S+)\s+FAILED_LOGIN\s+user=(?P<user>\S+)\s+src=(?P<src>\S+)")
def analyze(path):
    ips=Counter(); users=Counter(); total=0
    for line in open(path,encoding="utf-8"):
        m=FAIL.search(line)
        if m: total+=1; ips[m["src"]]+=1; users[m["user"]]+=1
    return total,ips,users
p=argparse.ArgumentParser(); p.add_argument("log"); a=p.parse_args()
total,ips,users=analyze(a.log)
print(f"Failed logins: {total}\n\nBy source IP:")
for ip,n in ips.most_common(): print(f"{ip}: {n}")
print("\nBy username:")
for u,n in users.most_common(): print(f"{u}: {n}")
print("\nAlerts (threshold >=5):")
for ip,n in ips.items():
    if n>=5: print(f"ALERT {ip}: {n} failed logins")