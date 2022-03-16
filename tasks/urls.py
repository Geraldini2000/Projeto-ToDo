

from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello),
    path('', views.tasksList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('yourname/<str:name>', views.yourName, name='your-name')
]
