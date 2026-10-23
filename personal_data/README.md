# Personal Data

This module provides regex-based filtering and redaction of sensitive log fields.

- `filter_datum()` redacts selected field values.
- `RedactingFormatter` applies redaction before formatting a log record.
- `PII_FIELDS` lists five fields selected for redaction.
- `get_logger()` returns the configured `user_data` logger.
