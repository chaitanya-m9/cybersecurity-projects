import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from text_crypto import generate_key, encrypt_text, decrypt_text

def test_round_trip():
    key = generate_key()
    message = "Cybersecurity lab message"
    token = encrypt_text(message, key)
    assert decrypt_text(token, key) == message

def test_wrong_key_rejected():
    key1 = generate_key()
    key2 = generate_key()
    token = encrypt_text("secret", key1)
    try:
        decrypt_text(token, key2)
    except ValueError:
        return
    raise AssertionError("Wrong key should be rejected")
