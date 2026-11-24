# SOC Phishing Email Investigation Report

## Incident Details

Incident ID: SOC-2026-001
Incident Type: Suspected Phishing
Severity: Medium (Training Classification)
Analyst: SOC Analyst L1

## Investigation Summary

A suspicious email claiming to originate
from a bank security team was investigated.

## Technical Findings

- Suspicious sender identified.
- SPF authentication failure observed.
- DKIM signature absent.
- DMARC authentication failure observed.
- Suspicious URL extracted.
- IP indicator identified.
- SHA-256 file hash generated.

## Tools Used

- Kali Linux
- Windows
- Python
- VirusTotal
- URLScan.io
- CyberChef

## Risk Assessment

Potential credential theft and
unauthorised account access.

## Recommended Response

- Quarantine suspicious email.
- Search for similar messages.
- Block confirmed malicious indicators.
- Investigate potentially affected accounts.
- Escalate confirmed compromise to SOC L2.

## Conclusion

The simulated email demonstrated multiple
phishing characteristics.

The investigation identified relevant
indicators and documented recommended
security response actions.

All indicators were fictional and used
for educational purposes.
