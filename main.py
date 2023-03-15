#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
import re 
import json
import cProfile     
import skimage
from scipy import misc
import pandas as pd


def scrape():
    # MAX PAGE: 1250
    url = 'https://www.jpl.nasa.gov/images?page='
    titles = []
    urls = []
    for i in range(1, 2):
        url = url + str(i)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser').find_all('li')

        for data in soup:
            h2s = data.find_all('span')
            image = data.find_all('img')

            for i in h2s:
                # Read Image:
                # image_numpy = skimage.io.imread(image[0]['data-src'])
                # data[i.text.strip()] = image[0]['data-src']
                titles.append(i.text.strip())
                urls.append(image[0]['data-src'])

    data = {'Titles': titles, 'Images': urls}
    df = pd.DataFrame(data)
    print(df)
    # print(json.dumps(key_items, sort_keys=True, indent=4))


def execute():
    scrape()


if __name__ == "__main__":
    execute()
