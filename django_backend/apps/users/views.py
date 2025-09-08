from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
# Create your views here.

def index(request):
	latest_users = User.objects.order_by("date_joined")
	context = {"latest_users": latest_users}
	return render(request, "users/index.html", context)