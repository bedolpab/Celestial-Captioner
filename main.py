#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape():
    url = 'https://www.jpl.nasa.gov/images?page='
    scraped_data = pd.DataFrame(columns=['Title', 'Image'])

    for i in range(1, 1251):
        url = f'https://www.jpl.nasa.gov/images?page={i}'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser').find_all('li')
        for li_element in soup:
            title = li_element.find('span').text.strip()
            image = li_element.find('img')['data-src']
            scraped_data.loc[len(scraped_data.index)] = [title, image]

    scraped_data.to_csv('data.csv', mode='a',
                        header=False, index=False)


def read_data(filename: str):
    return pd.read_csv(filename, lineterminator='\n')


def execute():
    scrape()


if __name__ == "__main__":
    execute()
