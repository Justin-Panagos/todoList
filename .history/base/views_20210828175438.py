from django.shortcuts import render
from django.views.generic.list import ListView
from models import

class TaskList(ListView):
    model = Task

