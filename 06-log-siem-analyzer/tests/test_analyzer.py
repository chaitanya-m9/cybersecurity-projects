import sys
from pathlib import Path
import tempfile
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from analyzer import analyze

def test_failed_login_analysis():
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "events.log"
        path.write_text(
            "2026-01-01T10:00:00Z FAILED_LOGIN user=alice src=10.0.0.5\n"
            "2026-01-01T10:01:00Z FAILED_LOGIN user=alice src=10.0.0.5\n",
            encoding="utf-8"
        )
        total, ips, users = analyze(path)
        assert total == 2
        assert ips["10.0.0.5"] == 2
        assert users["alice"] == 2
