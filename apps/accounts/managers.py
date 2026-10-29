"""A manager is a what sits behind User.objects. Django's default one assumes a username field, so
we replace it with one that works from an email."""

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Knows how to create users with email as the login identifier."""

    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")
        if not phone_number:
            raise ValueError("Users must have a phone number.")
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)  # hashes the password; never stores plaintext
        user.save(using=self._db)
        return user