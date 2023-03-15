#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
import re 
import json
import cProfile     


def scrape():
    # MAX PAGE: 1250
    url = 'https://www.jpl.nasa.gov/images?page='
    key_items = {}

    for i in range(1, 3):
        url = url + str(i)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser').find_all('li')

        for data in soup:
            h2s = data.find_all('span')
            image = data.find_all('img')

            for i in h2s:
                key_items[i.text.strip()] = image[0]['data-src']

    print(json.dumps(key_items, sort_keys=True, indent=4))


def execute():
    scrape()


if __name__ == "__main__":
    cProfile.run('execute()')
