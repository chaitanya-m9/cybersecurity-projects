# Safe Keylogger Monitor / Detection

Defensive endpoint-monitoring project. It does **not** capture or store keystrokes. Instead, it watches an explicit test directory for suspicious files/process indicators and records safe detection events.

## Run
```bash
python src/monitor.py --path ./lab_samples
```

This design demonstrates detection engineering without building credential-stealing functionality.