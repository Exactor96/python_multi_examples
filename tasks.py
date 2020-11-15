from random import randint
from urllib.parse import urljoin

import requests
from PIL import Image
from bs4 import BeautifulSoup


def make_random_image(width: int, height: int, name: str):
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    for width_index in range(width):
        for height_index in range(height):
            pixels[width_index, height_index] = (randint(0, 255), randint(0, 255), randint(0, 255))

    img.save(f'{name}.png')
    return f'{name}.png'


def _download_html_content(url: str):
    return requests.get(url).content


def collect_all_hrefs(url: str):
    content = _download_html_content(url)
    bs = BeautifulSoup(content, features="html.parser")
    hrefs = bs.find_all('a')
    return [urljoin(url, href.get('href')) for href in hrefs if href.get('href') is not None]
