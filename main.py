import requests as rq
from bs4 import BeautifulSoup

response = rq.get("https://www.geeksforgeeks.org/python-programming-language-tutorial/")
print(response)

soup = BeautifulSoup(response.content, "html.parser")

s = soup.find("div", class_="entry-content")
content = soup.find_all("p")

print(content)