# Log / SIEM Analyzer

## Author
**Chaitanya Mediboyina** — https://github.com/chaitanya-m9

## Purpose
A defensive log-analysis project that processes synthetic authentication events and generates threshold-based alerts for repeated login failures.

## Objectives
- Learn event parsing and normalization.
- Build a simple detection rule.
- Group events by source IP.
- Demonstrate alert generation and false-positive analysis.

## Workflow
Log source → parse fields → filter failed logins → group by source IP → threshold rule → alert → analyst investigation.

## Run
python src/analyzer.py sample_logs/auth_events.csv --threshold 3

## SIEM Concepts
Event normalization, detection rules, thresholds, alert triage, false positives, and security monitoring.

## Testing
python -m pytest tests

## Limitations
Repeated failures alone do not prove brute force. Shared networks, NAT, user mistakes, password managers, and automation can create legitimate failures.

## Future Work
Time-windowed rules, JSON/Syslog support, MITRE ATT&CK mapping, severity scoring, dashboards, and multi-event correlation.
