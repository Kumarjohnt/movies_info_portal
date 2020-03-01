from django.urls import path
from movie_info import views

urlpatterns = [
    path('movies-list/', views.GetMoviesSummeryData.as_view()),
    path('movie-details/<slug:movie_id>/', views.GetMovieDetailsData.as_view())
]