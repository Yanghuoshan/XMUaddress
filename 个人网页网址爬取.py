import requests
from bs4 import BeautifulSoup
import json

urls = [
    "https://informatics.xmu.edu.cn/faculty/jcrc.htm",
    "https://informatics.xmu.edu.cn/faculty/cogsci/professor.htm",
    "https://informatics.xmu.edu.cn/faculty/cogsci/associate_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/cogsci/assistant_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/cogsci/lector.htm",
    "https://informatics.xmu.edu.cn/faculty/cst/professor.htm",
    "https://informatics.xmu.edu.cn/faculty/cst/associate_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/cst/assistant_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/cst/lector.htm",
    "https://informatics.xmu.edu.cn/faculty/cst/engineer.htm",
    "https://informatics.xmu.edu.cn/faculty/se/professor.htm",
    "https://informatics.xmu.edu.cn/faculty/se/professor.htm",
    "https://informatics.xmu.edu.cn/faculty/se/assistant_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/ce/professor.htm",
    "https://informatics.xmu.edu.cn/faculty/ce/associate_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/ce/assistant_prof.htm",
    "https://informatics.xmu.edu.cn/faculty/ce/engineer.htm",
    "https://informatics.xmu.edu.cn/faculty/eietc/fg.htm",
    "https://informatics.xmu.edu.cn/faculty/eietc/gcs.htm"
]

head = 'https://informatics.xmu.edu.cn/'

peoples = []

def get_url():
    for url in urls:
        re = requests.get(url)
        re.encoding = 'utf-8'
        bs = BeautifulSoup(re.text, 'lxml')
        blocks = bs.find(name='div',attrs={"class":"row"}).find_all(name='div',attrs={"class":"col-md-6"})
        for block in blocks:
            people = block.find(name='a')
            name = people.get('title')
            peoples.append(head + people.get('href').strip('../').strip('../'))
            img_url = head + block.find(name='img').get('src')[1:]
            response = requests.get(img_url)
            with open(f"./resource/{name}.jpg","wb") as fp:
                fp.write(response.content)

    people = json.dumps(peoples,ensure_ascii=False)
    with open('teachers.txt','w',encoding='utf-8') as f:
        f.write(people)


get_url()