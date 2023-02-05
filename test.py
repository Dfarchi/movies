import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'movies.settings'
django.setup()

# from movies_app.models import *
#
# # Movie(
# #     movie_name='farchi and ziv',
# #     description='ziv is teaching Django to farchi while farchi is petting his cats',
# #     duration=124,
# #     release_year=2023).save()
#
# # Movie(
# #     movie_name='farchi and ziv 2',
# #     description='ziv is making farchi to fill another movie while farchi is still petting his cats',
# #     duration=94,
# #     release_year=2023).save()
#
# all_movies = Movie.objects.all()
# # total = 0
# # for movie in all_movies:
# #       total += movie.duration
# # # print(int(total),'min')
#
# # for movie in Movie.objects.all():
# #       Rating(movie=movie, rating=random.randint(8,10)).save()
#
# # Rating(movie = all_movies[1],rating=random.randint(6,10)).save()
#
# # movie = Movie.objects.get(pk=3)
# # [print(rating.movie.pic_url,rating.rating) for rating in movie.rating_set.all()]
#
# # print(Movie.objects.all().values_list('description', 'movie_name', 'duration'))
#
# m = Movie.objects.all()
# for m1 in m:
#     print(m1 , m1.actors.all())
# # m.actors.create(name='ziv', movies = "farchi and ziv", birth_year = '1998')
# # m.actors.create(name='yuval', movies = "farchi and ziv", birth_year = '1994')
#
# # new_actor2 = Actor(name='yuval', movies = "farchi and ziv",salary = '1000002', main_role = True)
import sys
print(sys.executable)
