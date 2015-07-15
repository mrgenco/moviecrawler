__author__ = 'mrgenco'

''' 
The purpose of this project is to crawl theater and movie informations
from http://www.google.com/movies and generate json data structure with it

The purpose is not crawling the entire site so we have max_pages limit 
as a stop criteria

'''

import requests
from bs4 import BeautifulSoup


def movie_crawler(max_pages):

    print("===========================================")

    page = 0

    while page <= max_pages * 10:
        url = 'http://www.google.com/movies?start=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.find_all('h2'):
            print(link.string)

        print("===========================================")
        page += 10



movie_crawler(3)
