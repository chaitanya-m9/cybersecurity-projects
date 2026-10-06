# Project Report — Network Scanner

## Abstract
An authorized-lab TCP connect scanner that identifies reachable ports using Python sockets.

## Objectives
- Understand TCP connectivity.
- Identify exposed services.
- Learn basic network reconnaissance.
- Demonstrate responsible security testing.

## Workflow
Target + port range → socket connection → timeout/error handling → open-port result.

## Example
`python src/scanner.py 127.0.0.1 --ports 1-1024`

## Interpretation
An open port indicates a service is reachable; it does not automatically mean the service is vulnerable.

## Safety
Only scan systems for which permission exists.

## Future Scope
Concurrency, service detection, CIDR support, JSON reports, rate limiting, IPv6, and authorized banner analysis.