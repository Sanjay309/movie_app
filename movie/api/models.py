from django.db import models
import datetime


class Actor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


    class Meta:
        ordering = ('name',)

    def age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    GENRES = (
        ('HORROR', 'horror'),
        ('THRILLER', 'thriller'),
        ('ROMANCE', 'romance'),
        ('ACTION', 'action'),
        ('FANTASY', 'fantasy'),
        ('ADVENTURE', 'adventure'),
        ('SUSPANCE', 'suspance'),
        ('BIOGRAPHY', 'biography'),
        ('SCIFI', 'sci-fi'),
        ('Anime', 'anime'),
    )
    title = models.CharField(max_length=100)
    actors =  models.ManyToManyField(Actor)
    producer = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, choices=GENRES)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title