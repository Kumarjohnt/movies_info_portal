import os
import requests

def download_csvs():
    movie_csv_url = 'https://school.cefalolab.com/assignment/python/movies.csv'
    movie_req = requests.get(movie_csv_url, verify=False)

    rating_csv_url = 'https://school.cefalolab.com/assignment/python/ratings.csv'
    rating_req = requests.get(rating_csv_url, verify=False)

    with open(os.path.split(movie_csv_url)[1], 'wb') as file:
        file.write(movie_req.content)

    with open(os.path.split(rating_csv_url)[1], 'wb') as file:
        file.write(rating_req.content)
