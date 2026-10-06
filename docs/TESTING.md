# Testing Guide
1. Test normal, empty, malformed, and boundary inputs.
2. Verify missing-file and invalid-data handling.
3. Never use real credentials, personal data, production logs, or unauthorized targets.
4. Verify generated cryptographic keys are ignored by Git.
5. For the network scanner, test only localhost or an explicitly authorized lab host.
6. For the keylogger monitor, verify it reports indicators without capturing keystrokes.