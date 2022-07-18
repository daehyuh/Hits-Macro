import requests
from bs4 import BeautifulSoup as bs

status = ""
user = "daehyuh318" //your username
repo = "daehyuh318" //your repo
fullurl = user + "%2F" + repo

while True:
    try:
        page = requests.get(
            "https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F" + fullurl)
        soup = bs(page.text, "html.parser")
        pry = soup.find_all("text")[3].string
        if status != pry:
          print(pry)
          status = pry
    except:
        pass