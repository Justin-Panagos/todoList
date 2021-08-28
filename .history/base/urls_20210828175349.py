from django.urls import path
from .views import TaskList

urlpatterns = [
    path('',TaskList.as.taskList, name='taskList'),
]