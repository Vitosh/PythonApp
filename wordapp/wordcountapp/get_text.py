import requests
from bs4 import BeautifulSoup


def get_text(url):
    r = requests.get(url)
    r_text = r.text

    soup = BeautifulSoup(r_text)
    text = soup.get_text()

    return text
