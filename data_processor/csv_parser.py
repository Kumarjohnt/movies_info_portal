import csv


def perse_csv_data():
    movies_csv_data = csv.DictReader(open('movies.csv'), delimiter=',')
    ratings_csv_data = csv.DictReader(open('ratings.csv'), delimiter=',')

    movies_data_dict = {}
    ratings_data_dict = {}

    for data in movies_csv_data:
        movie_id = data['movieId']
        movie_title = data['title']
        movie_genres = data['genres']
        movie_genres = movie_genres.split('|')
        movie_genres = ', '.join(movie_genres)
        movie_title = movie_title.split('(')
        movie_name = movie_title[0]
        if len(movie_title) > 1:
            release_year = movie_title[1]
        else:
            release_year = ""

        if movie_id not in movies_data_dict:
            movies_data_dict.update({movie_id: {'movie_name': movie_name, 'release_year': release_year,
                                               'movie_genres': movie_genres, 'rating': ""}})

    for data in ratings_csv_data:
        movie_id = data['movieId']
        rating = float(data['rating'])

        if movie_id not in ratings_data_dict:
            ratings_data_dict.update({movie_id: {'total_rating': rating, 'total_rating_count': 1}})
        else:
            ratings_data_dict[movie_id]['total_rating'] += rating
            ratings_data_dict[movie_id]['total_rating_count'] += 1


    for key, value in movies_data_dict.items():
        rating_val = ''
        if key in ratings_data_dict:
            total_rating = float(ratings_data_dict[key]['total_rating'])
            total_rating_count = int(ratings_data_dict[key]['total_rating_count'])

            rating_val = total_rating / total_rating_count
            rating_val = round(rating_val, 1)

        value['rating'] = rating_val

    return movies_data_dict