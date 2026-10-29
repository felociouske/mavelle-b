"""Local development: SQLite, DEBUG on, mock payments allowed."""
from .base import *  # noqa: F401,F403

DEBUG = True
SECRET_KEY = 'django-insecure-oa6qth^i4d=&a^nqf$kh4wmyta&_aa%-(8w&d8uzx4*yaf$$jh'  # noqa: F405
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CORS_ALLOWED_ORIGINS = env.list(  # noqa: F405
    "CORS_ALLOWED_ORIGINS",
    default=["http://localhost:3000", "http://localhost:5173"],
)
CSRF_TRUSTED_ORIGINS = env.list(  # noqa: F405
    "CSRF_TRUSTED_ORIGINS",
    default=["http://localhost:3000", "http://localhost:5173"],
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ENABLE_MOCK_PAYMENTS = True