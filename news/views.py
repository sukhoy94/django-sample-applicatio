from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


def test(request):
    return HttpResponse('<h1>Test Page</h1>')