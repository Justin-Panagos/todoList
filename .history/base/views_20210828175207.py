from django.shortcuts import render
from django.views.generic.list import ListView

def taskList(request):
    return HttpResponse('To do list')

