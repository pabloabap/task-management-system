from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import settings
from django.contrib.auth import get_user_model

# Serializers define the API representation.
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = get_user_model()
#        fields = ['url', 'username', 'email', 'is_staff']
#
## ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = get_user_model().objects.all()
#    serializer_class = UserSerializer
#
## Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.tasks.urls')),
    path('users/', include('apps.users.urls')),
    path('api/', include('apps.api.urls')),
	path("api/auth/", include('rest_framework.urls')),

#   path('api/', include('rest_framework.urls', namespace='rest_framework')),	
#   path('api/', include(router.urls)),
#  	path("auth/", include('rest_framework.urls')),

]
