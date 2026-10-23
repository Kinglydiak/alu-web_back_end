# Personal Data

This module provides regex-based redaction of sensitive fields in log messages.

- `filter_datum()` redacts selected field values using `re.sub`.
- `RedactingFormatter` applies redaction before formatting a log record.
- Sensitive values are replaced with `***`.
