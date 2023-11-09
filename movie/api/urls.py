from django.urls import path
from . import views
urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('add-movies/', views.MovieCreate.as_view(), name='movie-create'),
    path('actors/', views.ActorListCreate.as_view(), name='actor-list-create'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroy.as_view(), name='actor-retrieve-update-destroy'),
]