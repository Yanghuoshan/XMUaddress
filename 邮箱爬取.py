import requests
from bs4 import BeautifulSoup
import json


address = dict()


def get_email():
    with open('teachers.txt',"r",encoding='utf-8') as f:
        urls = json.loads(f.read())
        for url in urls:
            re = requests.get(url)
            re.encoding = 'utf-8'
            bs = BeautifulSoup(re.text, 'lxml')
            block = bs.find(name='div', attrs={"class": "infoContent"})
            name = block.find(name="div", attrs={"class": "expert-name"}).text.split(' ')[0]
            print(name)
            ps = block.find_all(name="p")
            for p in ps:
                if p.text[:4] == "电子邮件":
                    address[name] = p.text[5:].strip()
                    break

        with open('emails.txt',"w",encoding="utf-8") as fp:
            fp.write(json.dumps(address,ensure_ascii=False))


get_email()