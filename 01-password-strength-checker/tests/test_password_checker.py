import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from password_checker import check

def test_strong_password():
    rating, entropy, _ = check("Chaitu!Secure2026")
    assert rating in {"Strong", "Very Strong"}
    assert entropy > 40

def test_common_password_is_weak():
    rating, _, reasons = check("password")
    assert rating == "Very Weak"
    assert reasons

def test_short_password():
    rating, _, _ = check("abc")
    assert rating == "Weak"
