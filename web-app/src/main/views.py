from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def recognition(request):
    return render(request, 'main/recognition.html')