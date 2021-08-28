from django.urls import path
from .views import TaskList

urlpatterns = [
    path('',views.taskList, name='taskList'),
]