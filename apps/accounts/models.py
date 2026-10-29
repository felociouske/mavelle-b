from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from apps.core.models import TimestampedModel, UUIDModel

from .managers import UserManager
from .normalizers import normalize_email, normalize_phone

class AccountStatus(models.TextChoices):
    REGISTERED = "REGISTERED", "Registered"
    PENDING_VERIFICATION = "PENDING_VERIFICATION", "Pending verification"
    PENDING_KYC = "PENDING_KYC", "Pending KYC"
    KYC_UNDER_REVIEW = "KYC_UNDER_REVIEW", "KYC under review"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    SUSPENDED = "SUSPENDED", "Suspended"
    CLOSED = "CLOSED", "Closed"

class User(UUIDModel, TimestampedModel, AbstractBaseUser):
    """The single user table for investors and later administrators."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=16, unique=True)

    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    account_status = models.CharField(
        max_length=30,
        choices=AccountStatus.choices,
        default=AccountStatus.REGISTERED,
        db_index=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]

    def save(self, *args, **kwargs):
        self.email = normalize_email(self.email)
        self.phone_number = normalize_phone(self.phone_number)
        super().save(*args, **kwargs)


    @property
    def full_name(self) -> str:
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(p for p in parts if p)

    def __str__(self):
        return self.email

