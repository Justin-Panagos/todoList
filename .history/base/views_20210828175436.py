from django.shortcuts import render
from django.views.generic.list import ListView
from mod

class TaskList(ListView):
    model = Task

