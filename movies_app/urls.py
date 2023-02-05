from django.urls import path

from . import views

urlpatterns = [
    path('api/movies', views.movies_list),
    path('api/movies/<int:movie_id>', views.movie_details),
    path('api/movies/<int:movie_id>/actors', views.movie_actors),
    path('', views.index, name='index'),
    path('api/ratings', views.rating_list),
    path('api/ratings/<int:rating_id>', views.rating_details),
    path('api/actors', views.actors_list),
    path('api/actors/<int:actor_id>', views.actor_details),

]