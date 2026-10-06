import argparse, socket

def scan(host,start,end,timeout=0.3):
    open_ports=[]
    for port in range(start,end+1):
        s=socket.socket(); s.settimeout(timeout)
        try:
            if s.connect_ex((host,port))==0: open_ports.append(port)
        finally: s.close()
    return open_ports

p=argparse.ArgumentParser(); p.add_argument("host"); p.add_argument("--ports",default="1-1024"); a=p.parse_args()
lo,hi=map(int,a.ports.split("-")); print(f"Scanning {a.host}:{lo}-{hi}")
for port in scan(a.host,lo,hi): print(f"OPEN {port}")
