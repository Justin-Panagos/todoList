from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('',TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/',TaskDetail.as, name='task'),
]