from requests import get,utils
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
from config import Config
from random import randint
from app.system_db.orders import CRUDOrders
from app.cache_orders import add_orders

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
            a = cards_games[j].find("a",{"class":"game_image"})
            
            img = a.attrs["style"]
            img = f"https://flameingame.ru{img.strip().split(':')[-1].strip()[3:-1].strip('()')}"
            title = img.split("/")[-1]
            link = 'https://flameingame.ru'+a.attrs["href"]
            r_2 = get(link,headers=headers)
            soup_2 = BeautifulSoup(r_2.text,"lxml")
            container = soup_2.find("div",{"class":"spoler"})
            spoiler = container.find_all("p")
            body = ''
            for p in spoiler:
                body = f"{body}^{p.text.strip()}"
            data:dict = {
                "title":title[:-4],
                "path_main_image":Config.UPLOAD_ORDERS+img.split('/')[-1],
                "price":price,
                "body":body,
                "path_images":Config.UPLOAD_ORDERS+img.split('/')[-1][:-4]
            }
            yield data


for orders in init_orders():
    CRUDOrders.add(title=orders["title"],body=orders["body"],path_main_image=orders["path_main_image"],path_images=orders["path_images"],price=orders["price"])

