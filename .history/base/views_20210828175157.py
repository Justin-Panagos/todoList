from django.shortcuts import render
from django.views.generic.list import

def taskList(request):
    return HttpResponse('To do list')

