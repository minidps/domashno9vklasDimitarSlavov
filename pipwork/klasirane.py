import requests
import re
from bs4 import BeautifulSoup
url = "https://gong.bg/livescore/efbet-liga/klasirane"

r = requests.get(url)
bs = BeautifulSoup(r.text, features="html.parser")
divs = bs.find_all("div", {"class": "team"})
i = 1
for div in divs:  
    text = re.sub(r'^\s+|\s+$', '', div.text)
    if text != "Отбор":
        print(f"{i} {text}")
        i += 1