import re
import requests
from bs4 import BeautifulSoup


def scrap_movie_details_from_wiki(movie_url, movies_list):
    base_url = "https://en.wikipedia.org"
    url = base_url + movie_url
    print("Scraping Movie's Details From: {}".format(url))

    response_data = requests.post(url)

    html_dump = BeautifulSoup(response_data.content, 'html.parser')

    contect_html = html_dump.find('table', class_='infobox')

    keywords = [
        'Directed by', 'Produced by', 'Written by', 'Screenplay by', 'Story by', 'Based on', 'Starring',
        'Music by', 'Cinematography', 'Edited by', 'Animation by', 'Layouts by', 'Color process',
        'Production', 'Distributed by', 'Release date', 'Running time', 'Country', 'Language', 'Budget',
        'Box office'
    ]

    for keyword in keywords:
        try:
            current_tag = contect_html.find(lambda tag: tag.name == "th" and keyword in tag.text)
        except:
            current_tag = ''

        if current_tag:
            try:
                data = current_tag.next_sibling.find_all('td')
            except:
                data = ''

            if not data:
                data = current_tag.next_siblings

            value_list = []
            for value in data:
                value = re.sub("[[].*?[]]|\\n", "", value.text)
                value = re.sub('(?<![A-Z])\\B([A-Z])', r', \1', value)
                value = re.sub('(\\S)\\)(\\S)', r'\1) \2', value)
                value = value.replace("\xa0", " ").replace('by ', ' by ')
                value_list.append(value)

            value_list = list(filter(None, value_list))
            value_list = list(dict.fromkeys(value_list))

            key_str = keyword.lower()
            key_str = key_str.replace(" ", "_")
            movies_list[key_str] = ', '.join(value_list)

        else:
            key_str = keyword.lower()
            key_str = key_str.replace(" ", "_")
            movies_list[key_str] = ''


def scrap_movies_list_from_wiki():
    base_url = "https://en.wikipedia.org"
    oscar_wining_url = "/wiki/List_of_Academy_Award-winning_films"
    url = base_url + oscar_wining_url
    print("Scraping Movies List From: {}".format(url))

    response_data = requests.post(url)

    html_dump = BeautifulSoup(response_data.content, 'html.parser')

    contect_html = html_dump.find('table', class_='wikitable')

    movies = contect_html.find_all('tr')

    movies_details_info_list = []

    for movie in movies[1:]:
        movie_details = movie.find_all('td')
        movies_dict = {}

        try:
            movie_url = movie_details[0].find('a', {'href': True})['href']
        except:
            movie_url = ''

        movie_title = movie_details[0].i.text.strip()
        movie_release_year = movie_details[1].a.text.strip()
        no_of_awards = movie_details[2].text.strip()
        no_of_nominations = movie_details[3].text.strip()

        movies_dict['movie_url'] = movie_url
        movies_dict['movie_title'] = movie_title
        movies_dict['movie_release_year'] = movie_release_year
        movies_dict['no_of_awards'] = no_of_awards
        movies_dict['no_of_nominations'] = no_of_nominations

        if movie_url:
            scrap_movie_details_from_wiki(movie_url, movies_dict)

        movies_details_info_list.append(movies_dict)

    print("Movie Scraping Completed")
    return movies_details_info_list

print(scrap_movies_list_from_wiki())

