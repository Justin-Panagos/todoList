from django.urls import path
from .view import views

urlpatterns = [
    path('',views.taskList, name='taskList'),
]