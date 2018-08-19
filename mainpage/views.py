from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = 'Test'
    return render(request, 'index.html', locals())
