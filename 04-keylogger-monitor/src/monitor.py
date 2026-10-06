"""Defensive filesystem monitor for possible keylogger indicators.
This program does NOT capture keyboard input.
Author: Chaitanya Mediboyina
"""
import argparse
import hashlib
import json
from pathlib import Path

SUSPICIOUS_NAMES = {"keylogger.py", "keylog.py", "pynput_logger.py", "keystrokes.txt", "keylog.txt"}
CODE_INDICATORS = ("pynput.keyboard", "keyboard.on_press", "keylogger")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def scan(root: Path):
    events = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            if path.name.lower() in SUSPICIOUS_NAMES:
                events.append({"type": "suspicious_filename", "path": str(path), "sha256": sha256(path)})
            if path.suffix.lower() == ".py":
                text = path.read_text(encoding="utf-8", errors="ignore").lower()
                indicators = [item for item in CODE_INDICATORS if item in text]
                if indicators:
                    events.append({"type": "suspicious_code_indicator", "path": str(path), "indicators": indicators})
        except (OSError, PermissionError):
            continue
    return events

def main():
    parser = argparse.ArgumentParser(description="Defensive keylogger-indicator monitor.")
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    root = Path(args.path)
    if not root.exists():
        raise SystemExit("Path does not exist")
    result = {"path": str(root.resolve()), "events": scan(root)}
    print(json.dumps(result, indent=2))
    Path("detection_report.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
