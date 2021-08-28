from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('',TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreate.as_view(), name='task-create'),
]