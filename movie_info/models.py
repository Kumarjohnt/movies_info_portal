import logging
from django.db import models
from django.utils import timezone
from datetime import datetime


class MoviesDataManager(models.Manager):

    # Process movies details data to save it in the related databases
    def save_movies_data(self, movies_details_data):
        for movie_data in movies_details_data:
            try:
                # request to insert movies data
                movie_url = movie_data['movie_url']
                movie_title = movie_data['movie_title']
                movie_release_year = movie_data['movie_release_year']
                no_of_awards = movie_data['no_of_awards']
                no_of_nominations = movie_data['no_of_nominations']
                directed_by = movie_data['directed_by']
                produced_by = movie_data['produced_by']
                written_by = movie_data['written_by']
                screenplay_by = movie_data['screenplay_by']
                story_by = movie_data['story_by']
                based_on = movie_data['based_on']
                starring = movie_data['starring']
                music_by = movie_data['music_by']
                cinematography = movie_data['cinematography']
                edited_by = movie_data['edited_by']
                animation_by = movie_data['animation_by']
                layouts_by = movie_data['layouts_by']
                color_process = movie_data['color_process']
                production_company = movie_data['production']
                distributed_by = movie_data['distributed_by']
                release_date = movie_data['release_date']
                running_time = movie_data['running_time']
                country = movie_data['country']
                language = movie_data['language']
                budget = movie_data['budget']
                box_office = movie_data['box_office']
                movie_genres = movie_data['movie_genres']
                rating = movie_data['rating']

                movie_details_data = {
                    'movie_url': movie_url,
                    'movie_title': movie_title,
                    'movie_release_year': movie_release_year,
                    'no_of_awards': no_of_awards,
                    'no_of_nominations': no_of_nominations,
                    'directed_by': directed_by,
                    'produced_by': produced_by,
                    'written_by': written_by,
                    'screenplay_by': screenplay_by,
                    'story_by': story_by,
                    'based_on': based_on,
                    'starring': starring,
                    'music_by': music_by,
                    'cinematography': cinematography,
                    'edited_by': edited_by,
                    'animation_by': animation_by,
                    'layouts_by': layouts_by,
                    'color_process': color_process,
                    'production_company': production_company,
                    'distributed_by': distributed_by,
                    'release_date': release_date,
                    'running_time': running_time,
                    'country': country,
                    'language': language,
                    'budget': budget,
                    'box_office': box_office,
                    'movie_genres': movie_genres,
                    'rating': rating,


                }
                self.insert_movie_data(movie_data=movie_details_data)

            except Exception as e:
                logging.error(e)

    # insert into database
    def insert_movie_data(self, movie_data):
        self.create(
            movie_url=movie_data['movie_url'],
            movie_title = movie_data['movie_title'],
            movie_release_year = movie_data['movie_release_year'],
            no_of_awards = movie_data['no_of_awards'],
            no_of_nominations = movie_data['no_of_nominations'],
            directed_by = movie_data['directed_by'],
            produced_by = movie_data['produced_by'],
            written_by = movie_data['written_by'],
            screenplay_by = movie_data['screenplay_by'],
            story_by = movie_data['story_by'],
            based_on = movie_data['based_on'],
            starring = movie_data['starring'],
            music_by = movie_data['music_by'],
            cinematography = movie_data['cinematography'],
            edited_by = movie_data['edited_by'],
            animation_by = movie_data['animation_by'],
            layouts_by = movie_data['layouts_by'],
            color_process = movie_data['color_process'],
            production_company = movie_data['production_company'],
            distributed_by = movie_data['distributed_by'],
            release_date = movie_data['release_date'],
            running_time = movie_data['running_time'],
            country = movie_data['country'],
            language = movie_data['language'],
            budget = movie_data['budget'],
            box_office = movie_data['box_office'],
            movie_genres = movie_data['movie_genres'],
            rating = movie_data['rating'],
        )

    # get all movies data
    def all_movies_data(self):
        return self.order_by('id').all()

    # get movie details by ID
    def get_movie_data_by_id(self, movie_id):
        return self.filter(id=movie_id)


class MoviesData(models.Model):
    movie_url = models.CharField(max_length=750)
    movie_title = models.CharField(max_length=750)
    movie_release_year = models.CharField(max_length=20)
    no_of_awards = models.CharField(max_length=20)
    no_of_nominations = models.CharField(max_length=20)
    directed_by = models.CharField(max_length=750)
    produced_by = models.CharField(max_length=500)
    written_by = models.CharField(max_length=750)
    screenplay_by = models.CharField(max_length=750)
    story_by = models.CharField(max_length=750)
    based_on = models.CharField(max_length=750)
    starring = models.CharField(max_length=500)
    music_by = models.CharField(max_length=750)
    cinematography = models.CharField(max_length=750)
    edited_by = models.CharField(max_length=750)
    animation_by = models.CharField(max_length=750)
    layouts_by = models.CharField(max_length=750)
    color_process = models.CharField(max_length=750)
    production_company = models.CharField(max_length=500)
    distributed_by = models.CharField(max_length=500)
    release_date = models.CharField(max_length=750)
    running_time = models.CharField(max_length=750)
    country = models.CharField(max_length=750)
    language = models.CharField(max_length=750)
    budget = models.CharField(max_length=750)
    box_office = models.CharField(max_length=750)
    movie_genres = models.CharField(max_length=750)
    rating = models.CharField(max_length=20)


    created_at = models.DateTimeField(default=timezone.now)  # For our database
    updated_at = models.DateTimeField(default=timezone.now)  # For our database

    objects = MoviesDataManager()

    def __str__(self):
        return "Movie's details data inserted on {date}".format(
            date=datetime.strftime(self.created_at, "%B %d,%Y")
        )

