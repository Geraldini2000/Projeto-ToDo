

from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello),
    path('', views.tasksList, name='task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name')
]
