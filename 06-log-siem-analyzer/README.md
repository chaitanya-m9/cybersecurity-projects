# Log / SIEM Analyzer

Lightweight SIEM-style analyzer for structured authentication logs. It detects repeated failed logins, suspicious bursts, and summarizes events by source IP.

## Run
```bash
python src/analyzer.py sample_logs/auth.log
```
The sample data is synthetic and contains no real credentials.