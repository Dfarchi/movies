from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    # movies = models.TextField(db_column='movies', null=False)
    birth_year = models.IntegerField(db_column='birth_year', null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'actors'


class Movie(models.Model):
    movie_name = models.CharField(db_column='movie_name', max_length=256, null=False)
    description = models.TextField(db_column='description', null=False)
    duration = models.FloatField(db_column='duration', null=False)
    release_year = models.IntegerField(db_column='year', null=False,
                                       validators=[MinValueValidator(1899), MaxValueValidator(2024)])
    pic_url = models.URLField(db_column='pic_url', max_length=512, null=True)
    actors = models.ManyToManyField(Actor, through='Movie_Actor')

    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 'movies'


class Rating(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT)
    rating = models.SmallIntegerField(db_column='rating', null=False,
                                      validators=[MinValueValidator(0), MaxValueValidator(11)])
    rating_date = models.DateField(db_column='date', null=False, default='1900-01-01')

    class Meta:
        db_table = "ratings"


class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT)
    review = models.TextField(db_column='review', null=False)
    review_date = models.DateField(db_column='date', null=False, default='1900-01-01')

    class Meta:
        db_table = "reviews"


class Movie_Actor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    salary = models.IntegerField(null=True, blank=0)
    main_role = models.BooleanField(null=True, blank=False)
    # roll = models.TextField(db_column='roll')

    def __str__(self):
        return f"{self.actor.name} in movie {self.movie.movie_name}"

    class Meta:
        db_table = 'movie_actors'
