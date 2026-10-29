import uuid

import pytest
from django.db import IntegrityError

from apps.accounts.models import AccountStatus, User

pytestmark = pytest.mark.django_db


def make_user(**overrides):
    data = {
        "email": "Jane@Example.com",
        "phone_number": "0712345678",
        "password": "S0me-long-passphrase!",
        "first_name": "Jane",
        "last_name": "Doe",
    }
    data.update(overrides)
    return User.objects.create_user(**data)


def test_user_is_created_with_normalised_values_and_uuid():
    user = make_user()
    assert isinstance(user.id, uuid.UUID)
    assert user.email == "jane@example.com"
    assert user.phone_number == "+254712345678"


def test_new_user_defaults():
    user = make_user()
    assert user.account_status == AccountStatus.REGISTERED
    assert user.is_email_verified is False
    assert user.is_phone_verified is False
    assert user.is_active is True


def test_password_is_hashed_not_stored_in_plaintext():
    user = make_user()
    assert user.password != "S0me-long-passphrase!"
    assert user.check_password("S0me-long-passphrase!")


def test_email_uniqueness_ignores_case():
    make_user()
    with pytest.raises(IntegrityError):
        make_user(email="JANE@example.com", phone_number="0799999999")


def test_full_name_skips_empty_middle_name():
    assert make_user().full_name == "Jane Doe"
    assert make_user(email="a@b.com", phone_number="0700000001", middle_name="Wanjiru").full_name == "Jane Wanjiru Doe"