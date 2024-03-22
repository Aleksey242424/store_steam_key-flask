from requests import get,utils
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
from config import Config
from os import mkdir

def make_dir(dir_name:str,path:str = Config.PATH_ORDERS):
    mkdir(path+dir_name)
    return path+dir_name+"/"

def download_images(link:str,title:str):
    headers = utils.default_headers()
    headers.update({
        "user-agent":FakeUserAgent().random
    })
    r = get(link,headers)
    soup = BeautifulSoup(r.text,"lxml")
    carousel = soup.find("ul",{"class":"owl-carousel"})
    try:
        images = carousel.find_all("img")
    except AttributeError:
        return
    order_dir = make_dir(title)
    for img in images:
        img = img["src"]
        title_img = img.split("/")[-1]
        init_img = get(f"https://flameingame.ru{img}",headers=headers)
        with open(f"{order_dir}{title_img}","wb+") as f:
            f.write(init_img.content)


def download():
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
            a = cards_games[j].find("a",{"class":"game_image"})
            link = f"https://flameingame.ru{a.attrs['href']}"
            img = a.attrs["style"]
            img = f"https://flameingame.ru{img.strip().split(':')[-1].strip()[3:-1].strip('()')}"
            title = img.split("/")[-1]
            download_images(link,title[:-4])
            init_img = get(img,headers=headers)
            print(img)
            with open(f"{Config.PATH_ORDERS}{title}","wb+") as f:
                f.write(init_img.content)

        
                


