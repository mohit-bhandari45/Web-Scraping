from bs4 import BeautifulSoup

with open("./sample.html", "r") as f:
    content = f.read()

    soup = BeautifulSoup(content, "lxml")
    # print(soup.body.prettify())

    for tag in soup.body.find_all(True):
        # print(tag)
        print("\n")
        print(tag)
        print(len(soup.find(tag.name).text))