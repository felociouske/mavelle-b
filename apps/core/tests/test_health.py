from django.conf import settings


def test_health_endpoint_returns_ok(client):
    response = client.get(f"/{settings.API_PREFIX}/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_common_api_v1_prefix_is_not_served(client):
    assert client.get("/api/v1/health/").status_code == 404


def test_timezone_is_nairobi_and_aware():
    assert settings.TIME_ZONE == "Africa/Nairobi"
    assert settings.USE_TZ is True


def test_default_database_is_sqlite_in_development():
    assert settings.DATABASES["default"]["ENGINE"].endswith("sqlite3")