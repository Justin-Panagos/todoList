from django.urls import path
from .views import TaskList

urlpatterns = [
    path('',Task, name='taskList'),
]