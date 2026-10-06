import argparse, hashlib, json, time
from pathlib import Path

SUSPICIOUS_NAMES={"keylogger.py","keylog.py","pynput_logger.py","keystrokes.txt","keylog.txt"}

def sha256(p):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def scan(root):
    events=[]
    for p in root.rglob("*"):
        if not p.is_file(): continue
        if p.name.lower() in SUSPICIOUS_NAMES:
            events.append({"type":"suspicious_filename","path":str(p),"sha256":sha256(p)})
        if p.suffix.lower()==".py":
            text=p.read_text(errors="ignore").lower()
            indicators=[x for x in ("pynput.keyboard","keyboard.on_press","keylogger") if x in text]
            if indicators: events.append({"type":"suspicious_code_indicator","path":str(p),"indicators":indicators})
    return events

ap=argparse.ArgumentParser(); ap.add_argument("--path",required=True); a=ap.parse_args()
root=Path(a.path)
if not root.exists(): raise SystemExit("Path does not exist")
result={"timestamp":time.time(),"events":scan(root)}
print(json.dumps(result,indent=2)); Path("detection_report.json").write_text(json.dumps(result,indent=2))
