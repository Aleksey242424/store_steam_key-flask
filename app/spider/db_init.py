from requests import get,utils
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
from config import Config
from random import randint

def init_orders():
    headers = utils.default_headers()
    headers.update({
        "user-agent":FakeUserAgent().random
    })
    for i in range(1,68):
        r = get(f"https://flameingame.ru/katalog/stim/?PAGEN_17={i}")
        soup = BeautifulSoup(r.text,"lxml")
        catalog_section = soup.find("div",{"class":"catalog_section"})
        cards_games = catalog_section.find_all("div",{"class":"card_row"})
        for j in range(len(cards_games)):
            try:
                price = cards_games[j].find("div",{"class":"game_price"})
                price = int(price.find("div",{"class":"discont_price"}).text.strip()[:-1])
            except AttributeError:
                price = randint(300,1500)
            img = cards_games[j].find("a",{"class":"game_image"}).attrs["style"]
            img = f"https://flameingame.ru{img.strip().split(':')[-1].strip()[3:-1].strip('()')}"
            title = img.split("/")[-1]
            yield title,Config.path_orders+img.split('/')[-1],price


for orders in init_orders():
    print(orders)

