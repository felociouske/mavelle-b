from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(f"{settings.API_PREFIX}/", include("apps.core.urls")),
]
