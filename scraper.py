import requests
from bs4 import BeautifulSoup
from itertools import count

def webms(*boards):
    for page in count(0, 1):
        for board in boards:
            if page:
                req = requests.get(f'http://boards.4chan.org/{board}/{page}')
            else:
                req = requests.get(f'http://boards.4chan.org/{board}/')
            soup = BeautifulSoup(req.text, 'lxml')
            files = map(lambda div: div.select_one('a'), soup.find_all('div', class_='fileText'))
            webms = filter(lambda a: a.text.endswith('.webm'), files)
            for webm in webms:
                yield 'https:' + webm.get('href')