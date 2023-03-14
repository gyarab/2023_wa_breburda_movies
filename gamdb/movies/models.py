from django.db import models
class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.year})"
# Create your models here.
