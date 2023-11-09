from django.test import TestCase
from .models import Movie, Actor
from datetime import datetime


class ActorTestCase(TestCase):
    def setUp(self):
        Actor.objects.create(name="test", gender="M")


class MovieTestCase(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title="test movie", producer="sanjay", genre="ACTION", release_date=datetime.now)
        self.movie.actors.create(name="test", gender="M")

