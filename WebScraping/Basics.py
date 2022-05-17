from asyncio import tasks
from bs4 import BeautifulSoup

with open("index.html", "r") as html_file:
    content = html_file.read()

    bs4 = BeautifulSoup(content, "lxml")
    # print(bs4.prattify())
    a_tags = bs4.find_all("a")

    for a in a_tags:
        print(a.get("href"))
