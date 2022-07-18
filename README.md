# Hits-Macro
Hits 방문자 매크로
<h1 align=center>
🤪I'm manipulating the hits, Just for fun !🤪<br>
</h1>

```python
import requests
from bs4 import BeautifulSoup as bs

status = ""
user = "daehyuh318"
repo = "daehyuh318"
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
```

<div align=center>

I'm raising my ranking https://hits.seeyoufarm.com/#rank   

### 🏃 6/29 Run code 🏃   
### 👑 7/1 10th 👑     
### 👑 7/2 9th 👑   
### 👑 7/2 8th 👑   
### 👑 7/2 7th 👑   
### 👑 7/5 6th 👑   
### 👑 7/8 5th 👑 
### 👑 7/9 4th 👑 
### 👑 7/18 5th 👑 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdaehyuh318%2Fdaehyuh318&count_bg=%23638FDA&title_bg=%23555555&icon=ghostery.svg&icon_color=%23E7E7E7&title=hits+%28%EC%98%A4%EB%8A%98+%EB%B0%A9%EB%AC%B8%EC%9E%90+%2F+%EC%A0%84%EC%B2%B4+%EB%B0%A9%EB%AC%B8%EC%9E%90%29&edge_flat=false)](https://hits.seeyoufarm.com)
</div>
