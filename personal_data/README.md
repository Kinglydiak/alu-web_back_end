# Personal Data

This module provides regex-based filtering of sensitive fields in log messages.

## Function

`filter_datum(fields, redaction, message, separator)` replaces the values of
the specified fields with the redaction string using a single regular expression
and `re.sub`.

## Example

Input:

`name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;`

Output:

`name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;`
