import pytest

from apps.accounts.normalizers import normalize_email, normalize_phone


def test_email_is_trimmed_and_lowercased():
    assert normalize_email("  Jane.Doe@Example.COM ") == "jane.doe@example.com"


@pytest.mark.parametrize(
    "raw",
    ["0712 345 678", "254712345678", "+254 712-345-678", "00254712345678"],
)
def test_kenyan_phone_formats_become_e164(raw):
    assert normalize_phone(raw) == "+254712345678"


@pytest.mark.parametrize("raw", ["", "abc", "12345", "+0123456789"])
def test_invalid_phone_is_rejected(raw):
    with pytest.raises(ValueError):
        normalize_phone(raw)