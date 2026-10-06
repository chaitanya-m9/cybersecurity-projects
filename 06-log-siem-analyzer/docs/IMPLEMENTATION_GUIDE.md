# Implementation Guide — Log / SIEM Analyzer

## Problem
Security monitoring systems need to turn raw events into actionable alerts.

## Input
The educational parser expects lines containing a timestamp, FAILED_LOGIN event, username, and source IP.

## Detection
1. Read each event.
2. Parse fields with a regular expression.
3. Count failed logins by source IP and username.
4. Compare IP counts with a configurable threshold.
5. Print analyst-facing alerts.

## Investigation Note
A threshold alert is an indicator, not proof of compromise. Analysts should correlate with successful logins, user context, device ownership, geolocation, MFA events, and other telemetry.

## Testing
Run: python -m pytest tests
