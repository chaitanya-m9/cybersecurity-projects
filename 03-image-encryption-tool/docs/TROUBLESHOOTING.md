# Troubleshooting — Image Encryption Tool

## Dependency error
```powershell
python -m pip install -r requirements.txt
```

## File not found
Check the current directory and use the exact input path.

## Decryption authentication failure
Verify that the encrypted file was not modified and that the correct key is being used.

## Restored image cannot open
Confirm the original file was a valid image and that the output path was not overwritten by another process.
