import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=iphone"
headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}

data = {"title": [], "price": []}

r = rq.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

# print(soup.prettify())
spans = soup.select("h2.a-size-medium")
prices = soup.select("span.a-price")

for span in spans:
    data["title"].append(span.get_text())

for price in prices:
    whole_price = price.select_one("span.a-offscreen")
    if whole_price:
        data["price"].append(whole_price.get_text())
    if(len(data["price"])== len(data["title"])):
        break

df = pd.DataFrame.from_dict(data) 
df.to_csv("data.csv", index=False)
print(df)