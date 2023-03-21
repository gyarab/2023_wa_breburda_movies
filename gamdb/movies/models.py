from django.db import models
class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField('Genres')

    def __str__(self):
        return f"{self.name} ({self.year})"

    def genres_display(self):
        #self.genres.all()
        #out = ""
        #for genre in self.genres.all():
        #    out += f"{genre.name}, "
        #return out
        return ', '.join(genre.name for genre in self.genres.all()[:3])

class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField(blank=True, null=True)
    #movies = models.ManyToManyField(Movies)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Genres(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
# Create your models here.
