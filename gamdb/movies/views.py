from django.shortcuts import render
from .models import Movies
from .models import Director
from .models import Genres
from .models import Actor

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

def movies_detail(request, id):
    context = {
        "movies": Movies.objects.get(id=id)
    }

    return render(request, 'movie.html', context)

def director(request):
    context = {
        "directors": Director.objects.all()
    }

    return render(request, 'directors.html', context)

def director_detail(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }

    return render(request, 'director.html', context)

def actor(request):
    context = {
    "actors": Actor.objects.all(),
    }
    return render(request, 'actors.html', context)

def actor_detail(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }

    return render(request, 'actor.html',context)
# Create your views here.
