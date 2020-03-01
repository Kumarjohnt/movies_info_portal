from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from movie_info.models import MoviesData
from movie_info.serializers import MovieMinSerializer, MovieDetailsSerializer


class GetMoviesSummeryData(APIView):

    def get(self, request, *args, **kwargs):
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('page_size', 20)

        response_data = MoviesData.objects.all_movies_data()

        try:
            paginator = Paginator(response_data, page_size)
            movie_data_serializer = MovieMinSerializer(
                paginator.page(page_number),
                many=True, context={'request': request}
            )
            data = movie_data_serializer.data
            return Response(
                {
                    'data': data
                }, status=status.HTTP_200_OK
            )

        except:
            return Response(
                {
                    'message': "ERROR!!! Invalid Page No.",
                }, status=status.HTTP_201_CREATED
            )


class GetMovieDetailsData(APIView):

    def get(self, request, movie_id):
        response_data = MoviesData.objects.get_movie_data_by_id(movie_id)
        movie_data_serializer = MovieDetailsSerializer(response_data, many=True)

        return Response(movie_data_serializer.data, status=status.HTTP_200_OK)

