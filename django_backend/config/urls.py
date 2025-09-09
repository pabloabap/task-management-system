from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import settings
from django.contrib.auth import get_user_model
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.tasks.urls')),
    path('users/', include('apps.users.urls')),
    path('api/', include('apps.api.urls')),
	path("api/auth/", include('rest_framework.urls')),
]
