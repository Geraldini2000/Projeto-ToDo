from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Ola mundo')


def tasksList(request):
    return render(request, 'tasks/list.html')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
