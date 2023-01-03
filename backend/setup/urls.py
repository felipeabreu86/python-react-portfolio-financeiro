from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.usuarios.urls import usuarios_urls
from rest_framework import permissions

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Portfólio Financeiro API",
        default_version="v1",
        description="Documentação da API do site Portfólio Financeiro",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Configuração das URLs do projeto
urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", include(usuarios_urls)),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
