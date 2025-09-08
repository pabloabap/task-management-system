from django.urls import path, include

from . import views

app_name = "tasks"
urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("<int:pk>/", views.DetailView.as_view(), name="detail"),
	path("<int:pk>/result", views.ResultsView.as_view(), name="result"),
	path("<int:task_id>/vote", views.vote, name="vote"),
]