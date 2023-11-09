
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView 
from .models import Movie, Actor
from .serializers import ActorSerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from datetime import  timedelta
from django.db.models.functions import Now



class MovieList(ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'movies'
    throttle_classes = (ScopedRateThrottle,)

    def get_queryset(self):
        queryset = Movie.objects.all()
        n = self.request.query_params.get("minutes")
        if n is not None:
            #To get movies created in last 'n' minutes
            last_minutes = Now() - timedelta(minutes=int(n))
            queryset = queryset.filter(created_at__gte=last_minutes)
        return queryset

class MovieCreate(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    
class MovieRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

class ActorListCreate(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated,)

class ActorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated,)