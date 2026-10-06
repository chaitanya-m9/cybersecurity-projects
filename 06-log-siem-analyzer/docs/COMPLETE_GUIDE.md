# Complete Project Guide — Log / SIEM Analyzer

## Abstract
A lightweight SIEM-style analyzer that parses synthetic authentication events, aggregates failed logins by source IP/user, and applies a threshold alert rule.

## Objectives
- Understand security-event normalization.
- Parse structured log records.
- Aggregate events.
- Detect repeated authentication failures.
- Produce analyst-friendly results.

## Setup
```powershell
cd 06-log-siem-analyzer
python src/analyzer.py sample_logs/auth.log
```

## Step-by-step
1. Open the synthetic sample log.
2. Inspect event fields.
3. Run the analyzer.
4. Review counts by source IP and username.
5. Identify threshold alerts.
6. Add synthetic events.
7. Run again and compare.
8. Test malformed records.

## Architecture
Log file → parser → normalized event → aggregation → threshold rule → alerts/summary.

## Detection Logic
The educational rule alerts when failed-login count for a source IP reaches the configured threshold (five in the current implementation).

## SIEM Concepts
A SIEM combines collection, normalization, correlation, detection, and investigation workflows. This project demonstrates a small local subset.

## Test Plan
| ID | Test | Expected |
|---|---|---|
| SI-01 | Valid event | Parsed |
| SI-02 | Five failures from one IP | Alert |
| SI-03 | Four failures | No threshold alert |
| SI-04 | Multiple users | Correct aggregation |
| SI-05 | Malformed line | Safe handling |
| SI-06 | Empty log | Empty summary |
| SI-07 | Missing file | Clear error |

## Troubleshooting
- No events: compare the log format with the parser.
- Wrong count: inspect duplicate lines and IPs.
- Missing file: check the path.
- Real logs: sanitize sensitive information; use synthetic logs in GitHub.

## Security
Never commit real authentication logs, credentials, tokens, or personal information. Production thresholds should be configurable.

## Future Enhancements
Time-window correlation, multiple rules, severity, JSON/CSV output, dashboards, alert deduplication, and MITRE ATT&CK mapping.

## Viva Q&A
**What is SIEM?** Security Information and Event Management for collecting, correlating, detecting, and investigating security events.
**Why aggregate logs?** Patterns become easier to detect.
**What is threshold detection?** An alert is generated when a count reaches a defined limit.
**Why use synthetic logs?** They demonstrate the project without exposing sensitive data.

## Flowchart
```mermaid
flowchart TD
A[Start]-->B[Read log]
B-->C[Read line]
C-->D{Valid event?}
D-->|No|E[Skip or record malformed]
D-->|Yes|F[Normalize event]
F-->G[Aggregate by IP and user]
E-->H{More lines?}
G-->H
H-->|Yes|C
H-->|No|I[Apply threshold]
I-->J[Generate summary and alerts]
J-->K[End]
```
\n
## Recruiter Review — Sample Input, Output & Technical Evidence

### Sample Input
~~~text
2026-10-06T10:00:01Z FAILED_LOGIN user=admin src=192.0.2.10
2026-10-06T10:00:04Z FAILED_LOGIN user=admin src=192.0.2.10
2026-10-06T10:00:07Z FAILED_LOGIN user=test src=192.0.2.10
2026-10-06T10:00:10Z FAILED_LOGIN user=admin src=192.0.2.10
2026-10-06T10:00:14Z FAILED_LOGIN user=test src=192.0.2.10
2026-10-06T10:00:18Z FAILED_LOGIN user=admin src=198.51.100.25
~~~

The IP addresses shown are documentation/example ranges.

### Representative Output
~~~text
Failed login summary
--------------------
192.0.2.10 : 5 failures
ALERT: threshold reached

198.51.100.25 : 1 failure
No threshold alert
~~~

### Boundary Test
Four failures:
~~~text
Count = 4
Expected = No alert
~~~

Five failures:
~~~text
Count = 5
Expected = Alert
~~~

This verifies the detection-rule boundary.

### Test Matrix
| Test | Expected |
|---|---|
| Valid event | Parsed |
| Four failures | No threshold alert |
| Five failures | Alert |
| Multiple users | Correct aggregation |
| Malformed line | Safe handling |
| Empty log | Empty summary |
| Missing file | Clear error |

### Analyst Interpretation
Five failed logins are a detection signal, not automatic proof of compromise. An analyst should correlate time, account status, successful logins, device context, and other telemetry before deciding on an incident.

### What a Recruiter Can Evaluate
- Python log parsing
- Event normalization
- Security analytics
- Aggregation and threshold rules
- Detection engineering concepts
- Analyst reasoning
- Secure handling of security logs

### Interview Discussion
**Why normalize events?** Consistent fields make searching, aggregation, correlation, and detection easier.

**Why use synthetic logs?** They demonstrate functionality without exposing real credentials or organizational data.

**How would production detection improve?** Add time windows, multiple rules, severity, baselines, correlation, alert deduplication, and centralized telemetry.

### Portfolio Demonstration
A recruiter can inspect the supplied synthetic log, run the analyzer, add controlled events, and observe the alert threshold change. This demonstrates both coding and security-analysis reasoning.
