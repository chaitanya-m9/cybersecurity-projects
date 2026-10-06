# Project Report — Safe Keylogger Monitor / Detection

## Abstract
A defensive endpoint scanner that identifies static indicators associated with keylogging software without capturing keystrokes.

## Objectives
- Demonstrate detection engineering.
- Generate evidence using file hashes and indicators.
- Preserve user privacy.
- Provide a safe cybersecurity learning project.

## Workflow
Authorized lab directory → indicator scan → SHA-256 evidence → JSON report → analyst investigation.

## Example
A synthetic file named `keylogger.py` containing a suspicious keyboard-library string triggers a detection event.

## Important Limitation
Static indicators can create false positives and can be bypassed by sophisticated malware. This is a learning detector, not an EDR replacement.

## Future Scope
Sysmon/process telemetry, YARA, Windows Event Logs, persistence analysis, process-tree correlation, and SIEM integration.