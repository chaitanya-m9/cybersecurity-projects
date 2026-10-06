# Complete Cybersecurity Projects Handbook

## Purpose
This repository is a hands-on cybersecurity portfolio for learning defensive security, secure coding, cryptography, networking, endpoint monitoring, and SIEM-style analysis.

## Environment
Recommended: Windows 10/11 or Linux, Python 3.11+, VS Code, Git, and a terminal. Create a virtual environment for projects that use third-party packages.

### Common setup
```powershell
git clone https://github.com/chaitanya-m9/cybersecurity-projects.git
cd cybersecurity-projects
python --version
```

If `python` is unavailable on Windows, try `py --version`. Create a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 1. Password Strength Checker

## Objective
Evaluate password quality locally without storing or transmitting the password.

## Concepts
- Length and character diversity
- Common-password detection
- Repeated-character detection
- Approximate entropy
- Authentication hygiene

## Steps
1. Open `01-password-strength-checker`.
2. Review `src/password_checker.py`.
3. Run:
```bash
python src/password_checker.py
```
4. Enter a test password.
5. Review the rating, entropy estimate, and recommendations.

## Examples
Weak:
```
password123
```
Expected result: weak/common-password warning.

Better:
```
BlueRiver!47Moon
```
Expected result: strong or very strong depending on the scoring rules.

## Test cases
- Empty password
- 7-character password
- 8-character mixed password
- 12+ character passphrase
- Common password
- Repeated characters such as `aaa`

## Security notes
Entropy is an estimate, not a complete password-security measurement. Real authentication systems should use salted password hashing such as Argon2id/bcrypt rather than storing plaintext passwords.

---

# 2. Text Encryption Tool

## Objective
Protect text confidentiality using authenticated encryption provided by the Python cryptography library.

## Concepts
- Symmetric encryption
- Key management
- Confidentiality
- Integrity/authentication
- Fernet tokens

## Steps
```bash
cd 02-text-encryption-tool
python -m pip install -r requirements.txt
python src/text_crypto.py
```

Choose `1` to encrypt. Example:
```
Plaintext: Cybersecurity portfolio
```
The program produces ciphertext.

Choose `2`, paste the ciphertext, and use the same local key to decrypt.

## Important
The generated `secret.key` is sensitive. Never upload it to GitHub. If the key is lost, encrypted data cannot be recovered.

## Test cases
1. Encrypt ordinary text.
2. Decrypt the resulting ciphertext.
3. Change one ciphertext character and confirm decryption fails.
4. Delete the key and confirm old ciphertext cannot be decrypted with a new key.
5. Test Unicode text.

## Production considerations
For a real application, use secure key storage such as an OS keyring or a managed secrets service rather than a local key file.

---

# 3. Image Encryption Tool

## Objective
Encrypt image bytes using AES-256-GCM so confidentiality and integrity are protected.

## Why AES-GCM?
GCM provides authenticated encryption: unauthorized modification of ciphertext is detected during decryption.

## Steps
```bash
cd 03-image-encryption-tool
python -m pip install -r requirements.txt
python src/image_crypto.py encrypt photo.jpg encrypted.bin
python src/image_crypto.py decrypt encrypted.bin restored.jpg
```

Then compare `photo.jpg` and `restored.jpg`.

## Example workflow
Input: `college_photo.jpg`
Output: `encrypted.bin`
Decryption output: `restored.jpg`

The encrypted file is not intended to be opened as a normal image.

## Test cases
- JPEG input
- PNG input
- Empty file
- Missing input
- Modified encrypted bytes
- Wrong/missing key

## Security notes
Use a unique nonce for every encryption operation. Do not reuse AES-GCM nonces with the same key. Never commit encryption keys.

---

# 4. Safe Keylogger Monitor / Detection

## Objective
Demonstrate defensive detection engineering without building a keylogger.

## Safety boundary
This project does NOT:
- capture keystrokes
- record passwords
- install persistence
- hide itself
- transmit captured data
- evade antivirus

It instead scans an authorized laboratory directory for suspicious filenames and static code indicators.

## Steps
Create a laboratory directory and place synthetic test files inside it:
```
lab_samples/
  keylogger.py
  normal_script.py
```

Run:
```bash
cd 04-keylogger-monitor
python src/monitor.py --path ./lab_samples
```

The tool generates `detection_report.json`.

## Example indicator
A synthetic file containing a string such as `pynput.keyboard` can trigger a detection event.

## Interpretation
A detection is an indicator, not proof of malware. Analysts should investigate file origin, hash, signer, parent process, persistence mechanisms, and endpoint telemetry.

## Test cases
- Normal Python file
- Synthetic suspicious filename
- Synthetic suspicious code indicator
- Empty directory
- Invalid path

## Future defensive improvements
- Windows Event Log integration
- Sysmon telemetry
- Process-tree correlation
- Startup/persistence checks
- YARA rules
- SIEM forwarding
- Alert severity and analyst workflow

---

# 5. Network Scanner

## Objective
Identify reachable TCP ports on an authorized host.

## Legal/ethical requirement
Only scan systems you own or have explicit permission to test. Do not scan public IP ranges, university/company networks, or third-party systems without authorization.

## Steps
Test localhost first:
```bash
cd 05-network-scanner
python src/scanner.py 127.0.0.1 --ports 1-1024
```

Example:
```
Scanning 127.0.0.1:1-1024
OPEN 135
OPEN 445
```
Actual results depend on services running on the test machine.

## Concepts
- TCP three-way handshake
- Port states
- Socket timeout
- Service exposure
- Attack surface

## Test cases
- localhost
- known lab VM
- small authorized port range
- closed port
- unreachable host

## Improvements
- Concurrent scanning
- Service/version identification
- CIDR parsing
- JSON/CSV output
- Rate limiting
- IPv6
- Optional banner collection only in authorized labs

---

# 6. Log / SIEM Analyzer

## Objective
Parse authentication events and identify repeated failed-login activity.

## Steps
```bash
cd 06-log-siem-analyzer
python src/analyzer.py sample_logs/auth.log
```

The sample log is synthetic and uses documentation IP ranges.

## Example
If an IP produces six failed logins, the analyzer reports an alert because the example threshold is five.

## SIEM concepts demonstrated
- Log ingestion
- Parsing
- Normalization
- Aggregation
- Threshold detection
- Alert generation
- Analyst triage

## Investigation workflow
1. Identify source IP.
2. Count failures.
3. Identify targeted usernames.
4. Check event time range.
5. Correlate with successful logins.
6. Check endpoint/network telemetry.
7. Determine whether activity is benign or malicious.
8. Document the incident and response.

## Test cases
- No failed logins
- One failed login
- Five failures
- More than five failures
- Multiple source IPs
- Multiple usernames
- Malformed log lines

## Future improvements
- JSON/CSV output
- Time-window detection
- Geo/IP enrichment
- MITRE ATT&CK mapping
- Severity scoring
- Dashboard
- Splunk/Elastic integration
- Automated incident tickets

---

# Git/GitHub Workflow

After local changes:
```bash
git status
git add .
git commit -m "Improve cybersecurity portfolio documentation"
git push origin main
```

Never commit:
- passwords
- API keys
- private keys
- `.env` files
- real customer/company logs
- captured keystrokes
- confidential screenshots

## Portfolio presentation
For each project, explain:
1. Problem
2. Objective
3. Architecture
4. Technologies
5. Implementation
6. Example execution
7. Testing
8. Security controls
9. Limitations
10. Future enhancements

## Interview preparation
Be ready to explain:
- Why authenticated encryption is preferred over homemade encryption.
- Difference between hashing and encryption.
- Why AES-GCM needs a unique nonce.
- How TCP port scanning works.
- Difference between detection and prevention.
- What a SIEM does.
- How brute-force detection works.
- Why false positives occur.
- Why authorization matters in security testing.

## Final portfolio checklist
- [ ] Every project has source code.
- [ ] Every project has README and architecture documentation.
- [ ] Requirements are documented.
- [ ] Test cases are documented.
- [ ] Examples are synthetic/safe.
- [ ] Secrets are excluded from Git.
- [ ] Network scanning is restricted to authorized targets.
- [ ] Keylogger project remains detection-only.
- [ ] Resume descriptions are ready.
- [ ] GitHub repository is clean and understandable.
