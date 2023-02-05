import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'movies.settings'
django.setup()
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from movies_app.models import *
from movies_app.serializers import *
from django.http import HttpResponse


# Example of simple request without serializers
# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         response = []
#         for m in movies:
#             response.append({'name': m.name, 'year': m.release_year})
#         # note what to import
#         return Response(response)

# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, safe=False)


# @api_view(['GET'])
# def rating_list(request):
#     if request.method == 'GET':
#         ratings_qs = Rating.objects.all()
#         serializer = RatingSerializer(ratings_qs, many=True)
#         return Response(serializer.data)

@api_view(http_method_names=["GET"])
def rating_list(request: Request):
    ratings = Rating.objects.all()

    if "min_rating" in request.query_params:
        ratings = ratings.filter(rating__gte=request.query_params["min_rating"])
    if "max_rating" in request.query_params:
        ratings = ratings.filter(rating__lte=request.query_params["max_rating"])
    if "rating_year" in request.query_params:
        ratings = ratings.filter(rating_date__year=request.query_params["rating_year"])
    if "rating_month" in request.query_params:
        ratings = ratings.filter(
            rating_date__month=request.query_params["rating_month"]
        )
    if "rating_day" in request.query_params:
        ratings = ratings.filter(rating_date__day=request.query_params["rating_day"])
    if ("rating_from_date" in request.query_params) and (
            "rating_from_date" in request.query_params
    ):
        ratings = ratings.filter(
            rating_date__range=(
                request.query_params["rating_from_date"],
                request.query_params["rating_to_date"],
            )
        )
    else:
        if "rating_from_date" in request.query_params:
            ratings = ratings.filter(
                rating_date__gte=request.query_params["rating_from_date"]
            )
        if "rating_to_date" in request.query_params:
            ratings = ratings.filter(
                rating_date__lte=request.query_params["rating_to_date"]
            )

    if not ratings:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = RatingSerializer(instance=ratings, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
def rating_details(request, rating_id):
    rating = get_object_or_404(Movie, pk=rating_id)
    if request.method == 'GET':
        serializer = RatingSerializer(rating, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = RatingSerializer(rating, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()
    elif request.method == 'DELETE':
        rating.delete()
        return Response()


@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        movies_qs = Movie.objects.all()

        if 'name' in request.query_params:
            movies_qs = movies_qs.filter(movie_name__iexact=request.query_params['name'])
        if 'duration_from' in request.query_params:
            movies_qs = movies_qs.filter(duration__gte=request.query_params['duration_from'])
        if 'duration_to' in request.query_params:
            movies_qs = movies_qs.filter(duration__lte=request.query_params['duration_to'])
        if 'description' in request.query_params:
            movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

        serializer = MovieSerializer(movies_qs, many=True)
        if not serializer.data:
            return Response(data=[], status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            new_movie = serializer.create(serializer.validated_data)
            # if we want to return the created object
            return Response(data=MovieSerializer(new_movie, many=False).data)


@api_view(['GET', 'PATCH', 'DELETE'])
def movie_details(request, movie_id):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data)
        # follow-up: how can I check which exception is thrown?
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PATCH':
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()
    elif request.method == 'DELETE':
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return Response()


@api_view(['GET'])
def actors_list(request: Request):
    actors = Actor.objects.all()
    if request.method == 'GET':
        if 'name' in request.query_params:
            actors.filter(name__iexact=request.query_params['name'])

        if 'birth_year' in request.query_params:
            actors.filter(birth_year=request.query_params['birth_year'])

        serializer = ActorSerializer(actors, many=True)
        if not serializer.data:
            return Response(data=[], status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
def actor_details(request, actor_id):
    if request.method == 'GET':
        try:
            actor = Actor.objects.get(id=actor_id)
            serializer = ActorSerializer(actor, many=False)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PATCH':
        actor = Actor.objects.get(id=actor_id)
        serializer = ActorSerializer(actor, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()
    elif request.method == 'DELETE':
        actor = get_object_or_404(Movie, pk=actor_id)
        actor.delete()
        return Response()


@api_view(['GET', 'POST'])
def movie_actors(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieActorSerializer(movie.movieactor_set, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddMovieActorSerializer(data=request.data, many=False,
                                             context={'movie_id': movie_id, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response()




def index(request):
    return HttpResponse("Movies home page")
