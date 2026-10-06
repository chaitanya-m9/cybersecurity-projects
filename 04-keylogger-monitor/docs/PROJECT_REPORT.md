# Project Report — Safe Keylogger Monitor

## 1. Introduction
Keylogging is a common endpoint-security concern. This project demonstrates defensive identification of possible indicators without implementing keyboard surveillance.

## 2. Safety Boundary
The program does not install hooks, capture typed characters, collect clipboard contents, or transmit user input.

## 3. Objectives
- Demonstrate endpoint-monitoring logic.
- Search an authorized directory for synthetic indicators.
- Hash suspicious files as evidence.
- Produce a machine-readable detection report.

## 4. Methodology
The scanner recursively examines an explicitly supplied directory, compares filenames against configured indicators, inspects Python source for selected strings, and records SHA-256 hashes for suspicious files.

## 5. Example
A synthetic file named keylog.txt or a test Python file containing a keylogger-related indicator can generate a finding.

## 6. Testing
Run: python -m pytest tests

Tests use temporary synthetic files and do not collect keyboard input.

## 7. Security Considerations
False positives are possible. Findings should be investigated using process telemetry, file reputation, signatures, persistence information, and other endpoint evidence.

## 8. Limitations
Simple filename and string indicators can be bypassed and are not equivalent to EDR behavioral detection.

## 9. Future Enhancements
Windows event-log integration, JSON severity fields, allowlists, process telemetry, and richer correlation.

## 10. Conclusion
The project teaches defensive keylogger detection concepts while maintaining a clear ethical and technical boundary against credential capture.
