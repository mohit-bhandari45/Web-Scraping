import requests as rq
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

print(soup.title.string)

for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get_text())

print(soup.select("div.italic"))