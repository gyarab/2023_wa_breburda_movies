from django.db import models
class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField('Genres')
    actors = models.ManyToManyField('Actor')
    avg_rating = models.FloatField(blank=True, null=True)
    img_url = models.CharField(max_length=400,blank=True, null=True)
    comments = models.ManyToManyField('Comment')

    def __str__(self):
        return f"{self.name} ({self.year})"

    def comment(self):
        comments = Comment.objects.filter(movie=self).order_by('-created_at')
        return comments 

    def genres_display(self):
        #self.genres.all()
        #out = ""
        #for genre in self.genres.all():
        #    out += f"{genre.name}, "
        #return out
        return ', '.join(genre.name for genre in self.genres.all()[:3])

class Director(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True, null=True)
    photo_url = models.CharField(max_length=400,blank=True, null=True)
    #movies = models.ManyToManyField(Movies)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Genres(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Actor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True, null=True)
    photo_url = models.CharField(max_length=400,blank=True, null=True)
    description = models.TextField()
    #movies = models.ManyToManyField(Movies)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Comment(models.Model):
    #comment = models.TextField()
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True, blank=True)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.author} - {self.text}"


# Create your models here.
