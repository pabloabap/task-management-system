
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Task

# Create your views here.
class IndexView(generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "latest_task_list"
    def get_queryset(self):
        return Task.objects.order_by("created_at")[:5]

class DetailView(generic.DetailView):
    model = Task
    template_name = "tasks/detail.html"

class ResultsView(generic.DetailView):
    model = Task
    template_name = "tasks/results.html"

def vote(request, task_id):
    return HttpResponse(f"Vote for task {task_id}")
