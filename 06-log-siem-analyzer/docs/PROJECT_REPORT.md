# Project Report — Log / SIEM Analyzer

## 1. Introduction
Security operations teams transform large volumes of events into alerts. This project demonstrates a simple authentication-failure detection rule.

## 2. Objectives
- Parse security events.
- Aggregate failed logins by source IP and username.
- Apply a configurable threshold.
- Produce analyst-readable alerts.

## 3. Methodology
The parser reads synthetic log lines, extracts timestamp, username, and source IP, counts events, and generates an alert when an IP reaches the selected threshold.

## 4. Example
If an IP produces five or more FAILED_LOGIN events, the analyzer reports it for investigation.

## 5. Testing
Run: python -m pytest tests

The test suite verifies event parsing and aggregation with temporary synthetic data.

## 6. Analyst Interpretation
A threshold alert is an indicator, not proof of compromise. Investigate user context, device ownership, successful logins, MFA events, and other telemetry.

## 7. Security Considerations
Do not commit production logs containing personal or confidential information. Use synthetic logs in this repository.

## 8. Limitations
A single threshold rule has limited context and can generate false positives.

## 9. Future Enhancements
Time-window correlation, JSON/Syslog support, MITRE ATT&CK mapping, severity scoring, dashboards, and multi-event correlation.

## 10. Conclusion
The project introduces the fundamental SIEM workflow of parsing, normalization, detection, alerting, and analyst investigation.
