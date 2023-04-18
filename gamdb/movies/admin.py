from django.contrib import admin
from .models import Movies, Director, Genres, Actor, Comment

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'year', 'director', 'genres_display']
    list_display_links = ['id','name']
    search_fields = ['name']
    list_filter = ['genres', 'year']



admin.site.register(Movies, MoviesAdmin)
admin.site.register(Director)
admin.site.register(Genres)
admin.site.register(Actor)
admin.site.register(Comment)

# Register your models here.
