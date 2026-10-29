"""Production (Railway). Strict by default."""
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F401,F403

DEBUG = False

if not SECRET_KEY or SECRET_KEY.startswith("dev-only"):  # noqa: F405
    raise ImproperlyConfigured("Set DJANGO_SECRET_KEY to a long random value.")
if not ALLOWED_HOSTS:  # noqa: F405
    raise ImproperlyConfigured("Set DJANGO_ALLOWED_HOSTS.")

# HTTPS and cookie hardening
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Railway proxy
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Mock money endpoints must never exist in production.
ENABLE_MOCK_PAYMENTS = False