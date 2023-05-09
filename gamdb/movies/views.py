from django.shortcuts import render
from django.db.models import Q
from .models import Movies
from .models import Director
from .models import Genres
from .models import Actor
from .forms import CommentForm

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
    m = Movies.objects.get(id=id)
    f = CommentForm()
    context = {
        "movie": m,
        "form": f,
        "comments": Comment.objects.filter(movie=m).order_by('-created_at')
    }

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            c = Comment(
                movie=m,
                author= f.cleaned_data.get('author'),
                text= f.cleaned_data.get('text'),
                rating= f.cleaned_data.get('rating'),
            )
            if not c.author:
                c.author = "Anonymous"
            c.save()
            context['comments'] = m.comment_set.all().order_by('-id')

    return render(request, 'movie.html', context)

def director(request):
    director_queryset = Director.objects.all()
    search = request.GET.get('search')
    if search:
        director_queryset = director_queryset.filter(Q(name__icontains=search))
    
    context = {
        "directors": director_queryset,
    }

    return render(request, 'directors.html', context)

def director_detail(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }

    return render(request, 'director.html', context)

def actor(request):
    actor_queryset = Actor.objects.all()
    search = request.GET.get('search')
    if search:
        actor_queryset = actor_queryset.filter(Q(name__icontains=search))

    context = {
    "actors": actor_queryset,
    }
    return render(request, 'actors.html', context)

def actor_detail(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }

    return render(request, 'actor.html',context)
# Create your views here.
