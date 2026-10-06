import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from scanner import scan

def test_invalid_range():
    try:
        scan("127.0.0.1", 0, 10)
    except ValueError:
        return
    raise AssertionError("Invalid range should raise ValueError")
