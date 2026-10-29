import re 

# E.164: "+" then country code and number, 8 to 15 digits in total, no leading 0.
E164_PATTERN = re.compile(r"^\+[1-9]\d{7,14}$")

def normalize_email(email: str) -> str:
    """Trim spaces and lowercase, so jane@x.com and Jane@x.com are one account."""
    return (email or "").strip().lower()

def normalize_phone(raw: str, default_country_code: str = "254") -> str:
    """Return the phone number in E.164 format (e.g. +254712345678).

    Accepts: 0712 345 678, 254712345678, 00254712345678, +254 712 345 678.
    Raises ValueError if the result is not a valid E.164 number.
    """
    cleaned = re.sub(r"[\s\-().]", "", raw or "")

    if cleaned.startswith("+"):
        pass
    elif cleaned.startswith("00"):
        cleaned = "+" + cleaned[2:]
    elif cleaned.startswith("0"):
        cleaned = "+" + default_country_code + cleaned[1:]
    elif cleaned.startswith(default_country_code):
        cleaned = "+" + cleaned

    if not E164_PATTERN.match(cleaned):
        raise ValueError("Enter a valid phone number, e.g. +254712345678.")
    return cleaned