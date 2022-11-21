from django.conf import settings
from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions


api_prefix = settings.API_PREFIX
app_patterns = [
        path(api_prefix, include('user.urls')),
        path(api_prefix, include('product.urls')),
        path(api_prefix, include('company.urls')),
    ]

schema_view = get_schema_view(  # new
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Swagger documentation",
    ),
    patterns=app_patterns,
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path(  # new
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    re_path(  # new
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + app_patterns
