"""Swagger docs module"""

from django.conf.urls import include, url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Tutorials API",
        default_version="v1",
        description="Another django rest framework tutorial",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="johnshumon@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def docs_urls():
    urls = [
        url(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        url(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        url(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]

    return include((urls, "api-doc"), namespace="api-doc")
