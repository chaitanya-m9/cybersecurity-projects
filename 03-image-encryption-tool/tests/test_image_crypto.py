import sys
from pathlib import Path
import tempfile
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from image_crypto import generate_key, encrypt, decrypt

def test_binary_round_trip():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        original = root / "sample.bin"
        encrypted = root / "sample.enc"
        recovered = root / "recovered.bin"
        original.write_bytes(bytes(range(256)))
        key = generate_key()
        encrypt(original, encrypted, key)
        decrypt(encrypted, recovered, key)
        assert recovered.read_bytes() == original.read_bytes()
