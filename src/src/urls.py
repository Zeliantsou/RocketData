from django.conf import settings
from django.contrib import admin
from django.urls import path, include

api_prefix = settings.API_PREFIX

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_prefix, include('rest_framework.urls')),
    path(api_prefix, include('company.urls')),
    path(api_prefix, include('product.urls')),
    path(api_prefix, include('user.urls')),
]
