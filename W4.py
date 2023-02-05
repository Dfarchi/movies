import os
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import Q, FloatField
from django.db.models.aggregates import Aggregate, Avg, Min, Max, Count
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *
from django.db.models import Q
"""
Get all the actors in the db who are younger than 50 years old
Get movies that last less than 2.5 hours and were released after 2005
Get all the movies that contain a word “criminal”, “mob” or “cop” in their description
Like previous, but get only movies that were released before 2010
Get list of actors, and add amount of movies they played in (for each one)
Get average, min, and max rating in the system
Get Movies with their avg ratings
Get ratings that were created in 2023
Get all the actors in the system with min and max rating of the movies they played in
Get movies with average salary for actors in each one
Get actors with their average salaries
Get actors who played main roles at least once
Get movies and amount of actors who played main roles
 """

# print(Actor.objects.filter(birth_year__lte= 2023 - 50)) print(Movie.objects.filter(duration__lte= 150)) print(
# Movie.objects.filter(Q(description__icontains='mob') | Q(description__icontains='cop') | Q(
# description__icontains='criminal'))) print(Movie.objects.filter(Q(description__icontains='mob') | Q(
# description__icontains='cop') | Q(description__icontains='criminal')).filter(release_year__lte= 2010))

# actors = Actor.objects.annotate(num_movies=Count("movie_actor__movie"))
# print([(actor.name, actor.num_movies) for actor in actors])
# print(Rating.objects.aggregate(Max('rating'),Min('rating'),Avg('rating')))

[[print(m.movie_name,r.rating) for r in Rating.objects.filter(movie = m.id)] for m in Movie.objects.all()]
# [print(mr.rating, mr.movie) for mr in Movie.objects.all()]