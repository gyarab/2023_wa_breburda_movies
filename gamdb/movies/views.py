from django.shortcuts import render
from django.db.models import Q
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
    movies_queryset = Movies.objects.all()
    # print(request.GET.get('genre'))
    genre = request.GET.get('genre')
    search = request.GET.get('search')
    if genre:
        movies_queryset = movies_queryset.filter(genres__name=genre)

    if search:
        movies_queryset = movies_queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))

    context = {
        "movies": movies_queryset,
        "genres": Genres.objects.all().order_by('name'),
        "genre" : genre
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
