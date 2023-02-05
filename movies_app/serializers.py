from rest_framework import serializers
from movies_app.models import *


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'movie_id', 'rating_date']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'description', 'duration', 'release_year', 'pic_url']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieActorSerializer(serializers.ModelSerializer):

    actor = ActorSerializer(many=False, read_only=True)

    class Meta:
        model = Movie_Actor
        fields = ['salary', 'main_role', 'actor']


class WriteableMovieActorRelatedField(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        return Actor.objects.all()

    def to_internal_value(self, data):
        val = super().to_internal_value(data)
        return val.pk

class AddMovieActorSerializer(serializers.Serializer):

    # actor_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Actor.objects.all())
    actor_id = WriteableMovieActorRelatedField(read_only=False)
    salary = serializers.IntegerField(min_value=0)
    main_role = serializers.BooleanField()

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        return Movie_Actor.objects.create(movie_id=self.context['movie_id'], **validated_data)
