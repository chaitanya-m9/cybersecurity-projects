# Complete Cybersecurity Projects Guide

## 1. Purpose

This repository is a practical cybersecurity portfolio designed to demonstrate secure programming, cryptography, endpoint monitoring, networking, and security-log analysis.

### Projects
1. Password Strength Checker
2. Text Encryption Tool
3. Image Encryption Tool
4. Safe Keylogger Monitor / Detection
5. Network Scanner
6. Log / SIEM Analyzer

## 2. Recommended Learning Order

Follow the projects in this order:

**Project 1 → Project 2 → Project 3 → Project 4 → Project 5 → Project 6**

This moves from authentication fundamentals to cryptography, endpoint security, networking, and finally SOC/SIEM analysis.

## 3. Common Environment Setup

### Windows

Install Python 3.x and verify:

```powershell
python --version
python -m pip --version
```

Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install project dependencies from the relevant project directory:

```powershell
python -m pip install -r requirements.txt
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## 4. Project Workflow

For every project use this lifecycle:

1. Read the project README.
2. Read its architecture document.
3. Create a virtual environment where dependencies are required.
4. Install requirements.
5. Run the basic example.
6. Test normal and invalid input.
7. Read the source code line by line.
8. Record observations.
9. Modify one feature.
10. Retest.
11. Document the result.
12. Commit the project to GitHub.

## 5. Documentation Expected for a College Project

For each project prepare:

- Title
- Abstract
- Introduction
- Problem statement
- Objectives
- Existing system
- Proposed system
- Requirements
- Technologies
- System architecture
- Modules
- Algorithm/workflow
- Implementation
- Test cases
- Results
- Security considerations
- Limitations
- Future enhancements
- Conclusion
- References
- Viva questions

## 6. Git Workflow

After making changes:

```bash
git status
git add .
git commit -m "Improve project documentation"
git push
```

Never commit:

- passwords
- API keys
- private keys
- personal data
- real authentication logs
- captured keystrokes
- unauthorized scan results

## 7. Ethical Use

Network scanning and security monitoring must only be performed against systems you own or have explicit permission to test.

The keylogger project is deliberately defensive. It does not capture, store, transmit, or replay keystrokes.

## 8. Portfolio Goal

After completing the six projects, you should be able to explain:

- CIA triad
- password security
- entropy
- authenticated encryption
- AES-GCM
- endpoint detection
- TCP and ports
- network reconnaissance
- log parsing
- brute-force detection
- SIEM concepts
- secure coding
- Git/GitHub workflows
