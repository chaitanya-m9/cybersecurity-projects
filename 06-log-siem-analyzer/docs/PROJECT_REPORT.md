# Project Report — Log / SIEM Analyzer

## Abstract

This project demonstrates basic security monitoring by parsing synthetic authentication logs, counting failed login events, grouping activity by source IP and username, and generating threshold-based alerts.

## Problem Statement

Security teams receive large volumes of logs. Manual inspection is inefficient, so SIEM systems normalize, search, correlate, and alert on suspicious activity.

## Objectives

- Parse security events.
- Extract timestamp, username, and source IP.
- Aggregate failed authentication events.
- Identify high-volume sources.
- Generate analyst-readable alerts.
- Demonstrate SIEM concepts with safe synthetic data.

## Architecture

Log source → Parser → Normalization → Aggregation → Detection rule → Alert/report

## Example

```bash
python src/analyzer.py sample_logs/auth.log
```

The supplied sample contains repeated failures from `192.0.2.10`. Because the demonstration threshold is five failures, the analyzer generates an alert for that source.

## Detection Logic

```text
IF failed_login_count(source_ip) >= 5
THEN generate alert
```

This is a teaching rule, not a production detection rule.

## Test Cases

- No failed logins.
- One failed login.
- Five failures from one IP.
- Multiple users from one source.
- Multiple sources.
- Malformed line.
- Missing log file.

## SIEM Concepts Demonstrated

Event collection, parsing, filtering, aggregation, threshold detection, alert generation, and analyst investigation.

## Limitations

Only one synthetic log format is supported. There is no database, dashboard, time-window correlation, or threat-intelligence enrichment.

## Future Enhancements

- JSON/CSV output.
- Time-window detection.
- MITRE ATT&CK mapping.
- Splunk/Elastic/OpenSearch integration.
- Dashboard and risk scoring.

## Viva Questions

1. What is SIEM?
2. What is log normalization?
3. What is brute-force detection?
4. Why use thresholds?
5. What is correlation?
6. What is the difference between an event and an alert?
