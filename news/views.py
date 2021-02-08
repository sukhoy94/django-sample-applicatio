from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.
def index(request):
    news = News.objects.all();
    return render(request, 'news/index.html', {'news': news, 'title': 'News List'})


def test(request):
    return HttpResponse('<h1>Test Page</h1>')