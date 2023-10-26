import re

name = r"^[A-Z][A-z-]*\s{1}[A-Z][A-z-]*\b|^[A-Z][A-z'-]*\b"
name_regex = re.compile(name)

phone_number = r"(\d{10}|\(\d{3}\) ?\d{3}-?\d{4}|\d{3}-?\d{3}-?\d{4})"
phone_regex = re.compile(phone_number)

email_address = r"[A-z][A-z.0-9]*@[a-z]*.[a-z]*\b"
email_regex = re.compile(email_address)
