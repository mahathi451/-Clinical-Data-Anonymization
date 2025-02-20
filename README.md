# Clinical Data Anonymization Suite

HIPAA/GDPR-compliant de-identification toolkit for clinical trial data.

## Features
- Field-level pseudonymization
- K-anonymity verification
- Cryptographic encryption of sensitive fields
- Re-identification risk assessment

## Usage
from anonymize.core import ClinicalAnonymizer
anonymizer = ClinicalAnonymizer("config/privacy_rules.yaml")
safe_data = anonymizer.pseudonymize(raw_data)
risk_report = anonymizer.risk_assessment(safe_data)
text

## Compliance
- Automated audit logging
- Key management integration (AWS KMS supported)
- Data retention policy enforcement

## Requirements
- Python 3.9+
- pandas >= 2.0.0
- cryptography >= 41.0.0
