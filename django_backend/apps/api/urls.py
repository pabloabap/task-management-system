from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "api"
urlpatterns = [
	path("users/", views.users_list.as_view(), name="index"),
	path("users/me/", views.me.as_view(), name="me"),
	path("users/<int:pk>", views.user_details.as_view(), name="details"),
	
	path("auth/register/", views.register.as_view(), name="register"),
	path("login/", views.login.as_view(), name="login"),
	path("logout/", views.logout.as_view(), name="logout"),
	path("refresh/", views.refresh.as_view(), name="refresh"),
]

# Si queremos que se añada .json, .html en las URL. Intergiere con auth
# urlpatterns = format_suffix_patterns(urlpatterns)
# Para que no interfiera si queremos que pase lo anterior
# auth_urlpatterns = [
# 	path("auth/", include('rest_framework.urls')),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns) + auth_urlpatterns
#