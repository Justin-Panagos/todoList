from django.urls import path
from .views import TaskList

urlpatterns = [
    path('',TaskList.taskList, name='taskList'),
]