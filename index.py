# scraping all the html files in the directory

import os
from bs4 import BeautifulSoup
from collections import defaultdict

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        fname = os.path.join(directory, filename)
        print(fname)

        with open(fname, "r") as f:
            soup = BeautifulSoup(f, "lxml")

            tag_count = defaultdict(int)
            for tag in soup.find_all(True):
                tag_count[tag.name] += 1

            print(tag_count)
            print("\n")