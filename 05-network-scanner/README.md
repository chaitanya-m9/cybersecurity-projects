# Network Scanner

## Author
**Chaitanya Mediboyina** — https://github.com/chaitanya-m9

## Purpose
A small TCP connectivity scanner for learning socket programming, basic network discovery, and defensive asset inventory.

## Objectives
- Accept an explicitly chosen host and port range.
- Test TCP connectivity with controlled timeouts.
- Report reachable ports without exploitation.

## Run
python src/scanner.py 127.0.0.1 --start 1 --end 1024

## Safety
Only scan hosts and networks that you own or have explicit permission to assess. Use a local virtual machine or lab network for demonstrations.

## Workflow
Target + port range → TCP connection attempt → timeout/connection result → open-port report.

## Testing
python -m pytest tests

## Limitations
A TCP connect scan cannot identify every service and can be affected by firewalls, NAT, rate limits, and host availability.

## Future Work
Rate-limited concurrency, service identification in a lab, JSON/CSV output, IPv6 support, and richer unit tests.
