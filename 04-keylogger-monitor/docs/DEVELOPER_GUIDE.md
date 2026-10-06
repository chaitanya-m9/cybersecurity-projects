# Developer Guide — Safe Keylogger Monitor

## Architecture
Path selection → recursive file enumeration → filename/content indicator checks → SHA-256 hashing → detection records → JSON report.

## Detection philosophy
The tool uses transparent static indicators instead of executing suspicious code. This reduces risk during a classroom demonstration.

## Extension points
- Add configurable indicator files.
- Add file-size/type filters.
- Add allowlists for known-good lab files.
- Add severity levels.
- Add YARA integration in an isolated defensive lab.
- Add unit tests for each detector.

## False positives
Words such as `keylogger` may occur in documentation or security tools. Treat detections as triage signals and investigate context before declaring maliciousness.

## Safety requirement
Never add code that captures real keystrokes or credentials to this project.
