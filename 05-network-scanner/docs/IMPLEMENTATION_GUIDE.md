# Implementation Guide — Network Scanner

## Problem
Security teams need basic visibility into reachable services on authorized systems.

## Implementation
1. Accept a host and bounded port range.
2. Create a TCP socket per port.
3. Apply a short timeout.
4. Attempt a connection.
5. Report successful connections.
6. Close each socket immediately.

## Safety
Use localhost, a private lab VM, or another explicitly authorized target. Do not scan public systems without permission.

## Testing
Run: python -m pytest tests

The automated test validates input safety without performing a broad network scan.
