# Network Scanner

Authorized-lab TCP connect scanner for discovering reachable services on a host. It uses Python sockets and reports open ports; it does not exploit services.

## Run
```bash
python src/scanner.py 127.0.0.1 --ports 1-1024
```

Only scan hosts you own or have explicit permission to test.