
from rest_framework import serializers
from .models import Movie, Actor

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'actors',
            'producer',
            'genre',
            'release_date',
        ]

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"