from django.shortcuts import render
from django.views.generic.list import ListView

class taskList(request):
    return HttpResponse('To do list')

