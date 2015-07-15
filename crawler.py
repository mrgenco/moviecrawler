__author__ = 'mrgenco'

'''
Project Name = A Basic Movie Crawler

The purpose of this project is to crawl theater and movie informations
from http://www.google.com/movies and generate json data structure with it

The purpose is not crawling the entire site so we have max_pages limit
as a stop criterion
'''

import requests
from bs4 import BeautifulSoup

max_page = 2
seed_url = "http://www.google.com/movies"

theaters = {}
movies = {}


def crawl_theaters(max_pages, seed_url):
    '''
    This method will find theater names and their links
    @parameter max_pages : stop criterion
    @seed_url : starting point for our crawler
    '''
    print("===========================================")

    page = 0

    while page < max_pages * 10:
        url = seed_url + '?start=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for theater in soup.find_all("h2", {"class": "name"}):
            a_tag = theater.a

            # theater name
            theater_name = a_tag.string

            # theater link
            theater_url = "http://www.google.com" + a_tag.get('href')

            # Don't want to fetch same page twice
            # so we are holding previously visited links
            # in a lookup table as a key-value pair
            # key : theater_name
            # value : theater_url
            theaters[theater_name] = theater_url

            print(theater_name)
            print(theater_url)

        print("===========================================")
        page += 10


# TODO : crawl_movies function must take string parameter as a url instead
# TODO : crawl_movies function must crawl movie informations for a single theater

def crawl_movies(theaters):
    '''
    This method will crawl movie informations related to theater
    @parameter theaters : A dictionary which we hold theater names and urls
    '''
    for key in theaters:
        theater_url = theaters[key]
        source_code = requests.get(theater_url)
        plaint_text = source_code.text
        soup = BeautifulSoup(plaint_text, 'html.parser')

        print("Theater Name : " + key)

        for movie in soup.find_all("div", {"class": "name"}):
            a_tag = movie.a

            movie_name = a_tag.string
            print(movie_name)

            movie_info = movie.next_sibling
            print(movie_info.string)

            movie_times = movie_info.next_sibling

            for time in movie_times.find_all("span"):
                print(time)


crawl_theaters(1, seed_url)
crawl_movies(theaters)