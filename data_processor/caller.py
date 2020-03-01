from .csv_downloader import download_csvs
from .csv_parser import perse_csv_data
from .movies_wiki_scraper import scrap_movies_list_from_wiki


def data_processor():
    download_csvs()
    movies_csv_data = perse_csv_data()
    scrap_movies_list_from_wiki(movies_csv_data)

