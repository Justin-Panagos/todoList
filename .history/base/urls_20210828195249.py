from django.urls import path
from .views import TaskList, Task

urlpatterns = [
    path('',TaskList.as_view(), name='taskList'),
]