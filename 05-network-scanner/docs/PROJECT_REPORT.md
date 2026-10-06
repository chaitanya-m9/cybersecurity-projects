# Project Report — Network Scanner

## 1. Introduction
Network visibility is a basic requirement for defensive security. This project demonstrates controlled TCP connectivity testing in an authorized lab.

## 2. Objectives
- Learn Python socket programming.
- Test a bounded port range.
- Use connection timeouts.
- Report reachable TCP ports.

## 3. Methodology
For each selected port, the program creates a TCP socket, applies a timeout, attempts a connection, records successful connections, and closes the socket.

## 4. Example
python src/scanner.py 127.0.0.1 --start 1 --end 1024

The output lists reachable TCP ports on the local host.

## 5. Testing
Run: python -m pytest tests

The test suite validates port-range input without requiring a broad network scan.

## 6. Security Rules
Only scan hosts and networks you own or are authorized to assess. Prefer localhost or an isolated lab.

## 7. Limitations
TCP connectivity does not prove that a service is vulnerable and may not reveal filtered or UDP services.

## 8. Future Enhancements
Rate-limited concurrency, service identification in a lab, JSON/CSV reporting, IPv6 support, and richer test coverage.

## 9. Portfolio Value
The project demonstrates sockets, network fundamentals, input validation, timeouts, and responsible dual-use security practice.

## 10. Conclusion
The scanner is intentionally small and controlled so the core networking concepts are easy to understand and test safely.
