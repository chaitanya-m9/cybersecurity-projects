# User Guide — Safe Keylogger Monitor

## Purpose
This project is a defensive detector for suspicious keylogger-related files and static indicators. It is deliberately not a keylogger.

## Safety boundary
It does **not** capture keyboard events, collect credentials, hide itself, persist covertly, or transmit keystrokes.

## Setup
```powershell
cd 04-keylogger-monitor
python src/monitor.py --path ./lab_samples
```

Use a directory containing harmless fictional test files.

## Step-by-step demonstration
1. Create a lab folder.
2. Place a harmless Python file containing a test indicator such as the text `keylogger`.
3. Run the monitor against that folder.
4. Review the JSON detection report.
5. Inspect the reported filename, indicator, and SHA-256 hash.
6. Remove the test artifact after the lab.

## Example result
A file named `keylog.txt` or a Python file containing a known static indicator may be flagged. A flag is an indicator for investigation, not proof of malware.

## Ethical use
Scan only systems/directories you own or are explicitly authorized to assess.
