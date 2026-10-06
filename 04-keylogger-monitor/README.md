# Safe Keylogger Monitor

## Author
**Chaitanya Mediboyina** — https://github.com/chaitanya-m9

## Purpose
A defensive process-monitoring project that demonstrates how a security analyst can look for configured process-name indicators associated with possible keylogging software.

## Critical Safety Boundary
This project DOES NOT capture, record, store, or transmit keyboard input. It is intentionally limited to defensive process metadata so it can be used safely for cybersecurity education.

## Objectives
- Learn endpoint-monitoring concepts.
- Enumerate running processes.
- Compare process metadata with configurable indicators.
- Explain why simple indicators can produce false positives.

## Workflow
Process enumeration → indicator normalization → comparison → finding → analyst review.

## Run
pip install -r requirements.txt
python src/monitor.py

## Testing
python -m pytest tests

## Limitations
Process-name matching is weak by itself. Mature EDR solutions combine process ancestry, hashes, signatures, modules, memory telemetry, persistence indicators, and behavioral analytics.

## Future Work
Windows event-log integration, structured JSON alerts, allowlists, severity scoring, and additional defensive telemetry.
