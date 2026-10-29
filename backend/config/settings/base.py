""" Settings shared by every environment. Environment files import * from here."""

from pathlib import Path
import environ

#Backend/ directory 
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

#CORE

SECRET_KEY = 'django-insecure-oa6qth^i4d=&a^nqf$kh4wmyta&_aa%-(8w&d8uzx4*yaf$$jh'
DEBUG = False
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    # Third-party
    "rest_framework",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    # Local apps
    "apps.core",
    "apps.accounts",
]

# No sessions, no Django admin: auth is JWT-in-cookies and the admin
# dashboard is our own React app. Fewer moving parts = less to maintain/attack.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#Base usermodel
AUTH_USER_MODEL = "accounts.User"

ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"

# Database 
# SQLite by default for development. To switch to PostgreSQL later, set
DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Time -----------------------------------------------------------------
# Financial business date is Africa/Nairobi. Datetimes are stored in UTC.
TIME_ZONE = "Africa/Nairobi"
USE_TZ = True
LANGUAGE_CODE = "en-us"

STATIC_URL = "static/"

# --- API URL prefix -------------------------------------------------------
# One setting controls every API URL, so changing it later is a one-line edit.
# Final URLs look like  /<API_PREFIX>/investment-orders/
API_PREFIX = env("API_PREFIX", default="mw/r26").strip("/")

# --- Django REST Framework ------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Mavelle Wealth API",
    "DESCRIPTION": "Simulated investment platform. No real money is moved.",
    "VERSION": "r26",
    "SERVE_INCLUDE_SCHEMA": False,
}

# --- CORS (exact origins only; filled per environment) --------------------
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# --- Simulation safety switch --------------------------------------------
# Mock deposits/withdrawals are only ever enabled outside production.
ENABLE_MOCK_PAYMENTS = False