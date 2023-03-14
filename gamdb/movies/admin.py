from django.contrib import admin
from .models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'year']
    list_display_links = ['id','name']
    search_fields = ['name']

admin.site.register(Movies, MoviesAdmin)

# Register your models here.
