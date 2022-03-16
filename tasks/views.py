from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Task


def tasksList(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def hello(request):
    return HttpResponse('Ola mundo')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
