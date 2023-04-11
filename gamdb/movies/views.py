from django.shortcuts import render
from .models import Movies
from .models import Director

def homepage(request):
    context = {
        "title": "UWU",
    }

    return render(request, 'main.html',context)

def movies(request):
    context = {
        "movies": Movies.objects.all()
    }

    return render(request, 'movies.html', context)

def director(request):
    context = {
        "directors": Director.objects.all()
    }

    return render(request, 'director.html', context)

def actor(request):
    context = {
        "title": "UWU",
        "actors": []
    }

    return render(request, 'actor.html',context)
# Create your views here.
