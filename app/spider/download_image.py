from requests import get,utils
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
from config import Config

def download_image(page=1):
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
            img = cards_games[j].find("a",{"class":"game_image"}).attrs["style"]
            img = f"https://flameingame.ru{img.strip().split(':')[-1].strip()[3:-1].strip('()')}"
            title = img.split("/")[-1]
            init_img = get(img,headers=headers)
            print(img)
            with open(f"{Config.path_orders}{title}.jpg","wb+") as f:
                f.write(init_img.content)

        
                


