# Implementation Guide — Safe Keylogger Monitor

## Problem
Defenders need methods to identify suspicious keylogging indicators without deploying a credential-capture tool.

## Safety Design
This implementation performs filesystem inspection only. It does not register keyboard hooks, collect typed characters, capture clipboard contents, or transmit user input.

## Detection
1. Walk an explicitly selected directory.
2. Compare filenames with synthetic suspicious indicators.
3. Inspect Python source text for a small set of keylogging-related strings.
4. Hash suspicious files for evidence.
5. Produce a JSON detection report.

## Limitations
String matching is easy to evade and can create false positives. Real endpoint detection requires richer telemetry.

## Testing
Run: python -m pytest tests

Tests use synthetic temporary files and do not collect keyboard input.
