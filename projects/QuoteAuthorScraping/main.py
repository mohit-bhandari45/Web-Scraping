# ------------------------------------------- Scraping quotes and authors in csv or json file -------------------------------------------

import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

page = rq.get("http://quotes.toscrape.com/")

soup = BeautifulSoup(page.content, "lxml")

# print(soup.prettify())

quotes = soup.find_all(class_ = "text")
authors = soup.find_all(class_ = "author")

quote_texts = [quote.text for quote in quotes]
author_names = [author.text for author in authors]

np_quotes = np.array(quote_texts)
np_authors = np.array(author_names)

my_dict = {
    "quote": np_quotes,
    "author": np_authors
}

df = pd.DataFrame(my_dict)

df.to_csv("quotes.csv", index=False)
df.to_json("quotes.json", indent=2, orient="records")

print(df)