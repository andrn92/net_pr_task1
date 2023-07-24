import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time


ua = UserAgent()
headers = {'UserAgent': ua.ff}
host = 'https://scrapingclub.com'
path = '/home/username/dir_name/'

def get_soup(url:str):
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

def get_urls_images(page:int=2) -> dict:
    dict_urls = {}
    counter = 1
    for count in range(page):
        time.sleep(1)
        url = host + '/exercise/list_basic/?page={}'.format(count)
        soup = get_soup(url)
        all_cards = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for card in all_cards:
            name = card.find('h4', class_='card-title').find('a').text
            link = host + card.find('img', class_='card-img-top img-fluid').get('src')
            if name not in dict_urls:
                dict_urls[name] = link
            else:
                dict_urls[name + str(counter)] = link
                counter += 1
    return dict_urls

def download_image(name:str, url:str, path:str):
    path = path + name
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

def download_images(path:str, dict_urls:dict):
    for name, link in dict_urls.items():
        download_image(name, link, path)


if __name__ == '__main__':
	dict_urls = get_urls_images()
	download_images(path, dict_urls)

