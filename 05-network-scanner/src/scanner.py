"""Controlled TCP connectivity scanner for authorized labs.
Author: Chaitanya Mediboyina
"""
import argparse
import socket

def scan(host: str, start: int, end: int, timeout: float = 0.3):
    if not 1 <= start <= end <= 65535:
        raise ValueError("Port range must be 1..65535.")
    open_ports = []
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Authorized TCP port scanner.")
    parser.add_argument("host")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=1024)
    parser.add_argument("--timeout", type=float, default=0.3)
    args = parser.parse_args()
    print(f"Scanning {args.host}:{args.start}-{args.end}")
    for port in scan(args.host, args.start, args.end, args.timeout):
        print(f"OPEN TCP {port}")

if __name__ == "__main__":
    main()
