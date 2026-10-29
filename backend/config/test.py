"""Automated tests: fast and isolated."""
from .base import *  # noqa: F401,F403

DEBUG = False
SECRET_KEY = 'django-insecure-oa6qth^i4d=&a^nqf$kh4wmyta&_aa%-(8w&d8uzx4*yaf$$jh'
ALLOWED_HOSTS = ["testserver", "localhost"]
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # speed only
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
ENABLE_MOCK_PAYMENTS = True