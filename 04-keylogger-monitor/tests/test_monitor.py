import sys
from pathlib import Path
import tempfile
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from monitor import scan

def test_safe_indicator_scan():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "notes.txt").write_text("normal file", encoding="utf-8")
        assert isinstance(scan(root), list)

def test_detects_configured_filename():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "keylog.txt").write_text("synthetic test", encoding="utf-8")
        findings = scan(root)
        assert any(x["type"] == "suspicious_filename" for x in findings)
