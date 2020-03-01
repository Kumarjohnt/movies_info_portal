from rest_framework import serializers
from movie_info.models import MoviesData


class MovieMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        fields = ('id', 'movie_title', 'movie_release_year', 'no_of_awards', 'no_of_nominations')


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        exclude = ('created_at', 'updated_at')

